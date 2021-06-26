from xml_generator import NUMBER_OF_ENTRIES, OUTPUT_DIR
from common import *
import os

NUMBER_OF_ENTRIES = 1
OUTPUT_DIR = "data/json"


def generate_bacteria(id_):
    pass


def main(requested_items):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


if __name__ == "__main__":
    main(NUMBER_OF_ENTRIES)
