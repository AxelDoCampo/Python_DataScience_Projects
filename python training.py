#%%
from tkinter import *
# %%
if __name__ == '__main__':
    window = Tk()
    window.title('Calculadora')

    expression_field = Entry(window,width=30)
    expression_field.grid(row=0,column=0,columnspan=4)

    button1 = Button(window,text='1',height=3,width=3,borderwidth=1)
    button1.grid(row=1,column=0,sticky='ew')

    button2 = Button(window,text='2',height=3,width=3,borderwidth=1)
    button2.grid(row=1,column=1,sticky='ew')

    button3 = Button(window,text='3',height=3,width=3,borderwidth=1)
    button3.grid(row=1,column=2,sticky='ew')

    mult = Button(window,text='*',height=3,width=3,borderwidth=1)
    mult.grid(row=1,column=3,sticky='ew')

    button4 = Button(window,text='4',height=3,width=3,borderwidth=1)
    button4.grid(row=2,column=0,sticky='ew')

    button5 = Button(window,text='5',height=3,width=3,borderwidth=1)
    button5.grid(row=2,column=1,sticky='ew')

    button6 = Button(window,text='6',height=3,width=3,borderwidth=1)
    button6.grid(row=2,column=2,sticky='ew')

    minus = Button(window,text='-',height=3,width=3,borderwidth=1)
    minus.grid(row=2,column=3,sticky='ew')

    button7 = Button(window,text='7',height=3,width=3,borderwidth=1)
    button7.grid(row=3,column=0,sticky='ew')

    button8 = Button(window,text='8',height=3,width=3,borderwidth=1)
    button8.grid(row=3,column=1,sticky='ew')

    button9 = Button(window,text='9',height=3,width=3,borderwidth=1)
    button9.grid(row=3,column=2,sticky='ew')

    plus = Button(window,text='+',height=3,width=3,borderwidth=1)
    plus.grid(row=3,column=3,sticky='ew')

    window.mainloop()
# %%
a = 'I scream, you scream, we all scream for ice cream'
print([pos for pos, char in enumerate(a) if char == ' '])
# %%
b=[]
c=0
for i in a:
    if i==' ':
        b.append(c)
    c=c+1
print(b)
# %%
[i for i,v in enumerate(a) if v==' ']
# %%
'hola, hoy es {dia} mes {mes}'.format(dia='viernes', mes='enero')
# %%
a = 'https://www.hsbc.com.ar'
print(a.lstrip('https://'))
# %%
a = 'hola'
a[::-1]
# %%
the_string = "Python is cool, Python is great"
python_word_2 = the_string[-15:-9]
python_word_2
# %%
# Define here the variables in the problem statement.
full_name = 'Axel Do Campo'
address_line = 'Lavalleja 162'
post_code = '1414'
country = 'Argentina'
telephone_number = '1132323595'

# Define here the f-string
label = f'Name: {full_name}\nAddress: {address_line}\nPostal Code: {post_code}\nCountry: {country}\nPhone Number: {telephone_number}'

# Print here your string
print(label)
# %%
capital = int(input('Please enter your loan amount'))
interest = capital * 4/100
total = capital + interest
print(f'You will have to pay: {str(total)}')
# %%
with open(r'C:\Users\PC\Desktop\asd.txt', 'r') as archivo:
    data = archivo.read()
    data_final = str(int(data)+1)
with open(r'C:\Users\PC\Desktop\asd.txt', 'w') as archivo:
    archivo.write(data_final)

# %%
# Your code here
def how_much_should_each_of_us_pay(total_amount, number_of_people, tip_percentage):
    individual_pay = total_amount*(1+tip_percentage/100)/number_of_people
    
    print(f'Each of you need to pay: £{individual_pay}')
    
how_much_should_each_of_us_pay(10000,7,10)
# %%
def mean(*args):
    print(args)
    print(sum(args)/len(args))
    
mean(1,2,3,4,5,6,7,8,9)
# %%
def decimal_to_binary(val=0):
    binary = bin(val)
    return binary[2:]
    
binario = decimal_to_binary(10)
print(binario)
# %%
j='0b321321'
j[j.index('b')+1:]

# %%
z = 'laweac120cosmica'
def extract_from_number_to_end(input_string):
    output = input_string # return input if no number found
    for i,v in enumerate(input_string):
        if v.isdigit():
            #pos = input_string.find(char)
            output = input_string[i:]
            break #stop as we have found the first number
    return output

extract_from_number_to_end(z)
# %%
z.search('w')
# %%
j.partition('b')[2]
# %%

def is_even(number):
	return number % 2 == 0

def is_odd_or_even(num):
    if is_even(num):
        return 'Is even'
    else:
        return 'Is odd'

is_odd_or_even(13)
# %%
a = True
b = False
c = not b

if not b or not c and a:
    if a:
        print("A")
    print("B")
else:
    if not c:
        print("C")
    elif not b:
        print("D")
    elif not a:
        print("E")
    else:
        print("F")
        print("G")
print("H")
# %%
def get_zodiac_sign(month_of_birth, day_of_birth): # please don't change
	# your code here should return a string back. For example: return "Scorpio"
    if "Dec" in month_of_birth.title():
        if day_of_birth < 22:
            return "Sagittarius"
        else:
            return "Capricorn"
    elif "Jan" in month_of_birth.title():
        if day_of_birth < 20:
            return "Capricorn"
        else:
            return "Aquarius"
    elif "Feb" in month_of_birth.title():
        if day_of_birth < 19:
            return "Aquarius"
        else:
            return "Pisces"
    elif "Mar" in month_of_birth.title():
        if day_of_birth < 21:
            return "Pisces"
        else:
            return "Aries"
    elif "Apr" in month_of_birth.title():
        if day_of_birth < 20:
            return "Aries"
        else:
            return "Taurus"
    elif "May" in month_of_birth.title():
        if day_of_birth < 21:
            return "Taurus"
        else:
            return "Gemini"
    elif "Jun" in month_of_birth.title():
        if day_of_birth < 21:
            return "Gemini"
        else:
            return "Cancer"
    elif "Jul" in month_of_birth.title():
        if day_of_birth < 23:
            return "Cancer"
        else:
            return "Leo"
    elif "Aug" in month_of_birth.title():
        if day_of_birth < 23:
            return "Leo"
        else:
            return "Virgo"
    elif "Sep" in month_of_birth.title():
        if day_of_birth < 23:
            return "Virgo"
        else:
            return "Libra"
    elif "Oct" in month_of_birth.title():
        if day_of_birth < 23:
            return "Libra"
        else:
            return "Scorpio"
    elif "Nov" in month_of_birth.title():
        if day_of_birth < 22:
            return "Scorpio"
        else:
            return "Sagittarius"

if __name__ == "__main__":
    # Read from user here
    day = int(input('Enter day of birth'))# Read day from user
    month = input('Enter month of birth')# Read month from user
    
    zodiac_sign = get_zodiac_sign(month,day)# call get_zodiac_sign function here
    
    if zodiac_sign:
    	print(f'Your zodiac sign is {zodiac_sign}')# print the zodiac sign here
    else:
    	print(f'Your input is wrong')# print a message that the input was wrong!
# %%
number_of_students = 10
sum_of_all_grades = 0
grades = [4,8,4,2,1,3,6,5,4,1,10]
for i in grades:
    sum_of_all_grades+=i
    
average = sum_of_all_grades/number_of_students

print(f'Number of students: {number_of_students}\n\
Sum of all grades: {sum_of_all_grades}\n\
The avg grade is: {average}')

# %%
number_of_students = 10
sum_of_grades = 0

for i in range(number_of_students):
    grade = float(input(f"Please provide grade {i + 1}: "))
    sum_of_grades += grade

average = sum_of_grades / number_of_students
print(f"The average grade of the class is: {average}")
# %%
for i in range(10,0,-1):
    print(i)
# %%
x = 1
while x <= 10:
    print(x)
# %%
x = 1
while x <= 10:
    print(x)
    x += 2
# %%
for i in range(10): # 1st while loop
    for j in range(20): # 2nd while loop
        break
# %%
number_of_students = 0
sum_of_all_grades = 0

grade = float(input(f'Please enter grade n° {number_of_students+1}'))

while grade >= 0:
    sum_of_all_grades+=grade
    number_of_students+=1
    grade = float(input(f'Please enter grade n° {number_of_students+1}'))

average = sum_of_all_grades/number_of_students

print(f'Number of students: {number_of_students}\n\
Sum of all grades: {sum_of_all_grades}\n\
The avg grade is: {average}')
# %%
a = 'I\'m rafael'
# %%
print(a)
# %%
import random

def get_random_choice():
    tools = ["Rock", "Paper", "Scissors"]
    return random.choice(tools)

computer_wins = 0
human_wins = 0

while True:
    computer_choice = get_random_choice()
    human_choice = input("Please provide your input (Rock, Paper, Scissors): ")
    human_choice = human_choice.title()

    if human_choice != "Rock" and human_choice != "Paper" and human_choice != "Scissors":
        print("Invalid input. Terminating")
        break

    if human_choice == computer_choice:
        print(f"Tie. I also chose {computer_choice}.")
    elif human_choice == "Rock":
        if computer_choice == "Paper":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
        elif computer_choice == "Scissors":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1
    elif human_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1
        elif computer_choice == "Scissors":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
    elif human_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
        elif computer_choice == "Paper":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1

    print(f"Score: Human {human_wins} vs Computer {computer_wins}")
    print()

if human_wins > computer_wins:
    print("Congrats! You won the game!")
elif computer_wins > human_wins:
    print("Sorry! I won the game!")
else:
    print("Tie! Let's do another one, if you are brave!")

#%%
import random

def get_random_choice():
    tools = ["Rock", "Paper", "Scissors"]
    return random.choice(tools)

computer_wins = 0
human_wins = 0

computer_choice = get_random_choice()
human_choice = input("Please provide your input (Rock, Paper, Scissors): ")
human_choice = human_choice.title()


while human_choice in ['Rock', 'Paper', 'Scissors']:
    
    if human_choice != "Rock" and human_choice != "Paper" and human_choice != "Scissors":
        print("Invalid input. Terminating")
        break

    if human_choice == computer_choice:
        print(f"Tie. I also chose {computer_choice}.")
    elif human_choice == "Rock":
        if computer_choice == "Paper":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
        elif computer_choice == "Scissors":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1
    elif human_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1
        elif computer_choice == "Scissors":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
    elif human_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"I won: I chose {computer_choice}")
            computer_wins += 1
        elif computer_choice == "Paper":
            print(f"You won: I chose {computer_choice}")
            human_wins += 1

    print(f"Score: Human {human_wins} vs Computer {computer_wins}")
    print()

    computer_choice = get_random_choice()
    human_choice = input("Please provide your input (Rock, Paper, Scissors): ")
    human_choice = human_choice.title()

print('Thank you for playing!')

if human_wins > computer_wins:
    print("Congrats! You won the game!")
elif computer_wins > human_wins:
    print("Sorry! I won the game!")
else:
    print("Tie! Let's do another one, if you are brave!")

# %%
import random

guess = int(input("Please provide your guess: "))
secret_number = random.randint(1,100)
guesses = 1

while guess != secret_number:
    if guess < secret_number:
        print("Low")
    elif guess > secret_number:
        print("High")
    guesses += 1
    guess = int(input("Please provide your guess: "))

print(f"Bingo! You found the secret number {secret_number} with {guesses} guesses!")

#%%
import random
secret_number = random.randint(1,100)
guesses = 0

while True:
    guess = int(input("Please provide your guess: "))
    guesses += 1

    if guess < secret_number:
        print("Low")
    elif guess > secret_number:
        print("High")
    else:
        print(f"Bingo! You found the secret number {secret_number} with {guesses} guesses!")
        break


# %%
import random

def main():
    with open(r"C:\Users\PC\Desktop\words.txt") as my_file:
        lines = my_file.readlines()
        secret_word = random.choice(lines)
        secret_word = secret_word.rstrip("\n").lower()

    for index, char in enumerate(secret_word):
        if index == 0:
            print(f" {char.upper()}", end="")
        else:
            print(" _", end="")
    print()

    correct_letters = ""
    wrong_inputs = 0
    threshold = 5
    while True:
        user_input = input("Please provide a letter or the solution: ")
        if user_input.lower() == 'exit':
            print('Thank you for platying')
            break
        if len(user_input) > 1: # Is providing the solution
            if user_input.lower() != secret_word.lower():
                print(f"Game over, the secret word was '{secret_word}'")
                print('Do you want to play again? (yes/no)')
                play = input('Yes/No')
                if play.lower() == 'yes':
                    main()
                else:
                    break
            else:
                print(f"Correct!!!! The word was indeed '{secret_word}'")
                print('Do you want to play again? (yes/no)')
                play = input('Yes/No')
                if play.lower() == 'yes':
                    main()
                else:
                    break
        elif len(user_input) == 1:
            if user_input in secret_word:
                print(f"Correct, the letter '{user_input}' appears in the word!")
                correct_letters = correct_letters + user_input
            else:
                wrong_inputs += 1
                print(f"Wrong, the letter '{user_input}' does not appears in the word. Wrong inputs so far: {wrong_inputs} / {threshold}")

        if wrong_inputs >= threshold:
            print(f"You have provided {threshold} wrong answers. Game over! The word was '{secret_word}'.")
            print('Do you want to play again? (yes/no)')
            play = input('Yes/No')
            if play.lower() == 'yes':
                main()
            else:
                break

        for index, char in enumerate(secret_word):
            if index == 0:
                print(f" {char.upper()}", end="")
            elif char in correct_letters:
                print(f" {char}", end="")
            else:
                print(" _", end="")
        print()

main()
# %%
# 1 - Write a Python program that will compute and print the sum of the numbers from 1 to N. N will be given by the user.
user_input = int(input('Enter a Number'))
user_sum = sum(range(1,user_input+1))
print(f'The sum is: {user_sum}')
# %%
# 2- Write a program that will read from the user an integer number and it will print out if the number is an even or odd number.
user_input = int(input('Enter a number'))
if user_input % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# %%
# 3- Write a utility program for a teacher. The teacher asked you to create a small program that will help her to classify students' work. 
# The teacher wants to insert the grade of a student (1 to 10) and print out its class (10 - 9 is A+, 8-7 is A, 6-5 is B, 4 is C, 3 is D,
# 2 is E and 1 is F). Write a program to help the teacher to do this. Your program should stop once the teacher enters -1.

while True:
    user_input = int(input('Please enter a grade'))
    if user_input == -1:
        print('Goodbye')
        break
    elif user_input == 10 or user_input== 9:
        print('A+')
    elif user_input == 8 or user_input== 7:
        print('A')
    elif user_input == 6 or user_input== 5:
        print('B')
    elif user_input == 4:
        print('C')
    elif user_input == 3:
        print('D')
    elif user_input == 2:
        print('E')
    elif user_input == 1:
        print('F')
    
# %%
# 4- Write a program that will read a string from the user and then it will print out how many times the following letters appear in the 
# string: a, t, e, o, s
counter = {
    'a':0,
    't':0,
    'e':0,
    'o':0,
    's':0
}
user_input = input('Please enter your word')
for char in user_input:
    if char == 'a':
        counter['a'] = counter['a']+1
    elif char=='t':
        counter['t'] = counter['t']+1
    elif char=='e':
        counter['e'] = counter['e']+1
    elif char=='o':
        counter['o'] = counter['o']+1
    elif char=='s':
        counter['s'] = counter['s']+1

for key,value in counter.items():
    print(f'Letter: {key}, was entered {value} times')

# %%
# 5- Write a Python program that will read a number from the user and then it will check and print if that number is a prime number or not. 
# A prime number is the one who is divided exactly only with itself and 1 (e.g. 2, 3, 5, 7, 11, ....). For example, for number 7 it should 
# print "7 is a prime number" while for 8 it should print "8 is not a prime number". Keep in mind that too big numbers could hang your program 
# running for long time, so restrict your tests to small numbers (< 1000).

user_input = int(input('Enter a number'))

for i in range(2, user_input+1):
    if user_input % i == 0 and i != user_input:
        print(f'The number {user_input} is not a prime')
        break
    else:
        print(f'The number {user_input} is a prime')
        break
#%%
def proper_divisors(n):
    # Your code here
    div = []
    for i in range(1,n):
        if n % i == 0:
            div.append(i)
    return div

if __name__ == "__main__":
    # Your code here
    n = int(input("Please provide an integer: "))
    print(proper_divisors(n))

# %%
def average(students):
    # TODO
    total_grade = 0.0
    #for name, student_id, grade in students:
    for student in students:
        total_grade+= student[2]
    avg = total_grade / len(students)
    return avg        

def filter_average(students, average_grade):
    # TODO
    above_avg = []
    for student in students:
        if student[2] > average_grade:
            above_avg.append(student)
    return above_avg

if __name__ == "__main__":
    # TODO
    students = []
    for i in range(5):
        name = input(f"Please provide student's {i + 1} name: ")
        student_id = input(f"Please provide student's {i + 1} id: ")
        grade = float(input(f"Please provide student's {i + 1} grade: "))
        students.append((name, student_id, grade))
        print()
    
    """ students = [('axel', '1', 10.0),
                ('tito', '2', 2.0),
                ('duro', '3', 5.0),
                ('malki', '4', 0.0),
                ('percha', '3', 3.0)]   """  

    avg = average(students)
    above_avg = filter_average(students, avg)
    print(avg)
    print(above_avg)
    

# %%
def get_letters_frequency(phrase):
    letters_freq = {}
    for i in phrase:
        i = i.lower()
        if i.isalpha():
            if i in letters_freq.keys():
                letters_freq[i]+=1
            else:
                letters_freq[i]=1
    return letters_freq # You might consider returning a dictionary with the frequency here?

if __name__ == "__main__":
    phrase = input('Enter your phrase')# Read phrase from user here.
    freq = get_letters_frequency(phrase)# Call get_letters_frequency here
    cont=0
    for i,v in freq.items():# Print the result here.
        if cont==len(freq)-1:
            print(f'{i}:{v}')
        else:
            print(f'{i}:{v}\n')
        cont+=1
# %%
def new_sum(current_sum, value):
    result = current_sum
    try:
        result = current_sum + float(value)
    except ValueError:
        print("You enter an invalid, non-numeric value")

    return result

if __name__ == "__main__":
    user_input = input("Please enter an input: ")
    current_sum = 0
    while len(user_input) > 0:
        current_sum = new_sum(current_sum, user_input)
        print(f"Current sum: {current_sum}")
        user_input = input("Please enter an input: ")
# %%
def calculator(operand_1, operand_2, operator):
    if operator not in ["+", "-", "/", "*"]:
        raise ValueError(f"Operator should either be +, -, /, or * but '{operator}' was given.")

    if type(operand_1) is str:
        if not operand_1.isnumeric():
            try:
                operand_1 = float(operand_1)
            except ValueError:
                raise TypeError("Both operands should be numeric values.")
        else:
            operand_1 = int(operand_1)
    if type(operand_2) is str:
        if not operand_2.isnumeric():
            try:
                operand_2 = float(operand_2)
            except ValueError:
                raise TypeError("Both operands should be numeric values.")
        else:
            operand_2 = int(operand_2)
    if type(operand_1) not in [int, float] or type(operand_2) not in [int, float]:
        raise TypeError("Both operands should be numeric values.")
    if operator == "/" and operand_2 == 0:
        raise ValueError("Second operand should not be zero when dividing.")

    return eval(f"{operand_1} {operator} {operand_2}")

if __name__ == "__main__":
    print(calculator("58", 2.1, "a"))
# %%
# TODO: Define your class here

class Triangle:
    def __init__(self, *args):
        self.side_a = args[0]
        self.side_b = args[1]
        self.side_c = args[2]


if __name__ == "__main__":
    triangle = Triangle(2,4,6)
    print(triangle.side_a, triangle.side_b, triangle.side_c)
    
# %%
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True

    def classify(self):
        if self.side_a == self.side_b == self.side_c:
            return "Equilateral"
        elif self.side_a != self.side_b != self.side_c:
            return "Scalene"
        else:
            return "Isosceles"

if __name__ == "__main__":
    triangle = Triangle(2, 2, 2)
    print(f"The triangle is valid? {triangle.is_valid()}")
    print(f"The triangle is {triangle.classify()}")

# %%
import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True

    def classify(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a == self.side_b == self.side_c:
            return "Equilateral"
        elif self.side_a != self.side_b != self.side_c:
            return "Scalene"
        else:
            return "Isosceles"

    def __str__(self):
        return f"{self.classify()}({self.side_a}, {self.side_b}, {self.side_c})"

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def __lt__(self, other_triangle):
        return self.area() < other_triangle.area()

if __name__ == "__main__":
    triangle1 = Triangle(2, 2, 2)
    print(f"{triangle1} with area {triangle1.area()}")

    triangle2 = Triangle(1, 1, 1)
    print(f"{triangle2} with area {triangle2.area()}")

    print()
    print(f"{triangle1} < {triangle2} ? {triangle1 < triangle2}")
    print(f"{triangle2} < {triangle1} ? {triangle2 < triangle1}")


# %%
import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def __lt__(self, other_triangle):
        return self.area() < other_triangle.area()

class Equilateral(Triangle):
    def __str__(self):
        return f"Equilateral({self.side_a}, {self.side_b}, {self.side_c})"

class Scalene(Triangle):
    def __str__(self):
        return f"Scalene({self.side_a}, {self.side_b}, {self.side_c})"

class Isosceles(Triangle):
    def __str__(self):
        return f"Isosceles({self.side_a}, {self.side_b}, {self.side_c})"

def create_triangle(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return Equilateral(side_a, side_b, side_c)
    elif side_a != side_b != side_c:
        return Scalene(side_a, side_b, side_c)
    else:
        return Isosceles(side_a, side_b, side_c)

if __name__ == "__main__":
    triangle1 = create_triangle(2, 2, 2)
    print(f"{triangle1} with area {triangle1.area()}")

    triangle2 = create_triangle(2, 3, 4)
    print(f"{triangle2} with area {triangle2.area()}")

    print()
    print(f"{triangle1} < {triangle2} ? {triangle1 < triangle2}")
    print(f"{triangle2} < {triangle1} ? {triangle2 < triangle1}")

#%%
from enum import Enum
from dataclasses import dataclass
from dataclasses import field
from typing import List

Position = Enum('Position', 'GK LB CB RB DM CM LM RM LW SS RW CF')
Role = Enum('Role', 'Manager AssistantManager GoalkeepingCoach FitnessCoach ConditioningCoach Nutritionist Physiotherapist Masseur Scouter YouthTeamCoach')


@dataclass(frozen=True, order=True)
class Player:
    # By setting age to appear first and the last_name second we ensure Python 
    # will order them first based on age, second based on last_name and finally 
    # on the first_name. This is the trick for the final point that is tricky.
    age: int
    last_name: str
    first_name: str
    position: Position = field(compare=False)


@dataclass(frozen=True)
class Squad:
    players: List[Player]


@dataclass(frozen=True)
class Staff:
    first_name: str
    last_name: str
    age: int
    role: Role


if __name__ == "__main__":
    # Players
    player1 = Player(first_name="Manuel", last_name="Neuer", age=17, position=Position.GK)
    player2 = Player(first_name="Sergio", last_name="Ramos", age=26, position=Position.CB)
    player3 = Player(first_name="Gerard", last_name="Pique", age=25, position=Position.CB)
    player4 = Player(first_name="Giorgio", last_name="Chiellini", age=24, position=Position.CB)
    player5 = Player(first_name="Raphael", last_name="Varane", age=27, position=Position.CB)
    player6 = Player(first_name="Aymeric", last_name="Laporte", age=20, position=Position.CB)
    player7 = Player(first_name="Andrew", last_name="Robertson", age=18, position=Position.LB)
    player8 = Player(first_name="Trent", last_name="Alexander-Arnold", age=17, position=Position.RB)
    player9 = Player(first_name="Joshua", last_name="Kimmich", age=17, position=Position.DM)
    player10 = Player(first_name="Marcelo", last_name="Brozovic", age=28, position=Position.DM)
    player11 = Player(first_name="Kevin", last_name="Bruyne", age=30, position=Position.CM)
    player12 = Player(first_name="Luka", last_name="Modric", age=28, position=Position.CM)
    player13 = Player(first_name="Neymar", last_name="Santos", age=22, position=Position.LM)
    player14 = Player(first_name="Jadon", last_name="Sancho", age=32, position=Position.RM)
    player15 = Player(first_name="Cristiano", last_name="Ronaldo", age=34, position=Position.LW)
    player16 = Player(first_name="Lionel", last_name="Messi", age=29, position=Position.SS)
    player17 = Player(first_name="Angel", last_name="Di Maria", age=33, position=Position.RW)
    player18 = Player(first_name="Luis", last_name="Suarez", age=22, position=Position.CF)
    player19 = Player(first_name="Robert", last_name="Leqandowski", age=27, position=Position.CF)

    # Squad
    main_squad = Squad(players=[player1, player2, player3, player7, player8, player10, player11, player13, player15, player16, player19])

    # Let's sort
    players = main_squad.players

    print("Squad before sorting:")
    for player in players:
        print(f"{player.first_name} {player.last_name} ({player.age})")

    players.sort()

    print()
    print("Squad after sorting (based on age, then surname, then first name):")
    for player in players:
        print(f"{player.first_name} {player.last_name} ({player.age})")

    # Staff
    manager = Staff(first_name="Your Name", last_name="Your last name", age="Your age", role=Role.Manager)
    assistant_manager = Staff(first_name="Rafael", last_name="from WillowBits", age="30", role=Role.AssistantManager)

# %%
