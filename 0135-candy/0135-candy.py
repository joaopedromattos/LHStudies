'''

In: List[Int], Out: Int (num of candies I need)

- Can children have the same rating?
- Are the children in a circle? => First children is neighbor with the last?


[1 1 1] =>. 3

[1 1 1000] =>. 4
[1 1000 1] =>. 4
[1 1000 0] =>. 4


[.... 1 1000 1000 1000  .....]
              1

Principle: For the i-th child => candy_amt_i = only matters locally
    - For the i-th child (compare against i-1 and i + 1)
        - if i-th larger than one of them: 2 candies
        - else : 1 candy


'''

# [1,2,87,87,87,2,1]
#  1 2 2  1  2. 2 1



class Solution:
    def candy(self, ratings: List[int]) -> int:

        def larger_than_next(i):
            if i == len(ratings) - 1:
                return False

            return ratings[i] > ratings[i + 1]
        
        candies = [1] * len(ratings) # All kids have a candy
        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1


        for i in range(len(ratings) - 2, -1, -1):

            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        print(candies)
        return sum(candies)
 

            
            
        

        return candy_amnt

        