class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course, target):
            if course == target:
                return True
            
            if course in seen:
                return False
            
            seen.add(course)
            
            for nei in adj[course]:
                if dfs(nei, target):
                    return True
            
            return False
        
        for i, item in enumerate(queries):
            seen = set()
            prereq, course = item
            if dfs(course, prereq):
                queries[i] = True
            else:
                queries[i] = False

        return queries
