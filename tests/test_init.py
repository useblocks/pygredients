import pytest

from pygredients import Pygredients

def test_pygredients_init_empty():
    with pytest.raises(TypeError):
        pyg = Pygredients()


def test_pygredients_init_module():
    from testdata import calc
    pyg = Pygredients(calc)

    assert pyg.area is not None
    assert pyg.type == "module"
    assert pyg.code is not None
    assert pyg.ast is not None


def test_pygredients_init_class():
    from testdata import calc
    clazz = calc.Calc
    pyg = Pygredients(clazz)

    assert pyg.area is not None
    assert pyg.type == "class"
    assert pyg.code is not None
    assert pyg.ast is not None


def test_pygredients_init_function():
    from testdata import calc
    func = calc.Calc.calculate
    pyg = Pygredients(func)

    assert pyg.area is not None
    assert pyg.type == "function"
    assert pyg.code is not None
    assert pyg.ast is not None
