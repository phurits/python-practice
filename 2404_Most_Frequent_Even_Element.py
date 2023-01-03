class Solution:
    def mostFrequentEven(self, nums) -> int:
        sets = [x for x in nums if x % 2 == 0]
        nums = [x for x in nums if x % 2 == 0]
        if nums == None:
            return -1
        d = {}
        for i in sets:
            d[i] = nums.count(i)
        max_value = max(d.values())
        min_key = None
        for k, v in d.items():
            if v == max_value:
                if min_key is None or k < min_key:
                    min_key = k
        return(min_key)

nums = [0,1,2,2,4,4,1]
print(Solution().mostFrequentEven(nums))