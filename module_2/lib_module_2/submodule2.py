import os

def execute():
    print(f'''This is {os.path.basename(__file__)}''')
    print("dins de l'execute del submodul 2")

if __name__ == "__main__":
    main()