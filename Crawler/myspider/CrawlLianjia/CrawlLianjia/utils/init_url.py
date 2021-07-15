import redis

# 创建连接池
pool = redis.ConnectionPool(host="localhost", port=6379, password="", max_connections=1024)
# 创建连接对象
coon = redis.Redis(connection_pool=pool)
print("开始...")
for i in range(1, 101):
    url = "https://cd.lianjia.com/ershoufang/pg{}/".format(i)
    coon.lpush("lianjia:start_urls", url)
print("结束...")
