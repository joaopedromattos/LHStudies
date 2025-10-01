class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

#         def get_permutation(arr: List[int]) -> List[List[int]]:

#             if len(arr) == 1:
#                 return [arr]


#             perms = []
#             explored = arr[:]
#             while len(explored) > 0:
#                 cur_val = arr.pop(0)
#                 explored.pop(0)
#                 print(arr)
#                 cur_permutations = get_permutation(arr[:])
#                 for permutation in cur_permutations:
#                     perms.append([cur_val] + permutation)
                
#                 arr.append(cur_val)
            
#             return perms
        
#         return [] + get_permutation(nums)

# [3,2,1] -> [] + [3] -> [] + [3] + [2]  + [3, 2]-> 


        def subsets(self, nums):
                accum = [[]]
                for n in nums:
                    accum += [cur_list + [n] for cur_list in accum]
                return accum





