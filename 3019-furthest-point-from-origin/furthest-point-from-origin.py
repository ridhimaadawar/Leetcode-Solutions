class Solution(object):
    def furthestDistanceFromOrigin(self, moves): 
        L = moves.count('L')
        R = moves.count('R')
        blank = moves.count('_')
        
        return abs(R - L) + blank