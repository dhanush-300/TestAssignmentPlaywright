import pytest
import allure
from web_pages.registration_page import RegistrationPage

password_cases = [
    ("weak", "12345"),
    ("borderline", "Test123"),
    ("valid", "StrongPass123!")
]

expected_rules = {
    "weak": {
        "no_spaces": True,
        "latin_only": True,
        "digit": True,
        "lowercase": False,
        "uppercase": False,
        "special_char": False,
    },
    "borderline": {
        "no_spaces": True,
        "latin_only": True,
        "digit": True,
        "lowercase": True,
        "uppercase": True,
        "special_char": False,
    },
    "valid": {
        "no_spaces": True,
        "latin_only": True,
        "digit": True,
        "lowercase": True,
        "uppercase": True,
        "special_char": True,
    }
}


@pytest.mark.parametrize("label,pwd", password_cases)
def test_registration_negative(page, label, pwd):
    reg = RegistrationPage(page)
    reg.open_form()

    with allure.step(f"Testing password category: {label}"):
        reg.fill_form("invalid_email", pwd, pwd)

        rules = reg.password_rules_visible()
        print(f"RULE STATES for {label}: {rules}")

        for rule_name, expected_value in expected_rules[label].items():
            assert rules[rule_name] == expected_value, \
                f"Rule '{rule_name}' expected {expected_value} but got {rules[rule_name]}"