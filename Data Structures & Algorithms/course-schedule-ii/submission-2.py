class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        courses = set()
        for course, req in prerequisites:
            adj_list[course].append(req)
            courses.add(course)
            courses.add(req)
        
        for i in range(numCourses):
            courses.add(i)
        
        complete = []
        completed = [0] * numCourses
        
        def dfs(node):
            completed[node] = 1

            for req in adj_list[node]:
                if completed[req] == 2:
                    continue
                if completed[req] == 1:
                    return 
                if not dfs(req):
                    return False

            complete.append(node) 
            completed[node] = 2                

            return True
        
        for c in courses:
            if completed[c] == 0:
                if not dfs(c):
                    return []
        
        return complete if len(complete) == numCourses else []
        