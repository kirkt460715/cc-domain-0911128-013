import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from trialvault.contracts.schema import Schema
        schema=Schema(data['schema'])
        for row in data['rows']:
            schema.validate(row)
        columns={r['name'] for r in data['schema']['fields']}
        self.assertTrue(set(data['study']['features']+data['study']['responses'])<=columns)
        self.assertEqual(len(data['rows']),len({r['id'] for r in data['rows']}))
