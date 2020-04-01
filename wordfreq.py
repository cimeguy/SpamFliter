import main
from config import hampath,spampath,testpath,trainpath,train_ratio#运行main.py时不需要引用
from nltk.corpus import stopwords
import nltk


def readfile(filename,dirpath):#根据文件名获取文件内容
    with open(dirpath+filename,'r',encoding='utf-8') as f:#utf-8
        lines=f.readlines()
    return lines

def WordsListofFile(filename,dirpath):#获取单词列表和预处理后的单词的连接的句子
    lines=readfile(filename,dirpath)#获取句子列表
    
    content = (' '.join(lines)).replace('\r\n', ' ').replace('\t', ' ').replace('\n',' ')
    disease_List= nltk.word_tokenize(content)
    #去停用词
    filtered = [w for w in disease_List if(w not in stopwords.words('english'))]
    #去除标点符号
    punctuations = """,.:<>()*&^%$#@!'";~`[]{|、}\\/~+_-=?"""
    content=' '.join(filtered)
    for punctuation in punctuations:
        
        content = (' '.join(content.split(punctuation))).replace('  ', ' ')
        #小写 并去掉单个字母的单词
        word = [word.lower()for word in content.split(' ') if len(word) > 2]
    words_list=word
    words_sent=' '.join(word)#将所有单词连接成句子返回

    return words_list, words_sent

def isWordexistsinFile(info_lists,filename,word):
    if word in info_lists[filename]['wordslist']:
        return True
    else:
        return False
def wordsfreq(info_lists,wordlists,n):#n是文件个数
    d={}
    for word in wordlists:
        
        count=0
        for each in info_lists.keys():#每一篇    
            
            if(isWordexistsinFile(info_lists,each,word)):
                #如果存在
                count+=1
        if count==0:
            freq=0.01
        else:
            freq=count/n
        d[word]=freq
    
    return d



# def wordfreq_singletext(filename):
#     lines=readfile(filename)
#     content = (' '.join(lines)).replace('\r\n', ' ').replace('\t', ' ').replace('\n',' ')
#     disease_List= nltk.word_tokenize(content)
#     #去停用词
#     filtered = [w for w in disease_List if(w not in stopwords.words('english'))]
#     #去除标点符号
#     punctuations = """,.:<>()*&^%$#@!'";~`[]{|、}\\/~+_-=?"""
#     content=' '.join(filtered)
#     for punctuation in punctuations:
        
#         content = (' '.join(content.split(punctuation))).replace('  ', ' ')
#         #小写 并去掉单个字母的单词
#         word = [word.lower()for word in content.split(' ') if len(word) > 2]
#     freq = nltk.FreqDist(word)#词频统计
#     wordfreq={}
#     words_of_text_list=[]
#     for key,val in freq.items():
#         # print (str(key) + ':' + str(val))
#         wordfreq[str(key)]=val
#         words_of_text_list.append(str(key))
#     return wordfreq

# def wordfreqall(test_dict,train_dict):
#     allworddict={}
#     allworddict['allwords']={}
#     allworddict['alltestwords']={}
#     allworddict['alltrainwords']={}
#     for key in test_dict.keys() :#对于每一个test文件
       

#         test_dict[key]=wordfreq_singletext(testpath+'\\'+key)
#         for word in test_dict[key].keys():
#             if word in allworddict.keys():
#                 allworddict['allwords'][word]+=1#统计单词出现的文字书
#             else:
#                 allworddict['allwords'][word]=1
#         # for word in test_dict[key].keys():
#             if word in allworddict['alltestwords'].keys():
#                 allworddict['alltestwords'][word]+=1
#             else:
#                 allworddict['alltestwords'][word]=1
     
#     for key in train_dict.keys():
#         train_dict[key]=wordfreq_singletext(trainpath+'\\'+key)
#         for word in train_dict[key].keys():
#             if word in allworddict.keys():
#                 allworddict['allwords'][word]+=1
#             else:
#                 allworddict['allwords'][word]=1
#             if word in allworddict['alltrainwords'].keys():
#                 allworddict['alltrainwords'][word]+=1
#             else:
#                 allworddict['alltrainwords'][word]=1
   




#     return test_dict,train_dict,allworddict

# if __name__ == "__main__":
#     words,content=WordsListofFile('h2.txt',trainpath)
#     print(words,content)
