#include <stddef.h>
#include "lists.h"


listint_t *reverse_listint(listint_t **head)
{
	listint_t *nd = *head, *next, *prev = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = prev;
		prev = nd;
		nd = next;
	}

	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *tm, *rev, *mid;
	size_t size = 0, l;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tm = *head;
	while (tm)
	{
		size++;
		tm = tm->next;
	}

	tm = *head;
	for (l = 0; l < (size / 2) - 1; l++)
		tm = tm->next;

	if ((size % 2) == 0 && tm->n != tm->next->n)
		return (0);

	tm = tm->next->next;
	rev = reverse_listint(&tm);
	mid = rev;

	tm = *head;
	while (rev)
	{
		if (tm->n != rev->n)
			return (0);
		tm = tm->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
