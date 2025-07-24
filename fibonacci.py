#Fibonacci ədədləri ilk 2 ədədi 1 olan ,növbəti ədədləri özündən əvvəlki 2 ədədin cəmi olan ədədlərdir.


# ilk 2 ədədi listə yazırıq :
fibonacci = [1,1]

i = 2  # i bizim indexdir
while True :
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    i  +=  1
    if len(fibonacci) == 100: #Sonsuz döngünü limitləyirik
        break

print(fibonacci)
    