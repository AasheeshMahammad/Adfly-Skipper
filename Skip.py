from base64 import b64decode
from urllib.request import urlopen,Request
import pyperclip


def Algorithm(data):
    zeros, ones = '', ''
    for num, letter in enumerate(data):
        if num % 2 == 0: zeros += data[num]
        else: ones = data[num] + ones

    key = zeros + ones
    temp=[]
    for i in key:
        temp.append(i)
    #print(key)
    key=temp
    #print(key)
    i=0
    while i != len(key):
        hlp=0
        if str(key[i]).isnumeric():
            for y in range(i+1,len(key)):
                if str(key[y]).isnumeric():
                    hlp=hlp+1
                    temp=int(key[i])^int(key[y])
                    if int(temp) < 10:
                        #print(key[i],' ',key[y]," ",temp)
                        key[i]=str(temp)
                    i=y+1
                    break
        if hlp==0:
            i=i+1
            
    temp="".join(key)
    key=temp
    key = b64decode(key.encode("utf-8"))
    return key.decode('utf-8')

def Decrypt(url=0):
    if url==0:
        return
    req = Request(url, headers={'User-Agent': 'Chrome/91.0.4472.77'})  
    data_ = urlopen(req)
    data=data_.read()
    ysmm = data.split(b"ysmm = '")[1].split(b"';")[0]
    data_.close()
    ysmm=str(ysmm)
    ysmm.replace("\'","")
    temp=""
    s=0
    for i in range(0,len(ysmm)):
        if s==1 and ysmm[i]!="'":
            temp=temp+ysmm[i]
        if ysmm[i]=="'":
            s=1
    ysmm=temp
    decrypted_url = Algorithm(ysmm)
    decrypted_url=decrypted_url[16:-16]
    return str(decrypted_url)
    
if __name__=="__main__":    
    link=input("Enter Link :")
    decrypted_link=Decrypt(link)
    pyperclip.copy(decrypted_link)
    print(decrypted_link)