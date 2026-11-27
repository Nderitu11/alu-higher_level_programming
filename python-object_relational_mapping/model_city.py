#!/usr/bin/python3
"""Defines the City class linked to the table cities."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Class that maps the table cities of a MySQL database."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
