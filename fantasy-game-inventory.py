def add_inventory(inventory, loot):
  for v in loot:
    inventory.setdefault(v, 0)
    inventory[v] += 1


def print_inventory(stuff):
  print("Inventory:")
  total = 0

  for k, v in stuff.items():
    print(v, k)
    total += v

  print('\nTotal number of items:', total)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print_inventory(stuff)
add_inventory(stuff, loot)
print_inventory(stuff)
