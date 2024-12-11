import csv
import os


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

def css_color_to_rgb(color):
    color = color.strip()
    
    if color.startswith("#"):
        if len(color) == 7:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            print(f"({r}, {g}, {b})") 
            return (r, g, b)
        elif len(color) == 4:
            r = int(color[1]*2, 16)
            g = int(color[2]*2, 16)
            b = int(color[3]*2, 16)
            print(f"({r}, {g}, {b})") 
            return (r, g, b)
        else:
            raise ValueError("Invalid hex color format")
    
    elif color.startswith("rgb"):
        color = color[color.index("(")+1:color.index(")")]
        parts = color.split(",")
        if len(parts) != 3:
            raise ValueError("Invalid rgb color format")
        r = int(parts[0].strip())
        g = int(parts[1].strip())
        b = int(parts[2].strip())
        print(f"({r}, {g}, {b})") 
        return (r, g, b)
    
    elif color.startswith("hsl"):
        color = color[color.index("(")+1:color.index(")")]
        parts = color.split(",")
        if len(parts) != 3:
            raise ValueError("Invalid hsl color format")
        h = int(parts[0].strip())
        s = int(parts[1].strip().strip('%')) / 100.0
        l = int(parts[2].strip().strip('%')) / 100.0
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60.0) % 2 - 1))
        m = l - c / 2
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        elif 300 <= h < 360:
            r, g, b = c, 0, x
        else:
            raise ValueError("Invalid hsl color format")
        r = int((r + m) * 255)
        g = int((g + m) * 255)
        b = int((b + m) * 255)
        print(f"({r}, {g}, {b})") 
        return (r, g, b)
    
    else:

        file_path = os.path.join(os.path.dirname(__file__), 'cssNamedColors.csv')
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if row[1].strip().lower() == color.lower():
                    hex_value = row[2].strip()
                    return css_color_to_rgb(hex_value)
        raise ValueError("Unsupported color format")


if __name__ == "__main__":
    css_color_to_rgb("#ff0000") # (255, 0, 0)
    css_color_to_rgb("rgb(0, 255, 0)") # (0, 255, 0)
    css_color_to_rgb("rgb(255, 0, 0)") # (255, 0, 0)
    css_color_to_rgb("blue") # (0, 0, 255)
    css_color_to_rgb("red") # (0, 0, 255)
    css_color_to_rgb("invalid-color") # raises ValueError

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

