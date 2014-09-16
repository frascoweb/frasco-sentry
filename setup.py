from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-sentry',
    version='0.1',
    url='http://github.com/frascoweb/frasco-sentry',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Sentry integration for Frasco",
    long_description=desc(),
    py_modules=['frasco_sentry'],
    platforms='any',
    install_requires=[
        'frasco',
        'raven==5.0.0'
    ]
)