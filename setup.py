from setuptools import setup

from rome import __version__


setup(
    name='rome',
    version=__version__,
    author='Vladimir Keleshev',
    author_email='vladimir@keleshev.com',
    description='A practical Roman numerals implementation',
    license='MIT',
    keywords='roman numerals',
    url='http://github.com/halst/rome',
    py_modules=['rome'],
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
)
