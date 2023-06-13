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
	int is_pm = 0, lenght = 0, *arry, idx = 0;
	listint_t *start;

	start = *head;
	if (start == NULL)
	{	is_pm = 1;
		return (is_pm);	}
	while (start != NULL)
	{	start = start->next;
		lenght++;	}
	if (lenght == 1)
	{	is_pm = 1;
		return (is_pm);	}
	start = *head;
	arry = malloc(sizeof(int) * lenght);
	while (start != NULL)
	{	arry[idx] = start->n;
		start = start->next;
		idx++;	}
	if (lenght % 2 != 0)
	{
		is_pm = odd_is_palindrome(arry, lenght);
		free(arry);
		return (is_pm);
	}
	for (idx = 0; idx < lenght; idx++)
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
			free(arry);
			return (is_pm);
		}
	}
	return (is_pm);
}





/*			OLD WITH  FOR TESTING WITH PRINTF() */
/**
 * _is_palindrome - check palindrome function
 *
 * FOR TESTING WITH PRINTF()
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
int _is_palindrome(listint_t **head)
{
	int is_pm = 0, lenght = 0;
	int *arry, idx = 0;
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

	start = *head;
	arry = malloc(sizeof(int) * lenght);
	while (start != NULL)
	{	arry[idx] = start->n;
		start = start->next;
		idx++;
	}
	for (idx = 0; idx < lenght; idx++)
	{
		/*printf("idx is %d, value at is %d\n",idx, arry[idx]);*/
		/*printf("compare between: %d && %d\n",arry[idx],arry[lenght - idx - 1]);*/
		if (arry[idx] != arry[lenght - idx - 1])
		{	is_pm = 0;
			free(arry);
			free(start);
			return (is_pm);
		}
	}
	free(arry);
	free(start);
	is_pm = 1;
	return (is_pm);
}

/**
 * full_is_palindrome - check palindrome function
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
int full_is_palindrome(listint_t **head)
{
	int is_pm = 0, lenght = 0, *arry, idx = 0;
	listint_t *start;

	start = *head;
	if (start == NULL)
	{	is_pm = 1;
		return (is_pm);	}
	while (start != NULL)
	{	start = start->next;
		lenght++;	}
	if (lenght == 1)
	{	is_pm = 1;
		return (is_pm);	}
	start = *head;
	arry = malloc(sizeof(int) * lenght);
	while (start != NULL)
	{	arry[idx] = start->n;
		start = start->next;
		idx++;	}
	if (lenght % 2 != 0)
	{
		return (odd_is_palindrome(arry, lenght));
		for (idx = 0; idx < lenght / 2; idx++)
		{
			if (arry[idx] != arry[lenght - idx - 1])
			{	is_pm = 0;
				free(arry);
				return (is_pm);
			}
		}
	}
	for (idx = 0; idx < lenght; idx++)
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


