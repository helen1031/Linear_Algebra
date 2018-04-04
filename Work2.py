def create_voting_dict(strlist):
    vote=dict()
    for ppl in strlist:
        name=ppl[0]
        ppl=ppl[3:]
        vote[name]=[int(x) for x in ppl]
    return vote

def policy_compare(sen_a, sen_b, voting_dict):
    a=voting_dict[sen_a]
    b=voting_dict[sen_b]
    return sum([a[i]*b[i] for i in range(len(a))])


def most_similar(sen, voting_dict):
    most=dict()
    for name in voting_dict:
        if name !=sen:
            most[name]=policy_compare(sen, name, voting_dict)
    for key in most.keys():
        if most[key]==max(most.values()):
            return key

def least_similar(sen, voting_dict):
    least=dict()
    for name in voting_dict:
        if name!=sen:
            least[name]=policy_compare(sen, name, voting_dict)
    for key in least.keys():
        if least[key]==min(least.values()):
            return key

def find_average_similarity(sen, sen_set, voting_dict):
    #상원의원 이름 sen, 투표기록 sen_set
    tot=0;
    for i in sen_set:
        tot=policy_compare(sen, i, voting_dict)
    avg=tot/len(sen_set)
    return avg

def find_average_record(sen_set, voting_dict):
    #평균 투표기록
    st=[]
    for i in sen_set:
        tmp=voting_dict[i]
        if st==[]:
            st=tmp
        else:
            for j in range(len(tmp)):
                st[j]=(st[j]+tmp[j])/len(sen_set)

    return st

def bitter_rivals(voting_dict):
    compare=dict()
    for i in voting_dict:
        k=least_similar(i, voting_dict)#i 의원이랑 가장 먼거
        compare[(i,k)]=policy_compare(i, k, voting_dict)

    for i in compare:
        if compare[i]==min(compare.values()):
            return i



f=open('voting_record_dump109.txt')
mylist=[x.split() for x in f]

print(create_voting_dict(mylist))
print(policy_compare('Akaka', 'Allen',(create_voting_dict(mylist))))
print(most_similar('Akaka',create_voting_dict(mylist)))
print(least_similar('Akaka',create_voting_dict(mylist)))
print(most_similar('Chafee', create_voting_dict(mylist)))
print(least_similar('Santorum', create_voting_dict(mylist)))
print(find_average_record({'Akaka', 'Allen'}, create_voting_dict(mylist)))
print(bitter_rivals(create_voting_dict(mylist)))