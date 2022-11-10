class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
        string = ""
        while num != 0:
            if num >= 1000:
                key = 1000
                temp = num//1000
            elif num >= 100:
                key = 100
                temp = num//100
            elif num >= 10:
                key = 10
                temp = num//10
            else:
                key = 1
                temp = num
            
            num = num - (temp*key)

        return string

num = 58
print(Solution().intToRoman(num))




