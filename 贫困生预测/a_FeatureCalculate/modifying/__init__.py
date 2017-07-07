# from mrjob.job import MRJob
# 
# class MRWordCounter(MRJob):
#     def mapper(self,key,line): #接收每一行的输入数据，处理后返回一堆key:value，初始化value值为1
#         for word in line.split():
#             yield word,1
# 
#     def reducer(self,word,occurrences): #接收mapper输出的key:value对进行整合，把相同key的value做累加（sum）操作后输出
#         yield word,sum(occurrences)
# 
# if __name__ == '__main__':
#     MRWordCounter.run()