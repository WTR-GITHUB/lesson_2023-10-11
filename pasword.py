id_pwd_string = input("Please enter minimum 5 pasword sets. The string should look like >> username=, password=; username=, password=;....etc: \n")
split_list = id_pwd_string.split(";")

user_list = []
pass_list = []
pass_list_improved = []

for st in split_list:
    if "username=" in st:
        poz1 = st.find(",")
        poz2 = st.find("=")
        user_list.append(st[poz2+1:poz1])
        # user_list.append(st[poz1:poz2])
    if "password=" in st:
        poz3 = st.rfind("=")
        pass_list.append(st[poz3+1:])
        # user_list.append(st[poz1:poz2])

chars = ["1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","_","+","-"]

for passwd in pass_list:
    res = any(simb in passwd for simb in chars)
    if res != True:
        pass_list_improved.append(passwd + (chars[len(passwd)*-1]))
    else:
        pass_list_improved.append(passwd)
 

user_dict = dict(zip(user_list, pass_list))
user_dict_improved = dict(zip(user_list, pass_list_improved))
print("======================================================================================")
if user_dict != user_dict_improved:
    print("Some os users have weak paswords we sudges to change it to: \n", user_dict_improved)

print("======================================================================================")

log_count = 0
while True:
    user_id = input("Enter your id: ")    
    if user_id in user_dict.keys() or user_id in user_dict_improved.keys():
        user_pass = input(f"Please enter pasword: ")
        if user_dict[user_id] == user_pass or user_dict_improved[user_id] == user_pass:
            print(f"Hello {user_id}. Your curent password: >> {user_dict[user_id]} << is weak we sudgest to change it to: >> {user_dict_improved[user_id]} <<")
            break
        else:
            log_count += 1
            print(f"Bad pasword! Login atempt: {log_count}")
    else:
        log_count += 1
        print(f"No such user! Login atempt: {log_count}")