def dfs(matrix , visited ,start , n):
    stack = []
    stack.append(start)
    print(start)
    visited[start] = True

    for i in range(n):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix , visited , i , n)
            break

    while stack:
        top_element = stack.pop()
        if not visited[top_element]:
            print(top_element)
            visited[top_element] = True
        

if __name__ == "__main__":
    n = int(input("Enter number of nodes : "))
    
    matrix = []
    visited = [False] * n
    print("Enter adjacency matrix\n")
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)

    start = int(input("Enter starting vertex : "))

    dfs(matrix , visited ,start , n)


"""
Test Case ==>
0
1
1
0
0
1
0
1
1
0
1
1
0
0
1
0
1
0
0
1
0
0
1
1
0
"""
