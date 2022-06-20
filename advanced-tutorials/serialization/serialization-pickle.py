import pickle

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickled_string)
print(pickle.loads(pickled_string))