"""Check every keyword used in the supplied frozen output schema.

This small additional checker is not a general JSON Schema implementation.
The original course validator remains unchanged.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]


def check(value, schema, path='$'):
    assert set(schema) <= {'$schema', 'title', 'type', 'required', 'properties', 'items', 'additionalProperties'}
    assert isinstance(value, {'object': dict, 'array': list, 'string': str}[schema['type']]), path
    if isinstance(value, dict):
        assert set(schema.get('required', [])) <= set(value), path
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            assert set(value) <= set(properties), path
        for key, child in properties.items():
            if key in value:
                check(value[key], child, path + '.' + key)
    if isinstance(value, list) and 'items' in schema:
        for index, child in enumerate(value):
            check(child, schema['items'], f'{path}[{index}]')


if __name__ == '__main__':
    schema = json.loads((ROOT / 'core/output_schema.json').read_text(encoding='utf8'))
    for response in sorted((Path(__file__).parent / 'actual_runs').glob('*_raw.json')):
        check(json.loads(response.read_text(encoding='utf8')), schema)
        print(response.name + ': ALL PRESENT SCHEMA CONSTRAINTS PASSED')
