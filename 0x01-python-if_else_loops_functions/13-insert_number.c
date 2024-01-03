#include "lists.h"

/**
 * insert_node - Insert a num into a sorted singly list
 * @head: ptr to a ptr to the head of the list
 * @number: The value to insert
 * Return: The address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *pv = NULL;

	if (n_node == NULL)
		return (NULL);

	n_node->n = number;
	n_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}

	while (current != NULL && current->n < number)
	{
		pv = current;
		current = current->next;
	}

	n_node->next = current;
	pv->next = n_node;

	return (n_node);
}
