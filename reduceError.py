list_data = []
list_keys = []
list_errors = []
answer = []
n = int(input())
def search(p, ch, graph):
    if ch not in graph:
        return 'No'
    if p == ch or p in graph[ch]:
        return 'Yes'
    for k in range(len(graph[ch])):
        new_ch = search(p, graph[ch][k], graph)
        if new_ch == 'Yes':
            return 'Yes'
    return 'No'
for i in range(n):
    s = [i for i in input().replace(':', ' ').split()]
    list_data += [s]
    if s[0] not in list_keys:
        list_keys += [s[0]]
d = {e: [] for e in list_keys}
for i in range(n):
    for j in range(1, len(list_data[i])):
        d[list_data[i][0]] += [list_data[i][j]]
q = int(input())
for i in range(q):
    s = [i for i in input().split()]
    list_errors += s
right_location = [list_errors[0]]
for i in range(1, len(list_errors)):
    list_answer = []
    for c in right_location:
        list_answer += [search(c, list_errors[i], d)]
    if 'Yes' in list_answer:
        answer += [list_errors[i]]
    else:
        right_location += [list_errors[i]]
for c in answer:
    print(c)

