def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    a=0
    for i in data:
        if i['age']==age:
            a+=1
    return a



data = [
  {
    'name': 'John',
    'age': 27
  },
  {
    'name':'Mary', 
    'age': 42
  },
  {
      'name':'jamol',
      'age':42
  },
  {
    'name':'Ann',
    'age': 27
  }
  ]
age = 42

print(count_users_with_age(data,age))