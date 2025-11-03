import requests

checkurl = 'https://clouddata.scratch.mit.edu/health'

print('Сколько попыток сделать (5 если ничего не написано):')
inp = input('>> ')
try:
    if inp == '':
        attempts = 5
    else:
        attempts = int(inp)
except Exception as e:
    print('А ты точно попытки указал?')

successful = 0
print('')
for i in range(attempts):
    print(f'Попытка номер {i+1}: делаем запрос...')
    try:
        response = requests.get(checkurl)
        status = response.status_code
        print(f'Статус: {status}')
        if status == 200:
            print('Успешно')
            successful = successful + 1
        else:
            print('Провалено')
    except Exception as e:
        print('Провалено')
    print('')

print(f'Все {attempts} попыток сделаны. {successful} попыток были удачными')
if successful == attempts:
    print('Статус облачных переменных: работают')
elif successful == 0:
    print('Статус облачных переменных: упали')
else:
    print('Статус облачных переменных: почти работают')
