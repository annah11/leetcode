def rearrange_queue(n, t, s):
    queue = list(s)  
    for _ in range(t):  
        i = 0
        while i < n - 1:
            if queue[i] == 'B' and queue[i + 1] == 'G':
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                i += 2
            else:
                i += 1

    return "".join(queue)  

n, t = map(int, input().split())
s = input().strip()

print(rearrange_queue(n, t, s))
