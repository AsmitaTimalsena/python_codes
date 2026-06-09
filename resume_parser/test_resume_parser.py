from resume_eligibility_checker import eligibility_checker

def test_senior():
    assert eligibility_checker(6) == "Senior Developer"

def test_mid():
    assert eligibility_checker(3) == "Mid-Level Developer"

def test_junior():
    assert eligibility_checker(1) == "Junior Developer"

def test_invalid():
    assert eligibility_checker(-1) == "Not Eligible"