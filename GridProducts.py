#Euler Project 11 - Timothy Heath
#Find maximum product of consecutive PROD_SIZE tuples in a '/n', ' ' sep grid
PROD_SIZE = 4
grid_file = open('EulerGrid.dat','r') #load grid from file
i = 0
grid = []
max_prod = 1 #maximum product of consecutive PROD_SIZE tuples in grid so far
for row in grid_file:
    #parse grid_file into 2-dim array of ints    
    grid.append(str(row)[:-1].split(' '))
    grid_width = len(grid[i])
    for j in range(0, grid_width):
        grid[i][j] = int(grid[i][j])
        if(j >= PROD_SIZE):
            #check horizontal product
            prod = 1
            for k in range(j, j - PROD_SIZE, -1):
                prod *= grid[i][k]
            max_prod = max(prod, max_prod)
            if(i >= PROD_SIZE):
                #check forward diagonal product
                prod = 1
                for k in range(0, PROD_SIZE):
                    prod *= grid[i - k][j - k]
                max_prod = max(prod, max_prod)
        if(i >= PROD_SIZE):
            #check vertical product
            prod = 1
            for k in range(i, i - PROD_SIZE, -1):
                prod *= grid[k][j]
            max_prod = max(prod, max_prod)
            if(j <= grid_width - PROD_SIZE):
                #check backward diagonal product
                prod = 1
                for k in range(0, PROD_SIZE):
                    prod *= grid[i - k][j + k]
                max_prod = max(prod, max_prod)
    i += 1
print max_prod
