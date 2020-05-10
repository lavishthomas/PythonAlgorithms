def reorderElements(logFileSize, logLines):1
    # WRITE YOUR CODE HERE
    
    ### Two lists were created in order  to capture 
    ### the string type logs  and numerical type logs separately.
    string_logs = []
    numberical_log = []
    
    ### Iterating through the logs
    for log in logLines:
        #print (log)
        
        ### identifier is extracted
        identifier = log.split()[0]
        
        ### log string is extracted
        string = log.split(' ', 1)[1]
        #print(string)
        
        ### separately capturing numerical log and alphabetical logs
        if(string[0].isdigit()):
            numberical_log.append(log)
            
        else:
            tailed_identifier_log = log.split(' ', 1)[1] + ' ' + identifier
            #print(tailed_identifier_log )
            ### 
            string_logs.append(tailed_identifier_log)
    
    ### sorting the string logs in lexicographical order
    sorted_string_logs = sorted(string_logs)
    #print (sorted_string_logs)  
    word_logs = []
    for log in sorted_string_logs:
        
        identifier = log.split()[-1]
        log_string = log.rsplit(' ', 1)[0]
        
        ### the identifier is reverted back to starting of the string
        log_original = identifier + ' ' +log_string
        #print(log_original)
        word_logs .append(log_original )
        
    #print (word_logs) 
    #print (numberical_log)   
    
    ### Merging the string and numerical logs
    word_logs.extend(numberical_log)
    
    ### Result is returned
    return word_logs
    pass
