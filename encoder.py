import argparse
import importlib
import pkgutil

ENCODERS_DIR = 'encoders'


def load_encoders():
    encoders = [name for _, name, _ in pkgutil.iter_modules([ENCODERS_DIR])]
    return encoders


def encode_data(encoder, data):
    module = importlib.import_module(ENCODERS_DIR + '.' + encoder)
    return module.Encoder().encode(data)


def main():
    parser = argparse.ArgumentParser(description='convert strings to binary code')
    parser.add_argument('--data', dest='data', action='store', help='string to encode (from command line)')
    parser.add_argument('--file', dest='filename', action='store', help='file with data to encode')
    parser.add_argument('--enc', dest='encoder', choices=load_encoders(), required=True, help='encoding to covert')
    parser.add_argument('--out', dest='out_filename', action='store', required=True, help='file to store result')

    args = parser.parse_args()
    data = args.data

    if args.filename is not None:
        with open(args.filename, 'rb') as f:
            data = f.read()
    else:
        data = data.encode()

    result = encode_data(args.encoder, data)


if __name__ == '__main__':
    main()