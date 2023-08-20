from setuptools import setup, find_packages


with open('pysimpler/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pysimpler',
    version='0.0.1',
    author='Muhammed Pektas',
    description='pysimpler',
    long_description='This package simplifies the fundamental software engineering practices such as exception handling, logging etc.',
    url='https://github.com/m-pektas/pysimpler',
    keywords='software engineering, exception, cache, timer, python, decorators',
    python_requires='>=3.7, <4',
    install_requires=required,
    packages=find_packages(),
    package_data={p: ["*"] for p in find_packages()},
    include_package_data=True,
)