#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: A pointer to the first element of the linked list
 *
 * Return: Return 1 if the linked list is palindrome, and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, counter = 0;
	int arr[100]; 

	if (*head == NULL)
		return (1);
	
	temp = *head;

	while (temp)
	{
		arr[counter++] = temp->n;
		temp = temp->next;
	}

	for (i =0; i < counter / 2; i++)
	{
		if (arr[i] != arr[counter - i - 1])
			return (0);
	}

	return (1);
}
