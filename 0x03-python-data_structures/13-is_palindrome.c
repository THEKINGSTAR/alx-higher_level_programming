#include "lists.h"

int raverse_revers(listint_t *head);

/**
 * revrs_list - reverse inkd list
 *
 * @head: the head of the list
 *
 * Return: return the value of the last node in
 * in the list
 */
listint_t *revrs_list(listint_t *head)
{
	listint_t *current = head, *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * _is_palindrome - check palindrome function
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
	int is_pm = 0, s, r;
	listint_t *start, *reversed;

	start = *head;
	if (start == NULL || start->next == NULL)
	{	is_pm = 1;
		return (is_pm);
	}
	reversed = revrs_list(*head);
	while (start != NULL && start == reversed)
	{
		s = start->n;
		r = reversed->n;
		printf("COMPARE BETWEEN Start Value %d , Reverse Value %d\n", s, r);
		if (s != r)
		{
			printf("DIFFRENT VALUES ARE Start Value %d , Reverse Value %d\n", s, r);
			return (is_pm);
		}
		start = start->next;
		reversed = reversed->next;
	}
	is_pm = 1;
	return (is_pm);
}




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
	int is_pm = 0, s, r;
	listint_t *start;

	start = *head;
	if (start == NULL || start->next == NULL)
	{	is_pm = 1;
		return (is_pm);
	}
	while (start != NULL)
	{
		s = start->n;
		r = raverse_revers(start);
		/*printf("COMPARE BETWEEN Start Value %d , Reverse Value %d\n", s, r);*/
		if (s != r)
		{
			/*printf("DIFFRENT VALUES ARE Start Value %d , Reverse Value %d\n", s, r);*/
			return (is_pm);
		}
		start = start->next;
	}
	free(start);
	is_pm = 1;
	return (is_pm);
}

/**
 * raverse_revers - reverse traverse linkd list
 *
 * @head: the head of the list
 *
 * Return: return the value of the last node in
 * in the list
 */
int raverse_revers(listint_t *head)
{
	int val;
	listint_t *start, *prev;

	if (head->next == NULL)
		return (head->n);

	prev = head;
	start = prev->next;
	while (prev->next != NULL)
	{
		/*printf("s: %d \n", prev->n);*/
		if (start->next == NULL)
		{
			val = start->n;
			free(start);
			prev->next = NULL;
			continue;
		}

		start = start->next;
		prev = prev->next;
	}
	return (val);
}


