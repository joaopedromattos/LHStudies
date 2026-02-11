'''
In: Num Courses: Int, Pre-reqs: List[[Int, Int]]

Q: Are there always solutions? 
Q: How large can "Num courses" be? 

Principle: If course i + 1 can be done, it means course j was done (for all j pre-reqs).

num_courses = 4, pre-reqs: [[1, 2], [2, 3], [1, 4]]
to complete -> [3, 4] -> []
order in which we can complete -> [3, 4, 2, 1]
complete_courses = {3, 4, 2, 1}


num_courses = 4, pre-reqs: [[1, 2], [2, 3], [1, 4], [3, 4], [4, 2]]
to complete -> [] -> []
order in which we can complete -> -1
complete_courses = {}

num_courses = 5, pre-reqs: [[1, 2], [2, 3], [1, 4], [5, 4], [1, 5]]
to complete -> [3, 4] -> [1, 5] -> [5, 1] -> [1] -> 1
order in which we can complete -> [3, 4, 2, 5, 1]
complete_courses = {3, 4, 2, 5, 1}

Time: O(|V| + |V| * |E|), Space : O(|V|) -> Not considering inputs and outputs
'''
# import heapq
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

#         G = {i : {'locks' : set(), 'locked_by': set()} for i in range(numCourses)}
#         for u, v in prerequisites:
#             G[u]['locked_by'].add(v)
#             G[v]['locks'].add(u)


#         to_complete = [(0, course) for course in G.keys() if G[course]['locked_by'] == set()]
#         heapq.heapify(to_complete)

#         print("G", G)
#         print("To_complete", to_complete)
#         if not to_complete:
#             # No starting points...
#             print("First")
#             return []

#         solution = []
#         completed_courses = set()

#         while to_complete:
#             pre_reqs, course = heapq.heappop(to_complete)

#             # Check if current course can be completed (all pre-reqs have been completed):
#             if G[course]['locked_by'] <= completed_courses and (course not in completed_courses):
#                 solution.append(course)
#                 completed_courses.add(course)

#                 # If a course is completed, we can add its dependencies:
#                 for locked_course in G[course]['locks']:
#                     heapq.heappush(to_complete, (len(G[locked_course]['locked_by']), locked_course))
    
#                 if len(solution) == numCourses:
#                     return solution


#         print("Last\t", solution, numCourses)
#         return []



'''

Solution #2

We just need to keep track of a global variable that counts the in-degree of each node. 

Then we run bfs



'''



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        G = {i : {'locks' : set(), 'locked_by': set()} for i in range(numCourses)}
        indegree = [0] * numCourses
        for u, v in prerequisites:
            G[u]['locked_by'].add(v)
            G[v]['locks'].add(u)
            indegree[u] += 1



        to_complete = deque([course for course in G.keys() if G[course]['locked_by'] == set()])

        print("G", G)
        print("To_complete", to_complete)
        if not to_complete:
            # No starting points...
            print("First")
            return []

        solution = []
        completed_courses = set()

        while to_complete:
            course = to_complete.popleft()

            solution.append(course)

            for neigh_course in G[course]['locks']:
                indegree[neigh_course] -= 1

                if indegree[neigh_course] == 0:
                    to_complete.append(neigh_course)



        if len(solution) == numCourses:
            return solution
        else:
            return []


            
            


        