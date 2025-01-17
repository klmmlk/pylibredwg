from setuptools import setup, Extension

module = Extension('libredwg', sources=['src/libredwg.c'])

setup(
    name='pylibredwg',
    version='1.0',
    description='Python bindings for libredwg',
    ext_modules=[module],
    py_modules=['libredwg'],
)
