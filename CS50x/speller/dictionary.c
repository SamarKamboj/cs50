// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//Total words in the dictionary
unsigned int dict_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *cursor = table[hash(word)];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //TODO: Improve this hash function
    int h = (int)toupper(word[0]) - 65;
    //Return hash value
    return h;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }

    char wrd[LENGTH + 1];
    while (fscanf(input, "%s", wrd) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        //Copy string into word section of new node
        strcpy(n->word, wrd);

        // Insert new node into Hash Table
        n->next = table[hash(wrd)];
        table[hash(wrd)] = n;

        //Count the total words in the dictionary
        dict_size++;
    }

    //Close opened file
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dict_size;
}

//Free memory
void free_mem(node *cursor, int *x)
{
    //Check if reached till last word of single linked list
    while (cursor != NULL)
    {
        //Temporary node to delete/free words
        node *tmp = cursor;
        //Move cursor
        cursor = cursor->next;
        free(tmp);
        (*x)++;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int s = 0;
    //Free words from memory
    for (int i = 0; i < N; i++)
    {
        free_mem(table[i], &s);
    }
    //Check if dictionary unloaded successfully or not
    if (s == dict_size)
    {
        return true;
    }
    return false;
}