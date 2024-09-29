#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }

    // Check first four bytes
    BYTE bytes[BLOCK_SIZE];
    FILE *output = NULL;

    int jpgcount = 0;

    while (fread(&bytes, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {

        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {

            if (!(jpgcount == 0))
            {
                fclose(output);
            }

            char fn[8];
            sprintf(fn, "%03i.jpg", jpgcount);

            output = fopen(fn, "w");
            jpgcount++;
        }

        if (!(jpgcount == 0))
        {
            fwrite(&bytes, 1, BLOCK_SIZE, output);
        }
    }

    fclose(output);
    fclose(input);

    return 0;
}

