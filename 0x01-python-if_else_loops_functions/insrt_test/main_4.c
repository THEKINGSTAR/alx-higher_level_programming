#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - create list and test insert multiple numbers
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 402);
	add_nodeint_end(&head, 1024);
	print_listint(head);

	printf("-----------------\n");

	insert_node(&head, 5);
	insert_node(&head, -32);
	insert_node(&head, 5432);
	insert_node(&head, 101);
	insert_node(&head, 47);
	insert_node(&head, 6405);

	print_listint(head);

	free_listint(head);

	return (0);
}
