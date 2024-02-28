import itertools

# 定義布林運算符號
operators = {
    'and': lambda x, y: x and y,
    'or': lambda x, y: x or y,
    'if a then b': lambda x, y: (not x) or y,
    'if b then a': lambda x, y: (not y) or x
}

# 定義真值表函數
def truth_table():
    headers = 'a   b   |   a and b   a or b   if a then b   if b then a'
    print(headers)
    print('-' * len(headers))

    for values in itertools.product([False, True], repeat=2):
        a, b = values
        results = [a, b, operators['and'](a, b), operators['or'](a, b),
                   operators['if a then b'](a, b), operators['if b then a'](a, b)]
        print('  '.join(str(value) for value in values) +
              '  |  ' + '  '.join(str(result) for result in results))

# 測試
truth_table()
