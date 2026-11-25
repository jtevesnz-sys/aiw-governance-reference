import unittest
from kcap_handoff import FIELDS, render


class HandoffTests(unittest.TestCase):
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
