
def test_calculate():
    assert 2*2 == 4

def test_calculate_area_square_negative():
    assert 2*2 > 0

def test_calculate_area_square_string():
    assert 2*2 == "4"

def test_calculate_area_square_list():
    assert 2*2 == ["4"]
        