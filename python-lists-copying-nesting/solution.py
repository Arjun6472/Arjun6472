import copy 

def shallow_copy(lst: list) -> list:
    return lst.copy()
    """
    Return a NEW list object with the same elements as `lst`
    (the elements themselves are shared, not copied). Use the
    copy() method.
    """
    pass


def deep_copy(nested: list) -> list:
    return copy.deepcopy(nested)
    """
    Return a fully independent copy of `nested`: a new list
    whose inner lists (at every depth) are also new objects.
    Use copy.deepcopy (import the copy module at the top of
    your solution).
    """
    pass


def shares_inner_objects(original: list, duplicate: list) -> bool:
    return all(a is b for a, b in zip(original, duplicate))
    """
    `original` and `duplicate` are lists of equal length. Return
    True if, at every position, the two lists hold the exact
    same object (identity, `is`). Return False if any position
    holds different objects. Two empty lists give True.
    """
    pass


def add_row_safely(matrix: list, row: list) -> list:
    new_matrix = [copy.deepcopy(existing_row) for existing_row in matrix]
    new_matrix.append(copy.deepcopy(row))
    return new_matrix
    """
    `matrix` is a list of lists. Return a NEW matrix that
    contains independent copies of every row of `matrix` (as
    they were) followed by an independent copy of `row`.
    Neither `matrix` nor `row` (nor any row inside `matrix`)
    may be modified or shared with the returned matrix.
    """
    pass


def make_grid(rows: int, cols: int, fill) -> list:
    if rows <= 0:
        return []
    if cols <= 0:
        return [[] for _ in range(rows)]
    return [[fill for _ in range(cols)] for _ in range(rows)]
    """
    Return a NEW list of `rows` lists, each containing `cols`
    copies of `fill`. Every row must be a separate list object,
    so mutating one row never changes another. If rows or cols
    is 0 (or negative), return the matching empty structure
    (rows <= 0 -> []; cols <= 0 -> a list of empty rows).
    Use a comprehension.

    Example: make_grid(2, 3, 0) -> [[0, 0, 0], [0, 0, 0]]
    """
    pass


def rows_are_independent(grid: list) -> bool:
    ids = [id(row) for row in grid]
    return len(ids) == len(set(ids))

    """
    Return True if every row of `grid` (a list of lists) is a
    distinct object, i.e. no two rows have the same id().
    A grid with 0 or 1 rows returns True.
    """
    pass


def transpose(matrix: list) -> list:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return [[matrix[i][j] for i in range(num_rows)] for j in range(num_cols)]
    """
    `matrix` is a non-empty rectangular list of lists. Return
    a NEW matrix in which rows and columns are swapped. The
    input must not be modified, and the result's rows must be
    new list objects.

    Example: transpose([[1, 2, 3], [4, 5, 6]])
             -> [[1, 4], [2, 5], [3, 6]]
    """
    pass
