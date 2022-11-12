class MedianFinder:
    def __init__(self):
        self.value = []

    def addNum(self, num: int) -> None:
        self.value.append(num)

    def findMedian(self) -> float:
        self.value.sort()
        mid = len(self.value) //2
        if len(self.value) % 2 == 0:
            return (self.value[mid] + self.value[mid - 1])/2
        else:
            return self.value[mid]
            
medianFinder = MedianFinder
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    #arr = [1, 2]
medianFinder.findMedian(); # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    ## arr[1, 2, 3]
medianFinder.findMedian(); # return 2.0            
    