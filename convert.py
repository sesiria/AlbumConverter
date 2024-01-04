# python3

import os
import subprocess

# convert to flac support to 32bit depth (some player may not support this format!)
def convert_wav_to_flac_s32(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".wav"):
                wav_path = os.path.join(root, file)
                relative_path = os.path.relpath(wav_path, input_directory)
                flac_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".flac")
                # converting
                print("converting file " + wav_path)
                subprocess.run(["flac", "-o", flac_path, "-V", wav_path])


# normal convert to flac maximum support 24bit depth
def convert_wav_to_flac(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".wav"):
                wav_path = os.path.join(root, file)
                relative_path = os.path.relpath(wav_path, input_directory)
                flac_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".flac")
                print("converting file " + wav_path)
                subprocess.run(["ffmpeg", "-i", wav_path, "-c:a", "flac", flac_path, "-strict", "experimental"])


# convert to alac support 24bit depth.
def convert_wav_to_alac(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".wav"):
                wav_path = os.path.join(root, file)
                relative_path = os.path.relpath(wav_path, input_directory)
                alac_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".m4a")
                print("converting file " + wav_path)
                subprocess.run(["ffmpeg", "-i", wav_path, "-c:a", "alac", alac_path])


# convert to alac 32bit
# afconvert is not supported by Windows


# specify the input/output folder
input_directory = "I:\\wav"
output_directory = "I:\\flac"

# Start converting.
print("start to convert...")
convert_wav_to_flac(input_directory, output_directory)
# convert_wav_to_alac(input_directory, output_directory)
# convert_wav_to_flac_s32(input_directory, output_directory)
#convert_wav_to_alac_s32(input_directory, output_directory)