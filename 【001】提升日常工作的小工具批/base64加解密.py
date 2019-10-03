import base64

'''
Date:2019-10-3
Authour:DASHU
中文base64加解密程序
'''

def jiami(jia):
    a = base64.b64encode(jia.encode('utf-8')).decode('utf-8')
    print (a)
    
def jiemi(jie):
    a = base64.b64decode(jie.encode('utf-8')).decode('utf-8')
    print (a)
    
if __name__ == '__main__':
    jia = input('输入要加密的字符:')
    jiami(jia)
    jie = input('输入要解密的字符:')
    jiemi(jie)
    
