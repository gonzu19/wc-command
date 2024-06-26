import subprocess
from main import (checklines, checkwords, checkcharacters,
                  )


filename = 'text.txt'


def test_line_count() -> None:
    result = subprocess.run(['wc', '-l', filename], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split()
    n_original_wc = int(output[0])
    n_custom_wc = checklines(filename)
    assert n_custom_wc == n_original_wc


def test_words_count() -> None:
    result = subprocess.run(['wc', '-w', filename], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split()
    n_original_wc = int(output[0])
    n_custom_wc = checkwords(filename)
    assert n_custom_wc == n_original_wc


def test_characters_count() -> None:
    result = subprocess.run(['wc', '-m', filename], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split()
    n_original_wc = int(output[0])
    n_custom_wc = checkcharacters(filename)
    assert n_custom_wc == n_original_wc
