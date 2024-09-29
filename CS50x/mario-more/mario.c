#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        // Input of height of pyramid
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    //1st loop to print the row
    for (int i = 0; i < height; i++)
    {
        //2nd loop to give space
        for (int k = 0; k < height - i - 1; k++)
        {
            printf(" ");
        }
        //3rd loop to print the hash
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        printf("  ");

        //4th loop to print hash again after a gap
        for (int l = 0; l < i + 1; l++)
        {
            printf("#");
        }

        printf("\n");

    }
    return 0;
}