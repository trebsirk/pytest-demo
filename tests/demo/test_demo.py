import pandas as pd
import pytest

from src.demo.demo import add, mult

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
