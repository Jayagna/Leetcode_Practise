class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        q = deque(s)

        for i in range(len(s)):
            w = q.pop()
            q.appendleft(w)

            if "".join(q) == goal:
                return True

        return False
