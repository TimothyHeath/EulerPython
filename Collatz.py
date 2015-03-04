#Euler Project 14 - Timothy Heath
START_BOUND = 1000000
#Which Collatz sequence starting below START_BOUND goes longest to reach 1?
collatz = [0,1] #initialize Collatz seq lengths for 0 (ignore) and 1
max_len = 1 #holds max length seq so far
max_node = 1 #holds start of max length seq so far
for i in range(2,START_BOUND):
    collatz.append(0) #0 indicates unchecked node
for i in range(1,START_BOUND):
    node = i #for every node (value of seq length from a start number)
    seq = [] #make a sequence of nodes with unknown values
    while (node >= START_BOUND or collatz[node] == 0): #if value of this node not known
        seq.append(node) #add to list of unknown nodes
        if node % 2 == 0: #follow path one step from this node
            node = node / 2 
        else:
            node = 3 * node + 1
    length = collatz[node] + 1 #found a known node so values of nodes in seq now known
    while seq != []: #compute their values
        node = seq.pop()
        if node < START_BOUND:
            collatz[node] = length
        if seq == [] and length > max_len: #last node in seq is candidate for max_len
            max_len = length
            max_node = node
        length += 1
print max_node #max_node thus far starts the longest sequence
