##!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:06:15 2019

@author: dexter_chien
"""
"""
class Solution:
    def merge(self,intervals,veichle_time):
        if(len(intervals)==0 and intervals[0]!=veichle_time):
            return 0
        intervals.sort( key=lambda interval: interval[2])
        result=[]
        ans=0
        for interval in intervals:
            if interval[0]!=veichle_time:
                continue
            if not result or result[-1][3]<interval[2]:
                result.append(interval)      
                ans+=(interval[3]-interval[2])
            else:
                if interval[3]>=result[-1][3]:
                    ans+=interval[3]-result[-1][3]
                    result[-1][3]=interval[3]
                   
        return ans

    
test=[[100,3005,660100,660200],[100,3005,660100,660101]]
#test=[[100,3005,660000,660200],[100,3006,660000,660200],[100,3007,700000,700200],[200,3008,660000,6602500]]
vehicle_time=100
answer=Solution()
print(answer.merge(test,vehicle_time))

"""
class Solution:
    def numTrees(self, n: int) -> int:
        T = {}
        T[0], T[1] = 1, 1
        for k in range(2, n+1):
            T[k] = sum([T[r-1] * T[k-r] for r in range(1, k+1)])
        return T[n]
answer=Solution()
print(answer.numTrees(3))
x={'f':'b'}

x=[1,2,3,4]
print(x[5])
