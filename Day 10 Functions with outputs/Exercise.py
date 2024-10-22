
f_name = input("your first name: ")
l_name = input("last name: ")
def format_name(first, second):
    fu_name = first.title() + " " + second.title()

    return fu_name

output = format_name(first=f_name, second=l_name)
print(f"Your name is {output}")





