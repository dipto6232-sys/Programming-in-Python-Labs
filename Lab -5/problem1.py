resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    for resource in resources:
        print("ID:", resource[0])
        print("Name:", resource[1])
        print("Category:", resource[2])
        print("Quantity:", resource[3])
        print()


def search_by_category(resources, category):
    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)


def find_unavailable(resources):
    for resource in resources:
        if resource[3] == 0:
            print(resource)


print("All Resources:")
display_resources(resources)

print("Electronics Resources:")
search_by_category(resources, "Electronics")

print("Unavailable Resources:")
find_unavailable(resources)