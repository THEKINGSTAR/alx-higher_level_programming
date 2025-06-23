#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
    int test = 1;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
    
    printf("TEST %i ended!\n\n", test);
    test++;

	add_nodeint_end(&head, 1);
	print_listint(head);
	
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);
        
    printf("TEST %i ended!\n\n", test);
    test++;

	head = NULL;
        print_listint(head);

        if (is_palindrome(&head) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head);

    printf("TEST %i ended!\n\n", test);
    test++;

	head = NULL;
	add_nodeint_end(&head, 1);
        print_listint(head);

        if (is_palindrome(&head) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head);	

    printf("TEST %i ended!\n\n", test);
    test++;

	head = NULL;
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 3);
        print_listint(head);

        if (is_palindrome(&head) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head);	

    printf("TEST %i ended!\n\n", test);
    test++;

        head = NULL;
        add_nodeint_end(&head, 3);
        add_nodeint_end(&head, 1);
        add_nodeint_end(&head, 4);
        print_listint(head);

        if (is_palindrome(&head) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head);

    printf("TEST %i ended!\n\n", test);
    test++;

        head = NULL;
        add_nodeint_end(&head, 1);
        add_nodeint_end(&head, 17);
        add_nodeint_end(&head, 972);
        add_nodeint_end(&head, 50);
        add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 99);
	add_nodeint_end(&head, 100);
        add_nodeint_end(&head, 98);
        add_nodeint_end(&head, 50);
        add_nodeint_end(&head, 972);
        add_nodeint_end(&head, 17);
        add_nodeint_end(&head, 1);
        print_listint(head);

        if (is_palindrome(&head) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
	free_listint(head);
    printf("TEST %i ended!\n\n", test);
	return (0);
}
