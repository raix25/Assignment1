print("Pleae input your time for each 5k practice run:")

total = 0
for i in range (1,6):
    minute= int(input(f"Enter the minutes for the run{i} = "))
    second= int(input (f"Enter the seconds for the run{i}= "))

    total += ((minute*60) + second)

print("Calculating the time...")

average_minute= total // 60
average_second= total % 60

print(f"Your average running time is {average_minute} minute and {average_second} seconds.")