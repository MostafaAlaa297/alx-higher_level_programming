#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: A pointer to the first element of the list
 *
 * Return: 0 if there is no cycle and 1 if there is.
 */

int check_cycle(listint_t *list)
{
	listint_t *turt, *rab;
	turt = list;
	rab = list;

	while (rab != NULL && rab->next != NULL)
	{
		turt = turt->next;
		rab = rab->next->next;

		if (turt == rab)
			return (1);
	}
	return (0);
}
