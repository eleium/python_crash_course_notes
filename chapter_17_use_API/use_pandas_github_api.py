import pandas as pd
import requests

# 1. 正确的 URL 拼写：repositories
url = "https://api.github.com/search/repositories?q=language:python+stars:>10000&sort=stars"

r = requests.get(url, verify=False)

# 2. 检查是否成功
print(f"Status code: {r.status_code}")

# 3. 提取数据
data = r.json()["items"]

# 4. 直接变成 pandas 表格
df = pd.DataFrame(data)

# 5. 如果需要挑列，注意列名拼写：
df = df[["name", "stargazers_count", "html_url", "description"]]

print(df)
