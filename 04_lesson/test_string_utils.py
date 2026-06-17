import pytest
from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("россия", "Россия"),
    ("привет мир", "Привет мир"),
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", " "),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Россия", "Россия"),
    (" Россия   ", "Россия   "),
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  123", "123"),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Вселенная", "В", True),
    ("Россия", "я", True),
    ("Солнце", "л", True),
    ("Солнце", "р", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (" ", "р", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


def test_contains_numeric_input():
    with pytest.raises(TypeError):
        utils.contains("SkyPro", 123)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Вселенная", "В", "селенная"),
    ("Россия", "с", "Роия"),
    ("Солнце", "е", "Солнц"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Россия", "б", "Россия"),
    ("", "е", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
