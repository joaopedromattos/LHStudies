'''
Topo-sort

1. start from the node that does not have pre-reqs
2. iterate in all the nodes until you "finish" the pre-reqs

- if cycle is found -> return false

if all nodes have been visited -> return true

'''

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        G = {i: [] for i in range(numCourses)}

        # Number of courses that we still have to do
        # to be able to take the i-th course.
        # If in_degree[i] != 0, then this course will be "locked".
        in_degree = [0] * numCourses

        for dest, source in prerequisites:
            G[source].append(dest)
            in_degree[dest] += 1

        # you should do the courses that have no prereqs
        cur_courses = deque([i for i in range(numCourses) if in_degree[i] == 0])

        num_nodes_vis = 0
        while cur_courses:
            cur_course = cur_courses.popleft()
            num_nodes_vis += 1
            for next_course in G[cur_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    # We "unlock" this course
                    cur_courses.append(next_course)

        return num_nodes_vis == numCourses

            






        

        
        