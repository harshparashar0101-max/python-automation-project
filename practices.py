
from jira import JIRA

JIRA_URL  = "https://on24-inc.atlassian.net"
EMAIL     = "c-harsh.parasher@on24.com"
API_TOKEN = ""

jira = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))

# ── Fetch all child issues of a known parent and print their types ──
sub_jql = 'parent = LOGI-57236'   # 👈 Replace with any real issue key from your results
sub_issues = jira.search_issues(sub_jql, maxResults=50)

print(f"Found {len(sub_issues)} child issues:\n")
for sub in sub_issues:
    print(f"  {sub.key}  |  Type: {sub.fields.issuetype.name}")