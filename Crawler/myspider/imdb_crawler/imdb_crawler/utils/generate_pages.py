import redis

# 创建连接池
pool = redis.ConnectionPool(host="localhost", port=6379, password="", max_connections=1024)
# 创建连接对象
coon = redis.Redis(connection_pool=pool)
print("开始...")
for i in range(20):
    page_link = "https://www.imdb.com/search/title/?groups=top_1000&start={}".format(i * 50 + 1)
    coon.lpush("imdb:start_pages", page_link)
print("结束...")
