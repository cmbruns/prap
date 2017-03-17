from setuptools import setup
from setuptools.extension import Extension
import os.path
import sys

hello_ext_srcs = [
        './src/hello_ext.prap.cpp',
        ]
hello_ext_library_dirs = [
        'C:/Boost/lib',
        ]
hello_ext_libraries = [
        'boost_python3-vc140-mt-1_63',
        ]

setup(name="hello_ext",
    description='Hello world module for Boost.Python',
    packages=['hello_ext'],
    ext_modules=[
            Extension("hello_ext._hello_ext", 
                    sources=[
                            './src/hello_ext.prap.cpp',
                    ],
                    library_dirs=hello_ext_library_dirs,
                    libraries=hello_ext_libraries,
                    include_dirs=[
                            'C:/Boost/include/boost-1_63',
                            '../input_sources',
                            ],
                    depends=[],
                    )
            ]
)
