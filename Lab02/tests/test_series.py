from Lab02.series.series import fibonacci
from Lab02.series.series import lucas
from Lab02.series.series import sum_series


## fibonacci
def test_first_fibonacci():
    actual = fibonacci(1)
    excepted = 1
    assert actual == excepted

def test_two_fibonacci():
    actual = fibonacci(0)
    excepted = 0
    assert actual == excepted


def test_three_fibonacci():
    actual = fibonacci(8)
    excepted = 21
    assert actual == excepted

def test_four_fibonacci():
    actual = fibonacci(9)
    excepted = 34
    assert actual == excepted

def test_six_fibonacci():
    actual = fibonacci(10)
    excepted = 55
    assert actual == excepted

def test_seven_fibonacci():
    actual = fibonacci(7)
    excepted =13
    assert actual == excepted   

    

## lucas

def test_first_lucas():
    actual = lucas(3)
    excepted = 4
    assert actual == excepted

def test_sec_lucas():
    actual = lucas(4)
    excepted = 7
    assert actual == excepted

def test_third_lucas():
    actual = lucas(0)
    excepted = 2
    assert actual == excepted

def test_forth_lucas():
    actual = lucas(1)
    excepted = 1
    assert actual == excepted

def test_five_lucas():
    actual = lucas(5)
    excepted = 11
    assert actual == excepted

def test_six_lucas():
    actual = lucas(6)
    excepted = 18
    assert actual == excepted


def test_seven_lucas():
    actual = lucas(7)
    excepted = 29
    assert actual == excepted


## sum_series

def test_sum_series():
    actual = sum_series(1,5,10)
    excepted = 10
    assert actual == excepted

def test_first_sum_series():
    actual =sum_series(1)
    excepted = 1
    assert actual == excepted

def test_sec_sum_series():
    actual =sum_series(2)
    excepted = 1
    assert actual == excepted

def test_third_sum_series():
    actual =sum_series(0)
    excepted = 0
    assert actual == excepted


def test_forth_sum_series():
    actual =sum_series(6,8,12)
    excepted = 136
    assert actual == excepted

def test_forth_sum_series():
    actual =sum_series(2,8,18)
    excepted = 26
    assert actual == excepted

def test_forth_sum_series():
    actual =sum_series(1,11,28)
    excepted = 28
    assert actual == excepted    