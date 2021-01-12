import string
import random
def password_genrater(pass_len):
    s1=list(string.ascii_lowercase)
    s2=list(string.ascii_uppercase)
    s3=list(string.punctuation)
    s4=list(string.digits)
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    #if i dont use here join function then it will return me a list 
    return (''.join(s[0:pass_len]))
if __name__ == "__main__":
    a= password_genrater(7)
    print(a)