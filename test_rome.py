from pytest import raises

from rome import Roman


def test_one_letter_numerals():
    roman = 'IVXLCDM'
    arabic = [1, 5, 10, 50, 100, 500, 1000]
    for r, a in zip(roman, arabic):
        assert Roman(r) == a


def test_numerals_that_only_sum_up():
    assert Roman('XX') == 20
    assert Roman('MDCCCCX') == 1910


def test_numerals_that_need_to_substract():
    assert Roman('XIX') == 19
    assert Roman('MCMLIV') == 1954
    assert Roman('M cM xC') == 1990


def test_arabic_to_roman():
    assert Roman(20) == 20
    assert Roman(20) == Roman('XX')
    assert str(Roman(20)) == 'XX'
    assert repr(Roman(20)) == "Roman('XX')"
    assert Roman(1999) == Roman('MDCCCCLXXXXVIIII')


def test_expressions():
    assert Roman('XX') + Roman('X') == Roman('XXX')
    assert Roman('XX') - Roman('X') == Roman('X')


def test_errors():
    with raises(ValueError):
        Roman('ZYX')
    with raises(ValueError):
        Roman(-1)
    with raises(ValueError):
        Roman(0)


def test_construct_number_negatively():
    assert Roman(10)._negatively() == 'X'
    assert Roman(9)._negatively() == 'IX'
    assert Roman(6)._negatively() == 'IIIIX'
    assert Roman(44)._negatively() == 'VIL'
    assert Roman(20)._negatively() == 'XXXL'


def test_split_number_into_groups():
    assert Roman(1234)._split() == [1000, 200, 30, 4]
    assert Roman(50280)._split() == [50000, 0, 200, 80, 0]
    assert Roman(20)._split() == [20, 0]


def test_normalize_roman_number():
    assert str(Roman('MDCCCCLXXXXVIIII')) == 'MCMXCIX'
    assert str(Roman(1903)) == 'MCMIII'
    assert str(Roman('IIII')) == 'IV'
