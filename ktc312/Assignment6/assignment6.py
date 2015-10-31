from Functions import *
import re
intervals_list = list()

while True:
    if not intervals_list:
        response = raw_input("List of intervals?")
        
        if response=='quit':
            break
        
        response_list = re.split(r', (?=(?:"[^"]*?(?: [^"]*)*))|, (?=[^",]+(?:,|$))', response)
        for i in response_list:
            try:
                interval(i)
                intervals_list.append(i)
            except:
                print ("Invalid input")
            
    else:
        print("intervals list now is: ",intervals_list)
        response=raw_input("Interval? ")
        
        if response=='quit':
            break
        
        try:
            interval(response)
        except:
            print ("Invalid input")    
        else:
            insert(intervals_list, response)
            intervals_list.sort(key=lambda intervals_list: int(intervals_list.split(",")[0][1:]))

