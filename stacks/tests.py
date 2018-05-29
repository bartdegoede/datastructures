from usecases import reverse_string, parentheses, to_binary, base_converter

def run():
    assert(reverse_string('tsenereoh') == 'hoerenest')
    assert(parentheses('{{([][])}()}') == True)
    assert(parentheses('{{([][])}(}') == False)
    assert(parentheses('[{()]') == False)
    assert(to_binary(42) == '101010')
    assert(base_converter(25, 2) == '11001')
    assert(base_converter(25, 16) == '19')

if __name__ == '__main__':
    run()
