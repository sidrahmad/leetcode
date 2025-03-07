class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        #Seive of Eratoshenes
        def get_primes():
            is_prime=[True]*(right+1)
            is_prime[0]=is_prime[1]=False

            for n in range (2,int(sqrt(right))+1):
                if not is_prime[n]:
                    continue
                for m in range (n+n,right+1,n):
                    is_prime[m]=False
            primes=[]
            for i in range (len(is_prime)):
                if is_prime[i] and i>=left:
                    primes.append(i)
            return primes



        primes= get_primes() #all prime numbes
        res = [-1,-1]
        diff = right - left + 1

        for i in range (1,len(primes)):
            if primes[i]-primes[i-1] < diff:
                diff = primes[i]-primes[i-1]
                res =  [primes[i-1],primes[i]]
        return res
