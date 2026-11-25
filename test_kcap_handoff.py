import unittest
import subprocess
import sys
from kcap_handoff import FIELDS, render


class HandoffTests(unittest.TestCase):
    def test_cli_example_outputs_reviewable_handoff(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', 'kcap_handoff.py', 'kcap_example.json'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0)
        self.assertIn('## Evidence', result.stdout)
        self.assertIn('## Next steps', result.stdout)

    def test_cli_missing_file_fails(self):
        result = subprocess.run([sys.executable, 'kcap_handoff.py', 'nonexistent-kcap-example.json'], capture_output=True, text=True, encoding='utf-8')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Invalid handoff', result.stderr)

    def test_contains_all_sections_and_proposed_status(self):
        result = render({field: 'example' for field in FIELDS})
        self.assertIn('PROPOSED', result)
        for heading in ('Objective', 'Evidence', 'Outcome', 'Limitations', 'Next steps'):
            self.assertIn('## ' + heading, result)

    def test_missing_or_blank_field_is_rejected(self):
        for field in FIELDS:
            record = {key: 'example' for key in FIELDS}
            record[field] = ' '
            with self.subTest(field=field), self.assertRaises(ValueError):
                render(record)


if __name__ == '__main__':
    unittest.main()
