def generator():
    while True:
        yield 1
 
for n in generator():
    print(n)