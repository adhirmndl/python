'''
2
timetopractice
toc
zoomlazapzo
oza
'''

def change(s,pos):
    return s[:pos] +'.'+ s[pos+1:]
#t=int(input())
t=1
import sys
while(t):
    t-=1;
    #a=input().strip()
    a='timetopractice'
    #b=input().strip()
    b='toc'
    data = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    loop_stop = False
    for i in range(len(a)):
    	if loop_stop:break
    	s=a[i:]
    	mx=i
    	for j in b:
    		#print j,"j"
    		pos_ = s.find(j)
    		if pos_==-1 or j not in s:
    			#print "yes, loop _stop"
    			loop_stop=True
    			break
    		#else:
    			#print pos_,j,i,s
    		mx=max(mx,pos_)
    		print i,mx
    		s=change(s,pos_)
    	if not loop_stop:
    		if len(data)> len(a[i:mx+1]) and s.count('.') == len(b):
    			data = a[i:mx+1]
    print (data)