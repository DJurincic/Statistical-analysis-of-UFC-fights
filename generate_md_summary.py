# scripts/generate_md_summary.py
import sys
import json

def main(report_file):
    with open(report_file, 'r') as f:
        data = json.load(f)

    summary = data['summary']
    tests = data['tests']

    print("# ✅ Pytest Summary\n")
    print(f"**Total tests:** {summary['total']}")
    print(f"**Passed:** {summary['passed']}")
    print(f"**Failed:** {summary['failed']}")
    print(f"**Skipped:** {summary.get('skipped', 0)}\n")

    if summary['failed'] > 0:
        print("## ❌ Failed Tests\n")
        for test in tests:
            if test['outcome'] == 'failed':
                print(f"- `{test['nodeid']}`")

    print("\n---")

if __name__ == "__main__":
    main(sys.argv[1])
