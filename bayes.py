from main import testpath
import wordfreq as wf
from config import testpath
import config
thispath=testpath
#未作平滑处理的伯努利模型  联合概率分布 阈值判断
def naivebayes(file,filename,wordfreq_intrainham_dict,wordfreq_intrainspam_dict,Threshold,usetfidf=True):
    Ps=0.5#先验概率
    Ph=0.5
    words=[]
    if usetfidf==True:#使用tfidf过滤
        words=file['wordslist']
    else:#不使用tfidf
        words,sent=wf.WordsListofFile(filename=filename,dirpath=thispath)
    
    Ps_w_dict={}
    countnewword=0
    newword=[]
    for word in words:#  经过tf-idf处理
        #第一次出现
        if word not in wordfreq_intrainspam_dict.keys():
            Ps_w=0.4
            countnewword+=1
            newword.append(word)
            #原先的spam中没有这个单词
            # Update(filename,info_train_hamlist,allwordslist,sumofhamtrain)
        elif word not in wordfreq_intrainham_dict.keys():
            Ps_w=0.4
            countnewword+=1
            newword.append(word)
        #其他词
        else:
            Pws=wordfreq_intrainspam_dict[word]
            Pwh=wordfreq_intrainham_dict[word]
            Pw=(Pws*Ps)+(Pwh*Ph)
            Ps_w=(Pws*Ps)/(Pw)
        Ps_w_dict[word]=Ps_w#添加
    
    son =1
    mother=1
    motherpart1=son
    motherpart2=1
    # print(Ps_w_dict)
    #联合概率
    for word in Ps_w_dict.keys():#朴素贝叶斯  相互独立
        
        son*=Ps_w_dict[word]
        motherpart1=son
        motherpart2*=(1-Ps_w_dict[word])
        mother=motherpart1+motherpart2
    p=son/mother
    if p>Threshold:
        return False,Ps_w_dict,p#垃圾邮件
    else:
        return True,Ps_w_dict,p
    # return p
#作了平滑处理的伯努利模型  联合概率分布 阈值判断
def bernoulli(file,filename,info_train_spamlist,info_train_hamlist,allwordslist,Threshold,usetfidf=True):
    Ps=0.5#先验概率
    Ph=0.5
    words=[]
    if usetfidf==True:#使用tfidf过滤
        words=file['wordslist']
    else:#不使用tfidf
        words,sent=wf.WordsListofFile(filename=filename,dirpath=thispath)
    
    Ps_w_dict={}
    
    for word in words:#  #每一个单词
        #第一次出现
        counts=0
        counth=0
        for each in info_train_spamlist.keys():#每一篇    
            if(wf.isWordexistsinFile(info_train_spamlist,each,word)):
                #如果存在
                counts+=1
        counts+=1
        for each in info_train_hamlist.keys():#每一篇    
            if (wf.isWordexistsinFile(info_train_hamlist,each,word)):
                counth+=1

        counth+=1#拉普拉斯平滑
        Pws = counts/(config.sumofspamtrain+2)#仅此处不同
        Pwh = counth/(config.sumofhamtrain+2)
        Pw=(Pws*Ps)+(Pwh*Ph)
        Ps_w=(Pws*Ps)/(Pw)
        Ps_w_dict[word]=Ps_w#添加
    
    son =1
    mother=1
    motherpart1=son
    motherpart2=1
    #联合概率
    for word in Ps_w_dict.keys():#朴素贝叶斯  相互独立
        
        son*=Ps_w_dict[word]
        motherpart1=son
        motherpart2*=(1-Ps_w_dict[word])
        mother=motherpart1+motherpart2
    p=son/mother
    if p>Threshold:
        return False,Ps_w_dict,p#垃圾邮件
    else:
        return True,Ps_w_dict,p
        

#多项式 极大似然估计、贝叶斯估计
def polynomial(file,filename,allwords_trainhamlist_r,allwords_trainspamlist_r,allwordslist_r,usetfidf=True,uselapras=True):#返回PH和PS
    num_words_th_r=len(allwords_trainhamlist_r)
    num_words_ts_r=len(allwords_trainspamlist_r)
    num_words_t_r=len(allwordslist_r)
    #先验概率
    allwordslist,num_words_t = unrepeat(allwordslist_r)#去重
    
    if usetfidf==True:#使用tfidf过滤
        words=file['wordslist']
    else:#不使用tfidf
        words,sent=wf.WordsListofFile(filename=filename,dirpath=thispath)
    Ps_w_dict={}
    
    
    lamda=0
    K=2
    if uselapras==True:
        #使用拉普拉斯平滑
        lamda=1
    Klamda=K*lamda
    Ps=(num_words_ts_r+lamda)/(num_words_t_r+Klamda)#平滑处理
    Ph=(num_words_th_r+lamda)/(num_words_t_r+Klamda)
    Ph_t=Ph
    Ps_t=Ps
    for word in words:#将每个单词作为一个特征,以单词为粒度
        scountword=countword_inlist(word,allwords_trainhamlist_r)#在ham下出现次数之和
        Pw_h=(scountword+lamda)/(len(allwords_trainhamlist_r)+num_words_t)#类ham下单词在各个文档中出现过的次数之和+1/类下单词的总数(可重复)+总训练样本的不重复单词
        scountword=countword_inlist(word,allwords_trainspamlist_r)
        Pw_s=(scountword+lamda)/(len(allwords_trainspamlist_r)+num_words_t)
        Ph_t*=Pw_h
        Ps_t*=Pw_s
       
    if Ph_t>=Ps_t:
        return True,Ps_t#返回垃圾邮件的概率
    else:
        return False,Ps_t

def unrepeat(wordlistr):
    allwords=[]
    for i in wordlistr:
        if  i not in allwords:
            allwords.append(i) 
    
    return allwords,len(allwords)



def countword_inlist(word,wlist):
    count=0
    for i in wlist:
        if i==word:
            count+=1
    return count