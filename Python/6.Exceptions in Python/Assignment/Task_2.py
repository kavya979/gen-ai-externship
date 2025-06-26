def types_of_exception(list_of_triggers):
    for trigger in list_of_triggers:
        try:
            if trigger == "index":
                # IndexError: accessing invalid index in a list
                my_list = [1, 2, 3]
                print(my_list[5])
            elif trigger == "key":
                # KeyError: accessing non-existent dictionary key
                my_dict = {"name": "Alice"}
                print(my_dict["age"])
            elif trigger == "type":
                # TypeError: adding string and integer
                result = "Age: " + 25
                print(result)
            else:
                print(f"Unknown trigger: {trigger}")
        except IndexError:
            print("IndexError occurred! List index out of range.")
        except KeyError:
            print("KeyError occurred! Key not found in the dictionary.")
        except TypeError:
            print("TypeError occurred! Unsupported operand types.")

types_of_exception(["index", "key", "type"])

