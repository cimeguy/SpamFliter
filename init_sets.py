import os ,sys
import random
from config import hampath,spampath,testpath,trainpath,train_ratio
import shutil
import convertformat as cf

def init_testfiles():  #初始化，按照设定比率，随机选择测试集和训练集
    hamlist=getfiles(hampath)#所有ham 包括测试和训练
    spamlist=getfiles(spampath)
    #随机选择训练、测试ham
    train_hamlist=random.sample(hamlist,int(len(hamlist)*train_ratio))#按设定比率,随机选择ham作为训练集
    test_hamlist=[]#其余ham作为测试集
    for i in hamlist:
        if i not in train_hamlist:
            test_hamlist.append(i)
    #随机选择训练、测试spam
    train_spamlist=random.sample(spamlist,int(len(hamlist)*train_ratio))
    test_spamlist=[]
    for i in spamlist:
        if i not in train_spamlist:
            test_spamlist.append(i)
    #清空上次运行的文件夹
    RecreateDir(trainpath)
    RecreateDir(testpath)
    #移动文件
    movefiles(testpath,test_hamlist,hampath)
    movefiles(testpath,test_spamlist,spampath)
    movefiles(trainpath,train_spamlist,spampath)
    movefiles(trainpath,train_hamlist,hampath)
    #转换编码
    # cf.convertDir(testpath)
    # cf.convertDir(trainpath)
    print('初始化成功，测试集在test中，训练集在train中')
    return train_hamlist,test_hamlist,train_spamlist,test_spamlist#返回文件名

def getfiles(path):#获取某个目录（文件夹）下所有文件名，返回文件名列表
    fileslist=[]
    for root, dirs, files in os.walk(path):  #目录路径
        
        for file in files:
            fileslist.append(file)
    return fileslist

def RecreateDir(dirpath):#重新创建文件夹 用于划分测试集和训练集用

    if os.path.exists(dirpath):  # 如果文件夹存在
        shutil.rmtree(dirpath)    #递归删除文件夹
        os.makedirs(dirpath)#并创建新文件夹
    else:#否则创建新文件夹
        os.makedirs(dirpath)
        
def movefiles(destdir,pathlists,srcdir):#批量复制文件到另外的目录，pathlists是文件名，不包含目录
    srcpath=''
    destpath=''
    for path in pathlists:
        srcpath=srcdir+path
        destpath=destdir+path
        shutil.copyfile(srcpath,destpath)