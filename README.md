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


## KCAP handoffs and learning

KCAP lessons can be packaged as Markdown handoffs with the task, source evidence, outcomes, limitations and next steps. A recipient can use these records to carry context into a later task.

The design learning playbook describes capturing visual differences, failures, corrections and reusable methods. A documented Academy programme proposes curating KCAP lessons for agent workflows and potential model training, with the Test Team evaluating candidates and regressions. Hermes and smaller local models such as Qwen are potential recipients of reviewed learning material; actual ingestion, model fine-tuning, Test Team execution and resulting improvement require separate evidence. A Markdown handoff alone does not demonstrate training or model-weight changes.


### Run the KCAP handoff example

```sh
python kcap_handoff.py kcap_example.json
```

The tool checks that the objective, evidence, outcome, limitations and next steps are present, then prints a Markdown handoff. It reports missing or empty fields; it does not verify whether the content is true. To save the output, run `python kcap_handoff.py kcap_example.json > handoff.md`. The included example is fictional.
