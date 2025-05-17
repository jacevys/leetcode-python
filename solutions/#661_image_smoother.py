class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

        for row in range(rows):
            for col in range(cols):
                avg = 0
                count = 0
                for dr, dc in directions:
                    x, y = row + dr, col + dc
                    if 0 <= x < rows and 0 <= y < cols:
                        avg += img[x][y]
                        count += 1
                avg //= count
                res[row][col] = int(avg)
        return res
# ok
'''
date / time cost
2025.05.13, 51 m 51 s
'''