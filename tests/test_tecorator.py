from unittest import TestCase
from tecorator import *


class TestTecorator(TestCase):
    test_ok_patterns = [
        (
            ['今日', 'は', '良い', '天気', 'でし', 'た', '。'],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            '<span>今日</span><span>は</span><span>良い</span><span>天気</span><span>でし</span><span>た</span><span>。</span>'
        ),
        (
            ['今日', 'は', '良い', '天気', 'でし', 'た', '。'],
            [None, '#F3F3F1', None, None, (240, 222, 12, 0.56), None, None],
            [(240, 222, 12, 0.51), None, None, None, '#F11111', None, None],
            '<span style="color: rgba(240,222,12,0.51);">今日</span><span style="background-color: #F3F3F1;">は</span><span>良い</span><span>天気</span><span style="background-color: rgba(240,222,12,0.56);color: #F11111;">でし</span><span>た</span><span>。</span>'
        ),
    ]
    test_error_patterns = [
        (
            ['今日', 'は', '良い', '天気', 'でし', 'た', '。'],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            LengthsNotMatchError
        ),
        (
            ['今日', 'は', '良い', '天気', 'でし', 'た', '。'],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None],
            LengthsNotMatchError
        ),
        (
            ['今日', 'は', '良い', '天気', 'でし', 'た', '。'],
            None,
            None,
            NoColorsError
        ),
    ]

    def test_decorate_tokens_ok(self):
        for tokens, bgcolors, textcolors, gold_html in self.test_ok_patterns:
            with self.subTest(tokens=tokens, bgcolors=bgcolors, textcolors=textcolors):
                self.assertEqual(decorate_tokens(tokens, bgcolors, textcolors), gold_html)

    def test_decorate_tokens_error(self):
        for tokens, bgcolors, textcolors, error in self.test_error_patterns:
            with self.subTest(tokens=tokens, bgcolors=bgcolors, textcolors=textcolors):
                with self.assertRaises(error):
                    decorate_tokens(tokens, bgcolors, textcolors)
