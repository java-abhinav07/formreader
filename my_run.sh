#!/bin/sh

echo "Image Directory: $1";
echo "Output File: $2";


aocr predict --full-ascii --use-gru --folder_path $1 --output_dir $2

echo "Done!";
