# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 00:19:26 2016

@author: liuxinyi

"""

class calculte():
    def __init__(self):
        self.lookup = {}
        self.sum = 0
        
            
    def openFile(self,filename):
        file = open(filename,"r")
        for line in file:
            a = line.split()
            self.lookup[a[0]]=int(a[1])
            self.sum += int(a[1])
        for i in self.lookup:
            self.lookup[i]=self.lookup[i]/float(self.sum)
        self.lookup= sorted(self.lookup.iteritems(), key=lambda d:d[1], reverse = True)
        
        #print self.lookup
            
    def getMfrequent(self,n):
        print
        for i in xrange(n):
            print self.lookup[i][0]
            
    def getLfrequent(self,n):
        print
        for i in xrange(n):
            print self.lookup[-1-i][0]
    
    def prob(self, pre_right, pre_wrong):
        # all character should be uppercase!!!!!!!!!!!!
        #pre_right = str
        #pre_wrong = list[str]
        maxletter =''
        maxprob=0
        denominator = 0
        tmp = 0
        for item in self.lookup:
            tmp += item[1]
            if self.compare(pre_right, item[0],pre_wrong):
                denominator += item[1]
      #  print tmp    
        for i in xrange(97,123):
            prob_sum = 0
            l = chr(i).upper()
            if l in pre_right or l in pre_wrong:
                continue
            for item in self.lookup:
                posterior = 0
                if self.compare(pre_right, item[0],pre_wrong):
                    posterior = item[1]/denominator
                if self.ifany(pre_right, item[0],l):
                    prob_sum += posterior
            if prob_sum>maxprob:
                maxprob=prob_sum
                maxletter = l
        print maxletter,maxprob
                    
                
    def ifany(self,str1,str2,char):
        for i in xrange(len(str1)):
            if str1[i] == '_':
                if str2[i] == char:
                    return True
        return False
    
        
    def compare(self,str1,str2,strs):
        #str1 contain '_' represent every char
        #strs = list()
        #str should not conclude wrong guess
        for i in xrange(len(str1)):
            if str1[i] == '_':
                if str2[i] in strs or str2[i] in str1:
                    return False
                continue
            
            if str1[i] != str2[i]:
                return False
        return True
            
            
        
        
if __name__ == "__main__":
    c= calculte()
    c.openFile("D:/250a/hw1_word_counts_05.txt")
    #c.getMfrequent(15)
    #c.getLfrequent(14)
    c.prob("__U__",["O","D","L","C"])
    
