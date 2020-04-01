import os,sys
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