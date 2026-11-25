"""Small deterministic examples, not the original operational plugins."""
from datetime import datetime, timedelta


def review(criteria, evidence):
    allowed = {'PASS', 'FAIL', 'BLOCKED', 'UNTESTED'}
    return {name: evidence.get(name, 'UNTESTED') if evidence.get(name, 'UNTESTED') in allowed else 'UNTESTED' for name in criteria}


def heartbeat(observed, now, max_age_seconds):
    if not isinstance(now, datetime) or now.utcoffset() is None:
        raise ValueError('now must be timezone-aware')
    if max_age_seconds < 0:
        raise ValueError('threshold must be non-negative')
    if not isinstance(observed, datetime) or observed.utcoffset() is None or observed > now:
        return 'UNKNOWN'
    return 'CURRENT' if now - observed <= timedelta(seconds=max_age_seconds) else 'UNKNOWN'


def evidence_index(records):
    grouped = {}
    for record in records:
        source = record.get('source_id')
        if not isinstance(source, str) or not source.strip():
            raise ValueError('source_id is required')
        grouped.setdefault(source, [])
        if record not in grouped[source]:
            grouped[source].append(dict(record))
    return grouped


def kcap_candidate(title, evidence, limitation, prevention):
    values = (title, evidence, limitation, prevention)
    if any(not isinstance(value, str) or not value.strip() for value in values):
        raise ValueError('all candidate fields are required')
    return {'title': title, 'evidence': evidence, 'limitation': limitation,
            'proposed_prevention': prevention, 'status': 'PROPOSED'}
