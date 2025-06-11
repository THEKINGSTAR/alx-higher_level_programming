#include <stdio.h>
#include <stdlib.h>
#include "lists.h" 

/**
 * check_cycle: is linked list have cycle or not
 * list: the first node of the linkd list
 * Return: 0 if no cylcle 1 if there cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lst_hd, *current;
	lst_hd = list;
	
	if(lst_hd == NULL || lst_hd->next == NULL)
	{
		return(0);
	}

	current = lst_hd->next;

	while (current != NULL)
	{
		if(current->next != lst_hd)
		{
			current = current->next;
		}
		else
		{
			return (1);
		}
	}
	return (0);
	
}
