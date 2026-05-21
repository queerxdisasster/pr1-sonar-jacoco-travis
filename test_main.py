import os

import pytest

from main import (
    normalize_name,
    normalize_age,
    normalize_phone,
    normalize_email,
    process_line,
    main,
)


def test_normalize_name_correct_name_with_space():
    assert normalize_name("Иван Иванов") == "Иван Иванов"


def test_normalize_name_without_space_between_name_and_surname():
    assert normalize_name("ИванИванов") == "Иван Иванов"


def test_normalize_name_removes_extra_symbols():
    assert normalize_name("Иван123 Иванов!!!") == "Иван Иванов"


def test_normalize_name_with_extra_spaces():
    assert normalize_name("  Иван     Иванов  ") == "Иван Иванов"


def test_normalize_name_invalid_one_word():
    assert normalize_name("Иван") == ""


def test_normalize_name_invalid_three_words():
    assert normalize_name("Иван Иванов Петрович") == ""


def test_normalize_age_correct():
    assert normalize_age("27") == "27"


def test_normalize_age_with_spaces():
    assert normalize_age(" 35 ") == "35"


def test_normalize_age_invalid_text():
    assert normalize_age("двадцать") == ""


def test_normalize_age_zero():
    assert normalize_age("0") == ""


def test_normalize_age_too_large():
    assert normalize_age("121") == ""


def test_normalize_age_negative():
    assert normalize_age("-10") == ""


def test_normalize_phone_with_plus_seven():
    assert normalize_phone("+79990001111") == "+7 (999) 0001111"


def test_normalize_phone_with_eight():
    assert normalize_phone("89990001111") == "+7 (999) 0001111"


def test_normalize_phone_without_country_code():
    assert normalize_phone("9990001111") == "+7 (999) 0001111"


def test_normalize_phone_with_spaces_and_brackets():
    assert normalize_phone("+7 (999) 000 11 11") == "+7 (999) 0001111"


def test_normalize_phone_invalid_short_number():
    assert normalize_phone("12345") == ""


def test_normalize_phone_invalid_long_number():
    assert normalize_phone("+79990001111222") == ""


def test_normalize_email_correct():
    assert normalize_email("example@yandex.ru") == "example@yandex.ru"


def test_normalize_email_uppercase():
    assert normalize_email("EXAMPLE@YANDEX.RU") == "example@yandex.ru"


def test_normalize_email_double_at_and_dots():
    assert normalize_email("example@@yandex..ru") == "example@yandex.ru"


def test_normalize_email_invalid_without_domain():
    assert normalize_email("example@") == ""


def test_normalize_email_invalid_without_at():
    assert normalize_email("example.yandex.ru") == ""


def test_process_line_correct_data():
    line = "Иван Иванов|27|+79990001111|example@yandex.ru"
    expected = "Иван Иванов|27|+7 (999) 0001111|example@yandex.ru"

    assert process_line(line) == expected


def test_process_line_fix_data_from_task_example():
    line = "ИванИванов|27|+7999000 1 1 11|example@@yandex..ru"
    expected = "Иван Иванов|27|+7 (999) 0001111|example@yandex.ru"

    assert process_line(line) == expected


def test_process_line_invalid_parts_are_empty():
    line = "Иван|999|12345|wrong_email"
    expected = "|||"

    assert process_line(line) == expected


def test_process_line_missing_fields():
    line = "Иван Иванов|27"
    expected = "Иван Иванов|27||"

    assert process_line(line) == expected


def test_main_creates_output_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    input_text = "\n".join(
        [
            "ИванИванов|27|+7999000 1 1 11|example@@yandex..ru",
            "Петр Петров|35|89998887766|PETR@MAIL.RU",
            "Ошибка|200|123|bad_email",
        ]
    )

    with open("input.txt", "w", encoding="utf-8") as input_file:
        input_file.write(input_text)

    main()

    assert os.path.exists("output.txt")

    with open("output.txt", "r", encoding="utf-8") as output_file:
        result = output_file.read()

    expected = "\n".join(
        [
            "Иван Иванов|27|+7 (999) 0001111|example@yandex.ru",
            "Петр Петров|35|+7 (999) 8887766|petr@mail.ru",
            "| | |".replace(" ", ""),
        ]
    )

    assert result == expected