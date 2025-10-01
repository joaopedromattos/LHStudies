class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def get_permutation(arr: List[int]) -> List[List[int]]:

            if len(arr) == 1:
                return [arr]


            perms = []
            for i in range(len(arr)):
                arr_pop = arr[:]
                cur_val = arr_pop.pop(i)
                cur_permutations = get_permutation(arr_pop)
                for permutation in cur_permutations:
                    perms.append([cur_val] + permutation)
            
            return perms
        
        return get_permutation(nums)