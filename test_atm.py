from verification import (pin_verification, verify_account_number)

def test_verfication():
    assert pin_verification("1234") == True
    assert pin_verification("12345") == False
    assert pin_verification("abcd") == False
    assert pin_verification("12a4") == False
    assert pin_verification("12 4") == False

    assert verify_account_number("1234567890") == True
    assert verify_account_number("12345abc") == False
    assert verify_account_number("123 456") == False    
    if __name__ == "__main__":
        test_verfication()