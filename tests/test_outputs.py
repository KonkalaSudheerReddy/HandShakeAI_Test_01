import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def read_report():
    with REPORT_PATH.open(encoding="utf-8") as report_file:
        return json.load(report_file)


def test_findings_are_saved_for_review():
    """instruction.md criterion: Save your findings so they can be reviewed."""
    assert REPORT_PATH.is_file(), "report.json was not saved"


def test_total_request_count():
    """instruction.md criterion: Report how many requests there were."""
    assert read_report()["total_requests"] == 6


def test_clients_involved():
    """instruction.md criterion: Summarize the clients involved."""
    assert read_report()["unique_ips"] == 3


def test_popular_pages():
    """instruction.md criterion: Identify which pages were popular."""
    assert read_report()["top_path"] == "/index.html"
