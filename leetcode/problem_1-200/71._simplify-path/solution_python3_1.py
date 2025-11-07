class Solution:
    def simplifyPath(self, path: str) -> str:

        #
        comps = path.split('/')
        res = list()

        #
        for comp in comps:
            if comp == "" or comp == ".":
                continue
            if comp == "..":
                if res:
                    res.pop()
            else:
                res.append(comp)

        return "/" + "/".join(res)
