from augustus.cipher import SteppedAugustus


def test_SteppedAugustus_right_cipher():
    s = SteppedAugustus("Hello World")
    assert s.right_cipher == "Igopt Xqupi"


def test_SteppedAugustus_left_cipher():
    s = SteppedAugustus("Igopt Xqupi")
    assert s.left_cipher == "Hello World"
