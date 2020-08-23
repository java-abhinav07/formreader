import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(18, 21),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)

ocr_data = GeneratorCfg(
    num_image=50000,
    save_dir=OUT_DIR / "ocr_corpus",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "eng_text.txt"],  # TEXT_DIR / "chn_text.txt",
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng.txt",
                length=(5, 50),
                char_spacing=(0.25, 0.26),
                **font_cfg
            ),
        ),
        # lighting conditions handled by backgrounds
        # handwritten fonts used
        corpus_effects=Effects([Line(1), DropoutRand(0.10), Padding(0.8)]),
    ),
)

# fmt: off
configs = [
    # chn_data,
    # enum_data,
    # rand_data,
    # eng_word_data,
    # same_line_data,
    # extra_text_line_data,
    ocr_data,

]
# fmt: on
