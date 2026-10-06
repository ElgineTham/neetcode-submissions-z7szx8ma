class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        course_to_prereq = [0] * numCourses
        prereq_to_course = defaultdict(list)
        for course, prereq in prerequisites:
            course_to_prereq[course] += 1
            prereq_to_course[prereq].append(course)

        q = deque()
        for c in range(numCourses):
            if not course_to_prereq[c]:
                q.append(c)

        while q:
            curr_course = q.popleft()
            for unlocked_course in prereq_to_course[curr_course]:
                course_to_prereq[unlocked_course] -= 1
                if course_to_prereq[unlocked_course] == 0:
                    q.append(unlocked_course)
                
        for c in range(numCourses):
            if course_to_prereq[c] != 0:
                return False
        
        return True
            
            

