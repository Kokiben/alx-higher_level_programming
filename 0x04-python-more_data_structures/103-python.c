#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Prints bytes.
 * @p: python Obj
 * Return: No return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, l, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (l = 0; l < limit; l++)
		if (string[l] >= 0)
			printf(" %02x", string[l]);
		else
			printf(" %02x", 256 + string[l]);

	printf("\n");
}

/**
 * print_python_list - Prints list.
 * @p: python Obj
 * Return: No return
 */
void print_python_list(PyObject *p)
{
	long int size, l;
	PyListObject *list;
	PyObject *objc;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (l = 0; l < size; l++)
	{
		objc = ((PyListObject *)p)->ob_item[l];
		printf("Element %ld: %s\n", l, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(objc))
			print_python_bytes(objc);
	}
}
