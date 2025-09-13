def people(*people: str):
    print(people)

    for name in people:
        print(f'Hello {name}')

people('Alice', 'Bob', 'Charlie')

def people(**kwargs):
    print(kwargs)

    for name, age in kwargs.items():
        print(f'{name} is {age} years old')



people(Alice=25, Bob=30, Charlie=35)
