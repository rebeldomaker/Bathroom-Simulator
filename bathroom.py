def should_close_bathroom_door():
    """
    Asks the user whether the bathroom is moist or noisy and gives advice accordingly.
    """
    print("Is friend's bathroom moist or noisy?")
    print("1. Moist")
    print("2. Noisy")
    choice = input("Enter your choice (1 for Moist, 2 for Noisy): ")
    
    # Validate and respond to the user's choice
    if choice == "1":
        print("Close the door to keep moisture contained.")
    elif choice == "2":
        print("Close the door to reduce noise.")
    else:
        print("Invalid choice. Please enter 1 for Moist or 2 for Noisy.")

# Call the function to run the interactive session
should_close_bathroom_door()

"""def close_bathroom_door(bathroom_moist: bool = False, bathroom_noisy: bool = False):
    if bathroom_moist:
        return False
    if bathroom_noisy:
        return True"""
