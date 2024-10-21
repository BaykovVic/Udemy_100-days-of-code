try:
    file = open("file.txt")
    d = {"key": "value"}
    print(d["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as err:
    print(f"That key does not exist. {err}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")
#KeyError

#d = {"key": "value"}
#value = d["non_existent_key"]

#IndexError

#lst = ["0", "2", "3"]
#item = lst[3]

#TypeError


#text = "abc"
#print(text + 5)
