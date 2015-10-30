'''
main file which enables the interaction with the user
'''


if __name__ == '__main__':
    '''
    instructions to interact with the user
    '''
    
    import re
    import intervl
    
    user_list = ""
    intervals_format = "^(\[|\()([0-9]+), ([0-9]+)(\]|\))$"
    
    while re.search(intervals_format, user_list) is None:
        user_list = str(input("List of intervals ? "))
        if re.search(intervals_format, str(user_list)) is None:
            print "invalid interval"
    
    user_list_splited = user_list.split(", ")
    
    for i in range(0, len(user_list_splited)):
        user_list_splited[i] = intervl.interval(user_list_splited)
    
    merged_user_list = intervl.mergeOverlapping(user_list_splited)
    
    print merged_user_list
    
    additional_interval = ""
    additional_interval_format = "^(\[|\()([0-9]+),([0-9]+)(\]|\))$"
    while True:   
        while re.search(additional_interval_format, user_list) is None:
            additional_interval = str(input("Interval ? "))
        
        merged_user_list = intervl.insert(merged_user_list, additional_interval)
        
        print merged_user_list
            
    
        
    
        
        
    
