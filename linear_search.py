def linear_search_dict(data, target):  # Define the function `linear_search_dict` which takes two arguments: `data` (the dictionary to search) and `target` (the value to find)
    for key, value in data.items():    # Loop through each key-value pair in the dictionary `data`
        if value == target:            # Check if the current value is equal to the target value
            return key                 # If the target is found, return the current key
    return None                        # If the loop completes without finding the target, return None to indicate the target is not in the dictionary

# Example usage
data = {"a": 5, "b": 3, "c": 8, "d": 6, "e": 2, "f": 10, "g": 7}  # Define a dictionary with keys and values
target = 6                                                        # Define the target value to search for

result = linear_search_dict(data, target)                         # Call the `linear_search_dict` function with the dictionary `data` and target value `target`, and store the result in `result`

if result is not None:                                            # Check if the result is not None (which means the target was found)
    print(f"Element found at key: {result}")                      # Print the key where the target was found
else:                                                             # If the result is None (which means the target was not found)
    print("Element not found in the dictionary")                  # Print that the target was not found in the dictionary
