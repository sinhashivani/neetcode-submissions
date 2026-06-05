class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses
        adj_list = defaultdict(list)
        courses = set()

        for course, req in prerequisites:
            adj_list[course].append(req)
            courses.add(course)
            courses.add(req)

        def dfs(node):
            if state[node] == 2:
                return True
            if state[node] == 1:
                return False
            
            state[node] = 1

            for req in adj_list[node]:
                if not dfs(req):
                    return False

            state[node] = 2
            return True

        for course in courses:
            if not dfs(course):
                return False
        
        return True

        
    