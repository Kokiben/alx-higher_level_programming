#include "lists.h"

/**
 * check_cycle - checks if list has a cycle
 *
 * @list: a ptr to head of list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
listint_t *slowly = list;
listint_t *faster = list;

while (slowly != NULL && faster != NULL && faster->next != NULL)
{
slowly = slowly->next;
faster = faster->next->next;

if (slowly == faster)
{
return (1);
}
}

return (0);
}
