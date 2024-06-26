import subprocess
from main import checkbytes


filename = 'text.txt'


def test_bytes() -> None:
    result = subprocess.run(['wc', '-c', filename], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split()
    n_bytes_original_wc = int(output[0])
    n_bytes_custom_wc = checkbytes(filename)
    assert n_bytes_custom_wc == n_bytes_original_wc
