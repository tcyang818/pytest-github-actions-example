import pytest
import logging

from src.area import calculate_area_square

def test_001():
    logging.info(f"test log >>>>>>>")
    assert 2 == 2

def test_002():
    logging.info(f"test log >>>>>>>")
    assert 2 != 2

def test_003():
    logging.info(f"test log >>>>>>>")
    assert 2 == 2

def test_004():
    logging.info(f"test log >>>>>>>")
    assert 2 +2 == 4
        