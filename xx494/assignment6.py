from intervals import interval
import operator
import re

def merge_intervals(intervals):
    flag=1   # there is overlap
    while flag:
        flag=0   #reset to no overlap
        intervals=sorted(intervals, key=operator.attrgetter('lower_value'))
        length=len(intervals)
        for i in xrange(length):
            for j in xrange(i+1,length):
                try:
                    do_merge(interval[i],interval[j])
                except:
                    continue
                else:
                    flag=1
                    new_i=do_merge(interval[i],interval[j])
                    intervals.remove(intervals[j])
                    intervals.remove(intervals[i])
                    intervals.append(new_i)
    return intervals


def do_merge(i1,i2): #2 interval object
    # check the lower bound of 2 intervals
    if (len(set(i1.integers) & set(i2.integers)) > 0):
        if i1.lower_value<i2.lower_value:
            merge_interval=i1.lower_bound + str(i1.lower_value) + ','
        elif i2.lower_value<i1.lower_value:
            merge_interval=i2.lower_bound+str(i2.lower_value)+','
        else:
            if i1.lower_bound=='(' and i2.lower_bound=='(':
                merge_interval='('+str(i2.lower_value)+','
            else:
                merge_interval='['+str(i2.lower_limit)+','

        #check the upper bound of the intervals
        if i1.upper_value<i2.upper_value:
            merged_interval = merged_interval + str(int2.upper_value) + int2.upper_bound
        elif i2.upper_value<i1.upper_value:
            merge_interval = merge_interval+str(i1.upper_value)+i1.upper_bound
        else:
            if i1.upper_bound == ')' and i2.upper_bound == ')':
                merged_interval = merged_interval + str(i2.upper_value) + ')'
            else: 
                merged_interval = merged_interval + str(i2.upper_value) + ']'
    elif ((i1.lower_bound == '[' or i2.upper_bound == ']') and (i1.lower_value == i2.upper_value)):
        merged_interval = i2.lower_bound + str(i2.lower_value) + ',' + str(i1.upper_value) + i1.upper_bound
    
    elif ((i1.upper_bound == ']' or i2.lower_bound == '[') and (int1.upper_value == int2.lower_value)):
        merged_interval = i1.lower_bound + str(i1.lower_value) + ',' + str(int2.upper_value) + int2.upper_bound

    elif ((i1.lower_bound == '[' and i2.upper_bound == ']') and (i1.lower_value - 1 == i2.upper_value)):
        merged_interval = i2.lower_bound + str(i2.lower_value) + ',' + str(i1.upper_value) + i1.upper_bound

    elif ((i1.upper_bound == ']' and i2.lower_bound == '[') and (i1.upper_value + 1 == i2.lower_value)):
        merged_interval = i1.lower_bound + str(i1.lower_value) + ',' + str(i2.upper_value) + i2.upper_bound
        
    else:
        print "not overlap" 

    return interval(merged_interval)

if __name__=="__main__":
    flag=1  #set to input
    while flag:
        interval_list=raw_input("List of intervals?")
        if interval_list=="quit":
            break
        process_list=re.findall(r'[[(].*?[\])]',interval_list)
        if not len(process_list):
            print "no input"
            continue
        intervals=[]
        flag=0  #set to stop input
        for i in process_list:
            try:
                intervals.append(interval(i))
            except:
                print "invalid input"
                flag=1
                break
            else:
                intervals.append(interval(i))
        intervals=merge_intervals(intervals)
    while 1:
        new_interval=raw_input("interval?")
        if new_interval=='quit':
            break
        else:
            pre_pro_interval=re.findall(r'[[(].*?[\])]',new_interval)
            try:
                pre_pro_interval=interval(pre_pro_interval[0])
            except:
                print "input error"
                continue
            else:
                intervals.append(pre_pro_interval)
                intervals=merge_intervals(intervals)
                print intervals
