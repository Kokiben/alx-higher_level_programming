#include <Python.h>

/**
 * print_python_list_info - print data about Python list.
 * @p: PyObject lists.
 */
void print_python_list_info(PyObject *p)
{
	int size, allc, idx;
	PyObject *object;

	size = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allc);

	for (idx = 0; idx < size; idx++)
	{
		printf("Element %d: ", idx);

		object = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
