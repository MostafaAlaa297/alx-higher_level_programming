#include "hash_tables.h"
#include <stdlib.h>

/**
 * hash_table_delete - Deletes hash table
 * @ht: The hash table to be deleted
 *
 * Return: Nothing
 */

void hash_table_delete(hash_table_t *ht)
{
	hash_node_t *node, *temp;
	unsigned long int i = 0;

	if (ht == NULL)
		return;

	while (i < ht->size)
	{
		node = ht->array[i];
		while (node)
		{
			temp = node->next;
			free(node->key);
			free(node->value);
			free(node);
			node = temp;
		}
		i++;
	}
	free(ht->array);
	free(ht);
}
