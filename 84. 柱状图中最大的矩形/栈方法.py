class Solution:
    def largestRectangleArea(self, heights):
        FILO = []
        area = 0
        # area列表中初始化一个0， 防止heights为空时area为空
        # area = [0, ]
        for i in range(len(heights)):
            while FILO and heights[i] < heights[FILO[-1]]:
                index = FILO.pop()
                if FILO:
                    area = max(area, heights[index] * (i-FILO[-1]-1))
                    # 也可以将area做成列表，面积汇总之后最后做max，用空间换时间
                    # area.append(heights[index] * (i - FILO[-1] - 1))
                else:
                    area = max(area, heights[index] * i)
            FILO.append(i)
        while FILO:
            index = FILO.pop()
            if FILO:
                area = max(area, heights[index] * (len(heights) - FILO[-1] - 1))
            else:
                area = max(area, heights[index] * len(heights))
        return area

if __name__ == '__main__':
    s = Solution()
    area = s.largestRectangleArea([2,1,5,6,2,3])
    # 10
    print(area)
    area = s.largestRectangleArea([5,5,4,4,3,3,2,1,2])
    # 18
    print(area)