#!/usr/bin/python3
""" review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ review module"""
    place_id = ""
    user_id = ""
    text = ""
