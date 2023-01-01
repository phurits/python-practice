class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def checkDays(date):    
            y = date[0]
            m = date[1]
            d = date[2]
            dateinmonth = {
                1:31,
                2:28,
                3:31,
                4:30,
                5:31,
                6:30,
                7:31,
                8:31,
                9:30,
                10:31,
                11:30,
                12:31,
            }
            ttdays = 0
            #Years
            for i in range(1970,y):
                if i % 4 == 0 and i % 100 != 0 and i % 400 == 0:
                    ttdays += 366
                    print()
                else:
                    ttdays += 365
            print(ttdays)
                 
            #Months
            for month in range(1,m):
                ttdays += dateinmonth[month]
            print(ttdays)
            #Days
            if y % 4 != 0 and y % 400 != 0 and y % 100 == 0 and m > 2:
                ttdays += d + 1
            else:
                ttdays += d
            print(ttdays)
            return ttdays

        d1 = min(date1,date2)
        d2 = max(date1,date2)

        d1 = [int(x) for x in d1.split('-')]
        d2 = [int(x) for x in d2.split('-')]

        return checkDays(d2) - checkDays(d1)

        
        

date1 = "2020-01-15"
date2 = "2019-12-31"
print(Solution().daysBetweenDates(date1,date2))
