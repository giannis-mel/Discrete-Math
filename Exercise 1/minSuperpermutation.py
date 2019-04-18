# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:20:23 2019

@author: Giannis Meleziadis 
Compiled and run in python 3.7.1 

This program finds a superpermutation from a sequence of numbers (1...n) where
n is given. For n equal to [1-4] this program produces the minimum superpermutation that 
contains all the permutations of the sequence (1...n). This is checked using a function from the paper
Tackling the Minimal Superpermutation Problem (https://arxiv.org/abs/1408.5108). Useful for the creation of
the main algorithm was the paper Non-uniqueness of minimal superpermutations 
(https://www.sciencedirect.com/science/article/pii/S0012365X1300157X?via%3Dihub)

Some comments where left on purpose for debugging purposes

"""

# Imports
from __future__ import division
import itertools
from functools import reduce
#import sys

# Specify the number n of the sequence
n = 4

### Functions ###

# Function from the paper https://arxiv.org/abs/1408.5108
SYMBOLS = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def pal(n):
    assert 1 <= n <= len(SYMBOLS)
    s = SYMBOLS[n-1]
    
    if n == 1: return s
    return squash([ x + s + x for x in unsquash(n-1, pal(n-1)) if sorted(x) == list(SYMBOLS[:n-1]) ])

def overlap(x, y):
    n = min(len(x), len(y))
    for i in range(n, -1, -1):
        if x[len(x)-i:] == y[:i]:
            return i

def squash(xs):
    return reduce(lambda x, y: x + y[overlap(x, y):], xs, "")

def unsquash(n, s):
    for i in range(0, len(s)-n+1):
        yield s[i : i+n]


# Function which returns reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False


# Function that returns all the permutations of a given string with respect to n
def splitter(str):
    allPermutations = []
    for i in range(0, len(str)-n+1):
        start = i
        end = i + n
        allPermutations.append(str[start:end])
        
    return allPermutations

### Main program ###

Symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

myList = []

# Get the correct number of symbols
for i in range(n) :
    myList.append(Symbols[i])

# The permutations are
perms = []
perm = list(itertools.permutations(myList))
for k in perm :
    perms.append(''.join(k))

result = []

if n==1 :
    resultString = "1"
    print('The superpermutation of',n,' is',resultString, ' (Trivial)')
else :
    
    # Main algorithm
    M = []
    P = []
    Q = []
    Q2 = []
    
    i = 1
    while i < n :
        if i!=1 :
            M = []
            for j in range(len(Q)):
                M.append(Q[j])
    
            Q = []
            resultString = ""    
            for r in range(len(M)):
                    resultString = resultString + M[r]
            
            newString = ""
            r = 0
            while r < len(resultString):
                if r == len(resultString) -1 :
                    newString = newString + resultString[r]
                    r = r + 1
                elif resultString[r] == resultString[r+1] :
                    newString = newString + resultString[r]
                    r = r + 2
                else :
                    newString = newString + resultString[r]
                    r = r + 1
            P = []
            Q2 = Q
            
            #print('length of new string is',len(newString), 'and i is',i)
            #print(newString)
            r=0
            while r < len(newString):
                P.append(newString[r:(r+i)])
                #print('start is', r, ' and end is',r+i-1)
                if r + i >= len(newString) :
                    break
                r = r + 1
        
            for p in P[:]:
                if isPalindrome(p)==1 :
                    #print(p,'is a palindrome')
                    P.remove(p)

#            temp = []
#            temp3 = []
#            for d in range(i) :
#                temp3.append(Symbols[d])
#            temp = list(itertools.permutations(temp3))
#            P2 = P
#            P = []
#            for k in temp:
#                P.append(''.join(k))
                
            P2 = P
            for j in range(len(P)):
                Q.append(P[j] + str(i+1) + P[j])
            

            #print('size of P is',len(P))
            P = []
        
        else :
            M.append(''.join('1'))
            Q.append(''.join('121'))
            P.append(''.join('1'))
            #print('size of P is',len(P))
        
        i = i + 1
        
   
    # Add all the final Qs
    resultString = ""    
    for i in range(len(Q)):
        resultString = resultString + Q[i]
            
    # Delete the repeating values if found
    newString = ""
    i = 0
    while i < len(resultString):
        if i == len(resultString) -1 :
            newString = newString + resultString[i]
            i = i + 1
            break
        k = 0
        flag = 0
        while k<=n-2 :
            #print('Comparing',resultString[i:(i+k+1)], ' with', resultString[(i+k+1):(i+2*k+2)])
            if resultString[i:(i+k+1)] == resultString[(i+k+1):(i+2*k+2)] :
                #print('Comparing',resultString[i:(i+k+1)], ' with', resultString[(i+k+1):(i+2*k+2)])
                newString = newString + resultString[i:(i+k+1)]
                i = i + 2*k + 2
                flag = 1
                #print('found one')
                
            k = k+1
            if flag == 1 : break 
            
        newString = newString + resultString[i]
        i = i + 1
     
    print('')
    
    # The final answer is in the variable newString
    print('The superpermutation of',n,' is :')
    print(newString)
    print('')
    correct = pal(n)
    
    # The final correct answer from the paper
    print('The correct answer from the paper is :')
    print(correct)
    print('')

    # Check the 2 strings if they are equal 
    if correct == newString : print('This is the minimum string!')
    else : print('This is NOT the minimum string!')   
    
    # Check if all permutations are in the string
    # combinations has all the permutations in the variable newString
    # and perms has all the permutations from the sequence 1...n
    combinations = splitter(newString)
    result =  set(perms).issubset(combinations) #all(elem in combinations for elem in perms)
    if result : print('All permutations are in the string!')
    else : print('All permutations are not in the string!')
    
    #print(sys.version)
    
    
