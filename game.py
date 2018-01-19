def displayInventory(inventory):
    values = 0
    for k, v in inventory.items():
        print(v, k)
        values = values + v
    print("Total number of items: {}".format(values))


def addToInventory(inventory, addeditems):
    d = {}
    for k in addeditems:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1

    c = {}
    for x in set(inventory).union(d):
        c[x] = inventory.get(x, 0) + d.get(x, 0)
    return c


inve = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inve, dragonLoot)
displayInventory(inv)
