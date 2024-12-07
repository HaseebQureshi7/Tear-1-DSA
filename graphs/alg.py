from collections import deque


def dfsTraversal(graph):
    visited = set()
    res = []

    def helper(vIndex):
        if vIndex in visited:
            return

        res.append(vIndex)
        visited.add(vIndex)
        for v in graph[vIndex]:
            helper(v)

    helper(0)

    return res


def bfsTraversal(graph):
    visited = set()
    res = []

    q = deque()
    q.append(0)

    while q:
        vertex = q.popleft()
        if vertex not in visited:
            res.append(vertex)
            visited.add(vertex)

            # q.extend(graph[vertex])  # Destructuring the whole array in the queue
            for v in graph[vertex]:
                q.append(v)

    return res


def connectedComponents(graph: dict):
    count = 0
    visited = set()

    def dfs(v):
        if v in visited:
            return

        visited.add(v)

        for vertex in graph[v]:
            dfs(vertex)

    for k, _ in graph.items():
        if k not in visited:
            dfs(k)
            count += 1

    return count


def numOfIslands(grid) -> int:
    def dfs(r, c):
        # Boundary check and stop if it's water or already visited
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return

        # Mark the current cell as visited
        grid[r][c] = "0"

        # Visit all adjacent cells (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Initialize the island count
    num_islands = 0

    # Traverse every cell in the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":  # Found an island
                num_islands += 1  # Increment island count
                dfs(r, c)  # Perform DFS to mark the entire island

    return num_islands



def floodFill(image, sr, sc, color):
    start_color = image[sr][sc]
    if (
        start_color == color
    ):  # If the starting pixel already has the target color, return the image as is
        return image

    def dfs(r, c):
        # Boundary and color check
        if (
            r < 0
            or c < 0
            or r >= len(image)
            or c >= len(image[0])
            or image[r][c] != start_color
        ):
            return

        # Update the color
        image[r][c] = color

        # Recursive DFS in all 4 directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Start the DFS from the initial pixel
    dfs(sr, sc)
    return image
