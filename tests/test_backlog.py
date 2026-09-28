from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from backlog_analysis import analyse, classify, load  # noqa: E402

def test_dataset_size():
    assert analyse(load())["tickets"] == 12

def test_old_ticket_is_breached():
    row = next(r for r in load() if r["incident_id"] == "INC-B011")
    assert classify(row)["risk"] == "breached"

def test_new_p2_is_within_sla():
    row = next(r for r in load() if r["incident_id"] == "INC-B009")
    assert classify(row)["risk"] == "within-sla"

def test_summary_partitions_all_tickets():
    result = analyse(load())
    assert result["breached"] + result["at_risk"] + result["within_sla"] == 12
