#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Get the name of the user
    string name = get_string("What's your name? ");

    // Print the name of the user in the terminal
    printf("%s\n", name);
}