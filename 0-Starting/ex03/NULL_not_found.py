def NULL_not_found(object: any) -> int:
    types = {type(None): "Nothing", float: "Cheese", int: "Zero", str: "Empty", bool: "Fake"}
    typ = type(object)
    if (object and (typ is not float)) or typ not in types or (typ is float and object == object):
        print("Type not Found")
        return (1)
    print(f"{types[typ]}:", object, typ)
    return (0)