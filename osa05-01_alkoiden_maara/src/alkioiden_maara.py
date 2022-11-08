def laske_alkiot(my_matrix: list, element: int):
    counter = 0
    for i in range(len(my_matrix)): 
        for j in range(len(my_matrix[i])): 
            if my_matrix[i][j] == element:
                counter += 1
    return counter
    
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))