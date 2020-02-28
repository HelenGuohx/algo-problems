# O(n)
# O(C): constant

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)



a = get_number()
b = get_number()
res = []
for i in range(a,b+1):
    if (i-1)%2 != 0 and (i-1)%3 != 0:
        res.append(i)
print(len(res))



