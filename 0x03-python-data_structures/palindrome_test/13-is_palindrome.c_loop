#include "lists.h"

int odd_is_palindrome(int *arry, int lenght);

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
	int is_pm = 0, lenght = 0, lop_lenght = 0, *arry, idx = 0;
	listint_t *start;

	start = *head;
	if (start == NULL)
	{	is_pm = 1;
		return (is_pm);
	}
	while (start != NULL)
	{	start = start->next;
		lenght++;
	}
	if (lenght == 1)
	{	is_pm = 1;
		return (is_pm);
	}
	start = *head;
	arry = malloc(sizeof(int) * lenght);
	while (start != NULL)
	{	arry[idx] = start->n;
		start = start->next;
		idx++;
	}
	lop_lenght = lenght;
	if (lenght % 2 != 0)
	{
		/* is_pm = odd_is_palindrome(arry, lenght); */
		/* free(arry); */
		lop_lenght = lenght / 2;
	}
	for (idx = 0; idx < lop_lenght; idx++)
	{
		if (arry[idx] != arry[lenght - idx - 1])
		{	is_pm = 0;
			free(arry);
			return (is_pm);
		}
	}
	free(arry);
	is_pm = 1;
	return (is_pm);
}

/**
 * odd_is_palindrome - check palindrome function
 *
 * Technical interview preparation:
 * You are not allowed to google anything
 * Whiteboard first
 * Write a function in C that checks if a singly linked list is a palindrome.
 * Prototype: int is_palindrome(listint_t **head);
 *
 * @arry: array of the elements to check;
 * @lenght: lenght of the array
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 *
 * An empty list is considered a palindrome
 *
 */
int odd_is_palindrome(int *arry, int lenght)
{
	int is_pm = 1,	idx = 0;

	for (idx = 0; idx < lenght / 2; idx++)
	{
		if (arry[idx] != arry[lenght - idx - 1])
		{
			is_pm = 0;
			return (is_pm);
		}
	}
	return (is_pm);
}
