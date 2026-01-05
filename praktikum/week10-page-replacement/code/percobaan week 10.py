reference = [7,0,1,2,0,3,0,4,2,3,0,3,2]
frames = 3

def fifo(ref, frames):
    memory = []
    fault = 0
    for page in ref:
        if page not in memory:
            fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
    return fault

def lru(ref, frames):
    memory = []
    fault = 0
    for page in ref:
        if page not in memory:
            fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
    return fault

print("FIFO Page Fault:", fifo(reference, frames))
print("LRU Page Fault :", lru(reference, frames))
