from itertools import combinations
def solution(nums):
    answer=[]
    lst=combinations(nums,3)
    sol=0
    for i in lst:
        a=sum(i)
        if a%2==0:
            continue
        answer.append(a)
    for i in answer:
        chk=[]
        cnt=0
        while True:
            cnt+=1
            if cnt==i+1:
                break
            if i%cnt==0:
                chk.append(cnt)
        if len(chk)==2:
            sol+=1
    return sol