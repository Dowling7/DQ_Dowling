// mymodule.c
#include <stdio.h>
#include <Python.h>
static PyObject *add_numbers(PyObject *self, PyObject *args) {
    int num1, num2;
    if (!PyArg_ParseTuple(args, "ii", &num1, &num2)) {
        return NULL;
    }
    int result = num1 + num2;
    return PyLong_FromLong(result);
}

static PyMethodDef MyModuleMethods[] = {
    {"add_numbers", add_numbers, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",            // Module name
    "A simple C module",  // Module documentation
    -1,
    MyModuleMethods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
