'''
Note that the points that comprise maxArea much have max height from each side.
So only need to find all these points that have max height from each side.
And for the lower one of the two points, it will just be less area when matching with other max height point (the area is decided by the short edge), so we can move the point to next edge with maximal height from one side.
'''
class Solution:
    def maxArea(self, height):
        currentMaxArea = 0
        startPoint = 0
        endPoint = len(height) - 1
        while(startPoint < endPoint):
            currentMaxArea = max(currentMaxArea, 
                    (endPoint - startPoint) * min(height[startPoint], height[endPoint]))
            currentMinHeight = min(height[startPoint], height[endPoint])
            if height[startPoint] < height[endPoint]:
                while height[startPoint] <= currentMinHeight and startPoint < endPoint:
                    startPoint += 1
            else:
                while height[endPoint] <= currentMinHeight and startPoint < endPoint:
                    endPoint -= 1
        return currentMaxArea

solution = Solution()
heightArray = [int(x) for x in input().split()]
print(solution.maxArea(heightArray))
