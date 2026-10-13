class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = -1
        stack = []
        for i in range(len(heights)):
            curr = heights[i]
            while stack and heights[stack[-1]] > curr:
                prev_idx = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, heights[prev_idx] * width)
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            left = stack[-1] if stack else -1
            width = len(heights) - left - 1
            ans = max(ans, width * heights[idx])
        return ans
