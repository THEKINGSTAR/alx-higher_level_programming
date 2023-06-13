#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check palindrome function
 *
 * Technical interview preparation:
 * You are not allowed to google anything
 * Whiteboard first
 * Write a function in C that checks if a singly linked list is a palindrome.
 * Prototype: int is_palindrome(listint_t **head);
 *
 * @head: head of the linked_list to check;
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 *
 * An empty list is considered a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	int is_pm = 0, lenght = 0;
	listint_t *start;

	start = *head;
	if (start == NULL)
	{	is_pm = 1;
		return (is_pm);	}
	while (start != NULL)
	{
		start = start->next;
		lenght++;
	}
	/*printf("list lenght: %d\n", lenght);*/
	if (lenght % 2 != 0)
	{	/*printf("lenght not divided by 2\n");*/
		return (is_pm);	}
	int *arry, idx = 0;

	start = *head;
	arry = malloc(sizeof(int) * lenght);
	while (start != NULL)
	{
		arry[idx] = start->n;
		start = start->next;
		idx++;
	}
	for (idx = 0; idx < lenght; idx++)
	{
		/*printf("idx is %d, value at is %d\n",idx, arry[idx]);*/
		/*printf("compare between: %d && %d\n",arry[idx],arry[lenght - idx - 1]);*/
		if (arry[idx] != arry[lenght - idx - 1])
		{
			is_pm = 0;
			free(arry);
			return (is_pm);
		}
	}
	is_pm = 1;
	return (is_pm);
}
