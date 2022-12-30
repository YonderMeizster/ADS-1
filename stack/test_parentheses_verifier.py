from brackets_verifier import verify_brackets


def test_true():
    sequences = ['()()()()()',
                 '((((()))))',
                 '(()())()()',
                 '((())(()))',
                 '((()()()))']
    for seq in sequences:
        assert verify_brackets(seq) == True


def test_false():
    sequences = [')(()()()()',
                 '((((()())))',
                 '())())()()',
                 '((()))()))',
                 '((()()()())']
    for seq in sequences:
        assert verify_brackets(seq) == False