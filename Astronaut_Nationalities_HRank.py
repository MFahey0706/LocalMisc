def step(node):
    global visited
    global Networks
    global current_nation
    if visited[node]:
        return
    visited[node] = 1
    current_nation += [node]
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

Nations = []
for i in range(0, n):
    if not visited[i]:
        current_nation = []
        step(i) #DFS for our compatriots
        Nations += [set(current_nation)] #add completed nation
#calculate combinations
nation_nums = range(len(Nations))
print sum([len(Nations[i])*len(Nations[j]) for i in nation_nums for j in nation_nums if j > i])
    