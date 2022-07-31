class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        #problem is similar to Arithmetic series
        #i*(i+1)//2 main logic here
        group = 0
        
        
        for i in range(1,len(grades)+1):
            if i*(i+1)//2 <= len(grades):
                group = i
            else:
                group
                
        return group