from jira import JIRA

# ─────────────────────────────────────────
# 🔧 YOUR CONFIGURATION
# ─────────────────────────────────────────

JIRA_URL  = "https://on24-inc.atlassian.net"
EMAIL     = "c-harsh.parasher@on24.com"
API_TOKEN = ""
LABELS    = ["c-log-vshowanalytics", "c-log-presentersreportpage", "c-log-momentumemail"]

BASE_JQL    = "project = LOGI AND type = Test AND labels = "  # ✅ No search_issues here
OUTPUT_FILE = "jira_multilabel_results.txt"

# ─────────────────────────────────────────
# 🔌 Connect to Jira
# ─────────────────────────────────────────

print("Connecting to Jira...")
jira = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))
print("✅ Connected successfully!")

# ─────────────────────────────────────────
# 🔍 Loop through labels + Save in one block
# ─────────────────────────────────────────

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    for label in LABELS:

        # ✅ Build complete JQL with label
        jql = f'{BASE_JQL}"{label}"'

        print(f"\n🔍 Running JQL for label: {label}")
        print(f"   JQL: {jql}")

        # ✅ search_issues is INSIDE the loop with complete jql
        issues = jira.search_issues(jql, maxResults=100)

        print(f"✅ Found {len(issues)} issues for label: {label}")

        # ── Section Header ──
        f.write(f"\n{'=' * 60}\n")
        f.write(f"LABEL       : {label}\n")
        f.write(f"JQL         : {jql}\n")
        f.write(f"Total Issues: {len(issues)}\n")
        f.write(f"{'=' * 60}\n\n")

        if not issues:
            f.write("No issues found for this label.\n")
            continue

        # ✅ Issue writing is INSIDE the same loop
        for issue in issues:
            f.write(f"Issue Key   : {issue.key}\n")
            f.write(f"Summary     : {issue.fields.summary}\n")
            f.write(f"Status      : {issue.fields.status.name}\n")
            f.write(f"Assignee    : {issue.fields.assignee.displayName if issue.fields.assignee else 'null'}\n")
            f.write(f"Priority    : {issue.fields.priority.name if issue.fields.priority else 'null'}\n")
            f.write(f"Created     : {issue.fields.created[:10]}\n")
            f.write(f"Updated     : {issue.fields.updated[:10]}\n")
            f.write(f"Description : {issue.fields.description if issue.fields.description else 'null'}\n")
            f.write(f"Labels      : {', '.join(issue.fields.labels) if issue.fields.labels else 'null'}\n")

            f.write("-" * 60 + "\n\n")

print(f"\n✅ All labels done! Results saved to '{OUTPUT_FILE}'")