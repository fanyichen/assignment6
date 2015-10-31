
import re

class ClassIntervalDefinitionException(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class ClassIntervalOperationException(Exception):
    def __init__(self,msg):
        self.msg = msg


class interval(object):

    def __init__(self, intervalin):
        if isinstance(intervalin, str):
            self.intervalin = intervalin
            matchexpression = re.match(r'[\[(]+[-+]?\d+,+[-+]?\d+[\])]', intervalin.replace(' ', ''))
            if matchexpression == None:
                raise ClassIntervalDefinitionException(intervalin, 'String not defined correctly')
            else:
                if self.upperbound < self.lowerbound:
                    raise ClassIntervalDefinitionException(intervalin, 'Limits not defined correctly')
        else:
            raise ClassIntervalDefinitionException(intervalin, 'Input is not string')

    def __repr__(self):
        printtext = '%s' % self.intervalin
        printtext = printtext + ' represents the numbers %s' % self.lowerbound
        printtext = printtext + ' through %s' % self.upperbound
        return printtext

    def getlowerbound(self):
        """Sets the lower real bound of the interval"""
        intervalnospace = self.intervalin.replace(' ', '')
        signinit = intervalnospace[0]
        if signinit == '(':
            return int(intervalnospace.replace('(', '').split(',')[0])+1
        elif signinit == '[':
            return int(intervalnospace.replace('[', '').split(',')[0])

    def getupperbound(self):
        """Sets the upper real bound of the interval"""
        intervalnospace = self.intervalin.replace(' ', '')
        signlast = intervalnospace[-1]
        if signlast == ')':
            return int(intervalnospace.replace(')', '').split(',')[1])-1
        elif signlast == ']':
            return int(intervalnospace.replace(']', '').split(',')[1])

    lowerbound = property(getlowerbound, None, None, None)
    upperbound = property(getupperbound, None, None, None)


    @staticmethod
    def mergeIntervals(interval1,interval2):
        """Merges intervals, if they are of interval type, otherwise raises an exception"""
        if isinstance(interval1, interval) and isinstance(interval2, interval):
            lowerbound1 = interval1.lowerbound
            lowerbound2 = interval2.lowerbound
            upperbound1 = interval1.upperbound
            upperbound2 = interval2.upperbound
            limitsup = max(upperbound1, upperbound2)
            limitinf = min(lowerbound1, lowerbound2)
            if (upperbound1 >= upperbound2 and upperbound2 >= lowerbound1 and lowerbound1 >= lowerbound2) or (upperbound2 >= upperbound1 and upperbound1 >= lowerbound2 and lowerbound2 >= lowerbound1):
                return interval('[%i , %i ]'% (limitinf, limitsup))
            elif upperbound2 + 1 == lowerbound1 or upperbound1 + 1 == lowerbound2:
                return interval('[%i , %i ]'% (limitinf, limitsup))
            elif (upperbound1 <= upperbound2 and lowerbound1 >= lowerbound2) or (upperbound2 <= upperbound1 and lowerbound2 >= lowerbound1):
                return interval('[%i , %i ]'% (limitinf, limitsup))
            else:
                raise ClassIntervalOperationException(msg='Operation error')

    @staticmethod
    def mergeOverlapping(listinput):
        """Overlaps the intervals in the provided list. If no intervals can be ovelapped, rises and exception"""
        if isinstance(listinput, list):
            numberintervalsinlist = 0
            for i in range(len(listinput)):
                if isinstance(listinput[i], interval):
                    numberintervalsinlist = numberintervalsinlist + 1
            if numberintervalsinlist == len(listinput):
                listmergeableloop = listinput
                totalintervalsmergeable = 0
                for i in range(len(listinput)):
                    listcheckmergeable = [1]*len(listmergeableloop)
                    listchecknotmergeable =[1]*len(listmergeableloop)
                    for j in range(len(listinput)):
                        try:
                            interval.mergeIntervals(listmergeableloop[i], listmergeableloop[j])
                            listcheckmergeable[j] = listmergeableloop[j]
                            listchecknotmergeable[j] = 0
                        except ClassIntervalOperationException:
                            pass
                            listcheckmergeable[j]=0
                            listchecknotmergeable[j]=listmergeableloop[j]
                    totalmergeable=len([x for x in listcheckmergeable if x != 0])
                    totalintervalsmergeable = totalintervalsmergeable +1
                    if totalmergeable >= 2:
                        return [x for x in listcheckmergeable if x != 0]
                        reducedinterval = reduce(interval.mergeIntervals,[x for x in listcheckmergeable if x != 0])
                        listmergeableloop = [reducedinterval]
                        listmergeableloop.extend([x for x in listchecknotmergeable if x != 0])
                        listmergeableloop.extend([0]*(len(listinput) - len(listmergeableloop)))
                    else:
                        listmergeableloop = listmergeableloop

                if listmergeableloop == listinput:
                    raise ClassIntervalOperationException('Operation cannot go through')
                else:
                    return [x for x in listmergeableloop if isinstance(x,interval)]
            else:
                raise ClassIntervalDefinitionException(msg='One of the elements is not a Interval type')
        else:
            raise TypeError


    @staticmethod
    def insert(listinput, newint):
        """Inserts the interval newint in the list provided in the first argument, if it is not possible it returns the same interval """
        if isinstance(listinput, list) and isinstance(newint,interval):
            numberintervalsinlist = 0
            for i in range(len(listinput)):
                 if isinstance(listinput[i], interval):
                      numberintervalsinlist = numberintervalsinlist + 1
            if numberintervalsinlist == len(listinput):
                try:
                    interval.mergeOverlapping(listinput)
                except ClassIntervalOperationException:
                    pass
                newintervals = listinput
                newintervals.insert(0 , newint)
                listcheckmergeable = [1]*len(listinput)
                for i in range(1,len(newintervals)):
                    try:
                        interval.mergeIntervals(newintervals[0], newintervals[i])
                        listcheckmergeable[i - 1] = newintervals[i]
                    except ClassIntervalOperationException:
                        pass
                        listcheckmergeable[i - 1] = 0
                insertedinterval = interval.mergeOverlapping([x for x in newintervals if x != 0])
                return insertedinterval
            else:
                raise ClassIntervalDefinitionException(listinput, msg='One of the elements is not a Interval type')
        else:
            raise TypeError()
