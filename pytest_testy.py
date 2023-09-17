import pytest_funkcje
from pytest_funkcje import *
import pytest


def test_dodawania1():
    assert dodawanie(3,5) == 8 #sprawdz
    assert dodawanie(3, 5) == 8


def test_dodawania2():
    assert dodawanie(1,1) == 2

def test_mnożenie():
    assert mnożenie(1,2) == 2
    assert mnożenie(10, 1.1) == 11
    assert mnożenie(100, 1.1) == 110

def test_fissbuzz():
    assert fissbuzz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 3
    assert fissbuzz(4) == 4
    assert fissbuzz(5) == 'fiss'
    assert fissbuzz(6) == 6
    assert fissbuzz(7) == 7
    assert fissbuzz(8) == 8
    assert fissbuzz(9) == 9

def test_fissbuzz_andvance():
    assert fissbuzz(0) == None
    assert fissbuzz(-5) == None
    assert fissbuzz(5.8) == 'buzz'

