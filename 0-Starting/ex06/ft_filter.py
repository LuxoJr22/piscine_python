def default(x):
    """Return the value passed as argument"""
    return x


def ft_filter(func, object: any) -> any:
    """filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    if not func:
        func = default
    ret = []
    for i in object:
        if func(i):
            ret.append(i)
    return (iter(ret))
