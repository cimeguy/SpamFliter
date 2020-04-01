from nltk.text import TextCollection
import nltk
def getallwordtfidf_text(info_list,contents_list):#第一个是集合的信息表，contents_list是所有文章转化为句子的总列表
    for key ,val in info_list.items():
        #每一篇
        content=val['content']
        info_list[key]['tfidf']=computeTFIDF_text(texts=contents_list,singletext=content)
    return info_list

def computeTFIDF_text(texts,singletext):#texts是句子字符串列表（语料库）,singletext单个句子字符串,
    texts=[nltk.word_tokenize(text) for text in texts]#对句子列表所有句子分词
    
    corpus = TextCollection(texts)
    words=nltk.word_tokenize(singletext) #单词列表
    tfidf_words={}
    #计算机tfidf
    for word in words:
        idf=corpus.idf(word)#tf
        tf=corpus.tf(word, words)#idf
        tfidf=idf*tf
        tfidf_words[word]=tfidf
    return tfidf_words


def get_maxtfidf_word(info_list,num_maxtfidfwords):#获得几个最大tfidf值的单词
    for key  in info_list.keys():
        #每一篇
        d= info_list[key]['tfidf']
        L=list(d.items())       # 得到列表
        L.sort(key=lambda x:x[1],reverse=True)  #
        if num_maxtfidfwords>len(L):
            info_list[key]['maxtfidf']=L
        else:
            info_list[key]['maxtfidf']=L[:num_maxtfidfwords]
        for i in L[num_maxtfidfwords:]:
            
            info_list[key]['wordslist'].remove(i[0])#删除低tfidf 的概率
        
    return info_list
#h获得所有单词
def getallword(contents_list,repeat=False):#repeat允许重复
    text=' '.join(contents_list)
    allwords1=nltk.word_tokenize(text)#对句子列表所有句子分词
    #去重
    if repeat:
        return allwords1
    else:

        allwords=[]
        for i in allwords1:
            if not i in allwords:
                allwords.append(i) 
        return allwords
