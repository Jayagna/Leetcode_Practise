class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        res = []
        length = []
        for i in range(len(chars)):
            if not stack:
                stack.append(chars[i])  
                continue
            elif chars[i] != stack[-1]:
                res.append(stack[-1])
                if len(stack) > 1:
                    num = len(stack)
                    while num > 0:
                        length.append(str(num%10))
                        num = num//10
                    for j in range(len(length)-1,-1,-1):
                        res.append(length[j])
                    length = []
                while stack:
                    stack.pop()
            stack.append(chars[i])
        res.append(stack[-1])
        if len(stack) > 1:
            num = len(stack)
            while num > 0:
                length.append(str(num%10))
                num = num//10
            for j in range(len(length)-1,-1,-1):
                res.append(length[j])
            length = []
        

        for i in range(len(res)):
            chars[i] = res[i]
        for i in range(len(chars)-len(res)):
            chars.pop()

        return len(chars)
        
