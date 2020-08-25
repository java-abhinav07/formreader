"""
Default parameters.
"""
from datetime import datetime

class Config(object):
    """
    Default config (see __main__.py or README for documentation).
    """

    GPU_ID = 0
    VISUALIZE = False

    time = datetime.now()

    # I/O
    NEW_DATASET_PATH = './dataset.tfrecords'
    DATA_PATH = '/content/drive/My Drive/IITB_Assignment/datasets/alphanumeric_AZ09/training.tfrecords'
    MODEL_DIR = f'./checkpoints_{time}'
    LOG_PATH = f'aocr_{time}.log'
    OUTPUT_DIR = './results'
    STEPS_PER_CHECKPOINT = 100
    EXPORT_FORMAT = 'savedmodel'
    EXPORT_PATH = 'exported'
    FORCE_UPPERCASE = True
    SAVE_FILENAME = False
    FULL_ASCII = False

    # Optimization
    NUM_EPOCH = 300
    BATCH_SIZE = 64
    INITIAL_LEARNING_RATE = 1.0

    # Network parameters
    CLIP_GRADIENTS = True  # whether to perform gradient clipping
    MAX_GRADIENT_NORM = 5.0  # Clip gradients to this norm
    TARGET_EMBEDDING_SIZE = 10  # embedding dimension for each target
    ATTN_NUM_HIDDEN = 128  # number of hidden units in attention decoder cell
    ATTN_NUM_LAYERS = 2  # number of layers in attention decoder cell
    # (Encoder number of hidden units will be ATTN_NUM_HIDDEN*ATTN_NUM_LAYERS)
    LOAD_MODEL = True
    OLD_MODEL_VERSION = False
    TARGET_VOCAB_SIZE = 37  # 0: PADDING, 1: GO, 2: EOS, >2: 0-9, a-z
    CHANNELS = 1  # number of color channels from source image (1 = grayscale, 3 = rgb)

    MAX_WIDTH = 480
    MAX_HEIGHT = 32
    MAX_PREDICTION = 17

    USE_DISTANCE = True

    # Dataset generation
    LOG_STEP = 500
