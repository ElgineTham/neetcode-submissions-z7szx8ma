class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        prereqs = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            prereqs[course] += 1

        q = deque()
        for course in range(numCourses):
            if prereqs[course] == 0:
                q.append(course)

        finish = 0
        while q:
            prereq = q.popleft()
            finish += 1

            for course in adj[prereq]:
                prereqs[course] -= 1
                if prereqs[course] == 0:
                    q.append(course)
        
        return finish == numCourses
        