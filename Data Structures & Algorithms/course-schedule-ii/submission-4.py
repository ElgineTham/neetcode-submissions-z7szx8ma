class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            if course not in courseMap:
                courseMap[course] = []
            courseMap[course].append(prereq)
        
        answer = []
        seen, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in seen:
                return True
            
            cycle.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            seen.add(course)
            answer.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return answer