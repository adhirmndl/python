def colorful(A):
        prod = {}
        digit_prod = {}
        A = str(A)
        for char in A :
            num = int(char)
            if prod.get(num, None) == None :
               prod[num] = char
               digit_prod[char] = num
            else :
                return 0
        #print prod
        #print digit_prod
        for i in range(2, len(A)+1) :
            for j in range(len(A) - i + 1) :
                char = A[j : j + i]
                #print char
                p = digit_prod[char[: i - 1]] * digit_prod[char[-1]]
                if prod.get(p, None) == None :
                    prod[p] = char
                    digit_prod[char] = p
                else :
                    return 0
                #print prod
                #print digit_prod
        #print prod
        #print digit_prod

        return 1


print colorful(3245)