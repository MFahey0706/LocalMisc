def running(thelist):
    output = []
    for i in range(1,len(thelist)+1):
        output.append(sum(thelist[:i]))
    return output
