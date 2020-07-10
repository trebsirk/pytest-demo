import pandas as pd
import pytest

from src.demo.demo import add, mult, coin_change, coin_change_2

@pytest.fixture
def dummy_df():
    int_col = [1, None, 4, 2, 100]
    float_col = [100.234, 0.0, None, None, 9.19]
    df_dict = {'int': int_col, 'float': float_col}
    df = pd.DataFrame(df_dict)
    return df

@pytest.fixture
def dummy_list_of_lists():
    return [[1,2], [3,4], [5,6]]

def test_add(dummy_list_of_lists):
    r = list(map(lambda x: add(*x), dummy_list_of_lists))
    assert r == [3,7,11]

def test_mult(dummy_list_of_lists):
    r = list(map(lambda x: mult(*x), dummy_list_of_lists))
    assert r == [2, 12, 30]

def test_coin_change():
    coins = [25,10,5,1]
    amount = 10
    assert coin_change(amount, coins) == 1

def test_coin_change2():
    coins = [25,10,5,1]
    amount = 9
    assert coin_change(amount, coins) == 5


def test_coin_change3():
    coins = [25,10,5,1]
    amount = 10
    assert coin_change_2(amount, coins) == 1

def test_coin_change4():
    coins = [25,10,5,1]
    amount = 9
    assert coin_change_2(amount, coins) == 5