#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_adress - check for sililartiyt function
 * @list: list to nodes
 * @adress: adress of the current node
 * @count: number of nodes to check
 *
 * Return: 0 if not 1 if found simillar
 */
int check_adress(listint_t *list, listint_t *adress, int count)
{
	listint_t *check = list, *node_adress = adress->next;
	int adrs_check = 0;

	while (count--)
	{
		if (node_adress == check)
		{
			adrs_check = 1;
			/*free(node_adress); */
			/*free(check);*/
			return (adrs_check);
		}
		check = check->next;
	}
	/* free(node_adress); */
	return (adrs_check);
}

/**
 * check_cycle - check function
 * Write a function in C that checks if a singly linked list has a cycle in it.
 * Prototype: int check_cycle(listint_t *list);
 * @list: list to check the cycle exist or not
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * Requirements:
 * Only these functions are allowed: write, printf, putchar, puts, malloc, free
 */
int check_cycle(listint_t *list)
{
	int checker = 0, count = 0;
	listint_t *current = list;

	while (current != NULL)
	{
		count++;
		checker = check_adress(list, current, count);
		if (checker == 1)
		{
			return (checker);
		}
		current = current->next;
	}
	return (checker);
}
