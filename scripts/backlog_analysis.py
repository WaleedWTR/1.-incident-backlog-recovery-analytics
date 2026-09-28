#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "incidents.csv"
AS_OF = datetime(2026, 9, 28, 0, 0, tzinfo=timezone.utc)

def parse(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def load():
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def classify(row, as_of=AS_OF):
    age_hours = (as_of - parse(row["opened_at"])).total_seconds() / 3600
    target = float(row["sla_target_hours"])
    if age_hours > target:
        risk = "breached"
    elif age_hours >= target * 0.75:
        risk = "at-risk"
    else:
        risk = "within-sla"
    return {
        **row,
        "age_hours": round(age_hours, 1),
        "sla_consumed_pct": round(age_hours / target * 100, 1),
        "risk": risk,
    }

def analyse(rows):
    assessed = [classify(r) for r in rows]
    return {
        "tickets": len(assessed),
        "breached": sum(r["risk"] == "breached" for r in assessed),
        "at_risk": sum(r["risk"] == "at-risk" for r in assessed),
        "within_sla": sum(r["risk"] == "within-sla" for r in assessed),
        "by_priority": dict(Counter(r["priority"] for r in assessed)),
        "by_resolver": dict(Counter(r["resolver"] for r in assessed)),
    }

if __name__ == "__main__":
    rows = load()
    summary = analyse(rows)
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\nHighest SLA consumption:")
    for row in sorted((classify(r) for r in rows), key=lambda x: x["sla_consumed_pct"], reverse=True)[:5]:
        print(
            f'{row["incident_id"]}: {row["priority"]} | {row["resolver"]} | '
            f'{row["risk"]} | {row["sla_consumed_pct"]}%'
        )
