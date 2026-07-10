"""Given a list of integers, find and print both the
largest and the smallest numbers."""
def large_element(list):
    large=max(list)
    return large
def small_element(list):
    small=min(list)
    return small

n=int(input("Enter the tall of the list:"))
list=[]
for i in range(n):
    a=int(input(f"list[{i+1}]="))
    list.append(a)
print(f"Your list is {list}")
print(f"The largest element is {large_element(list)} and the smallest element is {small_element(list)}")