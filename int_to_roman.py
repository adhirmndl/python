conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],[ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],[  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],[   1, 'I']]
class Solution:
    def convert(self,N):
    	N=str(N)
    	s=""
    	for char in N:
    		i = 0;
    		while i < len(conv):
    			if int(char) == int(conv[i][0]):
    				s+=(conv[i][1])
    				i += 1;
    			else:i += 1;
    	return s
print Solution().convert(14)