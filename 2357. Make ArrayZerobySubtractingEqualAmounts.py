class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        #value to store operation count
        count=0
        
        #run while loop until array sume bcomes zero
        #heapify array to have pop array value in first operation
        #if popped value is greater than 0, then subtract it from all array elements
        #use abs to avoid negative values
        while(sum(nums) > 0):
            heapq.heapify(nums)
            minnum = heapq.heappop(nums)
            #print(minnum)
            if  minnum > 0:
                for i in range(len(nums)):
                    nums[i] = abs(nums[i] - minnum)
                count += 1
            else:
                continue
        return count