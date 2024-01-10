def NULL_not_found(object: any) -> int:
     #your code here
    type_to_label = {
        type(None): "Nothing",
        float: "Cheese" if object != object else None,  # Special case for NaN
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }

    # get type
    object_type = type(object)
    
    # check if its nan
    if object_type is float and object != object:
        print(f"Cheese: {object} {object_type}")
        return 0

    # is type known
    if object_type in type_to_label:
        label = type_to_label[object_type]
        if object_type is str:
            if object:
                print("Type not Found")
                return 1
            print(f"{label}: {object_type}")
        else:
            print(f"{label}: {object} {object_type}")
        return 0

    # else
    print("Type not Found")
    return 1

