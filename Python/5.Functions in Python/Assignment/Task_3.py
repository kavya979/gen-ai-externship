def make_sandwich(ingredients):
    print("Making a sandwich with the following ingredients:", end=' ')
    for i in ingredients:
        print(f"- {i}", end=" ")

make_sandwich(["Lettuce", "Tomato", "Cheese"])