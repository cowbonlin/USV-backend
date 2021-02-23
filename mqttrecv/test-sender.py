from argparse import ArgumentParser
import os
import paho.mqtt.client as mqtt

FILENAME_START = 256
IMG_SIZE_START = 16
MAX_PAYLOAD_SIZE = 268435455

parser = ArgumentParser()
parser.add_argument("path", help="path of the file")


def get_file_name(file_name):
    """Get the byte-formatted file name with extended null characts"""
    if len(file_name) > FILENAME_START:
        raise ValueError(f'Length of file name '
                         f'can\'t be bigger than {FILENAME_START}')
    filename_bytes = bytearray(file_name, 'utf-8')
    return filename_bytes + bytearray(FILENAME_START - len(filename_bytes))


def get_img_size(size):
    """Get the file size with extended null characts"""
    if size > MAX_PAYLOAD_SIZE:
        raise ValueError(f'Size of the image '
                         f'can\'t be bigger than {MAX_PAYLOAD_SIZE} bytes')
    size_bytes = bytearray(str(size), 'utf-8')
    return size_bytes + bytearray(IMG_SIZE_START - len(size_bytes))


if __name__ == '__main__':
    print('Test Sender Start')
    args = parser.parse_args()

    client = mqtt.Client()
    client.connect("mqtt", 1883, 60)
    client.loop_start()

    with open(args.path, 'rb') as image:
        img_data = bytearray(image.read())
    file_name = get_file_name(os.path.basename(args.path))
    img_size = get_img_size(len(img_data))
    payload = file_name + img_size + img_data

    client.publish("image", payload, qos=1)

    client.disconnect()
    client.loop_stop()
    print('Test Sender Finished')
