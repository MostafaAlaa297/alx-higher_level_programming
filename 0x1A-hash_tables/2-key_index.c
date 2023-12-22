#include "hash_tables.h"

/**
 * key_index - Gives you the index of a key
 * @key: The key to get its index
 * @size: The size of the array of the hash table
 *
 * Return: The index at which the key\value pair is stored
 * in the array of the hash table
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int index = hash_djb2(key) % size;

	if (index > size)
		return (-1);
	
	return (index);
}
