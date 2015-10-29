
import  re
from Interval import ClassIntervalDefinitionException
from Interval import interval
from Interval import ClassIntervalOperationException

def loop():
    while raw_input('List of intervals?  ') not in  ('quit()','q'):
        listintervalsinput=re.findall(r'[\[(]+[-+]?\d+,+[-+]?\d+[\])]', raw_input('List of intervals?  '))
        if len(listintervalsinput) == 0:
            continue
        else:
            objectlistinterval=[]
            if isinstance(listintervalsinput,list) and len(listintervalsinput) > 0:
                for i in range(len(listintervalsinput)):
                    try:
                        objectlistinterval.append(interval(listintervalsinput[i]))
                    except ClassIntervalDefinitionException:
                        print 'Interval %s not defined appropiatedly, error %s. Try again. \n' %(i,ClassIntervalDefinitionException.msg)
                        break
                while raw_input('Interval?  ') not in  ('quit()','q'):
                    intervalnew=re.findall(r'[\[(]+[-+]?\d+,+[-+]?\d+[\])]',raw_input('Interval?  '))
                    if len(intervalnew)==1:
                        try:
                            intervalnewi=interval(intervalnew)
                        except ClassIntervalDefinitionException:
                            print 'Interval input is not defined appropiatedly, error. Try again.'
                    try:
                        objectlistinterval = interval.insert(objectlistinterval,intervalnewi)
                    except ClassIntervalOperationException:
                        pass
                        listforoverlap=objectlistinterval
                        listforoverlap.insert(0,intervalnewi)
                        try:
                            objectlistinterval = interval.mergeOverlapping(listforoverlap)
                        except ClassIntervalOperationException:
                            print 'No possible union'

                else:
                    print 'Quitting'
            else:
                print 'Not a list! Enter intervals in list'
    else:
        print 'Quitting'



if __name__ == "__main__":
    try:
        loop()
    except EOFError:
        pass
