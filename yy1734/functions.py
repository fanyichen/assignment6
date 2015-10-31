class Interval:
    def __init__(self, string):
        try:        
            left_sign = string.strip()[0]
            left_num = int(string.split(',')[0].strip('[]() '))
            right_sign = string.strip()[-1]
            right_num = int(string.split(',')[1].strip('[]() '))
        except ValueError:
            print('Please write a valid interval')
            return
        if left_num > right_num:
            print ('Error: left bound is bigger than right bound')
            return
            
        self.left_sign = left_sign
        self.left_num = left_num
        self.right_num = right_num
        self.right_sign = right_sign
                        
        if left_sign == '(':
            self.start = left_num + 1
        elif left_sign == '[':
            self.start = left_num
                
        if right_sign == ')':
            self.end = right_num - 1
        elif right_sign == ']':
            self.end = right_num
        
    def __repr__(self):
        return (str(self.left_sign) + str(self.left_num) + ','+str(self.right_num)+str(self.right_sign))

 
#Interval('(3,-7]')
#Interval(test)


def mergeIntervals( int_a, int_b):
 #   int_a = Interval(int1)
 #   int_b = Interval(int2)
    if int_a.start < int_b.start:
        prev = int_a
        current = int_b
    else:
        prev = int_b
        current = int_a
        
    result = [prev]
        
    if prev.end >= current.start - 1:
        if current.end == max(prev.end, current.end):
            prev.end = current.end
            prev.right_num = current.right_num
            prev.right_sign = current.right_sign
    else:
        result.append(current)
      
    return result
        
        
# mergeIntervals('[7,  6)', '[10, 12)')      

def mergeOverlapping(intervals_raw):
    if not intervals_raw:
        return intervals_raw
        
    if type(intervals_raw) == str:
        intervals_temp = intervals_raw.split(',')
        intervals = [",".join(intervals_temp[i:i+2]) for i in range(0, len(intervals_temp), 2)]
    elif type(intervals_raw) == list:
        intervals = [str(intervals_raw[i]) for i in range(0, len(intervals_raw))]
    else:
        return "Invalid list!"
        
    intervals2 =[Interval(intervals[0])]
    
    for i in range (1, len(intervals)):
        intervals2.append(Interval(intervals[i]))
        
    intervals2.sort(key = lambda x: x.start)
    
    merge_result = [intervals2[0]]
    for i in range (1, len(intervals2)):
        prev, current = merge_result[-1], intervals2[i]
        merge_result.pop()
        merge_result.extend(mergeIntervals(prev, current))
    return merge_result


# mergeOverlapping([(2,   4),(5,   8),[4,5],(11,20)])    
# mergeOverlapping(test)
        
def insert(intervals, newint):
    intervals.append(Interval(newint))

    return mergeOverlapping(intervals)
    
    
#insert([(2,   4),(5,   8),[4,5]], '(0,10),(9,12)' )
