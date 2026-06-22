import json

if __name__ == '__main__':
    with open("input.json", 'r') as f:
        data = json.load(f)
    output = ",".join([*data[0]]) #The asterisk gets the keys of the json object without commas and brackets, then we .join will add commas because "," to create the header of csv. This is why we only use the first object of the json array because all objects have the same keys.

    for obj in data:
        try:
            with open("output.csv", "w") as f:
                  output += (f"\n{obj['Name']}, {obj['age']}, {obj['birthyear']}") # How to get the values of each key? The answer to that is to use the keys as indexes of the json object. For example, obj['Name'] will give us the value of the Name key. Want to know why? Because a json object is a dictionary in python, and we can access the values of a dictionary using the keys as indexes. So obj['Name'] will give us the value of the Name key in the current json object. We do this for each key to get all the values and then we concatenate them with commas to create a csv row. 
                  f.write(output)
        except Exception as e:
            print(f"An error occurred: {e}")
    print("Success")