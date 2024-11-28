def fibonacciFirst(n):
    
    if not isinstance(n, int):
        return TypeError("Invalid input - Input must be an integer")
    if n < 0:
        return TypeError("Invalid input - Input must be a positive integer")
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

def fibonacci(n):
    p = fibonacciFirst(n)
    #print(p)
    if n == 0:
        return p[n]
    else:
        return p[n-1]
    

""""
# Test the function
n = 0  # Number of Fibonacci numbers to generate
result = fibonacci(n)
print(result)


# Celsius to Fahrenheit
print(CelesiusToFahrenheit(54))
print(FahrenheitToCelsius(-80))
"""

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return TypeError("Invalid input - Input must be an integer or float")
    if celsius < -273.15:
        return ValueError("Invalid input - Temperature cannot be less than -273.15°C")
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        return TypeError("Invalid input - Input must be an integer or float")
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def is_prime(n):
    if not isinstance(n, int):
        return TypeError("Invalid input")
    if n <= 0:
        return False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    if start > end:
        a = start
        start = end
        end = a
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def rottate_array(arr, n):
    if arr is None:
        raise ValueError("Invalid input - Array cannot be null")
    
    if not isinstance(arr, list):
        raise ValueError("Invalid input - Array must be a list")
    if not isinstance(n, int):
        raise ValueError('A very specific bad thing happened.')
    if n < 0:
        n = len(arr) - n
    n = n % len(arr)
    return arr[n:] + arr[:n]


def split_into_threes(arr):
    if arr is None:
        raise ValueError("Invalid input - Array cannot be null")
    if not isinstance(arr, list):
        raise ValueError("Invalid input - Array must be a list")
    if len(arr) % 3 != 0:
        last_length = len(arr) % 3
        last_array = arr[-last_length:]
        arr = arr[:-last_length]
        result = [arr[i:i + 3] for i in range(0, len(arr), 3)]
        result.append(last_array)
    else:
        result = [arr[i:i + 3] for i in range(0, len(arr), 3)]
    return result

"""
def vowels_and_consonants(s):

    if not isinstance(s, str):
        raise ValueError("Invalid input - Input must be a string")
    vowels = 0
    consonants = 0
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiouáéíóúůý':
                vowels += 1
            if char.lower() in 'hjklmnprstvzžščřcjďťň':
                if char.lower() == "ch":
                    consonants += 1
                consonants += 1
    return {'vowels': vowels, 'consonants': consonants}
    """

def class_and_break_time(start_class, end_class):
    h = 45
    b = 0
    if start_class == end_class == 0:
        return 0, 0
    if (start_class == 0):  
        if(end_class == 1):
            return 1*h, 5
        if(end_class == 2):
            return 2*h, 15
        if(end_class == 3):
            return 3*h, 35
        if(end_class == 4):
            return 4*h, 45
        if(end_class == 5): 
            return 5*h, 55
        if(end_class == 6): 
            return 6*h, 60
        if(end_class == 7): 
            return 7*h, 65
        if(end_class == 8): 
            return 8*h, 70

def css_color_to_rgb(color):
    if not isinstance(color, str):
        raise ValueError("Invalid input - Input must be a string")
    if color[0] == "#":
        color = color[1:]
    if color.startswith("rgb(") and color.endswith(")"):
        color = color[4:-1]
        r, g, b = color.split(",")
        r = int(r.strip())
        g = int(g.strip())
        b = int(b.strip())
        return r, g, b

    if len(color) != 6:
        raise ValueError("Invalid input - Input must be a string")
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b

if __name__ == "__main__":
    print(css_color_to_rgb("#ffffff"))
    print(css_color_to_rgb("#ff0000"))
    print(css_color_to_rgb("rgb(255, 0, 0)"))

"""
print(split_into_thress([1, 2, 3, 4, 5, 6, 7]))
print(split_into_thress(123))
print(primes_in_range(15, 9))

print(rottate_array([1, 2, 3, 4, 5], 2))
print(rottate_array([1, 2, 3, 4, 5], -1))
print(rottate_array("is not an list", -1))


print(is_prime(1))
print(is_prime(2))
print(is_prime(0))
print(is_prime("a"))

print(primes_in_range(0, 11))

print("Hello World")

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))

twoDimArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(twoDimArray[1][1])

"""

