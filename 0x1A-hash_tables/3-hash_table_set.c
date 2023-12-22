#include "hash_tables.h"
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
/**
 * hash_table_set - Adds an element to the hash table
 * @ht: The hash table you want to add the key\value pair to
 * @key: The key
 * @value: The value
 *
 * Return: 1 if it succeeded and 0 otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned int index;

	hash_node_t *new_element, *current;

	if (ht == NULL || key == NULL || *key == '\0')
	{
		printf("Invalid input parameters\n");
		return (0);
	}
	
	index = key_index((unsigned char *) key, ht->size);
	printf("Index: %u\n", index);

	if (index >= ht->size)
	{
		printf("Invalid index\n");
		return (0);
	}

	current = ht->array[index];

	while (current != NULL)
	{
		if (strcmp(current->key, key) == 0)
		{
			free(current->value);
			current->value = strdup(value);
			if (current->value == NULL)
			{
				printf("Memory allocation error\n");
				return (0);
			}
			return (1);
		}
		current = current->next;
	}

	new_element = malloc(sizeof(hash_node_t));
	if (new_element == NULL)
	{
		printf("Memory allocation error\n");
		return (0);
	}

	new_element->key = strdup(key);
	new_element->value = strdup(value);
	if (new_element->key == NULL || new_element->value == NULL)
	{
		printf("Memory allocation error\n");
		free(new_element->key);
		free(new_element);
		return (0);
	}

	new_element->next = ht->array[index];
	ht->array[index] = new_element;

	return (1);
}
