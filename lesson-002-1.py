'''
Функции - ЯП
'''
def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for s in i:
    print_friends_count(s)
    print('-------')
         
     
