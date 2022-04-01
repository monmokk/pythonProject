import string

#기본 알고리즘, 정렬
def caesar3(s):
    alphabet = list(string.ascii_lowercase)

    s = list(s)
    for i, char in enumerate(s):
        position = (alphabet.index(char) + 3) % 26
        s[i] = alphabet[position]
    return ''.join(s)

print(caesar3("xyz"))

def bubbleSort(x): #버블정렬
    for i in range(0, len(x)-1):
        for j in range(0, len(x)-1-i):
            if x[j+1] < x[j]:
                x[j+1], x[j] = x[j], x[j+1]
    return x
#(n-1) + ... + 1번 = n(n-1) / 2

def selectionSort(x): #선택
    for i in range(0, len(x)-1):
        current = i
        for j in range(i+1, len(x)):
            if x[j] < x[current]:
                current = j
            x[j], x[current] = x[current], x[j]
    return x
#(n-1) + (n-2) + (n-3) + .... + 2 + 1 = n(n-1) / 2

def insertSort(x):
    for i in range(1, len(x)):
        key = x[i]
        while i>0 and key<x[i-1]:
            x[i], x[i-1] = x[i-1], x[i]
            i -= 1
    return x




#기본 알고리즘, 탐색
def PhonenumberSearch(Allnumber, Phonenumber):
    for i in range(0, len(Allnumber)):
        if Phonenumber == Allnumber[i]:
            return Phonenumber

def binary_search(target, allstage):
    first = 0
    last = len(allstage) - 1
    while first <= last:
        mid = (first + last) // 2
        if allstage[mid] == target:
            return mid
        elif allstage[mid] < target:
            first = mid + 1
        else:
            last = mid -1

#피보나치 수열 : F(n) = 1, where n <= 2
#F(n) = F(n-1) + F(n-2), where n > 2
def Fib(n):
    if n ==1 or n == 2: return 1
    else:
        tmp1 = tmp2 = 1
        for i in range(3, n+1):
            current = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = current
        return current
def Fib1(n):
    if n<=2: return 1
    else:
        return Fib1(n-1) + Fib1(n-2)
