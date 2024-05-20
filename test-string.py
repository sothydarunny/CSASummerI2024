# Test cases for ASCII code to character conversion

# Test with valid input
ascii_code = 97  # ASCII code for 'a'
expected_output = 'a'
character = chr(ascii_code)
assert character == expected_output, f"Test failed: expected {expected_output}, got {character}"

# Test with the lowest boundary
ascii_code = 0  # ASCII code for NULL character
expected_output = '\x00'
character = chr(ascii_code)
assert character == expected_output, f"Test failed: expected {expected_output}, got {character}"

# Test with the highest boundary
ascii_code = 127  # ASCII code for DELETE character
expected_output = '\x7f'
character = chr(ascii_code)
assert character == expected_output, f"Test failed: expected {expected_output}, got {character}"

# Test with a number outside the valid range (below 0)
ascii_code = -1
try:
    character = chr(ascii_code)
    assert False, "Test should have failed with an invalid ASCII code below 0"
except ValueError:
    print("Passed: ValueError raised as expected for ASCII code below 0")

# Test with a number outside the valid range (above 127)
ascii_code = 128
try:
    character = chr(ascii_code)
    assert False, "Test should have failed with an invalid ASCII code above 127"
except ValueError:
    print("Passed: ValueError raised as expected for ASCII code above 127")

print("All tests passed!")
