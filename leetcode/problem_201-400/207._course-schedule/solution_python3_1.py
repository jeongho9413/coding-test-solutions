class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #
        hm = {i : list() for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            hm[crs].append(pre)

        #
        def dfs(crs):
            if crs in visited:
                return False  # cycle detected
            if hm[crs] == []:
                return True

            visited.add(crs)

            for pre in hm[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)  # finished
            hm[crs] = []
            return True

        #
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
