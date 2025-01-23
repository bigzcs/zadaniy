def cl():
    while True:
        try:
            q, w, e = input("Напишите 2 числа - ").split()

            q = int(q)

            e = int(e)

            if q >= 11:
                print("Число должно быть меньше или равно 10")
                exit()
            if e >= 11:
                print("Число должно быть меньше или равно 10")
                exit()

            if w == "+":
                print(q+e)
            elif w =="-":
                print(q-e)
            elif w == "*":
                print(q*e)
            elif w == "/":
                print(q//e)
        except ValueError:
            print("throws Exception")
cl()





