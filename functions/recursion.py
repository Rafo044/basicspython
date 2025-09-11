def do_something(n : int):
        print(n)
        if n == 1:
            print("Function is done ")
            return

        do_something(n - 1)


do_something(3)
