from stringlab import is_palindrome


def run_tests():
    cases = [
        ("Saippuakivikauppias", True),
        ("Saippukivenkauppias", False),
        ("A man, a plan, a canal: Panama", True),
        ("", True),
        ("Hello", False),
    ]

    for text, expected in cases:
        result = is_palindrome(text)
        assert result == expected, f"is_palindrome({text!r}) -> {result}, expected {expected}"

    print("All palindrome tests passed.")


if __name__ == "__main__":
    run_tests()
