def get_fibonacci_number(number_of_element):
    start,second=0,1
    while start < number_of_element:
        print(start,end='')
        start, second=second, start + second
        print()

 print(get_fibonacci_number(10))