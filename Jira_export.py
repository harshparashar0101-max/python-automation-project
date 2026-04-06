from jira import JIRA

import sys
sys.stdout.reconfigure(encoding='utf-8')
import json


# ─────────────────────────────────────────
# 🔧 YOUR CONFIGURATION — Edit these values
# ─────────────────────────────────────────

JIRA_URL   = "https://mayankkhede.atlassian.net"   # Your Jira Cloud URL
EMAIL      = "harsh.parashar0101@gmail.com"                       # Your Atlassian email
API_TOKEN  = "API_TOKEN"                   # Token from Step 2

JQL_QUERY  = "project = LOGI AND type = Test AND labels = LOGI-7 ORDER BY created DESC"              # Your JQL
OUTPUT_FILE = "jira_results.txt"                     # Output file name

# ─────────────────────────────────────────
# 🔌 Connect to Jira
# ─────────────────────────────────────────

print("Connecting to Jira...")

jira = JIRA(
    server=JIRA_URL,
    basic_auth=(EMAIL, API_TOKEN)
)

print("✅ Connected successfully!")

# ─────────────────────────────────────────
# 🔍 Run JQL Query
# ─────────────────────────────────────────

print(f"Running JQL: {JQL_QUERY}")

issues = jira.search_issues(JQL_QUERY, maxResults=100)

print(f"✅ Found {len(issues)} issues")

# ─────────────────────────────────────────
# 💾 Save Results to Text File
# ─────────────────────────────────────────

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    f.write(f"JQL Query: {JQL_QUERY}\n")
    f.write(f"Total Issues Found: {len(issues)}\n")
    f.write("=" * 60 + "\n\n")

    for issue in issues:
        f.write(f"Issue Key   : {issue.key}\n")
        f.write(f"Summary     : {issue.fields.summary}\n")
        f.write(f"Status      : {issue.fields.status.name}\n")
        f.write(f"Assignee    : {issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned'}\n")
        f.write(f"Priority    : {issue.fields.priority.name if issue.fields.priority else 'None'}\n")
        f.write(f"Created     : {issue.fields.created[:10]}\n")
        f.write(f"Updated     : {issue.fields.updated[:10]}\n")
        f.write(f"Description : {issue.fields.description if issue.fields.description else 'null'}\n")
        f.write(f"Labels      : {', '.join(issue.fields.labels) if issue.fields.labels else 'null'}\n")
        f.write("-" * 60 + "\n")

print(f"✅ Results saved to '{OUTPUT_FILE}'")
