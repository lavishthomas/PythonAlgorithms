### 
### insert(userId, score)
### getScore(userId)
### getRank(userId)
### getTop(n) -> where n <= 100 
###
### 

class gameScoreCard:
    
    def __init__(self):
        self.userScore = []
    
    def insert(self, userId, score):
        # dict
        new_user = { 'userId' : userId ,
                     'score'  : score   }
        #
        
        position = len(self.userScore)
        
        while (position >= 0 ):
            if self.userScore [position].score > new_user.score : # 3
                self.userScore.append(new_user)
            else:  
                self.userScore[position + 1] = self.userScore[position]
                
        ## 4
        ### A, B , C , D, E , F
        ### 8, 7 , 5 , 3, 3 , 2 , __
        
    def getScore(userID):        
        return self.userScore[userID].score       
       
    def getRank(userId):
        return (self.userScore.getIndex(userID) + 1)
        
    def getTop(n):
        top_ranked_users = self.userScore[0: n]
        return top_ranked_users
            

        
    
        