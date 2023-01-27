 print ('Hello, World!')

# You know nothing, Jon Snow!

print ('Robert')
print ('Stannis')
print ('Renly')

print ('9780262531962')

print (' What Is Dead May Never Die')

print (81/9) #=>

print (6-(-81)) #=>

print (3**5) #=>
print ((-8)/(-4)) #=>

print (8/2+5-(-3)/2) #=>

print (70*(3+4)/(8+2)) #=>

print (0.39*0.22) #=>

print (5 ** 2 - 3 * 7)

print ('''"Khal Drogo's favorite word is \"athjahakar\""''')

print ('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

print('Winter came for ' + 'the House of Frey.')

print (chr(126));
print (chr(94)); 
print (chr(37))

motto = 'What Is Dead May Never Die!'
print(motto)

name = 'Brienna'
# BEGIN (write your solution here)
name = 'anneirB'
# END
print(name)

x = '2'
print (x)

family = 'Targaryen'
pet = 'Dragon'
# BEGIN (write your solution here)
print(family)
print(' and ')
print(pet)
# END

euros_count = 100
# BEGIN (write your solution here)
dollars = euros_count * 1.25
rubles = dollars * 60
print(dollars)
print(rubles)
# END

info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."
first_name = 'Joffrey'
greeting = 'Hello'
# BEGIN (write your solution here)
print (greeting + ', ' + first_name + "!")
print (intro + '\n' + info)
# END

first_number = 20
second_number = -100
print(first_number * second_number)

king = "Rooms in King Balon's Castle:"
# BEGIN (write your solution here)
king_number = 6
castle = 17
print(king)
print(king_number * castle)
# END

DRAGONS_BORN_COUNT = 3

stark = 'Arya'
# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}?')
# END

name = 'Na\nharis'
# BEGIN (write your solution here)
print(name[-1])
# END

value = 'Hexlet'
# BEGIN (write your solution here)
print(value[2:5])
# END

# BEGIN (write your solution here)
text = """Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground."""
# END
print(text)

print(-0.304)

a = "7"
b = "-8"
c = "-2"
print (int(a)-(int(b) - int(c)))

one = 'Naharis'
two = 'Mormont'
three = 'Sand'
# BEGIN (write your solution here)
print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
# END

value = 2.9
a = 'times'
# BEGIN (write your solution here)
print(int(value),a )
# END

company1 = 'Apple'
company2 = 'Samsung'
# BEGIN (write your solution here)
print(len(company1) + len(company2))
# END

number = 255
# BEGIN (write your solution here)
print(hex(number))
# END

number = 10.1234
# BEGIN (write your solution here)
print(round(number, 2))
# END

text = 'Never forget what you are, for surely the world will not'
# BEGIN (write your solution here)
print(f'First: {text[0]}\nLast: {text[-1]}')
# END

# BEGIN (write your solution here)
print(min(3, 10, 22, -3, 0))
# END

# imports are studied on Hexlet
from random import random
# BEGIN (write your solution here)
print(round(random()*10))
# END

motto = 'Family, Duty, Honor'
# BEGIN (write your solution here)
print(type(motto))
# END

text = 'a MIND needs Books as a Sword needS a WHETSTONE.'
# BEGIN (write your solution here)
print(text.lower())
# END

first_name = '  Grigor   \n'
# BEGIN (write your solution here)
print(first_name.strip())
# END

text = 'Never forget what you are, for surely the world will not'
# BEGIN (write your solution here)
print(f'Index Of N: {text.find("N")}\nIndex Of ,: {text.find(",")}')
# END

text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# BEGIN (write your solution here)
print(len(text[4:15].strip()))
# END

def print_motto():
    print("Winter is coming")

# BEGIN (write your solution here)
def say_hurray_three_times():
    return "hurray! hurray! hurray!"
# END

def truncate(text, length):
    # BEGIN (write your solution here)
    return text[:length] + '...'
    # END

def get_hidden_card(card_number, num = 4):
    return '*' * num + card_number[-4:]

def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions 

def is_pensioner(age):
    return True if age >= 60 else False

def is_mister(text):
    return text == 'Mister'

def is_international_phone(text):
    return text.startswith('+')

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
def is_not_palindrome(text):
    text = text.lower()
    return text != text[::-1]

def string_or_not(arg):
    return 'yes' if isinstance(arg, str) else 'no'

def guess_number(number):
    return 'You win!' if number == 42 else 'Try again!'

def normalize_url(url):
    if url.startswith('https://'):
        return url
    elif url.startswith('http://'):
        return 'https://' + url[len('http://'):]
    else:
        return 'https://' + url

def who_is_this_house_to_starks(human):
    if human in ['Karstark', 'Tully']:
        return 'friend'
    elif human in ['Lannister', 'Frey']:
        return 'enemy'
    else:
        return 'neutral'

def flip_flop(text):
    return 'flop' if text == 'flip' else 'flip'

def print_numbers(number):
    while number > 0:
        print(number)
        number -= 1
    print('finished!')

def multiply_numbers_from_range(low, higth):
    if low == higth:
        return low
    result = 1
    while low <= higth:
        result *= low
        low += 1

    return result

def join_numbers_from_range(begin, end):
    return ''.join([str(x) for x in range(begin, end + 1)])

def print_reversed_word_by_symbol(word):
    for i in word[::-1]:
        print(i)

def count_chars(word, char):
    return word.lower().count(char.lower())

def my_substr(text, n):
    return text[:n]

def is_arguments_for_substr_correct(text, start, length):
    if length < 0:
        return False
    elif start < 0:
        return False
    elif start >= len(text):
        return False
    elif start + length > len(text):
        return False
    elif start == 0 and length == 0:
        return True
    else:
        return True

print(is_arguments_for_substr_correct('Sansa Stark', 0, 0))

def filter_string(text, char):
    return text.replace(char, '')

def is_contains_char(text, char):
    return True if text.count(char) else False

def filter_string(text, char):
    result = ''
    for i in text:
        if i.lower() != char.lower():
            result += i
    return result
