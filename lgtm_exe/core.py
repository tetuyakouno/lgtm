import click

@click.command()
@click.option('--message', '-m', default='LGTM',
               show_default=True, help='Word on the picture')
@click.argument('keyword')
def cli(keyword, message):
    """A tool of creation LGTM picture"""
    lgtm(keyword, message)
    click.echo('lgtm') #for check


def lgtm(keyword, message):
    # coding logic here.
    pass