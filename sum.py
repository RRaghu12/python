'''def sum_numbers(lst):
    sum_negative = 0
    sum_even_positive = 0
    sum_odd_positive = 0
    
    for num in lst:
        if num < 0:
            sum_negative += num
        elif num % 2 == 0:
            sum_even_positive += num
        else:
            sum_odd_positive += num
    
    print("Sum of negative numbers:", sum_negative)
    print("Sum of positive even numbers:", sum_even_positive)
    print("Sum of positive odd numbers:", sum_odd_positive)

# Taking dynamic input from the user
numbers = []
while True:
    input_str = input("Enter a number (or type 'done' to finish): ")
    if input_str.lower() == 'done':
        break
    try:
        num = int(input_str)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

sum_numbers(numbers)'''

#2
values=[2,4,1,-3,-5,7]
negative_values=max(i for i in values if i<0)
positive_values=max(j for j in values if j%2 ==0)

print(negative_values)
print(positive_values)