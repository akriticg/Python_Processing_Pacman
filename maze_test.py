from dot import Dot
from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    '''testing removing a dot'''
    m.eat_dots(0, 100)
    assert m.dots.all_dots[0].x == 75
    assert m.dots.all_dots[0].y == 100
    '''testing removing two dots from intersection'''
    len1 = len(m.dots.all_dots)
    m.eat_dots(150, 300)
    assert len(m.dots.all_dots) == len1 - 2
    '''testing removed dot'''
    m.eat_dots(600, 300)
    assert Dot(600, 300) not in m.dots.all_dots
    '''testing already removed dot'''
    len2 = len(m.dots.all_dots)
    m.eat_dots(0, 100)
    assert len(m.dots.all_dots) == len2
