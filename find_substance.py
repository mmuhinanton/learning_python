#!/usr/bin/env/ python3


def find_subs(ph):
    if len(ph) > 0:
        value = float(ph)
        if value == 5.5:
            print(value, '- шампунь')
        elif value == 3.0:
            print(value, '- яблочный сок')
        elif 9.0 <= value <= 10.0:
            print(value, '- мыло для рук')
        else:
            print('Что за вещество?')
    else:
        print('Введите значение ph!')


if __name__ == '__main__':
    find_subs(input('Введите ph: '))
