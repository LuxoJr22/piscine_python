def ft_filter(func, object: any) -> any:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    dict = []
    try:
        for i in object:
            print(func(i))
            print("non")
            if func(i):
                dict.add(i)
        return (dict)
    except ValueError:
        return (dict)
