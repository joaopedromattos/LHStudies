'''

upload(4)
upload(5)

upload(1)
upload(2)

longest() -> 2

upload(n) -> insert ordered -> O(N)

longest() -> validate chain -> O(N)

Data structure -> Space O(N)


'''

import bisect

# class LUPrefix:

#     def __init__(self, n: int):
#         self.uploads = []
        


#     def upload(self, video: int) -> None:
#         bisect.insort(self.uploads, video)

#     def longest(self) -> int:

#         if not self.uploads:
#             return 0

#         idx_start = 0
#         while idx_start < len(self.uploads) and self.uploads[idx_start] == (idx_start + 1):
#             idx_start += 1

#         return idx_start



# Solution #2
# Insert O(1)
# Search O(N) -> TLE 

# class LUPrefix:

#     def __init__(self, n: int):
#         self.n = n
#         self.uploads = [False] * (n + 1) # 10^5 Bits ~ 300MB


#     def upload(self, video: int) -> None:
#         self.uploads[video] = True

#     def longest(self) -> int:

#         if not self.uploads[1]:
#             return 0

#         aux = 0
#         for i in range(1, self.n + 1):
#             if self.uploads[i]:
#                 aux += 1
#             else:
#                 break
#         return aux



# Solution #3

from collections import defaultdict
class LUPrefix:

    def __init__(self, n: int):
        self._longest = 0
        self.uploads = defaultdict(int)


    def upload(self, video: int) -> None:
        self.uploads[video] = 1
        
        while self.uploads[self._longest + 1]:
            self._longest += 1

    def longest(self) -> int:
        return self._longest

        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()