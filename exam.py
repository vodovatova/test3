import re 
def func1(): 
    a = open ('C:\\Users\\student\\Desktop\\mihaylov.txt', 'r', encoding = 'UTF-8') 
    f = a.read() 
    a.close() 
    return f 

def func2(f): 
    regex ='[А-Я]\. [А-ЯЁ][а-яё]+' 
    c = re.findall(regex, f) 
    for regex in c: 
        n = ', '.join(c) 
    if c: 
        print(n) 

def main(): 
    q = func1() 
    func2(q) 

if __name__=='__main__': 
    main()
