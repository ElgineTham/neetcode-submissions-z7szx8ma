class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)
        prereqs = [0] * numCourses
        for course, prereq in prerequisites:
            courseMap[prereq].append(course)
            prereqs[course] += 1

        q = deque()
        for i in range(numCourses):
            if prereqs[i] == 0:
                q.append(i)
        
        answer = []
        while q:
            node = q.popleft()
            answer.append(node)

            for nei in courseMap[node]:
                prereqs[nei] -= 1
                if prereqs[nei] == 0:
                    q.append(nei)

        return answer if len(answer) == numCourses else []

