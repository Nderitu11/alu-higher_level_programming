# Python - Almost a circle

Review of classes, inheritance, args/kwargs, JSON serialization and unit testing.

## Files

- models/base.py: Base class (id management, JSON string/file helpers, create, load_from_file)
- models/rectangle.py: Rectangle(Base) with validated attributes, area, display, update, to_dictionary
- models/square.py: Square(Rectangle) with size, update, to_dictionary
- tests/test_models/: unit tests for each module

## Run the tests

    python3 -m unittest discover tests
