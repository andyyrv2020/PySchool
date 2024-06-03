def phonebook():
    phone_book = {}
    
    while True:
        command = input().split()
        action = command[0]
        
        if action == "A":
            name, number = command[1], command[2]
            phone_book[name] = number
        elif action == "S":
            name = command[1]
            if name in phone_book:
                print(f"{name} -> {phone_book[name]}")
            else:
                print(f"Contact {name} does not exist.")
        elif action == "END":
            break

# Example usage
# phonebook()
