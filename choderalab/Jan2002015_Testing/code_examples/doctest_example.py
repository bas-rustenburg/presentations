# doctest_example.py
def my_function(x, y):
    """Subtract y from x
    Examples
    --------
    >>> my_function(7, 4)
    3
    >>> my_function(7, '4')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for -: 'int' and 'str'
    """
    return x - y
    
if __name__ == "__main__":
    #Execute script as: python doctest_example.py -v
    import doctest
    doctest.testmod()
