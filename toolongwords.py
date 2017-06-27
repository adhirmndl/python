'''
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

'''

n=int(raw_input())
for i__ in range(n):
	s=raw_input().strip()
	a=s[1:len(s)-1]
	if len(a)<=n-2:
		print s
	else:print s[0] + str(len(a)) + s[-1]