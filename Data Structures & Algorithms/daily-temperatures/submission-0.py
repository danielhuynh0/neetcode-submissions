class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack:
                top = stack[-1]
                if top[0] < temperatures[i]:
                    stack.pop()
                    result[top[1]] = i - top[1]
                else:
                    break
            stack.append((temperatures[i], i))

        return result