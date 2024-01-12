# 0x0B-python-input_output
## Pascal's Triangle:
row: [1]
i: 0
traingle: [[1]]
row: [1, 1]

i: 1
traingle: [[1], [1, 1]]

row: [1, 1, 1]
i: 2
j: 1
triangle[2 - 1][1 - 1]: 1
triangle[2 - 1][1]: 1
triangle[i-1][j-1] + triangle[i-1][j]: 2
traingle: [[1], [1, 1], [1, 2, 1]]

row: [1, 1, 1, 1]
i: 3
j: 1
triangle[3 - 1][1 - 1]: 1
triangle[3 - 1][1]: 2
triangle[i-1][j-1] + triangle[i-1][j]: 3
j: 2
triangle[3 - 1][2 - 1]: 2
triangle[3 - 1][2]: 1
triangle[i-1][j-1] + triangle[i-1][j]: 3
traingle: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

row: [1, 1, 1, 1, 1]
i: 4
j: 1
triangle[4 - 1][1 - 1]: 1
triangle[4 - 1][1]: 3
triangle[i-1][j-1] + triangle[i-1][j]: 4
j: 2
triangle[4 - 1][2 - 1]: 3
triangle[4 - 1][2]: 3
triangle[i-1][j-1] + triangle[i-1][j]: 6
j: 3
triangle[4 - 1][3 - 1]: 3
triangle[4 - 1][3]: 1
triangle[i-1][j-1] + triangle[i-1][j]: 4
traingle: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

## Final Output:
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
