import time

def counter(s):
    for let in s:
        count = 0
        for sub_let in s:
            if let == sub_let:
                count += 1
#        print(let, count)
start = time.time()
for i in range(1_000_000):
    counter("queue")
end = time.time()
print(end - start)

def counter(s):
    for let in set(s):
        count = 0
        for sub_let in s:
            if let == sub_let:
                count += 1
#        print(let, count)
start = time.time()
for i in range(1_000_000):
    counter("queue")
end = time.time()
print(end - start)

#start = time.time()
#for i in range(1_000_000):
#    counter('quetr')
#end = time.time()
#print(end - start)


def counter(s): 
    let_counter = {}
    for let in s:
        let_counter[let] = let_counter.get(let, 0) + 1
    #print(let_counter)
counter('qeue')

start = time.time()
for i in range(1_000_000):
    counter('queue')
end = time.time()
print(end - start)