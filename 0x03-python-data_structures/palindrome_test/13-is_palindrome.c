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
listint_t *revrs_list(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
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
	int is_pm = 0, s, r, lenght = 0, lop_lenght, idx;
	listint_t *start, *s_half;/*, *f_half;*/

	start = *head;
	if (start == NULL || start->next == NULL)
	{	is_pm = 1;
		return (is_pm);
	}
	while (start != NULL)
	{
		start = start->next;
		lenght++;
	}
	lop_lenght = lenght;
        if (lenght % 2 != 0)
        {
                lop_lenght = lenght / 2;
        }
	start = *head;
	for (idx = 0; idx < lop_lenght; idx++)
	{
		s_half = start->next;
		start = start->next;
	}
	s_half = start->next;
	start = *head;
	s_half = revrs_list(&s_half);
	printf("Start Comparing\n");
        for (idx = 0; idx < lop_lenght; idx++)
        {
                s = start->n;
                r = s_half->n;
		printf("COMPARE BETWEEN Start Value %d , Reverse Value %d\n", s, r);
                if (s != r)
                {
                        printf("DIFFRENT VALUES ARE Start Value %d , Reverse Value %d\n", s, r);
                        return (is_pm);
                }
                start = start->next;
                s_half = s_half->next;
        }
	is_pm = 1;
	return (is_pm);
}
