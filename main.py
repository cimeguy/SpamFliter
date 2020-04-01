# import graphviz
import os,sys
import bayes
import random
import shutil
from nltk.corpus import stopwords
import nltk
import convertformat as cf
import init_sets as init
import wordfreq as wf
import tfidf
import matplotlib.pyplot as plt
train_ratio=0.8
sumofspam=25
sumofham=25
sumofemail=sumofham+sumofspam

sumoftrain=int(sumofemail*train_ratio)
sumoftest=sumofemail-sumoftrain
sumofhamtrain=int(sumofham*train_ratio)
sumofhamtest=sumofham-sumofhamtrain
sumofspamtrain=int(sumofspam*train_ratio)
sumofspamtest=sumofspam-sumofspamtrain
path =os.path.abspath(os.path.dirname(sys.argv[0]))#当前路径
hampath=path+'\\email\\ham\\'
spampath=path+'\\email\\spam\\'
testpath=path+'\\test\\'
trainpath=path+'\\train\\'


if __name__ == "__main__":

    #对文件夹内的文本全部进行编码转换，这一步做一次就可以了
    # cf.convertDir(hampath)
    # cf.convertDir(spampath)
    #当直接剔除新出现的单词时，误判率
    with open('mylog.txt','a')as f:
        f.write("=========================================")
    time=5#运行次数
    Threshold=0.9#垃圾邮件阈值
    num_maxtfidfwords=15#只留下tfidf最大的几个值 目的是为了去除常见的词
    usetfidf=True
    with open('mylog.txt','a')as f:
        f.write("运行次数={0}\n".format(time))
        if usetfidf:
            f.write("利用TF-IDF算法，每篇文章保留{0}个特征单词\n".format(num_maxtfidfwords))
        else:
             f.write('不使用TF-IDF算法\n')
        f.write("检测垃圾邮件的阈值{0}\n".format(Threshold))
    average_accur=0
    sum_accur=0
    Accuracy=[0]*time
    
        
    for j in range(time):
        with open('mylog.txt','a')as f:
            f.write('\nNo.'+str(j))
        print('第{}次'.format(j+1))
        train_hamlist,test_hamlist,train_spamlist,test_spamlist=init.init_testfiles()#文件名列表
        train_list=train_spamlist+train_hamlist
        test_list=test_hamlist+test_spamlist
        contents_train_list=[]#储存所有处理好的的txt对应的句子
        
        info_train_hamlist={}#储存train_ham每篇的信息
        info_train_spamlist={}
        info_test_hamlist={}#储存test_ham每篇的信息
        info_test_spamlist={}
        for i in train_hamlist:
            dict1={}
            dict1['wordslist'],dict1['content']=wf.WordsListofFile(i,trainpath)
            contents_train_list.append(dict1['content'])
            info_train_hamlist[i]=dict1
        for i in train_spamlist:
            dict1={}
            dict1['wordslist'],dict1['content']=wf.WordsListofFile(i,trainpath)
            contents_train_list.append(dict1['content'])
            info_train_spamlist[i]=dict1
        allwordslist=tfidf.getallword(contents_train_list,repeat=False)#获得所有单词  不重复
        allwordslist_canrepeat=tfidf.getallword(contents_train_list,repeat=True)#总单词
        for i in test_hamlist:
            dict1={}
            dict1['wordslist'],dict1['content']=wf.WordsListofFile(i,testpath)
            info_test_hamlist[i]=dict1
        for i in test_spamlist:
            dict1={}
            dict1['wordslist'],dict1['content']=wf.WordsListofFile(i,testpath)
            info_test_spamlist[i]=dict1
        #通过tfidf预处理
        #tfidf#train
        info_train_hamlist=tfidf.getallwordtfidf_text(info_train_hamlist,contents_train_list)#获取各个词的tfidf值
        info_train_hamlist=tfidf.get_maxtfidf_word(info_train_hamlist,num_maxtfidfwords)#去除小的值
        info_train_spamlist=tfidf.getallwordtfidf_text(info_train_spamlist,contents_train_list)
        info_train_spamlist=tfidf.get_maxtfidf_word(info_train_spamlist,num_maxtfidfwords)
        #test 注意是在contents_train_list环境中获得tfidf值
        info_test_hamlist=tfidf.getallwordtfidf_text(info_test_hamlist,contents_train_list)#获取各个词的tfidf值
        info_test_hamlist=tfidf.get_maxtfidf_word(info_test_hamlist,num_maxtfidfwords)#去除小的值
        info_test_spamlist=tfidf.getallwordtfidf_text(info_test_spamlist,contents_train_list)
        info_test_spamlist=tfidf.get_maxtfidf_word(info_test_spamlist,num_maxtfidfwords)
        #计算词频
        wordfreq_intrainham_dict=wf.wordsfreq(info_train_hamlist,allwordslist,sumofhamtrain)
        wordfreq_intrainspam_dict=wf.wordsfreq(info_train_spamlist,allwordslist,sumofspamtrain)
        #联合概率贝叶斯
        
        
        counthamok=0
        countspamok=0
        for i in range(len(test_hamlist)):
            filename=test_hamlist[i]
            ham=info_test_hamlist[filename]
            okemail,pswdict,p=bayes.naivebayes(ham,filename,wordfreq_intrainham_dict,wordfreq_intrainspam_dict,Threshold=Threshold,usetfidf=usetfidf)
            if okemail:
                #如果检测正确
                counthamok+=1
            else:#检测失败
                with open('mylog.txt','a')as f:
                    f.write("\nFail:"+test_hamlist[i])
                    f.write('\n{0}\n'.format(pswdict))
                print('\nFail：'+test_hamlist[i]+':',p)#输出文件名
                print(pswdict)
        for i in range(len(test_spamlist)):
            filename=test_spamlist[i]
            spam=info_test_spamlist[filename]
            okemail,pswdict,p=bayes.naivebayes(spam,filename,wordfreq_intrainham_dict,wordfreq_intrainspam_dict,Threshold=Threshold,usetfidf=usetfidf)
            if okemail==False:
                countspamok+=1
            else:#检测失败
                with open('mylog.txt','a')as f:
                    f.write("\nFail:"+test_spamlist[i])
                    f.write('\n{0}\n'.format(pswdict))
                print('\nFail：'+test_spamlist[i]+':',p)#输出文件名
                print(pswdict)
        Accuracy[j]=(counthamok+countspamok)/sumoftest
        print(Accuracy[j])#计算正确性
        sum_accur+=Accuracy[j]
    # 
    average_accur=sum_accur/time
    print("平均正确率：", average_accur)
    with open('mylog.txt','a')as f:
        f.write("平均正确率：{0}\n".format(average_accur))
    x=[x for x in range(1,time+1)]
    y=Accuracy[:]
    plt.scatter(x,y)
    plt.show()
    # for key in info_train_hamlist.keys():
    #     print(wf.isWordexistsinFile(info_train_hamlist,key,info_train_hamlist[key]['wordslist'][0]))
        
    # print(info_train_hamlist)
    # train_dict=dict.fromkeys(train_list,{})
    # test_dict=dict.fromkeys(test_list,{})
    # test_dict,train_dict,allworddict=wordfreqall(test_dict,train_dict)
    # print(allworddict['alltestwords'])

