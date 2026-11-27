# Python - Object-relational mapping

Scripts that connect Python to MySQL, first with MySQLdb and then with the SQLAlchemy ORM.

- 0-5: MySQLdb scripts (select, filter, SQL injection demo and fix, joins)
- model_state.py, model_city.py: SQLAlchemy models for `states` and `cities`
- 7-13: SQLAlchemy scripts (fetch all, first, filter, get, insert, update, delete)
- 14: cities with their state through SQLAlchemy

Usage example: `./0-select_states.py <mysql user> <mysql password> <database>`
