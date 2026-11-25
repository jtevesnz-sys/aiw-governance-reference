# Watchtower, Watchdog, Librarian and KCAP

An early public reference showing four complementary governance roles in an AI-assisted workflow. This repository is newly written demonstration code inspired by the existing AIW workflows; it is not the original plugins or a running service.

- **Watchtower** reviews stated acceptance criteria against supplied evidence and reports PASS, FAIL, BLOCKED or UNTESTED.
- **Watchdog** classifies a supplied heartbeat as current or unknown according to an explicit age threshold. It does not run continuously or send alerts.
- **Librarian** builds an evidence index using exact source IDs and preserves conflicting records for review.
- **KCAP** captures a lesson as a non-canonical candidate, with evidence, limitations and a proposed preventive action.

## Try it

Python 3.11 or newer; no dependencies or credentials.

```sh
python demo.py
python -m unittest -v
```

The demo uses synthetic records only. These functions do not monitor infrastructure, call AI models, verify external evidence, repair systems, publish messages, or promote memories. Caller-provided evidence and timestamps need independent verification. This is an illustrative prototype, not a production security system. No license has been selected.
