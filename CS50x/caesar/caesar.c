#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);

    string pt = get_string("plaintext: ");
    int l = strlen(pt);

    for (int i = 0; i < l; i++)
    {
        if (pt[i] >= 97 && pt[i] <= 122)
        {
            pt[i] = (char)(((int)pt[i] - 97 + k) % 26 + 97);
        }
        else if (pt[i] >= 65 && pt[i] <= 90)
        {
            pt[i] = (char)(((int)pt[i] - 65 + k) % 26 + 65);
        }
    }

    printf("ciphertext: %s\n", pt);
    return 0;
}