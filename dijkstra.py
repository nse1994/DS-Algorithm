#hash table for node neighbors
graph= {}
graph["start"]={}
graph["start"]["a"]= 6
graph["start"]["b"]= 2

graph["a"]={}
graph["a"]["finish"]= 1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["finish"]=5

graph["finish"]= {}
#hash table for cost 
infinity = float("inf")
costs= {}
costs["a"]= 6
costs["b"]= 2
costs["finish"]= infinity

#hash table for parent
parents={}
parents["a"]= 'start'
parents["b"]= 'start'
parents["finish"]= None

processed = [] #to keep track of processed nodes

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#find the lowest-cost node that you haven't processed yet 
node = find_lowest_cost_node(costs)
while node is not None: #if all the nodes processed, this while loops ends 
    cost= costs[node]
    neighbors= graph[node]
    for n in neighbors.keys(): # go through all the neighbors of this node 
        new_cost = cost + neighbors[n] # if it's cheaper to get to this neighbor 
        if costs[n]>new_cost: # by going through this node....
            costs[n]= new_cost # ...update the cost for this node 
            parents[n]= node # this node becomes the new parent for this neighbor
    processed.append(node) # Mark this node as processed 
    node = find_lowest_cost_node(costs) # find the next node to process, and loop

print("Cost from the start to each node:")
print(costs)