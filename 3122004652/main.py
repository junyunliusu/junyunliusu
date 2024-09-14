import sys
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#采用余弦相似度算法计算文本相似度
def company(p1, p2):
    vectorizer = CountVectorizer()
    list = [p1, p2]#将两个文件拼接为列表
    vectors = vectorizer.fit_transform(list)#先拟合数据，然后转化它将其转化为标准形式，一步到位
    similarity = cosine_similarity(vectors)
    return similarity[0][1]

def readfile(address):
    f = open(address,'r',encoding='utf-8')   #设置文件对象
    p = f.read()
    f.close()
    return p

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()#为读取命令行参数作准备
    parser.add_argument('add1', type=str, default = None)
    parser.add_argument('add2', type=str, default=None)
    parser.add_argument('add3', type=str, default=None)
    args = parser.parse_args()
    p1=readfile(args.add1)
    p2=readfile(args.add2)
    result = company(p1, p2)*100
    f=open(args.add3,'w',encoding='utf-8')
    f.write("两个文本相似度为： %.2f"%result)#采用百分制，保留两位小数
    f.close()
