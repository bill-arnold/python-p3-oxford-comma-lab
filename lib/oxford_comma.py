def oxford_comma(elements):
    """Convert an array of string elements into a string using the Oxford comma."""
    if len(elements) == 1:
        # If there's only one element, return it as is
        return elements[0]
    elif len(elements) == 2:
        # If there are two elements, join them with ' and '
        return f"{elements[0]} and {elements[1]}"
    else:
        # If there are more than two elements, join them with commas and use ' and ' before the last element
        return f"{', '.join(elements[:-1])}, and {elements[-1]}"

# Example usage:
result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)
# Output: "fiddleheads, okra, and kohlrabi"
