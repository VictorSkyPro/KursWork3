import pytest

from main import card_stels, date_dd_mm_eeee, display_info


def test_date_dd_mm_eeee():
    assert date_dd_mm_eeee("2019-11-19T09:22:25.899614") == '19.11.2019'

def test_card_stels():
    assert card_stels("Maestro 7810846596785568") == 'Maestro 781084**5568'
    assert card_stels("Visa Gold 7756673469642839") == 'Visa Gold 775667**2839'
    assert card_stels("Счет 73222753239048295679") == 'Счет **5679'
    assert card_stels("MasterCard 8532498887072395") == 'MasterCard 853249**2395'
    assert card_stels("МИР 8201420097886664") == 'МИР 820142**6664'
    assert card_stels("Visa Platinum 2241653116508487") == 'Visa Platinum 224165**8487'