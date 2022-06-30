string_name=input()

number_list=[]
string_list=[]
take_list=[]
skip_list=[]
for k in range(len(string_name)):
    if string_name[k].isdigit():
        number_list.append(int(string_name[k]))
    else:
        string_list.append(string_name[k])

for j in range(len(number_list)):
    if j % 2==0:
        take_list.append(number_list[j])
    else:
        skip_list.append(number_list[j])

take_number=0
skip_number=0

index=0
new_string=""

for k in range(len(take_list)):
    take_number=take_list[k]
    skip_number=skip_list[k]
    new_string+="".join(string_list[:take_number])
    del string_list[0:take_number+skip_number]

print(new_string)