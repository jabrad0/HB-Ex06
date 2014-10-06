def hash_key(aMap, key):
    return hash(key) % len(aMap)

print hash(10)
print hash_key([200,4,5,6,6], 20)