#include "greet.cpp"
#include <boost/python.hpp>

BOOST_PYTHON_MODULE(_hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}
