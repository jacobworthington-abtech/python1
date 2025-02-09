message = "Hello, Jacob! Welcome to Python programming."
print(message)

message = "Hurray for Python"
print(message)

# Initial guest list
guest_list = [
    "My Grandfather",
    "Albert Einstein",
    "Billy Graham"
]

# Print initial invitation messages
print("\nInitial Guest List:")
for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner.")

# Inform that a bigger dinner table is found
print("\nWe found a bigger dinner table! More space is now available.")

# Adding three new guests
guest_list.insert(0, "Jacques-Yves Cousteau")  # Add to the beginning
guest_list.insert(len(guest_list) // 2, "Charles Darwin")  # Add to middle
guest_list.append("Thomas Edison")  # Add to the end

# Sort the list alphabetically
guest_list.sort()

# Print updated invitation messages for the sorted list
print("\nUpdated Guest List - Sorted:")
for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner.")


# Addition
print(5 + 3)

# Subtraction
print(16 - 8)

# Multiplication
print(2 * 4)

# Division
print(64 / 8)
