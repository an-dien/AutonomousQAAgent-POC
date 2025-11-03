from utils import calc
import pytest

def test_calc():
    assert calc.get_square_root(25) == 5
    assert calc.get_square_root(37249) == 193
    assert calc.get_square_root(0) == 0

    with pytest.raises(ValueError):
        calc.get_square_root(-1)

    with pytest.raises(TypeError):
        calc.get_square_root("9")