from pyspark import Row
from pyspark.sql import SparkSession
from MySQLconfig import *

# 操作Spark SQL DataFrame，读取结构化数据
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# 读取文本文件，非结构化数据
sc = spark.sparkContext

filePath = 'hdfs://localhost:9000/mydata/Details.txt'
# textFile: RDD
# RDD: 文件在spark中的表示，全称resilient distributed dataset
textFile = sc.textFile(filePath)

# 一般情况下不要调用collect
# collect会将所有节点的数据收集到当前节点并放到内存里
# data = textFile.collect()
# data: list
# print(type(data))


def to_pair(item):
    # see pipeline of CrawlLianjia
    tmp_list = item.split(',')
    area = tmp_list[0]
    # price = tmp_list[1]
    return area, 1


# x表示值(1)
# map, reduceByKey称为转换操作
# collect称为行动操作
rdd = textFile.map(lambda x: to_pair(x)).reduceByKey(lambda x, y: x + y)

# 把rdd转换为DataFrame
rowRDD = rdd.map(lambda x: Row(area=x[0], count=x[1]))
dataFrame = spark.createDataFrame(rowRDD)

# Register the DataFrame as a global temporary view
dataFrame.createGlobalTempView("house")

# Global temporary view is tied to a system preserved database `global_temp`
spark.sql('SELECT * FROM global_temp.house limit 5').show()

# coon_param = {}
# coon_param['user'] = Mysql_User
#
# dataFrame.write.jdbc(Mysql_conn, 'city_count', 'overwrite', coon_param)
# print('执行结束')
# coon_param['user']

conn_param = {"user": Mysql_User, "password": Mysql_Pwd, "driver": Mysql_Driver}

dataFrame.write.jdbc(Mysql_Conn, "city_count", "overwrite", conn_param)
print("执行结束")
