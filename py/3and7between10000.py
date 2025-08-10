# Problem : 10000 ədədin neçəsini 5 və 7 ilə bitir.

str_numbers =[]


for i in range(2,1000):
    str_num = str(i)
    if str_num.endswith("3"):
        str_numbers.append(i)
    elif str_num.endswith("7"):
        str_numbers.append(i)


print(str_numbers)
print(len(str_numbers))