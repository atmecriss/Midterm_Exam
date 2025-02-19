#Q1
a = 10
a = a + 2
print(a*2)

a = 19
print(a + 3)
a = a // 2
print(a)

#Q2
print(2+3*6/2)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#Q3
a = 3
b = 4


day_of_week = 2
month_of_year = 2

a = a + day_of_week
b += month_of_year

print(a)
print(b)

c = a + b
print(c)

d = "abc" * (c // 3)
print(d)

#Q4
def palindrome(word):
    return word == word[::-1]

numbers = {
    "A": "4257304920394478392772938744930294037524",
    "B": "7798338247658278460338648728567428338977",
    "C": "2704702208931031198668911301398022074072",
    "D": "0974101607733149676776769413377061014790"
}
for option, num in numbers.items():
    print(f"{option}: {'Palindrome' if palindrome(num) else 'Not a Palindrome'}")

#Q5
def count_un_an_patterns(text):
    """
    This function finds all occurrences of words that start with 'un' and end with 'an'
    and returns the count of matches.
    """
    # We have to split the text into words to get an answer
    words = text.split()
    count = 0  # Initialize the counter to 0

    # We have to loop through each word
    for word in words:
        # We check each word with .startswith("un") and .endswith("an")
        if word.startswith("un") and word.endswith("an"):
            # And finally count the words that work for both conditions
            count += 1

    return count  # Return the total count


# Sample text to check the pattern
text = "unhappy unkind unbroken uncertain unusualunman undoneun an ultra unman"

# The function should return 2 as there are only 2 words that start with "un" and end with "an"
print(count_un_an_patterns(text))

#Q6
my_list = [1, 2, 3]
print("Original List:", my_list)

my_list[0] = 10
print("Modified List:", my_list)

my_list.append(4)
print("List after Append:", my_list)

my_string = "hello"
print("Original String:", my_string)

# new string
new_string = "H" + my_string[1:]
print("New String:", new_string)

#Q7
import random
random_numbers = []

# Step 1: Generate 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Loop through the list and apply conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace the numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        # Replace numbers less than 50 with "XX"
        random_numbers[i] = "XX"

# Step 3: Print the new list
print(random_numbers)

# Q8
def is_valid_url(url):
    """
    This function checks if the passed parameter is a valid URL or not.
    It uses only the string methods and concepts learned in class.
    """

    # Check if the URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False  # Not a valid URL

    # Check if the URL contains at least one dot (.) for domain
    if url.count('.') < 1:
        return False  # No dot, hence not a valid URL

    # Are there any spaces in the URL
    if ' ' in url:
        return False  # Spaces are not allowed in URLs

    # All checks pass, then it is a valid URL
    return True


# Example
urls = [
    "https://example.com",
    "http://example.org",
    "www.example.com",
    "https://example",
    "https://example .com",
    "https://example.com/page",
    "example.com"
]

# Check each URL and print if it's valid or not
for url in urls:
    print(f"{url}: {'Valid' if is_valid_url(url) else 'Invalid'}")

#Q9
def days_since_birthday(birthday):

    day, month, year = birthday.split('-')
    year = int(year)

    current_year = 2025

    full_years = current_year - year - 1

    leap_years = 0
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_years += 1

    total_days = (full_years * 365) + leap_years

    return total_days

birthday = "09-05-2004"
print(f"Days passed since your birthday: {days_since_birthday(birthday)}")
