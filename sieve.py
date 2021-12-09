## CountNonDivisible
#
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # sorted_mylist = sorted(((v, i) for i, v in enumerate(A)), reverse=True)
    # print(sorted_mylist)
    results = dict()
    resarray = [0] * len(A)
    for i in range(len(A)):
        count = results.get(A[i], 0)
        if count == 0:
            for j in range(len(A)):
                if i != j:
                    if A[i] % A[j] ==0:
                        pass
                    else:
                        count += 1
            results[A[i]] = count
            resarray[i] = count
        else:
            # print(i, A[i], count)
            resarray[i] = count
    return resarray


def create_prime(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    i = 2
    while(i*i <=n):
        if sieve[i]:
           k = i * i
           while  k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve


def arrayF(n):
    F = [0] * (n+1)
    i =2
    while (i * i <n):
        if (F[i] == 0):
            k = i*i
            while k <=n:
                if F[k] ==0:
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x,F):
    primefactor = []
    while F[x] > 0:
        primefactor += [F[x]]
        x = x // F[x]
    primefactor += [x]
    return primefactor


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

###CountNonDivisible
def solution(A):
    # write your code in Python 3.6

    A_max = max(A)

    count = {}

    for element in A:

        if element not in count:

            count[element] = 1

        else:

            count[element] += 1



    divisors = {}

    for element in A:

        divisors[element] = set([1, element])



    # start the Sieve of Eratosthenes

    divisor = 2

    while divisor*divisor <= A_max:

        element_candidate = divisor

        while element_candidate  <= A_max:

            if element_candidate in divisors and not divisor in divisors[element_candidate]:

                divisors[element_candidate].add(divisor)

                divisors[element_candidate].add(element_candidate//divisor)

            element_candidate += divisor

        divisor += 1



    result = [0] * len(A)

    for idx, element in enumerate(A):

        result[idx] = (len(A)-sum([count.get(divisor,0) for divisor in divisors[element]]))



    return result


### CountSemiPrimes

def create_semiprime(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1]= sieve[2]= sieve[3] = False
    F = arrayF(n)
    for i in range(5, n):
        if len(factorization(i, F)) ==2:
            sieve[i] = True
        else:
            sieve[i] = False
    suffixarry = [0] * (n+1)
    # print(sieve)
    # sieve.append(sieve[-1])
    for j in range(1, n+1):
        suffixarry[j] = suffixarry[j-1] + sieve[j]
    print(suffixarry)
    # suffixarry.append(suffixarry[-1])
    return suffixarry

def solution(N, P, Q):
    # write your code in Python 3.6
    # you can write to stdout for debugging purposes, e.g.
    if N < 4:
        return [0] * len(P)
    else:
        suffixarray = create_semiprime(N)
        results = [0] * len(P)
        # print(len(suffixarray))
        for j in range(len(P)):
            # print(Q[j], P[j]-1, suffixarray[Q[j]], suffixarray[P[j]-1])
            results[j] = suffixarray[Q[j]] - suffixarray[P[j]-1]
        return results
