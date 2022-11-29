import random
num = ['1','2','3','4','5','6','7','8','9']
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charbig = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special = ["@",'$','!','#',"%"]

select = [num,char,charbig,special]


def passwordgen():
    password = []
    for i in range(16):
        val = select[random.randint(0,3)]
        password.append(val[random.randint(0,len(val)-1)])
    
    password = ''.join(password)
    print(password)



if __name__ == "__main__":
    passwordgen()