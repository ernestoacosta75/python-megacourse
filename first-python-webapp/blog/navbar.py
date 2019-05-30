from flask_nav.elements import *

from . import nav


@nav.navigation()
def main_nav():
    navbar = Navbar('Blog')
    navbar.items.append(View('Home', 'main.index'))

    return navbar