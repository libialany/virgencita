import sys

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='virgencita',
    version='1.0',
    description='Little virgin',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    #packages=['virgencita'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "appdirs==1.4.4",
        "attrs==21.4.0",
        "cattrs==1.10.0",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "click==8.1.3",
        "Flask==2.1.2",
        "geographiclib==1.52",
        "geopy==2.2.0",
        "idna==3.3",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.1",
        "requests==2.27.1",
        "requests-cache==0.9.4",
        "six==1.16.0",
        "url-normalize==1.4.3",
        "urllib3==1.26.9",
        "Werkzeug==2.1.2",
    ],
    extras_require={
        'lint': ['pycodestyle'],
        'test': ['tox'],
    },
)
