import seasons
from datetime import date
from pytest import raises

def test_get_date():
    assert seasons.get_date("2023-05-02") == [2023, 5, 2]
    with raises(SystemExit) as exit_code:
        seasons.get_date("2023-05-02-01")
    assert exit_code.type == SystemExit
    assert exit_code.value.code == "Invalid date"


def test_check_date():
    today = date.today()
    assert seasons.check_date([(today.year-1), today.month, today.day]) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.check_date([(today.year-2), today.month, today.day]) == "One million, fifty-one thousand, two hundred minutes"

