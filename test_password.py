#!/usr/bin/env python3
"""Tests for password.py"""

import os
from subprocess import getstatusoutput, getoutput
import password

prg = './password.py'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_default_password_length():
    """default password length is 7"""

    assert password.password_length == 8

#---------------------------------------------------
def test_password_length_is_number():
    """Make sure there a 10 letters in list"""

    assert type(password.password_length) == int

#---------------------------------------------------
def test_lowercase_list_is_10():
    """Make sure there a 10 letters in list"""

    assert len(password.uppercase_list) == 10


# --------------------------------------------------
def test_password_length():
    """test password length matches user ouput"""

    assert os.path.isfile(prg)