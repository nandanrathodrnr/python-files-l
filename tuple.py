def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0
    else:
        return True
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Determine if the numbers are prime or le
for number in numbers:
    print(f"{number} is {'a prime number' if is_prime(number) else 'not a prime number'} and {'a leap year' if is_leap_year(number) else 'not a leap year'}.")