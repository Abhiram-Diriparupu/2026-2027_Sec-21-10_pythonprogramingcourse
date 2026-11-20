dict_data = {"one": 1, "two": 2, "three": 3}
print("Keys:", dict_data.keys())
print("Values:", dict_data.values())
print("Items:", dict_data.items())
print("get two:", dict_data.get("two"))
print("get z:", dict_data.get("z"))

dict_data.update({"two": 20, "four": 4})
print("After update:", dict_data)

removed = dict_data.pop("one")
print("Removed:", removed)
print("After pop:", dict_data)