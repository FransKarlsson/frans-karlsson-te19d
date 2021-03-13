def morse(x):
    morseCode={}
    medelande=''
    x=x.upper()
    with open('morse.txt', 'r', encoding='utf8') as f:
        f=f.read()
        f=f.split('\n')
    
    for i in f:
        morseCode[i[0]]= i[3:]
    
    for i in x:
        if i == ' ':
            medelande+='/'
        try:
             medelande+=morseCode[i]
        except KeyError:
            medelande+=i
        medelande+=' '
    
    return medelande

    

print(morse('gus gus buss 123'))        