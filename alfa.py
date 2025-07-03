import http.client
import json
from datetime import date, timedelta

def get_rub(date):
    conn = http.client.HTTPConnection('openexchangerates.org')
    conn.request('GET', f"/api/historical/{date}.json?app_id=ad1c3a856f32428db34c670bfefe84c1")
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    result = json_data["rates"]["RUB"]
    print(result)

today = date.today()
yesterday = today - timedelta(days=1)
get_rub(today)
get_rub(yesterday)

