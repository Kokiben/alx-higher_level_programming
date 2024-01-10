#include <Python.h>


void print_python_list(PyObject *p)
{
	int size, alloc, l;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *va = (PyVarObject *)p;

	size = va->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (l = 0; l < size; l++)
	{
		type = list->ob_item[l]->ob_type->tp_name;
		printf("Element %d: %s\n", l, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[l]);
	}
}

void print_python_bytes(PyObject *p)
{
	unsigned char l, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (l = 0; l < size; l++)
	{
		printf("%02hhx", bytes->ob_sval[l]);
		if (l == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
