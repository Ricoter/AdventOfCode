with open('input/8', 'r') as f: # read data
    data = [int(i) for line in f for i in line.strip('\n').split()]

def Recursive_tree_search():
    
    child_nodes = data.pop(0) # number of child nodes
    metadata_entries = data.pop(0) # number of metadata entries
    child_values = [] # list to save the 'values' of the children

    for child in range(child_nodes): # iterate recursively through children
        value = Recursive_tree_search() # save value of childs
        child_values.append(value)
    
    value = 0
    for _ in range(metadata_entries):
        entry = data.pop(0)
        if child_nodes == 0: # value= sum(metadata) if it has no children
            value += entry
        elif entry <= child_nodes: #
            value += child_values[entry - 1]
    
    return value


value = Recursive_tree_search()
print(value)
