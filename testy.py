def sudy_nebo_lichy(cislo):
    return "lichy" if cislo % 2 else "sudy"


def test_sudy_nebo_lichy():
    assert sudy_nebo_lichy(1) == "lichy"
    assert sudy_nebo_lichy(2) == "sudy"