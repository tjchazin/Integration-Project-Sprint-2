#My Math Calculator
#Tyler Chazin COP 1500
#10/26/21
#Math is imported.
import math
def main():
#The beginning of the calculator
     start = (input("Welcome to my math calculator. Press any button to "
                             "begin."))
#Options of the calculator
     start_options = ["1.Circumference of a circle","2.Pythagorean Theorem",
                "3.Squareroot","4.Quadratic formula","5.Area","6.Sum of 5 "
                                                              "numbers"]
#Once ran, the options are all on new lines.
     start_options = '\n'.join(start_options)
     print(start_options)
#This loop will continue as long as the inputs by the user are between 1 and 7.
     for user_input in range(1,7):
#The try except is used in case the user inputs something other than an
# integer. If so, the program will print an error, and call back to main.
#If the user inputs the number 99, the program will stop.
        try:
            user_input = int(input("Enter a number 1 - 6. To end the "
                                   "program, type '99'."))
            if user_input == 99:
                break
        except ValueError:
            print("Error. Only the input of numbers is allowed here.")
            main()
#If the user inputs the number 1, the program asks the user for the radius,
# and then calls the circumference function. It also has a try and an except
# in case the input is not a number, reinforcing the notice that only
# numbers may be inputted.
        if user_input == 1:
            try:
                radius = (int(input("Enter the radius: ")))
                circumference(radius)
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
#If the user inputs the number 2, the program asks the user for one of two
# options, to find the hypotenuse or a side using the pythagorean theorem.
        elif user_input == 2:
            pythag_options = ["1.Find Hypotenuse","2.Find a Side"]
            pythag_options = '\n'.join(pythag_options)
            print(pythag_options)
#Again, another try except is used in case the user inputs something other
# than an integer.
            try:
                pythag_input = int(input("Enter the number of your "
                                         "objective: "))
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
                main()
#If the user inputs 1, the program asks for the value of a and b given from
# the user. It then calls the hypotenuse function with the arguments of a
# and b. Another try except in case the user doesn't input an integer.
            if pythag_input == 1:
                try:
                    a_input = int(input("Enter a side value: "))
                    b_input = int(input("Enter the other side value: "))
                    hypotenuse(a_input, b_input)
                except ValueError:
                    print("Error. Enter numbers only. The program will "
                          "restart.")
#If the user inputs 2, the program asks for the side value given and the
# hypotenuse. It then calls the side function with the arguments of the side
# and the hypotenuse.
            elif pythag_input == 2:
                try:
                    side_input = int(input("Enter the side value given: "))
                    hypo_input = int(input("Enter the hypotenuse: "))
                    side(side_input, hypo_input)
                except ValueError:
                    print("Error. Enter numbers only. The program will "
                          "restart.")
#If the user inputs 3, the program asks for a number that the user wants to
# get the square root of. It then calls the squareroot function with the
# argument of the input given. Another try except is used.
#If the square root is less than 0, the program says that the square root is
# undefined, because it would be a negative.
        elif user_input == 3:
            try:
                sqrt_input = int(input("Enter the number you want to square "
                                   "root: "))
                if sqrt_input >= 0:
                    squareroot(sqrt_input)
                elif sqrt_input < 0:
                    print("Error. This square root is undefined.")
            except ValueError:
                print("Error. Enter numbers only. The program will restart.")
#If the user inputs 4, the program asks for the values of a, b, and c. It
# then calls the quadratic function with the arguments of the three inputs.
#The quadratic function will give the two values of x from the quadratic
# formula. Another try except is used.
        elif user_input == 4:
            try:
                a = int(input("Enter the value for a: "))
                b = int(input("Enter the value for b: "))
                c = int(input("Enter the value for c: "))
                quadratic(a, b, c)
            except ValueError:
                print("Error. Enter numbers only. The program will restart.")
#If the user inputs the number 5, the program prompts the user for one of
# three options, to see which shape the user wants to find the area of.
        # Another try except is used.

        elif user_input == 5:
            area_options = ["1.Triangle","2.Square","3.Circle"]
            area_options = '\n'.join(area_options)
            print(area_options)
            try:
                area_input = int(input("Enter the number for which shape "
                "would you like to find the area for: "))
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
                main()
#If the user inputs one, the program asks for the base and the height of the
# triangle, and calls the triangle function with the arguments of the base
# and height.
            if area_input == 1:
                tri_base = int(input("Enter the base of the triangle: "))
                tri_height = int(input("Enter the height of the triangle: "))
                triangle(tri_base, tri_height)
#If the user inputs two, the program asks for the base and the height of the
# square, and calls the square function with the arugments of the base and
# height.
            elif area_input == 2:
                sq_base = int(input("Enter the base of the square: "))
                sq_height = int(input("Enter the height of the square: "))
                square(sq_base, sq_height)
#If the user inputs three, the program asks for the radius of a circle,
            # and calls the circle function with the argument of the radius.
            elif area_input == 3:
                radius = int(input("Enter the radius of the circle: "))
                circle(radius)
#if the user inputs the number 6, the program will prompt the user for 5
# numbers, and will output the sum of those 5 numbers.
        elif user_input == 6:
            num_amount = 0
            sum = 0
            print("Enter 5 numbers: ")
#The while loop continues while the amount of numbers inputted is less than
# 5, and not greater than 5.
            while num_amount < 5 and not num_amount >= 5:
                sum_input = int(input())
                num_amount += 1
                sum += sum_input
#When 5 numbers are inputted, the while loop stops and outputs the sum.
                if num_amount == 5:
                    print("Your sum is:", sum)
#If the user doesn't input a number between 1-6 or 99, the program lets the
        # user know that they inputted an invalid number, and to try again.
        else:
            print(input("You have entered an invalid number, press any "
                "button to try again."))



#The circumference function defined.
def circumference(radius):
#The circumference is pi x r^2, and because math is imported, math.pi is
# equal to pi.
     circumference = 2 * math.pi * radius
#The format of circumference with .2f makes it so that the output of the
# circumference will have only two decimal places.
     print("The cirumference of a circle with the radius of", radius, "is",
           format(circumference, ".2f"))
#The hypotenuse function defined, the first option of the pythagorean theorem.
def hypotenuse(a_input, b_input):
#The pythagorean theorem is a^2 + b^2 = c^2. the math.sqrt lets us find out
# the square root of a^2 + b^2, which in turn tells the the hypotenuse.
# Again, the format .2f outputs the hypotenuse with two decimal palces.
    pythagorean_theorem = math.sqrt(a_input ** 2 + b_input ** 2)
    print("The value of the hypotenuse with the sides of", a_input, "and",
          b_input, "is", format(pythagorean_theorem, ".2f"))
#The side function defined, the second option of the pythagorean theorem.
def side(side_input, hypo_input):
    pythagorean_theorem = math.sqrt(hypo_input ** 2 - side_input ** 2)
    print("The value of the side with the side of", side_input, "and the "
          "hypotenuse of", hypo_input, "is", format(pythagorean_theorem,
                                                    ".2f"))
#The squareroot function defined.
def squareroot(sqrt_input):
#math.sqrt gives the square root of the input. the format .2f outputs it
# with only two decimal places.
    square_root = math.sqrt(sqrt_input)
    print("The square root of the value", sqrt_input, "is", format(
        square_root, ".2f"))
#The quadratic function defined.
def quadratic(a, b, c):
#The discriminant is part of the quadratic formula, and the program checks
# if the discriminant is greater than 0 or equal to 0, and then plugs it
# back into the quadratic formula, and outputs the two x values with two
# decimal places.
    discriminant = (b ** 2.0 - 4.0 * a * c)
    if discriminant > 0 or discriminant == 0:
        sqrt_discriminant = math.sqrt(discriminant)
        quadratic_formula1 = ((-b + sqrt_discriminant) / (2.0 * a))
        quadratic_formula2 = ((-b - sqrt_discriminant) / (2.0 * a))
        print("From the input of", a, b, "and", c, "the x "
        "values are: ", format(quadratic_formula1, ".2f"), format(
        quadratic_formula2, ".2f"))
#If the discriminant is less than 0 or does not equal 0, the program prints
    # that the discriminant is undefined, because the square root of a
    # negative number is undefined.
    elif (discriminant < 0) or discriminant != 0:
        print("The discriminant is undefined.")
#The triangle function defined.
def triangle(tri_base, tri_height):
#Area of a triangle is b x h divided by 2. .2f outputs it with only two
# decimal places.
    tri_area = tri_base * tri_height / 2.0
    print("The area of a triangle with a base of", tri_base, "and a height "
            "of", tri_height, "is", format(tri_area, ".2f"))
#The square function defined.
def square(sq_base, sq_height):
#Area of a square is b x h. The .2f outputs the area with only two decimal
# places.
    sq_area = sq_base * sq_height
    print("The area of a square with a base of", sq_base, "and a height of",
          sq_height, "is", format(sq_area, ".2f"))
#The circle function defined.
def circle(radius):
#The area of a circle is pi x r^2. The .2f outputs the area of the circle
# with only two decimal places.
    cir_area = math.pi * radius ** 2.0
    print("The area of a circle with a radius of", radius, "is", format(
        cir_area, ".2f"))
#The call to main
main()