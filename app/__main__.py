import click

from . import app


_DEFAULT_HOST = '0.0.0.0'
_DEFAULT_PORT = 8000


@click.group()
def main():
    pass


@main.command()
@click.option('-h', '--host', default=_DEFAULT_HOST)
@click.option('-p', '--port', default=_DEFAULT_PORT)
@click.option('-d', '--debug', is_flag=True)
def run(host, port, debug):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
