def all_thing_is_obj(object: any) -> int:
   #your code here
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "is in the kitchen"
    }

    # get type 
    obj_type = type(object)

    # checks and do the prints
    if obj_type == str:
        print(f"{object} {type_names[obj_type]} : {obj_type}")
    elif obj_type in type_names:
        print(f"{type_names[obj_type]} : {obj_type}")
    else:
        print("Type not found")

    return 42
