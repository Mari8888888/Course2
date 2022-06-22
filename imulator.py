n = int(input())
list_namespace = ['global']
list_data = []
list_get = []
def search(a, ns, lst, dn):
    if a in dn[ns]:
        return ns
    else:
        for key, value in dn.items():
            if ns in dn[key]:
                return search(a, key, lst, dn)
for i in range(n):
    s = [i for i in input().split()]
    if s[1] not in list_namespace:
        list_namespace += [s[1]]
    list_data += [s]
list_namespace = list_namespace[::-1]
d = {e: [] for e in list_namespace}
for i in range(n):
    if list_data[i][0] == 'add':
        d[list_data[i][1]] += [list_data[i][2]]
    if list_data[i][0] == 'create':
        d[list_data[i][2]] += [list_data[i][1]]
    if list_data[i][0] == 'get':
        list_get += [search(list_data[i][2], list_data[i][1], list_namespace, d)]
for c in list_get:
    print(str(c))
