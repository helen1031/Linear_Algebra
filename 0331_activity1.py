def addn(v, w):
    res=[]
    for i in range(len(v)):
        res.append(v[i]+w[i])
    return res

v=[1,2,3,4]
w=[5,6,7,8]
print(addn(v,w))
