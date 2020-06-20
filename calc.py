def main():
    def add(x, y):
        return x + y
    
    def sub(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def div(x, y):
        return x / y

    operation = input('1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n')

    if operation in ('1', '2', '3', '4'):
        x = float(input('First Number: '))
        y = float(input('Second Number: '))

        if operation == '1':
            print(add(x , y))
        elif operation == '2':
            print(sub(x, y))    
        elif operation == '3':
            print(mult(x, y))
        elif operation == '4':
            print(div(x, y))
    else:
        print('Please try again.')

        if operation == 1:
            print(add(x, y))
            
if __name__ == "__main__":
    main()