# Get input from the user
ascii_code = int(input("Enter an ASCII code (between 0 and 127): "))

# Check if the input is within the valid range
if 0 <= ascii_code <= 127:
    # Convert ASCII code to character and display it
    character = chr(ascii_code)
    print(f"The character for ASCII code {ascii_code} is '{character}'")
else:
    # Inform the user if the input is out of bounds
    print("Invalid input! Please enter a number between 0 and 127.")
