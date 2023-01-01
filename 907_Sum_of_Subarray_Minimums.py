class Solution:
    def sumSubarrayMins(self, arr) -> int:

        # #Solution1
        # alllist = []
        # for swsize in range(len(arr)):                          #Sliding Window Size
        #     for index in range(len(arr)-swsize):                #Decrease Number up to Sliding Window
        #         alllist.append(min(arr[index:index+swsize+1]))  #Get only min of value in that list (+1 for size of subarray)
        # return sum(alllist)

        #Solution2  Sum along with find subarray
        # total = 0
        # for swsize in range(len(arr)):
        #     for index in range(len(arr)-swsize):
        #         total += (min(arr[index:index+swsize+1]))
        # return total
        return


arr = [3,1,2,4]
print(Solution().sumSubarrayMins(arr))