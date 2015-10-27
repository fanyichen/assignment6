import sys
import re

class interval: 
    def __init__(self,int):
        if int[0]=="(" and int[-1]==")":
            print "both esclusive",int[0],int[-1]
            self.checkNumberOrder(int,"ESCLUSIVE")
        elif int[0]=="[" and int[4]=="]":
            print "both inclusive",int[0],int[-1]
            self.checkNumberOrder(int,"INCLUSIVE")
        else:
             print "mixed",int[0],int[-1]
             self.checkNumberOrder(int,"MIXED")
        print int     
    
    def checkNumberOrder(self,int,intType):
        numbers=int.replace(')','').replace('(','').replace(']','').replace('[','').split(',')
        if intType=="ESCLUSIVE" and numbers[0]<numbers[1]:
            print numbers
        elif intType=="INCLUSIVE" and numbers[0]<=numbers[1]:
            print numbers
        elif intType=="MIXED" and numbers[0]<(float(numbers[1])-1):
            print numbers    
        else:
            print "wrong interval"     
        self.mergeIntervals(numbers,numbers)        
    
    def mergeIntervals(self, int1,int2):
        print int1[0],int1[1]#convert into integer!!!
        print list( range(2,5))
    
    
    
def parseInput(inputIntervals):
    intervals=inputIntervals.replace('),', ')*').replace('],',']*').split('*')
    return intervals
            
def start():
    validatedIntervals=[]
    try:
        inputIntervals = raw_input("List of intervals?")    
        if inputIntervals.strip('0123456789(,)[]') or inputIntervals=="":
            print "baaaaad"
        else:
#            print "good input to parse"        
            if (inputIntervals == "quit"):
                print "quitting"
            else:
                intervals=parseInput(inputIntervals) 
                print "Intervalli selezionati: ",intervals 
                for intervalInList in intervals:
                    intervalInstance = interval(intervalInList.strip())
                    validatedIntervals.append(intervalInstance)       
    except: # catch *all* exceptions  
        print "exception"
   
   
            
            


if __name__ == '__main__':
    start()
    