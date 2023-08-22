from setuptools import setup, Extension

module = Extension('example',
                   sources=['examplemodule.c'])

setup(name='example',
      version='1.0',
      description='Example C extension module for Python',
      ext_modules=[module])
