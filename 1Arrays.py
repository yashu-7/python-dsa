a = [1,2,3,4,5,6,7,8,9]

# Arrays
print(len(a))
print(a[0],a[8])

# Iterators
for index,value in enumerate(a):
    print(f"AT POS {index} lies > {value}")

# Invariants
# Enable a correct or for proof
min_val = 6
for i in a:
    if i<min_val:
        min_val = i
    else:
        continue
print(min_val)