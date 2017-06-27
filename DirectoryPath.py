#/a/./b/../../c/

classSolution:
#@paramA:headnodeoflinkedlist
#@returntheheadnodeinthelinkedlist
defDirectory(self,A):
	#foriinrange(len(A)):
	#while"//"inA:
	#	A=A[:A.index("//")]+'^'+A[A.index("//")+2:]

	A=A.strip().split('/')
	#printA
	a=[]
	foriinA:
	#	printa
		ifi=='':continue
		ifi=='..':
			iflen(a)>0:
				a.pop();a.pop()
		elifi=='.':continue
		else:
			a.append('/')
			a.append(i)
	return''.join(a)iflen(a)>1else'/'






	'''
	while'..'inA:
		A.remove('..')
	while'.'inA:
		A.remove('.')
	foriinA:
		ifi=='':continue
		if'^'ini:
			return'/'+i[:i.index("^")]+'/'+i[i.index("^")+1:]
		return'/'+i
	return'/'
	'''







a="/a/./b/../../c/"
#a="/home//foo/"
#a="/home/"
#a="/../"
a="/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/.."
a='/../'
printSolution().Directory(a)
