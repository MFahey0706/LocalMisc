
def step(node):
    global visited
    global Networks
    global nation
    if visited[node]:
        return
    visited[node] = 1
    nation += [node]
    for x in Networks[node]:
        step(x)  
    return 
 
n, q = map(int,raw_input().strip().split(' '))
visited = [0]*n
Networks = {x:[] for x in range(0,n)}
for _ in xrange(q):
    astro_1, astro_2 = map(int,raw_input().strip().split(' '))
    Networks[astro_1] += [astro_2]
    Networks[astro_2] += [astro_1]

Nation_sizes = []
nationals = 0
for i in range(0, n):
    if not visited[i]:
        queue = [i]
        nationals = 0
        while queue:
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = 1
                nationals += 1
                queue += Networks[node]
        Nation_sizes += [nationals]
#calculate combinations
def buh(Nation_sizes):
    result = 0
    L = len(Nation_sizes)
    for i in range(L-1):
        for j in range(L):
            if j > i:
                result += Nation_sizes[i]*Nation_sizes[j]
    return result
    
print buh(Nation_sizes)
    