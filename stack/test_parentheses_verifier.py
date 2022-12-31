from parentheses_verifier import verify_parentheses


def test_true():
    sequences = ['()()()()()',
                 '((((()))))',
                 '(()())()()',
                 '((())(()))',
                 '((()()()))']
    for seq in sequences:
        assert verify_parentheses(seq) == True


def test_false():
    sequences = [')(()()()()',
                 '((((()())))',
                 '())())()()',
                 '((()))()))',
                 '((()()()())']
    for seq in sequences:
        assert verify_parentheses(seq) == False