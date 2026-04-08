from jira import JIRA

JIRA_URL = "https://mayankkhede.atlassian.net"
EMAIL = "harsh.parashar0101@gmail.com"
API_TOKEN = "ATATT3xFfGF0WLUWVWx_l6okbgi4FTYNxfuEu9tUJPzFnh38xBnOsB7XVJ2HwLaDiPLZtaik116JqsQs1iF1lD_ZRMXzmerTLvmmwosC6cW6Nd59wXWwwqAzXf0pSLnL-0V0QBpiCFF5S7oMXQw3KF181o6u-cHA0MtRu3KUpZktbzKHchryG4U=27126071"

try:
    jira_conn = JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))
    print("Jira connection successful")

    me = jira_conn.myself()
    print("Logged in as:", me["displayName"])

except Exception as e:
    print("Connection failed:")
    print(str(e))