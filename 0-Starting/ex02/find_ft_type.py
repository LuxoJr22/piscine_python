def all_thing_is_obj(object: any) -> int:
    new = type(object)
    
    if (new is str):
        print(object, "is in the kitchen :", new)
    elif isinstance(object, (list, tuple, set, dict)):
        print(new.__name__.capitalize(), ":", new)
    else:
        print("Type not found")
    return (42)