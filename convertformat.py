import chardet
import os
#编码转换

def converformat(file):
    filename=os.path.splitext(file)
    print(('convert{0}.{1}').format(filename[0],filename[1]))
    with open (file,'rb+')as f:
        content=f.read()
        encode=chardet.detect(content)['encoding']
        if(encode!='utf-8'):
            try:
                gbk_content=content.decode(encode)
                utf_byte=bytes(gbk_content,encoding='utf-8')
                f.seek(0)
                f.write(utf_byte)
            except IOError:
                print('fail')



def convertDir(dirpath):
    print('====================编码转化=======================')
    for file in os.listdir(dirpath):
        file = os.path.join(dirpath,file)
        converformat(file)

