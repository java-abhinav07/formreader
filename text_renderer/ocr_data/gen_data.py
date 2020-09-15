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

# lighting conditions handled by backgrounds
# handwritten fonts used

CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = "/home/abhinavjava/Projects/IITB_Assignment/dataset/test/"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(45, 50),
)

perspective_transform = NormPerspectiveTransformCfg(1, 1, 0.25)

ocr_data = GeneratorCfg(
    num_image=17000,
    save_dir=OUT_DIR,
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "eng_caps.txt"],  # TEXT_DIR / "chn_text.txt",
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng_AZ09.txt",
                length=(5, 25),
                char_spacing=(0.35, 0.36),
                **font_cfg,
            ),
        ),
        corpus_effects=Effects([Padding(1), Line(1), DropoutRand(0.20)]),
    ),
)

rand_data = GeneratorCfg(
    num_image=70000,
    save_dir=OUT_DIR,
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(
            RandCorpusCfg(
                chars_file=CHAR_DIR / "eng_AZ09.txt",
                length=(5, 25),
                **font_cfg,
                char_spacing=(0.30, 1.0),
            )
        ),
        corpus_effects=Effects([Padding(0.4), Line(0.4)]),
    ),
)

enum_data = GeneratorCfg(
    num_image=16000,
    save_dir=OUT_DIR,
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "enum_text.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng_AZ09.txt",
                **font_cfg,
                char_spacing=(0.45, 0.46),
            ),
        ),
        corpus_effects=Effects([Padding(1), Line(1), DropoutRand(0.10)]),
    ),
)

eng_word_data = GeneratorCfg(
    num_image=5,
    save_dir=OUT_DIR,
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "eng_caps.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng_AZ09.txt",
                **font_cfg,
                char_spacing=(0.35, 0.36),
            ),
        ),
        corpus_effects=Effects([Padding(1), Line(0.5), DropoutRand(0.10)]),
    ),
)


# fmt: off
configs = [
    # chn_data,
    # enum_data,
    rand_data,
    # eng_word_data,
    # same_line_data,
    # extra_text_line_data,
    # ocr_data,

]
# fmt: on
