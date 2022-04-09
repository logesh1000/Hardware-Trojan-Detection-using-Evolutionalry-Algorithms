import random
# the rank is calculated based on the TRIAGE Paper fitness score

def calc_rank(arr1,arr2,x):
    w1=0.5
    w2=0.5
    c=1
    if x[1]==0:
        res=(w1/(arr2[1]+c))+w2*(arr1[1]+arr1[3])
    else:
        res=(w1/(arr2[2]+c))+w2*(arr1[2]+arr1[3])
    return res

