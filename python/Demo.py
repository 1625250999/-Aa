# encoding: utf-8
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS


master = "local[4]"
appName = "SparkStreamingRokidTrace"
timecell = 5

sc = SparkContext(master=master, appName=appName)

text = sc.textFile("D:\\test\\ml-latest-small\\ratings.csv")
text = text .filter(lambda x: "movieId" not in x)    # 去除标题行

print("#####################################数据测试1")
print("用户信息的数据总数为："),( text.count())    # 查看数据数量
print("用户信息的前五条为："),( text.take(5))       # 查看前5条数据

movieRatings = text.map(lambda x: x.split(",")[:3])   # 取出前三列
print("进行预测 并取前五条" ),(movieRatings.take(5))      #查看前五条


print("用户的数量为："),( movieRatings.map(lambda x: x[0]).distinct().count()) # 用户数量
print("电影的数量为："),( movieRatings.map(lambda x: x[1]).distinct().count()) # 电影数量

model = ALS.train(movieRatings, 10, 10, 0.01)   # 模型训练
#针对用户推荐
#ALS针对用户，可以使用model.recommendProducts(user: int, num: int) ，其中user为用户ID，num 为推荐数量。
print("为用户1推荐的五部电影分别为："),( model.recommendProducts(1, 5))  # 为用户 1 推荐 5 部电影


#将电影推荐给五个用户
print("将电影7034 推荐给以下五位用户："),( model.recommendUsers(7034, 5))  # 将电影 7034 推送给 5 个用户


#将电影id与用户对应
movies = sc.textFile("D:\\test\\ml-latest-small\\movies.csv")
movies = movies.filter(lambda x: "movieId" not in x)   # 去除标题行

print("影库里电影的总数："),( movies.count())
print("前五部电影的名字"),( movies.take(5))
#创建字典 电影id对应的电影名字
movieTitle = movies.map(lambda x: x.split(",")[: 2]).collectAsMap()# 创建字典



recommandP = model.recommendProducts(1, 5)  # 为用户推荐电影
for p in recommandP:
    print("为用户"),( str(p[0])),( "推荐电影《"),( movieTitle[str(p[1])]),( "》，推荐评分："),( p[2])

print("------------------------------------------------------------------------------------------")

