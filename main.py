input_the_road = str(input('''Please, input the road witout spaces: 
o = hole
. = normal
'''))

if 'o' not in input_the_road and '.' not in input_the_road:
    print('Incorrect data')
    exit()

try:
    X = int(input('Enter a length of car: '))
    S = int(input('Enter a count of skip_hole: '))
except ValueError:
    print('This value must be a number')
    exit()

the_road = [elem for elem in input_the_road]
the_new_road = []
len_the_road = len(the_road)
iterator_the_road = iter(the_road)
count_of_iteration = 0
def fix_hole():
    global len_the_road, count_of_iteration
    count_of_iteration += 1
    len_the_road -= X  
    for elem in range(X - 1):
        try:
            next(iterator_the_road)
        except StopIteration:
            len_the_road = 0

while len_the_road > 0:
    try:
        if next(iterator_the_road) == 'o':
            fix_hole()
            for elem in range(X):
                the_new_road.append('.')
            if S != 0:
                if next(iterator_the_road) == 'o':
                    the_new_road.append('o')
                    for elem in range(S - 1):
                        if next(iterator_the_road) == 'o':
                            the_new_road.append('o')
                        else:
                            the_new_road.append('.')
                    len_the_road -= S
                else: 
                    len_the_road -= 1
                    the_new_road.append('.')
        else: 
            if S != 0:
                the_new_road.append('.')
            len_the_road -= 1
    except StopIteration:
                len_the_road = 0   
print('Number of iterations that will remove the holes is:', count_of_iteration)
print('The road after fix holes: ', *the_new_road)

