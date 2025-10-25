'''
Day 25 solution for 1716. Calculate Money in Leetcode Bank
You have a bank that gives you money every day. The amount of money you receive on each day follows a specific pattern:
On the 1st day, you receive $1.
On the 2nd day, you receive $2.
On the 3rd day, you receive $3.
...On the 7th day, you receive $7.
From the 8th day onwards, the pattern repeats but with an increment of $1 for each subsequent week. 
For example, on the 8th day, you receive $2 (which is $1 + $1), on the 9th day, you receive $3 (which is $2 + $1), on the 10th day, you receive $4 (which is $3 + $1), and so on.
Given an integer n, representing the number of days you have been receiving money, calculate the total amount of money you have received after n days.

this solution submitted by @rahulguggilam and it beats 100% of python3 submissions 
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        l=[1,2,3,4,5,6,7]
        k=1
        j=0
        add=0
        for i in range(0,n,1): 
            if(i<=6):
                add+=l[i]
            
            else:
                add+=l[j]+k
                j+=1
                if(j>6):
                    j=0
                    k+=1
                
                
                
                
        return(add) 
        