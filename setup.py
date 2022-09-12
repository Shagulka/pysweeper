from setuptools import setup, find_packages


setup(
    name='pysweeper',
    version='0.1',
    license='MIT',
    author="Boris Khesin",
    author_email='rob.falls.do@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Shagulka/pysweeper',
    keywords='minesweeper',
    install_requires=[
          'enum',
          'random'
      ],

)