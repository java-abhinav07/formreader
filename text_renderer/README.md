# Text Renderer
Generate text images for training deep learning OCR model (e.g. [CRNN](https://github.com/bgshih/crnn)). ![example](./image/example.gif)

- [x] Modular design. You can easily add [Corpus](https://oh-my-ocr.github.io/text_renderer/corpus/index.html), [Effect](https://oh-my-ocr.github.io/text_renderer/effect/index.html), [Layout](https://oh-my-ocr.github.io/text_renderer/layout/index.html).
- [x] Support generate `lmdb` dataset which compatible with [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), see [Dataset](https://oh-my-ocr.github.io/text_renderer/dataset.html)
- [x] Support render multi corpus on image with different font, font size or font color. [Layout](https://oh-my-ocr.github.io/text_renderer/layout/index.html) is responsible for the layout between multiple corpora
- [ ] Generate vertical text
- [ ] Corpus sampler: helpful to perform character balance

## Quick Start

To use text_renderer, you should prepare:

  - Font file: `.ttf` or...
  - Background image
  - Text: Optional. Depends on the [corpus](https://oh-my-ocr.github.io/text_renderer/corpus/index.html) you use.
  - Character set: Optional. Depends on the [corpus](https://oh-my-ocr.github.io/text_renderer/corpus/index.html) you use.

Run following command to generate image using example data:

```bash
git clone https://github.com/oh-my-ocr/text_renderer
cd text_renderer
python3 setup.py develop
pip3 install -r docker/requirements.txt
python3 main.py \
    --config example_data/example.py \
    --dataset img \
    --num_processes 2 \
    --log_period 10
```

The data is generated in the `example_data/output` directory.

`main.py` script only has 4 arguments:
- config：Python config file path
- dataset: Dataset format `img`/`lmdb`
- num_processes: Number of processes used
- log_period: Period of log printing. (0, 100)

All parameters related to the example image generation process are all configured in
[example.py](https://github.com/oh-my-ocr/text_renderer/blob/master/example_data/example.py)

Learn more at [documentation](https://oh-my-ocr.github.io/text_renderer/index.html)

