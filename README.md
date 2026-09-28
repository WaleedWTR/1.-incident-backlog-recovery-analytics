# Incident Backlog Recovery Analytics

![Backlog analytics tests](https://github.com/WaleedWTR/1.-incident-backlog-recovery-analytics/actions/workflows/tests.yml/badge.svg)

A portfolio service-operations project for turning an aged incident backlog into a prioritised, measurable recovery plan.

> **Portfolio note:** All tickets and performance data in this repository are synthetic. The method is informed by real backlog-recovery experience without publishing employer information.

## What this project demonstrates

- aged backlog analysis
- SLA breach detection
- risk-band prioritisation
- priority and resolver segmentation
- recovery-wave planning
- governance and daily control
- Python analytics
- SQL operational reporting
- automated tests

## Recovery approach

```text
Baseline backlog
      |
      v
Validate ticket state
      |
      v
Prioritise by impact / age / SLA
      |
      +--> close invalid/stale records correctly
      +--> assign genuine active work
      +--> escalate blockers
      +--> identify systemic causes
      |
      v
Daily control
      |
      v
Sustainable BAU
```

## Run

```bash
python scripts/backlog_analysis.py
```

## Key documentation

- [Recovery plan](docs/recovery-plan.md)
- [Daily backlog control](docs/daily-control.md)
- [Governance model](docs/governance.md)
- [Sample analysis](docs/sample-analysis.md)
- [SQL backlog controls](sql/backlog-controls.sql)

## Skills demonstrated

**Incident Management · ITSM · Backlog Recovery · SLA Analytics · Service Operations · Python · SQL · Continual Improvement**
