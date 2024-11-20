end = 20
start = 2
for user_num in range(start, end + 1):
    is_prime = True
    
    for i in range(2, user_num):
        if user_num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f'Число {user_num} - просте')