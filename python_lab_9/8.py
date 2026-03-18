check_same_values = lambda d: len(set(d.values())) == 1

dict1 = {'a': 10, 'b': 10, 'c': 10}
print("All values same:", check_same_values(dict1))