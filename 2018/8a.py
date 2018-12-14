with open('input/8', 'r') as f: # read data
    data = [int(i) for line in f for i in line.strip('\n').split()]

metadata = [] # list with all metadata entries
def Recursive_tree_search(metadata):
    child_nodes = data.pop(0)
    n_metadata_entries = data.pop(0)
    for child in range(child_nodes):
        metadata = Recursive_tree_search(metadata)
    for _ in range(n_metadata_entries):
        metadata.append(data.pop(0))
    return metadata

print(sum(Recursive_tree_search(metadata)))
