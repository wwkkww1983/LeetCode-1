class Solution:
    def trap(self, height: list):
        area = 0
        for i in range(len(height)):
            left, right = 0, 0
            for j in range(i + 1):
                left = max(left, height[j])
            for j in range(i, len(height)):
                right = max(right, height[j])
            area += min(left, right) - height[i]
        return area


if __name__ == '__main__':
    s = Solution()
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
    area = s.trap([])
    # 0
    print(area)
