def input_type(value):
    valueType = type(value)
    if valueType =="<class 'str'>":
        return print("string")
    elif valueType == "<class 'int'>":
        return print("integer")
    elif valueType =="<class 'float'>":
        return print("double")
    else:
        return print("Boolen")


def main():
    input_type("Hello everybody")
    input_type(323)
    input_type(21.1)

   

if __name__ == '__main__': 
    main()