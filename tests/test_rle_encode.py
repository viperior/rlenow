"""Tests for the rle_encode() function"""

import pytest

import src.rle as rle


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('a', '1a'),
        ('aa', '2a'),
        ('1', '11'),
        ('11', '21'),
        ('111', '31'),
        ('wwwawwwawwwa', '3w1a3w1a3w1a'),
        ('wwwwwwwwwwawwwwwwwwwwawwwwwwwwwwa', '10w1a10w1a10w1a'),
        ('', ''),
        ('aaab', '3a1b'),
    ]
)
def test_rle_encode(test_input: str, expected):
    """Tests for the rle_encode() function"""
    assert rle.encode(test_input, limit=9999) == expected


@pytest.mark.parametrize(
    'test_input,limit,expected',
    [
        ('a', 9, '1a'),
        ('aa', 9, '2a'),
        ('1', 9, '11'),
        ('11', 9, '21'),
        ('111', 9, '31'),
        ('wwwawwwawwwa', 9, '3w1a3w1a3w1a'),
        ('wwwwwwwwwwawwwwwwwwwwawwwwwwwwwwa', 9, '9w1w1a9w1w1a9w1w1a'),
        ('', 9, ''),
        ('aaab', 9, '3a1b'),
        ('a', 2, '1a'),
        ('aa', 2, '2a'),
        ('1', 2, '11'),
        ('11', 2, '21'),
        ('111', 2, '2111'),
        ('wwwawwwawwwa', 2, '2w1w1a2w1w1a2w1w1a'),
        (
            'wwwwwwwwwwawwwwwwwwwwawwwwwwwwwwa',
            2,
            '2w2w2w2w2w1a2w2w2w2w2w1a2w2w2w2w2w1a'
        ),
        ('', 2, ''),
        ('aaab', 2, '2a1a1b'),
        ('aaab', 9, '3a1b'),
        ('a', 3, '1a'),
        ('aa', 3, '2a'),
        ('1', 3, '11'),
        ('11', 3, '21'),
        ('111', 3, '31'),
        ('wwwawwwawwwa', 3, '3w1a3w1a3w1a'),
        (
            'wwwwwwwwwwawwwwwwwwwwawwwwwwwwwwa',
            3,
            '3w3w3w1w1a3w3w3w1w1a3w3w3w1w1a'
        ),
        ('', 3, ''),
        ('aaab', 3, '3a1b'),
        ('wwwwwwwwwwwwwww', 5, '5w5w5w'),
        ('wwwwwwwwwwwwwwww', 5, '5w5w5w1w'),
        ('wwwwww', 5, '5w1w'),
        ('wwwwww', 4, '4w2w'),
    ]
)
def test_rle_encode_with_limit(test_input: str, limit: int, expected: str):
    """Test the RLE encode function using the limit parameter"""
    assert rle.encode(test_input, limit=limit) == expected
