def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    a=0
    for i in data.values():
        if a<i:
            a=i
    return a
data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }
print(find_max_value(data))