import requests
import datetime

# 目标URL
url = "https://api.arkhamintelligence.com/portfolio/timeSeries/address/1AsHPP7WcGnDLzxW2bUa2FcbJP3eZVEqpx?pricingId=bitcoin"

# 发出GET请求
response = requests.get(url)
data = response.json()

# 获取今天和明天的日期字符串
today = datetime.datetime.now().strftime("%Y-%m-%dT00:00:00Z")
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00Z")

# 提取最新日期的balance值
if today in data:
    latest_balance = data[today]["bitcoin"]["bitcoin"]["balance"]
elif tomorrow in data:
    latest_balance = data[tomorrow]["bitcoin"]["bitcoin"]["balance"]
else:
    latest_balance = None

print(f"最新日期的balance值: {latest_balance}")
