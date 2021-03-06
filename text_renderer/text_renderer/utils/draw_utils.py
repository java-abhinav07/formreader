from typing import Tuple, Union

from PIL import ImageDraw, Image
from PIL.Image import Image as PILImage
import numpy as np

from text_renderer.utils.font_text import FontText


def transparent_img(size: Tuple[int, int]) -> PILImage:
    """

    Args:
        size: (width, height)

    Returns:

    """
    return Image.new("RGBA", (size[0], size[1]), (255, 255, 255, 0))


def draw_text_on_bg(
    font_text: FontText,
    text_color: Tuple[int, int, int, int] = (0, 0, 0, 255),
    char_spacing: Union[float, Tuple[float, float]] = -1,
) -> PILImage:
    """

    Parameters
    ----------
    font_text : FontText
    text_color : RGBA
        Default is black
    char_spacing : Union[float, Tuple[float, float]]
        Draw character with spacing. If tuple, random choice between [min, max)
        Set -1 to disable

    Returns
    -------
        PILImage:
            RGBA Pillow image with text on a transparent image
    -------

    """
    if char_spacing == -1:
        return _draw_text_on_bg(font_text, text_color)

    chars_size = []
    width = 0
    for c in font_text.text:
        size = font_text.font.getsize(c)
        chars_size.append(size)
        width += size[0]

    max_size = max(chars_size)[0]

    height = font_text.size[1]

    char_spacings = []
    for i in range(len(font_text.text)):
        if isinstance(char_spacing, list) or isinstance(char_spacing, tuple):
            s = np.random.uniform(*char_spacing)
            char_spacings.append(int(s * height))
        else:
            char_spacings.append(int(char_spacing * height))

    width += sum(char_spacings[:-1])

    text_mask = transparent_img((int(width * 1.1), int(height * 1.5)))

    draw = ImageDraw.Draw(text_mask)

    c_x = int(width * 0.05)
    c_y = int(0.08 * height)
    colors = [
        "#000",
        "#080808",
        "#101010",
        "#181818",
        "#202020",
        "#282828",
        "#303030",
        "#383838",
        "#404040",
        "#484848",
        "#505050",
    ]
    c_color = np.random.choice(np.array(colors))

    y_offset = font_text.offset[1]
    x = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    flag  = True
    if x%7 == 0:
        flag = False
    for i, c in enumerate(font_text.text):

        xo = c_x - (char_spacings[i] // 2) * (1.05)
        yo = c_y - (y_offset // 16)

        y1 = c_y + int(height) - (y_offset // 16)
        x1 = xo + chars_size[i][0] + int(char_spacings[i] * 1.05)
        # print(xo, yo, x1, y1)

        # draw random background text
        r = np.random.choice(
            np.array(["", "D", "M", "Y", "", "A", "B", "C", "E", " ", "F"])
        )
        rgb = np.random.randint(20, 80)
        draw.text(
            (c_x, c_y - y_offset),
            str(r),
            fill=(rgb, rgb, rgb, rgb - 20),
            font=font_text.font,
            width=2,
        )

        draw.text(
            (c_x, c_y - y_offset),
            c,
            fill=text_color,
            font=font_text.font,
            stroke_fill="#000",
            width=np.random.choice([1, 2, 3]),
        )

        c_x += chars_size[i][0] + char_spacings[i]
        # text_mask.show()

        # draw a box around text
        if flag:
            draw.rectangle((xo, yo, x1, y1), width=2, outline="#000", fill=None)

    return text_mask


def _draw_text_on_bg(
    font_text: FontText, text_color: Tuple[int, int, int, int] = (0, 0, 0, 255),
) -> PILImage:
    """
    Draw text

    Parameters
    ----------
    font_text : FontText
    text_color : RGBA
        Default is black

    Returns
    -------
        PILImage:
            RGBA Pillow image with text on a transparent image
    """
    text_width, text_height = font_text.size
    text_mask = transparent_img((text_width, text_height))
    draw = ImageDraw.Draw(text_mask)

    xy = font_text.xy

    # TODO: figure out anchor
    draw.text(
        xy, font_text.text, font=font_text.font, fill=text_color, anchor=None,
    )

    return text_mask
