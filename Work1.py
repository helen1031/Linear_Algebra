def makeInverseIndex(strlist):
    dic={}
    for i,string in enumerate(strlist):
        words=string.split()
        for w in words:
            if w in dic:
                dic[w].add(i)
            else:
                dic[w]={i}

    return dic
    
def orSearch(inverseIndex, query):
    #query 리스트에 있는 단어들 중 하나라도 있으면 해당 번호 집합 출력
    num=set()
    for w in query:
        if w in inverseIndex:
            num.update(inverseIndex[w])
    return num


def andSearch(inverseIndex, query):
    num=set()
    nums=[]
    for w in query: #query 단어 중 하나
        tmp=set()
        if w in inverseIndex: #inverseIndex에 있으면
            tmp.update(inverseIndex[w])
            nums.append(tmp)
    num=nums[0]
    for i in range(1,len(nums)):
        num=num.intersection(nums[i])
            
    return num
            
    
query=['British', 'Class', 'For']

f=open("stories_small.txt")
s=makeInverseIndex(list(f))
print(orSearch(s, query))
print(andSearch(s, query))

f2=open("stories_big.txt")
s2=makeInverseIndex(list(f2))
print(orSearch(s2, query))
print(andSearch(s2, query))

