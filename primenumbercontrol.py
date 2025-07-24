#Daxil olan ədədin sadə olub olmamasının yoxlanılması

num = int(input("Bir ədəd daxil edin : "))

prime = True

for i in range(2,num):
    if num %i ==0:
        prime = False
        break

if prime == True:
    print(f"{num} sadə ədəddir")
else:
    print(f"{num}  sadə ədəd deyil")
    