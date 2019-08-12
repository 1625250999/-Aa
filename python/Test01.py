#coding=utf-8
import re



#if __name__ == '__main__':




    #正则表达 句前匹配
   # str = ["ABccd", "ABcred", "Bccd"]
   # jieguo = []
    #for i in str:
       # if re.findall(r"^AB", i):
          #  jieguo.append(i)
           # print(i)



    #print(re.match('www', 'www.runoob.com').span())
if __name__ == '__main__':

   # tar = "eereaclouzz clur clouud  "

   # print(re.findall(r"clo*u",tar))


    print(re.match('wWw','www.runoob.com',re.I).span())
    print(re.search('www','www.runoob.com').span())

    def va(a):
        '''姓名:小浩'''
        if a > 4:
            print(a+1)
        else:
            print("buhege")
        va(3)

    def pas(name,age,sex):
         print(name,age,sex)
    pas(age=18, name="xiaohao", sex="nan")

    def jf(a, b=3):
        print(a+b)
    jf(3)

    name = {"a":"b","c":"d"}
    def kbcs(**name):
        for key,value in  name.items():
            print (key,value)

    kbcs(**name) #shuchu1
    kbcs(a="b",c="d") #shuchu2



    def cf(a,b):
        c = a*b
        return c
    v = cf(2,3)
    print(v)


#定义一个类 写了一个方法  最后调用这个类的构造方法以及自定义方法
class lei:
    '''这是一个类'''
    name ="cc"

    def __init__(self):
        print(name)
    def a(self,v,n):
        print(v*n)
a = lei()
a.name


a = 10
print( "a"  +"\t" + a)