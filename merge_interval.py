class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	def display(self):
		return (self.start,self.end)
def display(A):
	for i in A:
		print i.display(),
class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, A,B):
    	i=0
    	if B.start>A[-1].end:
    		A.append(B)
    		return A
    	elif B.end<A[0].start:
    		return [B]+[A]
    	elif B.start==A[-1].end:
            A[-1].end = B.end
            return A
    	freash = []
    	while i<len(A) and A[i].end<B.start:
    		freash.append(A[i])
    		i+=1
    	j=i

    	while j<len(A) and A[j].start<B.end:
    		j+=1
    	if A[j].start>B.end:
    		j-=1
    	freash.append(Interval(min(A[i].start,B.start),max(A[j].end,B.end)))
    	for i in range(j+1,len(A)):
    		freash.append(A[i])
    	return freash

a=[Interval(1,2),Interval(3,4),Interval(15,16),Interval(17,18),Interval(19,20),Interval(21,22)]
#display(Solution().insert(a,Interval(22,27)))
display(Solution().insert(a,Interval(21,22)))
#display(Solution().insert(a,Interval(22,27)))
#display(Solution().insert(a,Interval(22,27)))








