def confirm(s):
    print(s)
    yn = input("Proceed?[y/N] ")
    return yn == "y" or yn == "Y"
