number_vertices = 7 # number of vertices

Graph = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 0, 22, 0, 18],    #Graph to be tested
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 18, 24, 0, 0]]

V_in_mst = [0, 0, 0, 0, 0, 0, 0]   #this Array is created to track the selected vertex

number_of_edge = 0   # Intialise number of edges to zero at first
V_in_mst[0] = True  #We are selecting the first vertix 

print("Edge : Weight\n")
while (number_of_edge < number_vertices - 1):  #Loop to find vertices in MST 
    min = 9999999    #assuming minimum weight to equal to infinity number 
    x = 0   # set vertices to zero
    y = 0
    for i in range(number_vertices):
        if V_in_mst[i]:
            for j in range(number_vertices):
                if ((not V_in_mst[j]) and Graph[i][j]):  # if vertex is not yet in MST array and there is an edge
 
                    if min > Graph[i][j]:   #if current weight is less than min set 
                        min = Graph[i][j]  #make the min take the current weight
                        x = i
                        y = j
    print(str(x+1) + "-" + str(y+1) + ":" + str(Graph[x][y])) #printing selected vertices in the graph and their weight
    V_in_mst[y] = True  #Mark current vertex as selected to avoid repetition 
    number_of_edge += 1  #Move to the next edge

