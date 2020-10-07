from setuptools import setup
from dtool_lookup_server_plugin_scaffolding import __version__

url = "https://github.com/IMTEK-Simulation/dtool-lookup-server-plugin-scaffolding"
version = __version__
readme = open('README.rst').read()

setup(
    name="dtool-lookup-server-plugin-scaffolding",
    packages=["dtool_lookup_server_plugin_scaffolding"],
    description="This scaffolding serves as a minimal template for dtool lookup server plugin developments.",
    long_description=readme,
    author="Johannes Hörmann",
    author_email="johannes.hoermann@imtek.uni-freiburg.de",
    version=version,
    url=url,
    entry_points={
        'dtool_lookup_server.blueprints': [
            'dtool_lookup_server_plugin_scaffolding=dtool_lookup_server_plugin_scaffolding:scaffolding_bp',
        ],
    },
    install_requires=[
        "dtool-lookup-server",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
