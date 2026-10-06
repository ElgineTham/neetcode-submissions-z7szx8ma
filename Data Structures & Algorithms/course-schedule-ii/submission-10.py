class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        prereqs_left = [0] * numCourses
        prereq_to_course = defaultdict(list)

        for course, prereq in prerequisites:
            prereqs_left[course] += 1
            prereq_to_course[prereq].append(course)
        
        q = deque()
        for c in range(numCourses):
            if not prereqs_left[c]:
                q.append(c)
        
        while q:
            curr_course = q.popleft()
            order.append(curr_course)

            for unlocked_course in prereq_to_course[curr_course]:
                prereqs_left[unlocked_course] -= 1
                if prereqs_left[unlocked_course] == 0:
                    q.append(unlocked_course)
        
        if len(order) < numCourses:
            return []
        else:
            return order