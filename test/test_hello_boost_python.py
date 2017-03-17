#!/bin/env python

from textwrap import dedent
import unittest

print("Hello")

# "Hello world" example from 
# http://www.boost.org/doc/libs/1_62_0/libs/python/doc/html/tutorial/index.html#tutorial.quickstart

class TestHello(unittest.testcase):
    
    # Possible artifacts:
    # 1) input source code file(s)
    # 2) output wrapper code file(s)
    # 3) output CMakeLists.txt
    # 4) input module test program
    def test_hello(self):
        test_bp_module(
                module_name='hello_ext',
                # C program to wrap
                cpp_srcs=[('greet.c',    
                        dedent("""
                        char const* greet()
                        {
                           return "hello, world";
                        }
                        """))],
                # Generated boost python wrapper code
                wrapper_srcs=[('hello_ext.prap.cpp',
                        dedent("""
                        #include <boost/python.hpp>
                        
                        BOOST_PYTHON_MODULE(hello_ext)
                        {
                            using namespace boost::python;
                            def("greet", greet);
                        }
                        """))],
                # Python program to test resulting module
                """
                import hello_ext
                print hello_ext.greet()
                """,
                "hello, world")

if __name__ == '__main__':
    unittest.main()
