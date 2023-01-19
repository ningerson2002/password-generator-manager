import pass_gen
import re


def test_str_to_bool_y():
    answer = "y"
    expected_output = True
    actual_output = pass_gen.str_to_bool(answer)
    assert expected_output == actual_output


def test_str_to_bool_n():
    answer = "n"
    expected_output = False
    actual_output = pass_gen.str_to_bool(answer)
    assert expected_output == actual_output


def test_str_to_bool_other():
    answer = "other"
    assert pass_gen.str_to_bool(answer) == ValueError(f"{answer} not a valid answer.")


def test_generate_password_spec_chars():
    length = 10
    special_chars = True
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    password = pass_gen.generate_password(length, special_chars)
    assert regex.search(password) is not None


def test_generate_password_no_spec_chars():
    length = 10
    special_chars = True
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    password = pass_gen.generate_password(length, special_chars)
    assert regex.search(password) is None


def test_generate_password_length_short():
    length = 5
    special_chars = False
    password = pass_gen.generate_password(length, special_chars)
    assert len(password) == length


def test_generate_password_length_long():
    length = 1000000
    special_chars = False
    password = pass_gen.generate_password(length, special_chars)
    assert len(password) == length
