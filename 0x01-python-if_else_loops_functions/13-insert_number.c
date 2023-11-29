#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: A pointer to the first node of the list
 * @number: The number to be inserted
 *
 * Return: The address of the new node of NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	temp = *head;
	
	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;
	
	newnode->next = temp->next;
	temp->next = newnode;

	return (newnode);
}
