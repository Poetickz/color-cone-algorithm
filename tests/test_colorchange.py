from ColorCone import colorchange as cc

rgb_example = (239, 126, 115)
rgb_float_example = (0.9372549019607843,
                     0.49411764705882355, 0.45098039215686275)


def test_modify_color():
    """This test that the color modifies corretly
    """
    result = cc.modify_rgb(rgb_example, 1.2)
    assert isinstance(result, tuple)
    assert result == (246, 120, 107)


def test_rgb_float_to_int():
    assert cc.rgb_float_to_int(rgb_float_example) == rgb_example


def test_rgb_int_to_float():
    assert cc.rgb_int_to_float(rgb_example) == rgb_float_example
