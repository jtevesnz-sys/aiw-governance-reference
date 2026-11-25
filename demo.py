from datetime import datetime, timedelta, timezone
from governance import review, heartbeat, evidence_index, kcap_candidate

now = datetime.now(timezone.utc)
print('WATCHTOWER:', review(['tests', 'rollback'], {'tests': 'PASS'}))
print('WATCHDOG:', heartbeat(now - timedelta(seconds=120), now, 60))
print('LIBRARIAN:', evidence_index([{'source_id': 'example-1', 'note': 'fictional observation'}]))
print('KCAP:', kcap_candidate('Fictional incident', 'example-1', 'Synthetic test only', 'Review before retrying'))
