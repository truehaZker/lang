tat = {
    "ones": {
        "empty": "",
        0: "ноль",
        1: "бер",
        2: "ике",
        3: "өч",
        4: "дүрт",
        5: "биш",
        6: "алты",
        7: "җиде",
        8: "сигез",
        9: "тугыз",
        10: "ун",
        11: "унбер",
        12: "унике",
        13: "унөч",
        14: "ундүрт",
        15: "унбиш",
        16: "уналты",
        17: "унҗиде",
        18: "унсигез",
        19: "унтугыз"
    },
    "tens": {
        "empty": "",
        1: "ун",
        2: "егерме",
        3: "утыз",
        4: "кырык",
        5: "илле",
        6: "алтмыш",
        7: "җитмеш",
        8: "сиксән",
        9: "туксан"
    },
    "hundreds": {
        "empty": "",
        0: "йөз",
    }
}

rus = {
    "ones": {
        "empty": "",
        0: "ноль",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "весемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "весемнадцать",
        19: "девятнадцать"
    },
    "tens": {
        "empty": "",
        1: "десять",
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "весемдесят",
        9: "девяносто"
    },
    "hundreds": {
        "empty": "",
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот"
    }
}

eng = {
    "ones": {
        "empty": "",
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fouteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    },
    "tens": {
        "empty": "",
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    },
    "hundreds": {
        "empty": "",
        0: "hundred"
    }
}


def rus_gen(number):
    number = int(number)

    if number < 20:
        return rus['ones'][number]
    if 1000 > number >= 20:
        hundreds = number // 100
        tens = number % 100 // 10
        ones = number % 10

        if hundreds == 0:
            hundreds = "empty"
        if tens == 0:
            tens = "empty"
        if ones == 0:
            ones = "empty"
        if number % 100 < 20:
            ones = number % 100
            tens = "empty"
        # Этот чудо-код уберет лишние пробелы между словами
        return " ".join(" ".join([rus['hundreds'][hundreds], rus['tens'][tens], rus['ones'][ones]]).split())
    if number == 1000:
        return "тысяча"


def eng_gen(number):
    number = int(number)

    if number < 20:
        return eng['ones'][number]
    if 1000 > number >= 20:
        hundreds = number // 100
        tens = number % 100 // 10
        ones = number % 10
        show = 0

        if hundreds == 0:
            hundreds = "empty"
            show = "empty"
        if tens == 0:
            tens = "empty"
        if ones == 0:
            ones = "empty"
        if number % 100 < 20:
            ones = number % 100
            tens = "empty"

        # Этот чудо-код уберет лишние пробелы между словами
        return " ".join(
            " ".join([eng['ones'][hundreds], eng['hundreds'][show], eng['tens'][tens], eng['ones'][ones]]).split())
    if number == 1000:
        return "one thousand"


def tat_gen(number):
    number = int(number)

    if number < 20:
        return tat['ones'][number]
    if 1000 > number >= 20:
        hundreds = number // 100
        tens = number % 100 // 10
        ones = number % 10
        show = 0

        if hundreds == 0:
            hundreds = "empty"
            show = "empty"
        if tens == 0:
            tens = "empty"
        if ones == 0:
            ones = "empty"
        if number % 100 < 20:
            ones = number % 100
            tens = "empty"

        # Этот чудо-код уберет лишние пробелы между словами
        return " ".join(
            " ".join([tat['ones'][hundreds], tat['hundreds'][show], tat['tens'][tens], tat['ones'][ones]]).split())
    if number == 1000:
        return "мең"


print(tat_gen(input()))
