import unittest
from datetime import datetime, timedelta, timezone
from governance import review, heartbeat, evidence_index, kcap_candidate


class GovernanceTests(unittest.TestCase):
    def test_review_never_invents_pass(self):
        self.assertEqual(review(['a', 'b'], {'a': 'PASS', 'b': 'OTHER'}), {'a': 'PASS', 'b': 'UNTESTED'})

    def test_stale_missing_future_and_current(self):
        now = datetime.now(timezone.utc)
        self.assertEqual(heartbeat(now, now, 60), 'CURRENT')
        for value in (None, now - timedelta(seconds=61), now + timedelta(seconds=1)):
            self.assertEqual(heartbeat(value, now, 60), 'UNKNOWN')

    def test_duplicate_evidence_does_not_erase_conflicts(self):
        first = {'source_id': 's', 'note': 'one'}
        index = evidence_index([first, first, {'source_id': 's', 'note': 'two'}])
        self.assertEqual(len(index['s']), 2)
        with self.assertRaises(ValueError):
            evidence_index([{'note': 'missing ID'}])

    def test_candidate_remains_proposed(self):
        self.assertEqual(kcap_candidate('title', 'evidence', 'limit', 'action')['status'], 'PROPOSED')
        with self.assertRaises(ValueError):
            kcap_candidate('title', '', 'limit', 'action')


if __name__ == '__main__':
    unittest.main()
