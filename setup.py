from setuptools import setup, find_packages
import shellboard


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="shellboard",
    author="sweaty-bunny",
    author_email="sw3atyspace@gmail.com",
    url="https://github.com/Sw3aty-Acc/shellboard.git",
    version=shellboard.__version__,
    packages=find_packages(),
    install_requires=["colorama>=0.4.4"],
    license="MIT",
    description="shellboard - cross-platform framework that facilitates the development of a graphical interface for the command shell",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords="menu qt shell visual vishhhl visualmenu",
    project_urls={
        "Repository": "https://github.com/Sw3aty-Acc/shellboard.git",
        "Issues": "https://github.com/Sw3aty-Acc/shellboard/issues",
    },
    python_requires='>=3.7'
)
