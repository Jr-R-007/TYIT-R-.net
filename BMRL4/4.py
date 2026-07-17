#write the programme on which of these number 12,15,22,30,44,55,60 divided by 5
numbers=[12,15,22,30,44,55,60]
divisor=5
divisible_by_five= [x for x in numbers if x%divisor==0]
print(divisible_by_five)
