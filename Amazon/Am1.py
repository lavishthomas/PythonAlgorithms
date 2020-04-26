from collections import Counter 

def topNCompetitors(numCompetitors, topNCompetitors, competitors, 
                    numReviews, reviews):
    # WRITE YOUR CODE HERE
    
    ### A dictionary is created to capture competitors_count
    competitors_count = {}
    sorted_competitors = sorted(competitors)
    #print (competitors)
    ### Intiallizing dictionary with 0 for all competitors
    for c in sorted_competitors:
        competitors_count[c] = 0
    
    ### iterating through reviews
    for r in reviews:
        r_tokenized = r.split()
        
        for c in sorted_competitors:
            #print ('r' , r)
            #print ('c' , c )
            
            ### Only one capture per review. multiple mentions in a review is discarded.
            if( c in r_tokenized):
                competitors_count[c] = competitors_count[c]+1
    
    ### Removing the competitors with 0 occurance
    #print(competitors_count) 
    competitors_count = {k:v for k,v in competitors_count.items() if v != 0}  
    #print(competitors_count)   
    
    
    k = Counter(competitors_count) 
    high = k.most_common(topNCompetitors) 
    
    #print(high[0])
    top_list = []
    
    for i in high: 
        top_list.append(i[0])
    return top_list    
    
    
    pass

c = [ 'ana', 'zeta' , 'beta', 'delta', 'euro']
r= ['ana was good',
'beta is bas',
'zeta is ',
'ana zeta beta',
'ana',
]
topNCompetitors(5, 2, c, 5 , r)