class Solution(object):
    def romanToInt(self, s):
        # Convert the string to uppercase to handle both lowercase and uppercase inputs
        s = s.upper()  # Handle lowercase input

        # Initialize the total sum and previous value to 0
        sum = 0
        prevValue = 0

        # Define the mapping of Roman numeral characters to their integer values
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # Loop through each character in the string
        for char in s:
            currentValue = value[char]  # Get the integer value of the current Roman numeral character

            # If the current value is greater than the previous value, subtract twice the previous value
            # This handles cases like IV (4) or IX (9) using BODMAS
            if currentValue > prevValue:
                sum += currentValue - 2 * prevValue
            else:
                # Otherwise, simply add the current value to the total sum
                sum += currentValue

            # Update the previous value for the next iteration
            prevValue = currentValue

        # Return the final sum, which is the integer representation of the Roman numeral
        return sum
