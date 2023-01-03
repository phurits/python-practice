class Solution(object):
    def threeSum(self, nums):
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        t = tuple(sorted([nums[i],nums[j],nums[k]]))
                        ans.add(t)
        return ans

class Solution2(object):
    def threeSum(self, nums):
        ans = set()
        p,n,z = [],[],[]

        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)

        P,N = set(p),set(n)
        
        if len(z) > 2:
            ans.add((0,0,0))

        if len(z) > 0:
            for pos in p:
                if -pos in n:
                    ans.add((-pos,0,pos))
        
        for pos1 in range(len(p)):
            for pos2 in range(pos1+1,len(p)):
                if -(p[pos1] + p[pos2]) in N:
                    ans.add(tuple(sorted([-(p[pos1] + p[pos2]),p[pos1],p[pos2]])))
        
        for neg1 in range(len(n)):
            for neg2 in range(neg1+1,len(n)):
                if -(n[neg1] + n[neg2]) in P:
                    ans.add(tuple(sorted([n[neg1],n[neg2],-(n[neg1] + n[neg2])])))
        
        return ans

nums = [-1,0,1,2,-1,-4]
print(Solution2().threeSum(nums))