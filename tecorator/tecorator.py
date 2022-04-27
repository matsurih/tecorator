from typing import List, Tuple, Union, Optional


class LengthsNotMatchError(Exception):
    pass


class NoColorsError(Exception):
    pass


def __create_html_start(
        bgcolor: Union[str, Tuple[int, int, int, float]] = None,
        textcolor: Union[str, Tuple[int, int, int, float]] = None,
):
    """
    Generate html start tag with bgcolors and/or textcolors
    :param bgcolor:
    :param textcolor:
    :return:
    """
    if not bgcolor and not textcolor:
        return '<span>'
    if type(bgcolor) is tuple:
        bgcolor = f'rgba({",".join(map(str, bgcolor))})'
    if type(textcolor) is tuple:
        textcolor = f'rgba({",".join(map(str, textcolor))})'
    html = ['<span style="']
    if bgcolor:
        html += ['background-color: ', bgcolor, ';']
    if textcolor:
        html += ['color: ', textcolor, ';']
    html += ['">']
    return ''.join(html)


def decorate_tokens(
        tokens: List[str],
        bgcolors: List[Optional[Union[str, Tuple[int, int, int, float]]]] = None,
        textcolors: List[Optional[Union[str, Tuple[int, int, int, float]]]] = None,
):
    """
    Decorate tokens with bgcolors and/or textcolors
    :param tokens: List of str, such as tokens.
    :param bgcolors: List of str or Tuple. str is color-hashcode(ex. '#RRGGBB') or color-name(ex. 'DeepPink'),
     and Tuple is rgba(ex. (R, G, B, A)). This will be used for text background color.
    :param textcolors: List of str or Tuple. str is color-hashcode(ex. '#RRGGBB') or color-name(ex. 'DeepPink'),
     and Tuple is rgba(ex. (R, G, B, A)). This will be used for text color.
    :return:
    """
    zip_items = None
    if not bgcolors and not textcolors:
        raise NoColorsError('No color passed, please fill any of arguments, `bgcolors` or `textcolors`.')
    if bgcolors:
        if len(tokens) != len(bgcolors):
            raise LengthsNotMatchError('Lengths of tokens and bgcolors are different.')
        zip_items = zip(tokens, bgcolors, [None] * len(tokens))
    if textcolors:
        if len(tokens) != len(textcolors):
            raise LengthsNotMatchError('Lengths of tokens and textcolors are different.')
        zip_items = zip(tokens, [None] * len(tokens), textcolors)
    if bgcolors and textcolors:
        if len(bgcolors) != len(textcolors):
            raise LengthsNotMatchError('Lengths of bgcolors and textcolors are different.')
        zip_items = zip(tokens, bgcolors, textcolors)

    html = ''.join(
        [
            f'{__create_html_start(bgcolor, textcolor)}{token}</span>'
            for token, bgcolor, textcolor in zip_items
        ]
    )
    return html
