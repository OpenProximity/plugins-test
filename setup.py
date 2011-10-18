from setuptools import setup
from test import __version__

setup(
    name = "openproximity-plugin-test",
    version = __version__,
    packages = ['test',],
    summary = "A Test Plugin",
    description = 
    """A very simple example on what an OpenProximity plugins looks like""",
    author = "Naranjo Manuel Francisco",
    author_email = "manuel@aircable.net",
    license = "GPL2",
    url = "https://github.com/OpenProximity/plugins-test", 
)
