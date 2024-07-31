import sqlite3

import click
from flask import current_app, g


# g is a special object that's unique for each request. It handles the connection to the database on each request.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# reads the schemas.sql file and creates the tables based on it
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Allows initialization of database from command line and closes the database upon app termination
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Defines the initialization command
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


