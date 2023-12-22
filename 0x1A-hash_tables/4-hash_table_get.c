#include "hash_tables.h"
#include <stdlib.h>
#include <string.h>

/**
 * hash_table_get - Retrieves a value associated with a key
 * @ht: The hash table to look into
 * @key: The key to search for
 *
 * Return: The value associated with the key,
 * or NULL if key coudn't be found
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned int index;
	hash_node_t *current;

	if (ht == NULL || key == NULL || *key == '\0' || strcmp(key, "") == 0)
		return (NULL);

	index = key_index((const unsigned char *) key, ht->size);
	current = ht->array[index];

	if (current == NULL)
		return (NULL);

	while (strcmp(current->key, key) && current != NULL)
	{
		current = current->next;
	}
	if (current == NULL)
		return (NULL);
	else
		return (current->value);
}
