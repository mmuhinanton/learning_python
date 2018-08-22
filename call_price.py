#!/usr/bin/env/ python3


def call_price(code, time):

    city_price = {
        "Екатеринбург": 15,
        "Омск": 18,
        "Воронеж": 13,
        "Ярославль": 11
    }

    if code == 343:
        print("Стоимость разговора в г. Екатеринбург составляет:",
              time * city_price['Екатеринбург'])
    elif code == 381:
        print("Стоимость разговора в г. Омск составляет:",
              time * city_price['Омск'])
    elif code == 473:
        print("Стоимость разговора в г. Воронеж составляет:",
              time * city_price['Воронеж'])
    elif code == 485:
        print("Стоимость разговора в г. Ярославль составляет:",
              time * city_price['Ярославль'])
    else:
        print("Введен неверный код")


if __name__ == '__main__':
    call_price(int(input("Код города:")),
               int(input("Длительность вызова:")))
