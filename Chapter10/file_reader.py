#file_path = "text_folder/pi_digits.txt"
#with open(file_path) as file_object:
    #contents = file_object.read()
#print(contents.strip)

#filename = 'pi_digits.txt'

#with open(filename) as file_object:
   # for line in file_object:
    #print(line)

filename = 'Pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

