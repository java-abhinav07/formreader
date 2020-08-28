from __future__ import absolute_import

import sys

import numpy as np
import tensorflow as tf

from PIL import Image
from six import BytesIO as IO

from .bucketdata import BucketData

try:
    TFRecordDataset = tf.data.TFRecordDataset  # pylint: disable=invalid-name
except AttributeError:
    TFRecordDataset = tf.contrib.data.TFRecordDataset  # pylint: disable=invalid-name


class DataGen(object):
    GO_ID = 1
    EOS_ID = 2
    IMAGE_HEIGHT = 32
    CHARMAP = ["", "", ""] + list(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,\"'.<>/?;:[]{}!@#$%^&*()-=+\|` "
    )

    augmentations = [color]

    @staticmethod
    def set_full_ascii_charmap():
        DataGen.CHARMAP = ["", "", ""] + [chr(i) for i in range(32, 127)]

    def __init__(self, annotation_fn, buckets, epochs=1000, max_width=None):
        """
        :param annotation_fn:
        :param lexicon_fn:
        :param valid_target_len:
        :param img_width_range: only needed for training set
        :param word_len:
        :param epochs:
        :return:
        """
        self.epochs = epochs
        self.max_width = max_width

        self.bucket_specs = buckets
        self.bucket_data = BucketData()

        dataset = TFRecordDataset([annotation_fn])
        dataset = dataset.map(self._parse_record)

        # Apply the augmentation, run 4 jobs in parallel.
        dataset = dataset.map(self.color, num_parallel_calls=4)

        # Make sure that the values are still in [0, 1]
        dataset = dataset.map(lambda x: tf.clip_by_value(x, 0, 1), num_parallel_calls=4


        dataset = dataset.shuffle(buffer_size=10000)
        self.dataset = dataset.repeat(self.epochs)

    def clear(self):
        self.bucket_data = BucketData()
    
    def color(self, image, label):
        x = image
        x = tf.image.random_hue(x, 0.03)
        x = tf.image.random_saturation(x, 0.3, 1.1)
        x = tf.image.random_brightness(x, 0.02)
        x = tf.image.random_contrast(x, 0.4, 1.1)
        return x

    def gen(self, batch_size):

        dataset = self.dataset.batch(batch_size)
        iterator = dataset.make_one_shot_iterator()

        images, labels, comments = iterator.get_next()
        config = tf.ConfigProto(allow_soft_placement=True)
        config.gpu_options.allow_growth = True
        with tf.Session(config=config) as sess:

            while True:
                try:
                    raw_images, raw_labels, raw_comments = sess.run(
                        [images, labels, comments]
                    )
                    for img, lex, comment in zip(raw_images, raw_labels, raw_comments):

                        if self.max_width and (
                            Image.open(IO(img)).size[0] <= self.max_width
                        ):
                            word = self.convert_lex(lex)

                            bucket_size = self.bucket_data.append(
                                img, word, lex, comment
                            )
                            if bucket_size >= batch_size:
                                bucket = self.bucket_data.flush_out(
                                    self.bucket_specs, go_shift=1
                                )
                                yield bucket

                except tf.errors.OutOfRangeError:
                    break

        self.clear()

    def convert_lex(self, lex):
        if sys.version_info >= (3,):
            lex = lex.decode("iso-8859-1")

        assert len(lex) < self.bucket_specs[-1][1]
        # print(lex)
        # self.CHARMAP.append(' ')
        # print(self.CHARMAP)
        return np.array(
            [self.GO_ID] + [self.CHARMAP.index(char) for char in lex] + [self.EOS_ID],
            dtype=np.int32,
        )

    @staticmethod
    def _parse_record(example_proto):
        features = tf.parse_single_example(
            example_proto,
            features={
                "image": tf.FixedLenFeature([], tf.string),
                "label": tf.FixedLenFeature([], tf.string),
                "comment": tf.FixedLenFeature([], tf.string, default_value=""),
            },
        )
        return features["image"], features["label"], features["comment"]
