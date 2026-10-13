class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = defaultdict(list)
        ans = []

        for prereq in prerequisites:
            course, pre = prereq
            adj[pre].append(course)
            indegrees[course] = indegrees[course] + 1

        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
                ans.append(course)
        while queue:
            cur = queue.popleft()

            for child in adj[cur]:
                if indegrees[child] > 0:
                    indegrees[child] = indegrees[child]-1
                if indegrees[child] == 0 and child not in ans:
                    ans.append(child)
                    queue.append(child)

        if len(ans) == numCourses:
            return ans
        else:
            return []

        