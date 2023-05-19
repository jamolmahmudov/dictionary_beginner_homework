def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    a=[]
    for i in data:
        if i['age']>min_age and i['age']<max_age:
            a.append(i['age'])

    return a 
data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
min_age=int(input("min age"))
max_age=int(input("max age"))
age=27
print(get_user_names_with_age_range(data,min_age,max_age))