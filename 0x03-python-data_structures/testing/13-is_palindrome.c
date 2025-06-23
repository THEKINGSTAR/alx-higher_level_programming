#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome- check if lists is palindrome
 * @head: pointer to pointer of the first node of listint_t list
 * Return: 1 if is palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
    int check = 0, len = 0, loop = 0;
    listint_t *new, *lst_len, *list;
    int * num_list;

    new = *head;
    lst_len = *head;
    list = * head;

    if(*head == NULL)
    {
        check = 1;
        return(check);
    }
    
    while(lst_len != NULL)
    {
        len++;
        lst_len = lst_len->next;
    }
    if(len == 1)
    {
        check = 1;
        return(check);
    }
    else
    {
        num_list = malloc(sizeof(int) * len);
        if(num_list == NULL)
            return(check);
        while(list != NULL)
        {
            num_list[loop] = list->n;
            list = list->next;
            loop++;
        }
        loop = 0;
        while(new != NULL)
        {
            if(num_list[loop] != num_list[len - 1 - loop])
            {
                return(check);
            }
            loop++;
            new = new->next;
        }
    }
    check = 1;
    free(num_list);
    return(check);
}
