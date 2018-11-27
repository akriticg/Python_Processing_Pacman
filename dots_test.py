from dots import Dots
from dot import Dot


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    '''testing eating dots'''
    ds = Dots(600, 600, 150, 450, 150, 450)
    for dot in ds.all_dots:
        print(dot.x, dot.y)
    ds.eat(150, 0)
    assert ds.all_dots[18].x == 150
    assert ds.all_dots[18].y == 75
    '''testing eating dots at intersection'''
    len1 = len(ds.all_dots)
    ds.eat(450, 150)
    assert len(ds.all_dots) == len1 - 2
    '''testing removed dot'''
    ds.eat(150, 375)
    assert Dot(150, 375) not in ds.all_dots
    '''testing already removed dot'''
    len2 = len(ds.all_dots)
    ds.eat(150, 375)
    assert len(ds.all_dots) == len2
    '''testing all remaining dots'''
    assert ds.dots_left() == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                              (ds.HEIGHT//ds.SPACING + 1) * 2) - 5
    '''testing dot eating at edges'''
    ds.eat(450, 600)
    ds.eat(600, 450)
    assert ds.dots_left() == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                              (ds.HEIGHT//ds.SPACING + 1) * 2) - 9


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)

test_eat()