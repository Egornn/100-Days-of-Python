try:
    file = open('file.txt')
    dictionary = {'a': "b"}
    dictionary['a']
except FileNotFoundError as error_message:
    file = open('file.txt', 'w')
    file.write('First Line of Data')
    print(error_message)
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed')
    raise KeyError("Some strange Key")

height = float(input("Type your height: "))
weight = float(input("Type your weight: "))
if height > 3:
    raise ValueError("Height cannot be greater than 3 meters.")
bmi = weight / height ** 2
print(bmi)
