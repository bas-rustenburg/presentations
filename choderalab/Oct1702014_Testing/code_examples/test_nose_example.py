# test_nose_example.py
def my_function(x, y):
    """Subtract y from x"""
    return x - y

def test_my_function():
    assert my_function(7,4) == 3
