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
nation = []
for i in range(0, n):
    if not visited[i]:
        nation = []
        step(i) #DFS for our compatriots
        Nation_sizes += [len(nation)]
#calculate combinations
result = 0
for i in range(len(Nation_sizes)-1):
    result += Nation_sizes[i]*sum(Nation_sizes[i+1:])
print result
    