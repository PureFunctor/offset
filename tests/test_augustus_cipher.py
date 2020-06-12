from augustus.cipher import SteppedAugustus


def test_SteppedAugustus_right_cipher():
    s0 = SteppedAugustus("Hello World")
    s1 = SteppedAugustus("Hello\tWorld")
    s2 = SteppedAugustus("Hello\nWorld")

    assert s0.right_cipher == "Igopt Xqupi"
    assert s1.right_cipher == "Igopt\tXqupi"
    assert s2.right_cipher == "Igopt\nXqupi"


def test_SteppedAugustus_left_cipher():
    s0 = SteppedAugustus("Igopt Xqupi")
    s1 = SteppedAugustus("Igopt\tXqupi")
    s2 = SteppedAugustus("Igopt\nXqupi")

    assert s0.left_cipher == "Hello World"
    assert s1.left_cipher == "Hello\tWorld"
    assert s2.left_cipher == "Hello\nWorld"
