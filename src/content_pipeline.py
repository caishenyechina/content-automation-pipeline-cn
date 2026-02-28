import argparse
import csv
import datetime as dt
from pathlib import Path


def load_topics(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return [x.strip() for x in f.readlines() if x.strip()]


def generate_post(topic: str):
    hook = f"你可能忽略了一个细节：{topic}"
    body = (
        f"今天聊聊【{topic}】。\n"
        "1) 先说问题\n"
        "2) 再给可执行步骤\n"
        "3) 最后给一个马上能做的小动作"
    )
    cta = "如果你也想要同款模板，私信我“模板”。"
    return f"{hook}\n\n{body}\n\n{cta}"


def repurpose(text: str, platform: str):
    platform = platform.lower()
    if platform in {"x", "twitter"}:
        return text.replace("\n", " ")[:260]
    if platform in {"xiaohongshu", "xhs"}:
        return text + "\n\n#效率 #自动化 #AI"
    if platform in {"wechat", "公众号"}:
        return "【可执行清单】\n" + text + "\n\n— 完 —"
    return text


def plan_week(topics, out_path: Path):
    weekdays = ["周一", "周二", "周三", "周四", "周五"]
    lines = ["# 本周内容排期", f"生成时间：{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ""]
    for i, t in enumerate(topics[:5]):
        lines.append(f"- {weekdays[i]}：{t}")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Content automation helpers")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate")
    p_gen.add_argument("--topic", required=True)

    p_rep = sub.add_parser("repurpose")
    p_rep.add_argument("--input", required=True)
    p_rep.add_argument("--platform", required=True)

    p_plan = sub.add_parser("plan-week")
    p_plan.add_argument("--topics", required=True)
    p_plan.add_argument("--out", required=True)

    args = parser.parse_args()

    if args.cmd == "generate":
        print(generate_post(args.topic))
    elif args.cmd == "repurpose":
        text = Path(args.input).read_text(encoding="utf-8")
        print(repurpose(text, args.platform))
    elif args.cmd == "plan-week":
        topics = load_topics(Path(args.topics))
        out = plan_week(topics, Path(args.out))
        print(f"已生成：{out}")


if __name__ == "__main__":
    main()
