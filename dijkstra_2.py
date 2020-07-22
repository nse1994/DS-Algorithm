#hash table for node neighbors 
graph= {}
graph["book"]={}
graph["book"]["lp"]= 5
graph["book"]["poster"]=0

graph["lp"]={}
graph["lp"]["bass_guitar"]= 15
graph["lp"]["drums"]=20

graph["bass_guitar"]={}
graph["bass_guitar"]["piano"]=20

graph["drums"]={}
graph["drums"]["piano"]=10

graph["poster"]={}
graph["poster"]["bass_guitar"]= 30
graph["poster"]["drums"]=35

graph["piano"]={}


# hash table for costs
infinity = float("inf")
costs= {}
costs["lp"]= 5
costs["poster"]= 0
costs["bass_guitar"]= infinity
costs["drums"]= infinity
costs["piano"]= infinity

# hash table for parent
parents={}
parents["lp"]= 'book'
parents["poster"]= 'book'
parents["bass_guitar"]= None
parents["drums"]= None
parents["piano"]= None

processed = [] 

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#code
node = find_lowest_cost_node(costs)
while node is not None: 
    cost= costs[node]
    neighbors= graph[node]
    for n in neighbors.keys(): 
        new_cost = cost + neighbors[n]  
        if costs[n]>new_cost:
            costs[n]= new_cost  
            parents[n]= node 
    processed.append(node) 
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)