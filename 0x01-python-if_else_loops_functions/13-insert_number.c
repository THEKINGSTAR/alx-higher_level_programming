#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert function
 *
 * Technical interview preparation:
 * You are not allowed to google anything
 * Whiteboard first
 * Write a function in C that inserts a number
 * into a sorted singly linked list.
 * Prototype: listint_t *insert_node(listint_t **head, int number);
 * @head: head of the function to insert in
 * @number: the number to insert in the functino
 *
 * Return: the address of the new node, or NULL if it failed
 * listint_t *insert_node(listint_t **head, int number);
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *insrt, *prev;

	current = *head;
	prev = NULL;
	if (current == NULL)
		return (NULL);
	insrt = malloc(sizeof(listint_t));
	while (current != NULL)
	{
		prev = current;
		current = current->next;
		if (prev == NULL)
		{
			insrt = prev;
			return (insrt);
		}
		if (prev->n < number && current->n > number)
		{
			insrt->next = current;
			prev->next = insrt;
			insrt->n = number;
			return (insrt);
		}

	}
	return (NULL);
}
