#       Name:  Jesus Ivan Gonzalez
#       Date:  Aug 16th 2015
#       Description:  Grabs 1st three unique entries, using each combination of, and return all
#           possible +, -, *, and / combinations
#--------------------------------------------------------------------------

import itertools

#class stores and returns if three unique numbers fit a particular math operation
#but returns None if math operation isn't true for a given permutation
class Mathematics(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums(self):
        if (self.a + self.b == self.c):
            return "%d + %d = %d" %(self.a, self.b, self.c)
        return None

    def subNums(self):
        if (self.a - self.b == self.c):
            return "%d - %d = %d" %(self.a, self.b, self.c)
        return None

    def multiNums(self):
        if (self.a * self.b == self.c):
            return "%d * %d = %d" %(self.a, self.b, self.c)
        return None

    def divNums(self):
        if self.a == 0:
            return None
        if (self.a / self.b == self.c):
            return "%d / %d = %d" %(self.a, self.b, self.c)
        return None
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    
listNums = {1,1,2,3}    #<--------- INPUT VALUES

# Main portion of code
for i in itertools.permutations(listNums,3):
    newMathSession = Mathematics(i[0], i[1], i[2])
    addResult = newMathSession.addNums()
    if addResult != None:
        print(addResult)
    subResult = newMathSession.subNums()
    if subResult != None:
        print(subResult)
    multiResult = newMathSession.multiNums()
    if multiResult != None:
        print(multiResult)
    divResult = newMathSession.divNums()
    if divResult != None:
        print(divResult)
