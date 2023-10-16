
pass_list = ["darbas", "geris"]
chars = ["1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","_","+","-"]
# (passwd + chars[len(passwd)*-1] for passwd in pass_list)
# for passwd in pass_list:

passwd = "jhgjhgs"
  
print(passwd + (chars[len(passwd)*-1]))
    
