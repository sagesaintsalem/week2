class High_Scores:
    def __init__(self):
        self.scores = []


    def latest(self, player_scores):
        return player_scores[-1]
        #player_scores = [range(player_scores[-1])]
        



    def personal_best(self, scores):
        return max(scores)

        


    def personal_top_three(self, scores):
        scores.sort()
        return scores[-3::]
        
    def high_to_low(self, scores):
        scores.sort(reverse=True)
        return scores
        
    def no_ties(self, scores):
        scores.sort()
        no_tie_list = []
        for i in range(len(scores)):
            if scores[i] != scores[i-1]:
                no_tie_list.append(scores[i])
        return no_tie_list[-3::]

    def less_three(self, scores):
        if len(scores) < 3:
            scores.append(0)
        scores.sort()
        return scores

    def only_one(self, scores):
        while len(scores) < 3:
            scores.append(0)
        scores.sort()
        return scores