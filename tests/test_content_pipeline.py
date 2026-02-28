from pathlib import Path
import tempfile

from src.content_pipeline import generate_post, repurpose, plan_week


def test_generate_post():
    out = generate_post("老板助手自动化")
    assert "老板助手自动化" in out


def test_repurpose_x():
    out = repurpose("line1\nline2", "x")
    assert "\n" not in out


def test_plan_week():
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "week.md"
        plan_week(["A", "B", "C"], out)
        txt = out.read_text(encoding="utf-8")
        assert "本周内容排期" in txt
