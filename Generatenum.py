# Generate Numbers
password_list = [str(i) for i in range(60000000, 100000000)]

# Write the list to a file
with open('60to100mil.txt', 'w') as file:
    for password in password_list:
        file.write(password + '\n')

print(" list has been generated and saved .")
