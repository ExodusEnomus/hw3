import random

names = ['Мел Гибсон','Михаэль Шумахер','Джулия Ормонд','Адриано Челентано','Николас Кейдж','Дэвид Боуи','Элвис Прэсли','Алексей Николаевич Толстой','Валерий Харламов',' Джим Кэрри']
dates = ['03.01.1956','03.01.1969','04.01.1965','06.01.1938','07.01.1964','08.01.1947','08.01.1935','10.01.1883','14.01.1948','17.01.1962']

play = 'yes'

print(len(names))
print(len(dates))

while play == 'yes':
    selected_names = random.sample(names,5)
    print(selected_names)

    right_answers = 0
    for name in selected_names:
        answer = input('Input date of birth: ' + name)
        if(answer == dates[names.index(name)]):
            print('Right answer!')
            right_answers+=1
        else:
            print('Wrong!!!' + ' Right answer is ' + dates[names.index(name)])
    print(f'Right answers:{right_answers}')
    play = input('Continue playing? yes/no')

