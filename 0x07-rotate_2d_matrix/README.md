## 0x07. Rotate 2D Matrix
### Rotate 2D Matrix In-Place

#### Problem Statement

Given an `n x n` 2D matrix, implement a function `rotate_2d_matrix(matrix)` to rotate it 90 degrees clockwise. The rotation should be performed in-place, meaning you should modify the original matrix without using additional memory.

#### Prototype

```python
def rotate_2d_matrix(matrix):
    # Implementation goes here
```

#### Constraints

- The input matrix will be an `n x n` 2D matrix.
- The matrix will not be empty.

#### Note

Do not return anything from the function; the matrix must be edited in-place.

#### Example

```python
# Example Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# After rotation, the matrix should become
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

rotate_2d_matrix(matrix)
```

#### Explanation

The original matrix is rotated 90 degrees clockwise in-place. The resulting matrix is shown in the example.
