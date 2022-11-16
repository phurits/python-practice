class Solution(object):
    def threeSum(self, nums):
        ans = set()
        p,n,z = [],[],[]

        #Classify list to 3 sub-list
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        P,N = set(p),set(n)

        #Case That Have Only Zero in List
        if len(z) >= 3:
            ans.add((0,0,0))
        
        # Case That Have Only One Zero
        if z:
            for neg in n:
                if -neg in p:
                    ans.add((neg,0,-neg))

        # One Negative and Two Positve
        for p1 in range(len(p)):
            for p2 in range(p1+1,len(p)):
                target = -1 * (p[p1] + p[p2])
                if target in N:
                    ans.add(tuple(sorted([target,p[p1],p[p2]])))

        # One Positive and Two Negative
        for n1 in range(len(n)):
            for n2 in range(n1+1,len(n)):
                target = -(n[n1] + n[n2])
                if target in P:
                    ans.add(tuple(sorted([n[n1],n[n2],target])))

        return ans

nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print(ans)
