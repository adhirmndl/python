import sys
d=[]
data=[]
def rr(r_0,g,s,p):
	return (r_0*g+s)%p
def rec(a,b,c,pos,cnt):
	if d[pos]==0:
		return 
	if pos-1 in [a,b,c]:
		data.append(cnt)
		return 
	k=l=-1
	dp=d[pos]
	d[pos]=0
	if pos+dp<len(d):
		rec(a,b,c,pos+dp,cnt+1)
	if pos-dp>-1:
		l=rec(a,b,c,pos-dp,cnt+1)


def circularWalk(n, s, t, r_0, g, seed, p):
	global d
	d.append(r_0)
	for i_ in range(1,n):
		d.append(rr(d[len(d)-1],g,seed,p))
	cl=len(d)
	d+=d+d

	rec(t,cl+t,2*cl+t,cl+s,0)


n, s, t = raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
if len(data)==0:print (-1)
else: print (min(data))
