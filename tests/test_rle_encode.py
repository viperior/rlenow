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
    assert rle.encode(test_input) == expected
