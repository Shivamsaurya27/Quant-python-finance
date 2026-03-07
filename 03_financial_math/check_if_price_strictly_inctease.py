# Question 4
# Create a function that checks if a list of prices is strictly increasing.
# Example
# Input: [100,102,103,104]
# Output: True
# Input: [100,102,101,103]
# Output: False


lst = list(map(int, input("Enter a list of prices separated by spaces: ").split()))

def check_inc(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return False
    return True

print(check_inc(lst))
