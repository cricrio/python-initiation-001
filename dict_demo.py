dict1 = {
    "name": "John",
    "age": 30,
}

age = dict1["age"]

print("age", age)

if "city" in dict1:
    print("city with key access", dict1["city"])

print("city with get access", dict1.get("city"))

print("age with get access", dict1.get("age", 50))

dict1["city"] = "Berlin"

print(dict1.get("city", "Paris"))
