import pytest
from SalaryInputs import SalaryInputs
from TooHigherError import TooHigherError
from TooLowerError import TooLowerError


def test_get_salary_expect_value_error():
    sio = SalaryInputs
    with pytest.raises(ValueError):
        sio.get_salary('Itay is cool')


def test_get_salary_expect_too_higher_error():
    sio = SalaryInputs()
    with pytest.raises(TooHigherError):
        sio.get_salary(120000)


def test_get_salary_expect_too_lower_error():
    sio = SalaryInputs()
    with pytest.raises(TooLowerError):
        sio.get_salary(9999)


@pytest.mark.parametrize("amount", [16783, 78987])
def test_get_salary_parameter(amount):
    sio = SalaryInputs()
    actual = sio.get_salary(amount)
    expected = amount
    assert actual == expected