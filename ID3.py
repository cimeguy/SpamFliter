import nltk
import config
import math

#未写完
#需要nltk.download('averaged_perceptron_tagger')
#下载过慢则GitHub：https://github.com/nltk/nltk_data/blob/gh-pages/packages/taggers/averaged_perceptron_tagger.zip
#下载zip文件放入C:\Users\11960\AppData\Roaming\nltk_data\taggers\
#并解压
s=['benoit', 'mandelbrot', '1924', '2010', 'wilmott', 'team', 'mathematician', 'father', 'fractal', 'mathematics', 'advocate', 'sophisticated', 'modelling', 'quantitative', 'finance', 'died', '14th', 'october', 'aged', 'magazine', 'often', 'featured', 'ideas', 'work', 'others', 'inspired', 'fundamental', 'insights', 'you', 'must', 'logged', 'view', 'articles', 'past', 'issues', 'hommies', 'just', 'got', 'phone', 'call', 'roofer', 'come', 'spaying', 'foaming', 'today', 'dusty', 'pls', 'close', 'doors', 'windows', 'could', 'help', 'bathroom', 'window', 'cat', 'sliding', 'door', 'behind', 'know', 'cats', 'survive', 'sorry', 'inconvenience', 'scifinance', 'automatically', 'generates', 'gpu', 'enabled', 'pricing', 'risk', 'model', 'source', 'code', 'runs', '300x', 'faster', 'serial', 'using', 'new', 'nvidia', 'fermi', 'class', 'tesla', 'series', 'scifinance®', 'derivatives', 'development', 'tool', 'concise', 'high', 'level', 'specifications', 'parallel', 'computing', 'cuda', 'programming', 'expertise', 'required', 'automatic', 'monte', 'carlo', 'generation', 'capabilities', 'significantly', 'extended', 'latest', 'release', 'this', 'includes', 'linkedin', 'kerry', 'haloney', 'requested', 'add', 'connection', 'peter', 'like', 'professional', 'network', 'with', 'jose', 'town', 'want', 'meet', 'keep', 'things', 'going', 'interesting', 'stuff', 'let', 'eugene', 'ryan', 'whybrew', 'commented', 'status', 'wrote', 'turd', 'ferguson', 'butt', 'horn', 'that', 'cold', 'retirement', 'party', 'are', 'leaves', 'changing', 'color', 'yay', 'fine', 'working', 'mba', 'design', 'strategy', 'cca', 'top', 'art', 'school', 'program', 'focusing', 'right', 'brained', 'creative', 'strategic', 'approach', 'management', 'way', 'done', 'hello', 'since', 'owner', 'least', 'one', 'google', 'groups', 'group', 'uses', 'customized', 'welcome', 'message', 'pages', 'files', 'writing', 'inform', 'longer', 'supporting', 'features', 'starting', 'february', '2011', 'made', 'decision', 'focus', 'improving', 'core', 'functionalities', 'mailing', 'lists', 'forum', 'discussions', 'instead', 'encourage', 'use', 'products', 'designed', 'specifically', 'file', 'storage', 'page', 'creation', 'docs', 'sites', 'for', 'example', 'easily', 'create', 'share', 'site', 'http', 'www', 'com', 'support', 'bin', 'answer', '174623', 'members', 'also', 'store', 'attaching', '90563', 'looking', 'place', 'upload', 'download', 'suggest', 'try', '50092', 'access', 'either', '66343', 'individual', '86152', 'assigning', 'edit', 'received', 'mandatory', 'email', 'service', 'announcement', 'update', 'important', 'changes', 'sure', 'thing', 'sounds', 'good', 'time', 'would', 'prepared', 'regards', 'vivek', 'thanks', 'definitely', 'check', 'how', 'book', 'heard', 'chapter', 'came', 'shape', 'hope', 'well', 'cheers', 'troy', 'jay', 'stepp', 'reply', 'comment', 'see', 'thread', 'follow', 'link', 'zach', 'hamm', 'doggy', 'style', 'enough', 'said', 'thank', 'night', 'running', 'website', 'jquery', 'jqplot', 'plugin', 'far', 'away', 'prototype', 'launch', 'used', 'think', 'there', 'guy', 'gas', 'station', 'told', 'knew', 'mandarin', 'python', 'get', 'job', 'fbi', 'the', 'hotels', 'ones', 'rent', 'tent', 'they', 'lined', 'hotel', 'grounds', 'much', 'nature', 'couple', 'dozen', 'tour', '100m', 'pictures', 'trip', 'jpgs', 'favorite', 'scenic', 'where', 'jocelyn', 'york', 'will', 'tokyo', 'chinese', 'year', 'perhaps', 'two', 'thailand', 'winter', 'holiday', 'mom', 'take', 'care', 'what', 'talked', 'john', 'computer', 'went', 'bike', 'riding', 'rain', 'museum', 'yesterday', 'free', 'food', 'giants', 'game', 'train', 'fans', 'drunk', 'mail', 'sent', 'notification', 'only', 'address', 'accept', 'incoming', 'please', 'online', 'reservation', 'selected', 'located', 'item', 'placed', 'hold', 'name', 'note', 'items', 'held', 'day', 'prices', 'may', 'differ', 'questions', 'need', 'assistance', 'contact', 'number', 'listed', 'information', 'hours', 'location', 'web', 'borders', 'storedetailview', 'arvind', 'thirumalai', 'julius', 'forward', 'invitation', 'ordercializviagra', 'save', '0nline', 'pharmacy', 'noprescription', 'buy', 'canadian', 'drugs', 'wholesale', 'fda', 'approved', 'superb', 'quality', 'major', 'credit', 'cards', 'order', 'from', 'have', 'everything', 'gain', 'incredib1e', 'gains', 'length', 'inches', 'yourpenis', 'permanantly', 'amazing', 'increase', 'thickness', 'betterejacu1ation', 'control', 'experience', 'rock', 'harderecetions', 'explosive', 'intenseorgasns', 'volume', 'ofejacu1ate', 'doctor', 'endorsed', '100', 'herbal', 'natural', 'safe', 'off', 'watchesstore', 'discount', 'watches', 'all', 'famous', 'brands', 'arolexbvlgari', 'dior', 'hermes', 'oris', 'cartier', 'louis', 'vuitton', 'bags', 'wallets', 'gucci', 'tiffany', 'jewerly', 'enjoy', 'full', 'warranty', 'shipment', 'via', 'reputable', 'courier', 'fedex', 'ups', 'dhl', 'ems', 'speedpost', 'recieve', 'codeine', '15mg', '203', 'visa', 'methylmorphine', 'narcotic', 'opioid', 'pain', 'reliever', '30mg', 'pills', '385', '562', 'home', 'based', 'business', 'opportunity', 'knocking', 'don', 'rude', 'chance', 'earn', 'great', 'income', 'find', 'financial', 'life', 'transformed', 'learn', 'here', 'your', 'success', 'finder', 'experts', 'percocet', '625', 'withoutprescription', 'tabs', '225', 'analgesic', 'treat', 'moderate', 'moderately', 'severepain', 'express', 'shipping', 'discreet', 'private', 'cheap', 'hydrocodone', 'vicodin', 'brand', 'watson', '750', '195', '120', '570', '325', '199', '588', 'days', 'delivery', '200', 'buyviagra', '25mg', '50mg', '100mg', 'brandviagra', 'femaleviagra', 'per', 'pill', 'viagranoprescription', 'needed', 'certified', 'amex', 'worldwide', 'biggerpenis', 'grow', 'safest', 'most', 'effective', 'methods', 'penisen1argement', 'money', 'bettererections', 'ma1eenhancement', 'supplement', 'trusted', 'millions', 'oem', 'adobe', 'microsoft', 'softwares', 'fast', 'office', 'plus', '2007', '129', 'ultimate', '119', 'photoshop', 'cs5', 'acrobat', 'pro', 'thousand', 'titles', 'bargains', 'phentermin', 'genuine', 'low', 'cost', 'accepted', '130', '219', '292', '366', '180', '513', 'competitive', 'price', 'net', 'wilson', '156', '291', 'freeviagra', '396', '492']

def get_characters(info_trainham_list,info_trainspam_list):#获取每个特征的值
    characters=[]
    
    for i in info_trainham_list.keys():#单个文本
        sum=len(info_trainham_list[i]['wordslist'])
        new=nltk.pos_tag(info_trainham_list[i]['wordslist'])#关键词词性标注获得元组
        # print(new)
        singlechar=[]
        Vlist=[]
        Nlist=[]
        CDlist=[]
        for j in new:
            v2=j[1]
            if 'V' in v2:#动词
                Vlist.append(j[0])
            if 'N' in v2:
                Nlist.append(j[0])
            if 'CD' in v2:
                CDlist.append(j[0])
        
        singlechar.append(len(Vlist)/sum)
        singlechar.append(len(Nlist)/sum)
        singlechar.append(len(CDlist)/sum)
        singlechar.append(1)
        characters.append(singlechar)#添加结果
    
    for i in info_trainspam_list.keys():
        sum=len(info_trainspam_list[i]['wordslist'])
        new=nltk.pos_tag(info_trainspam_list[i]['wordslist'])#关键词词性标注获得元组
        singlechar=[]
        Vlist=[]
        Nlist=[]
        CDlist=[]
        for j in new:
            v2=j[1]
            if 'V' in v2:#动词
                Vlist.append(j[0])
            if 'N' in v2:
                Nlist.append(j[0])
            if 'CD' in v2:
                CDlist.append(j[0])
        
        singlechar.append(len(Vlist)/sum)
        singlechar.append(len(Nlist)/sum)
        singlechar.append(len(CDlist)/sum)
        singlechar.append(0)
        characters.append(singlechar)#添加结果
    sumV=0
    sumN=0
    sumCD=0
    for single in characters:
        sumV+=single[0]
        sumN+=single[1]
        sumCD+=single[2]
    aveV=sumV/len(characters)
    aveN=sumN/len(characters)
    aveCD=sumCD/len(characters)
    for single in characters:
        if single[0]>=aveV:
            single[0]=1
        else:
            single[0]=0
        if single[1]>=aveN:
            single[1]=1
        else:
            single[1]=0
        if single[1]>=aveCD:
            single[2]=1
        else:
            single[2]=0
      
    return characters

def ID3decision(ID3list):
    d=converlist(ID3list)
    root=[]
    GV=Entropy(d['S'],d['V'])
    GN=Entropy(d['S'],d['N'])
    GCD=Entropy(d['S'],d['CD'])
    T1=[]
    T2=[]
    if GV>=GN and GV>=GCD:
        root='V'
        T1=GN
        T2=GCD
    elif GN>GV and GN>GCD:
        root='N'
        T1=GV
        T2=GCD
    else:
        root='CD'
        T1=GN
        T2=GV
    D1=[]
    D0=[]
    rootlist=d[root]
    for i in range(len(d[root])):
        if rootlist[i]==1:

    D1=d[root]

def converlist(ID3list):
 
    V_char=[]
    N_char=[]
    CD_char=[]
    S=[]
    #几个特征值
    for t in ID3list:
        V_char.append(t[0])
        N_char.append(t[1])
        CD_char.append(t[2])
        S.append(t[3])
    d={}
    d['V']=V_char
    d['N']=N_char
    d['CD']=CD_char
    d['S']=S
    return d


def Entropy(S,T):#计算信息增益
    #两个列表
    
    countT0S0=0
    countT0S1=0
    countT1S0=0
    countT1S1=0
    for i in range(T):
        if T[i]==0:#当T=0时
            if S[i]==0:
                countT0S0+=1
            else:
                countT0S1+=1
        else:
            if S[i]==0:
                countT1S0+=1
            else:
                countT1S1+=1
    countT0=countT0S1+countT0S0
    countT1=countT1S0=countT1S1
    countT=countT1+countT0
    #T0  math.log(x,2)
    ss0=math.log((countT0S0/countT0),2)*((0-countT0S0)/countT0)
    ss1=math.log((countT0S1/countT0),2)*((0-countT0S1)/countT0)
    EntroyT0=ss0+ss1
    #T1
    ss0=math.log((countT1S0/countT0),2)*((0-countT1S0)/countT0)
    ss1=math.log((countT1S1/countT0),2)*((0-countT1S1)/countT0)
    EntroyT1=ss0+ss1
    E=EntroyT0*(countT0/countT)+EntroyT1*(countT1/countT)
    #S的信息熵
    countS1=countT0S1+countT1S1
    countS0=countT1S0+countT0S0
    countS=countS1+countS0
    ss0=math.log((countS0/countS),2)*((0-countS0)/countS)
    ss1=math.log((countS1/countS),2)*((0-countS1)/countS)
    ES=ss0+ss1
    G=ES-E
    return G