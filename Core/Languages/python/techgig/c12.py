grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]

def mark_path(grid,x,y,visited):
    if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
        return
    if visited[x][y] == True:
        return
    
    visited[x][y]=True
    
    if grid[x][y]==0:
        return
    mark_path(grid,x-1,y,visited)
    mark_path(grid,x+1,y,visited)
    mark_path(grid,x,y-1,visited)
    mark_path(grid,x,y+1,visited)

cols = len(grid[0])
rows = len(grid)
visited = [[0]*cols]*rows

result = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if visited[x][y] != True and grid[x][y]=='1':
            result +=1
            mark_path(grid,x,y,visited)
        visited[x][y]=True

print(result)


