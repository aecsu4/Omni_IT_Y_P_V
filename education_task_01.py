nearestChrpMin = []
nearestChrpMinName = []
nearestChrpMax = []
nearestChrpMaxName = []
vfd = {
  'ЧРП-1': 17,
  'ЧРП-2': 32,
  'ЧРП-3': 54,
  'ЧРП-4': 73,
  'ЧРП-5': 90,
}
def chrpSelectProcess():
    chrpCurrent = int(input("Введите номинальный ток ЧРП: "))
    for chrpName in vfd:
        if chrpCurrent == vfd[chrpName] or chrpCurrent > vfd[chrpName]*0.7 and chrpCurrent < vfd[chrpName]:
            resultSelection = vfd[chrpName]
            print(f'Ваш ЧРП: {chrpName} - {resultSelection} А')
        elif chrpCurrent > 90:
            alert = 'code_1'
            chrpExceptionAlert(alert)
            chrpSelectProcess()
    if 'resultSelection' not in locals():
        alert = 'code_2'
        chrpExceptionAlert(alert)
        for chrpName in vfd:
            if chrpCurrent < vfd[chrpName]:
                nearestChrpMin.append(vfd[chrpName])
                nearestChrpMinName.append(chrpName)

            elif chrpCurrent > vfd[chrpName]:
                nearestChrpMax.append(vfd[chrpName])
                nearestChrpMaxName.append(chrpName)
            else:
                continue
        print(f'Ближайший больший по току {min(nearestChrpMinName)} - {min(nearestChrpMin)} А\n'
              f'Ближайший меньший по току {min(nearestChrpMaxName)} - {min(nearestChrpMax)} А')

def chrpExceptionAlert(alert):
    if alert == 'code_1':
        print('Вы указали слишком большой ток для ЧРП. Выберите меньший ток.')

    elif alert == 'code_2':
        print('Мы не смогли подобрать ЧРП к вашему току. Т.к нижняя граница 70% от номинального тока ЧРП. Ближайший по току ЧРП: ')

chrpSelectProcess()




