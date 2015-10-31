"""This class checks for valid intervals"""
import re

class interval:


    list_interval = []

    def __init__(self,string_interval):

        pattern = '(\(|\[)(-?\d+),(-?\d+)(\)|\])'
        format = False
        m=re.search(pattern,string_interval)

        if(m!=None):

            self.LowerBound = m.group(2)
            self.UpperBound = m.group(3)
            self.LowerBound = int(self.LowerBound)
            self.UpperBound = int(self.UpperBound)
            if (m.group(1)=='['):
                self.LowerBoundInclusive = True
            if (m.group(1)=='('):
                self.LowerBoundInclusive = False
            if (m.group(4)==']'):
                self.UpperBoundInclusive = True
            if (m.group(4)==')'):
                self.UpperBoundInclusive = False


            if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == True)
                 and (self.LowerBound<=self.UpperBound)):
                format = True
                self.RealLowerBound = self.LowerBound
                self.RealUpperBound = self.UpperBound
            if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == False)
                  and self.LowerBound<self.UpperBound):
                format = True
                self.RealLowerBound = self.LowerBound
                self.RealUpperBound = self.UpperBound-1
            if (((self.LowerBoundInclusive == False and self.UpperBoundInclusive == True))
                  and self.LowerBound<self.UpperBound):
                format = True
                self.RealLowerBound = self.LowerBound+1
                self.RealUpperBound = self.UpperBound
            if (((self.LowerBoundInclusive == False) and (self.UpperBoundInclusive == False))
                 and (self.LowerBound<((self.UpperBound)-1))):
                format = True
                self.RealLowerBound = self.LowerBound+1
                self.RealUpperBound = self.UpperBound-1


            #print self.RealLowerBound
            #print self.RealUpperBound
            #print "Break"

            if format==True:
                x=1+2
            else:
                print "ERROR: bad input for interval range"

        else:
            print("Bad format - try again")




    @staticmethod
    def mergeIntervals(int1, int2):
        try:
            if (int1.RealUpperBound >= (int2.RealLowerBound-1)):
                #start = min(int1.RealLowerBound,int2.RealLowerBound)
                #end = max(int1.RealUpperBound,int2.RealUpperBound)
                #print range (start,end+1)
                if (int1.RealLowerBound<=int2.RealLowerBound):
                    start_value = int1.LowerBound
                    #print "yayyy"
                    #print int1.LowerBoundInclusive
                    if int1.LowerBoundInclusive:
                        start_char = '['
                    else:
                        start_char = '('
                else:
                    #print "nayyy"
                    start_value = int2.LowerBound
                    if int2.LowerBoundInclusive:
                        start_char = '['
                    else:
                        start_char = '('

                if (int1.RealUpperBound>=int2.RealUpperBound):
                    end_value = int1.UpperBound
                    if int1.UpperBoundInclusive:
                        end_char = ']'
                    else:
                        end_char = ')'
                else:
                    end_value = int2.UpperBound
                    #print "dayum"
                    if int2.UpperBoundInclusive:
                        end_char = ']'
                    else:
                        end_char = ')'



                #starting_char = start.LowerBoundInclusive
                #print starting_char
                print "{0}{1},{2}{3}".format(start_char,start_value,end_value,end_char)
                NewInterval = interval("{0}{1},{2}{3}".format(start_char,start_value,end_value,end_char))
                return NewInterval
            else:
                raise
        except:
            #print "Bad intervals: Not adjacent or overlapping and hence cannot be merged"#, sys.exc_info()[0]
            return "bad intervals"



    @staticmethod
    def mergeOverlapping(intervals):
        intervals.sort(key= lambda x: x.RealLowerBound)
        final_list = list()
        final_list.append(intervals[0])
        for i in range(len(intervals)-1):
            if intervals[i].RealUpperBound < intervals[i+1].RealLowerBound:
                final_list.append(intervals[i+1])
            else:
                final_list[-1] = interval.mergeIntervals(final_list[-1], intervals[i+1])
        return final_list



    @staticmethod
    def insert(intervals, newint):
        try:
            intervals1 = intervals
            for i in range(0,len(intervals1)):
                #print "i value is {0}".format(i)
                if (newint.RealLowerBound<=intervals[i].RealLowerBound):
                    intervals.insert(i, newint)

            merged_list = interval.mergeOverlapping(intervals)

            return merged_list
        except:
            print "ERROR"#, sys.exc_info()[0]
            #raise

"""
    @staticmethod
    def main_function():
        ListOfIntervals = list()
        while len(ListOfIntervals)==0:
            try:
                intervals = raw_input("List of intervals:")
                if intervals == "quit":
                    break
                temp = re.compile('(\(|\[)(-?\d+),(-?\d+)(\)|\])').findall(intervals)

                for i in temp:
                    ListOfIntervals.append(interval(i))
                if len(ListOfIntervals)==0:
                    print("Bad input. Please try again with the proper input format")

            except Exception as ErrorMessage:
                print ErrorMessage

        while True:
            NewInt = raw_input("another interval?")
            if intervals == "quit" or "Quit":
                break
            try:
                ListOfIntervals = interval.insert(ListofIntervals,interval(NewInt))
                print ListOfIntervals
            except Exception and ErrorMessage:
                print ErrorMessage
"""



#interval("[30,70]")

#interval.mergeIntervals(interval("[10,20]"), interval("[16,40]"))
#interval.mergeOverlapping([interval("(0,5]"), interval("[2,6)"), interval("(8,10]"), interval("[8,18]")])
#interval.insert([interval("[1,3]"), interval("[6,9]")], interval("[2,5]"))

#print y
#interval.main_function()

#for index, value in enumerate(i):
                    #i[index]
