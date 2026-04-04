class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        courses = {}
        for a, b in prerequisites:
            if a not in courses:
                courses[a] = []
            
            courses[a].append(b)

        taken = [False] * numCourses

        seen = set()

        def dfs(i):
            if i in seen:
                return
                
            if i not in courses:
                taken[i] = True
                return

            seen.add(i)

            can_take = True
            for prereq in courses[i]:
                dfs(prereq)
                can_take = can_take and taken[prereq]
            
            taken[i] = can_take
        
        for i in range(numCourses):
            if not taken[i]:
                dfs(i)
            
            if not taken[i]:
                return False
        
        return True
