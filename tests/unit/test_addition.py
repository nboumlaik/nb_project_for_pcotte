from complex_nb.complex_nb import ComplexOper as cmpx


def test_add():
    var1 = cmpx(3, -2)
    var2 = cmpx(-45, 1)

    res1 = var1 + var2

    assert res1.preel == -42
    assert res1.pimag == -1
