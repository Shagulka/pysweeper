from setuptools import setup, find_packages


setup(
    name='pythonsweeper',
    version='0.1.6',
    license='MIT',
    author="Boris Khesin",
    author_email='rob.falls.do@gmail.com',
    description='A Python implementation of the classic Minesweeper game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Shagulka/pysweeper',
    keywords=['minesweeper', 'game', 'python', 'backend']
)