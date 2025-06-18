try:
    num=int(input("enter a number: "))
    a=[3,6]
    print(a[num])
except ValueError:
    print("invalid number!")
except IndexError:
    print("invalid Index!")