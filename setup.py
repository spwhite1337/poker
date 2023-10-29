from setuptools import setup, find_packages

setup(
    name='poker',
    version='1.0',
    description='Poker strategy guide',
    author='Scott P. White',
    author_email='spwhite1337@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': [
    ]},
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scipy',
        'requests',
        'ipykernel',
        'tqdm',
        # 'cython',
        # 'pystan',
        'flask',
        'plotly',
        'dash',
        'dash-bootstrap-components',
        'awscli',
        'openpyxl'
    ]
)
