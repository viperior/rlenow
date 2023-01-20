"""Run-length encoding algorithm implementation"""


def encode(data: str, limit: int = 9) -> str:
    """Return the input data encoded using Run-length encoding (RLE)"""
    encoded = ''
    n = len(data)
    i = 0
    if n == 0:  # Handle empty string input by returning an empty string
        return encoded
    while i < n:
        count = 1
        while i < n - 1 and data[i] == data[i+1] and count < limit:
            count += 1
            i += 1
        i += 1
        encoded += str(count)
        encoded += data[i-1]
    return encoded
