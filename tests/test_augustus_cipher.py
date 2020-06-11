from augustus.cipher import SteppedAugustus


def test_SteppedAugustus_right_cipher():
    s = SteppedAugustus("Hello")
    assert s.right_cipher == "Igopt"


def test_SteppedAugustus_left_cipher():
    s = SteppedAugustus("Igopt")
    assert s.left_cipher == "Hello"
