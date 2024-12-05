#encontrar el número mínimo de días que Kelly necesita para resolver más problemas que Sam
def minNum():
    samDaily = int(input("Enter the number of problems Sam solves per day: "))
    kellyDaily = int(input("Enter the number of problems Kelly solves per day: "))
    difference = int(input("Enter the difference between the problems solved by Sam and Kelly: "))
    
    days = 0
    sam_problems = 0
    kelly_problems = 0
    
    while kelly_problems <= sam_problems:
        sam_problems += samDaily
        kelly_problems += kellyDaily
        days += 1
    
    return days


print(f"The minimum number of days is: {minNum()}")