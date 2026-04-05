class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = path.split("/")

        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)

        return "/" + "/".join(stack)
        