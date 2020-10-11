# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:26:20 2020

@author: rayde
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        #remove initial dashes 
        S = S.replace('-','')
        
        #num in first group
        length_group1 = len(S) % K           
    
        
        if length_group1!=0:
            S1 = S[:length_group1] + "-"
            S2 = '-'.join([S[i:i+K] for i in list(range(length_group1, len(S),K))])
            S = S1 + S2
        else:
            #num of other groups
            num_other_groups = (len(S)-length_group1)//K
            S = '-'.join([S[i:i+num_other_groups] for i in range(0, len(S), num_other_groups)])
        return S
        