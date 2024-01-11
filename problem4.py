def is_palindrome(num):
    # Convert the number to a string and check if it reads the same backward and forward
    return str(num) == str(num)[::-1]

def largest_palindrome_product():
    largest_palindrome = 0

    # Loop through all 3-digit numbers
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j

            # Check if the product is a palindrome and larger than the current largest palindrome
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

# Call the function and print the result
result = largest_palindrome_product()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
