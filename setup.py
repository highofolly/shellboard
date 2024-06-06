from setuptools import setup, find_packages
from src import shellboard as sh


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="shellboard",
    author="highofolly",
    author_email="sw3atyspace@gmail.com",
    url="https://github.com/highofolly/shellboard.git",
    version=sh.__version__,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    namespace_packages=["shellboard"],
    install_requires=["colorama>=0.4.4"],
    license="MIT",
    description="shellboard - cross-platform framework that facilitates the development of a graphical interface for the command shell",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords="menu qt shell visual vishhhl visualmenu",
    project_urls={
        "Repository": "https://github.com/highofolly/shellboard",
        "Issues": "https://github.com/highofolly/shellboard/issues",
    },
    entry_points={
        'shellboard.plugins': [],
    },
    python_requires='>=3.7'
)
