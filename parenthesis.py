import sys
def oppo(a):
    if a==')':return '('
    elif a=='}':return '{'
    elif a==']':return '['
t = int(raw_input().strip())
for a0 in range(t):
    A = raw_input().strip()
    
    a=[];b=[];
    for i in A:
        if i in ['(','{','[']:
            a.append(i)
        else:
            if 

    print a
    print b
    print ("YES" if a==b else "NO")