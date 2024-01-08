#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slowly = *head;
	listint_t *faster = *head;
	listint_t *st_half = *head;
	listint_t *sec_half = NULL;

	int is_palind = 1;

	while (faster != NULL && faster->next != NULL)
	{
		faster = faster->next->next;
		slowly = slowly->next;
	}

	if (faster != NULL)
	{
		slowly = slowly->next;
	}

	sec_half = reverse_list(&slowly);

	while (sec_half != NULL)
	{
		if (st_half->n != sec_half->n)
		{
			is_palind = 0;
			break;
		}
		st_half = st_half->next;
		sec_half = sec_half->next;
	}

	return is_palind;
}

listint_t *reverse_list(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prv;
		prv = current;
		current = next;
	}

	*head = prv; 
	return (prv);  
}
