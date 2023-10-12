id_pwd_string = input("Please enter minimum 5 pasword sets. The string should look like >> username=, password=; username=, password=;....etc: \n")

id_pwd_string = id_pwd_string.replace("username=","")
id_pwd_string = id_pwd_string.replace("password=","")

print(id_pwd_string)

# split_list = id_pwd_string.split(";")
# final_split = []
# final_split2 = []
# for item in split_list:
#     final_split += (item.split(","))

# for item in final_split:
#     final_split2 += (item.split("="))

# for item in final_split2:
#     final_split2.remove("username")

# print(final_split2)



id_list = []
pwd_list = []


    