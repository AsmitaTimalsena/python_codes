from resume_score_calculator import score_calculator
def test_full_score():
    assert score_calculator("yes", "yes") == 20

def test_python_only():
    assert score_calculator("yes", "no") == 10

def test_none():
    assert score_calculator("no", "no") == 0

def test_intentional_fail():
    assert score_calculator("yes", "no") == 20  #fail test case
