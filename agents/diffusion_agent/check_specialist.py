from pathlib import Path
import json, hashlib, subprocess, sys

A=Path(__file__).resolve().parent
S=A.parents[1]
schema=json.loads((S/'core/output_schema.json').read_text())
def validate(value, rule, path='$'):
    errors=[]
    kind=rule.get('type')
    types={'object':dict,'array':list,'string':str}
    if kind in types and not isinstance(value,types[kind]):
        return [path+': wrong type']
    if isinstance(value,dict):
        errors += [path+': missing '+k for k in rule.get('required',[]) if k not in value]
        props=rule.get('properties',{})
        if rule.get('additionalProperties') is False:
            errors += [path+': forbidden extra field '+k for k in value if k not in props]
        for k,v in value.items():
            if k in props: errors += validate(v,props[k],path+'.'+k)
    if isinstance(value,list) and 'items' in rule:
        for i,v in enumerate(value): errors += validate(v,rule['items'],path+f'[{i}]')
    return errors

if __name__=='__main__':
    results=[]
    def check(name,ok,detail=''):
        results.append(dict(check=name,passed=bool(ok),detail=detail))
    inp=json.loads((S/'core/input_schema.json').read_text())
    cases={n:json.loads((A/f'cases/{n}.json').read_text()) for n in ['primary','contrast_1','contrast_2']}
    resp={n:json.loads((A/f'responses/{n}_response.json').read_text()) for n in cases}
    for n in cases:
        check(n+' common input contract',not validate(cases[n],inp))
        check(n+' full common output contract',not validate(resp[n],schema))
    draft=json.loads((A/'history/v0.1/primary_response.json').read_text())
    errors=validate(draft,schema)
    check('preserved v0.1 failure is detected',any('forbidden extra field rogers_assessment' in e for e in errors),'; '.join(errors))
    changed=[k for k in cases['primary'] if cases['primary'][k]!=cases['contrast_1'][k]]
    check('posture contrast isolates intended context change',set(changed)=={'adoption_posture','management_question'},str(changed))
    check('technology held constant in all contexts',len({c['emerging_technology'] for c in cases.values()})==1)
    check('dated source packet held constant',len({c['additional_context'] for c in cases.values()})==1)
    check('general diffusion finding invariant across contexts',len({r['general_et_finding'] for r in resp.values()})==1)
    check('application finding invariant under posture-only change',resp['primary']['application_finding']==resp['contrast_1']['application_finding'])
    check('timing implications vary across contexts',len({r['recommendation_management_implication'] for r in resp.values()})==3)
    check('new application changes application finding',resp['primary']['application_finding']!=resp['contrast_2']['application_finding'])
    frozen=[]
    for line in (S/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
        if line.strip():
            h,p=line.split(None,1); frozen.append(hashlib.sha256((S/p.strip()).read_bytes()).hexdigest()==h)
    check('all seven frozen core hashes unchanged',len(frozen)==7 and all(frozen))
    out=dict(automated_checks=len(results),passed=sum(r['passed'] for r in results),checks=results,scope='Contract and selected regression properties only. Not independent semantic or model performance evaluation.')
    (A/'records/check_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if all(r['passed'] for r in results) else 1)
