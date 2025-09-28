class Solution:

    # Self comments for the future:
    # Remember this problem as a 
    def canJump(self, nums: List[int]) -> bool:
        gasoline = 0
        for i in nums:
            if gasoline < 0:
                return False
            
            # Always assume the "safest"
            elif i > gasoline:
                gasoline = i

            gasoline = gasoline - 1

        return True