information = {}
print("Hi , Enter information about 5 of your friends !  ")
for i in range(5):
    name=input(f"{i+1} - Person , What is your name ? ")
    age =input(f"{i+1} - Person , How old are your ? ")
    information[f"friend_{i+1}_name"]=name
    information[f"friend_{i+1}_age"]=age   
print(information)

for keys,values in information.items():
    print(values)
    
