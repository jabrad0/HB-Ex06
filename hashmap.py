# Creates a list with num_buckets items (default 256), each item is an empty list
def new(num_buckets = 256):
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap


# Returns a number between 0 and 255 based on the result of the hash function
# on the input string.
def hash_key(aMap, key):
    return hash(key) % len(aMap)

# Assigns the return value of "hash_key" to bucket_id and returns that index item from aMap
def get_bucket(aMap, key):
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

#
def get_slot(aMap, key, default = None):
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default

def get(aMap, key, default=0):
    i,k,v = get_slot(aMap, key, default = default)
    return v

def set(aMap, key, value):
    bucket = get_bucket(aMap, key)
    i,k,v = get_slot(aMap, key)

    if i >= 0:
        bucket[1] = (key, value)
    else:
        bucket.append((key, value))

def delete(aMap, key):
    bucket = get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k,v