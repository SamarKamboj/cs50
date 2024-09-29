#include <math.h>
#include "helpers.h"

void swap(uint8_t *x, uint8_t *y);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            //Fetch all RGB values and average it
            int average = round((image[row][col].rgbtRed + image[row][col].rgbtGreen + image[row][col].rgbtBlue) / 3.0);

            //New pixel value
            image[row][col].rgbtRed = average;
            image[row][col].rgbtGreen = average;
            image[row][col].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            //Store RGB values
            uint8_t originalRed = image[row][col].rgbtRed;
            uint8_t originalGreen = image[row][col].rgbtGreen;
            uint8_t originalBlue = image[row][col].rgbtBlue;

            //Formula to convert a normal pixel to sepia looking pixel
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            //New pixel value
            image[row][col].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[row][col].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[row][col].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width / 2; col++) // col stands for Column
        {
            //Swap pixels on horizontally opposite sides
            swap(&image[row][col].rgbtRed, &image[row][width - 1 - col].rgbtRed);
            swap(&image[row][col].rgbtGreen, &image[row][width - 1 - col].rgbtGreen);
            swap(&image[row][col].rgbtBlue, &image[row][width - 1 - col].rgbtBlue);
        }
    }
    return;
}

void swap(uint8_t *x, uint8_t *y)
{
    uint8_t tmp = *x;
    *x = *y;
    *y = tmp;
    return;
}

// Blur blur
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Copy 'blur' in temporary 2D array 'blur'
    RGBTRIPLE blur[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            blur[row][col] = image[row][col];
        }
    }

    // Take the average value and update image
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            int aRed = 0;
            int aGreen = 0;
            int aBlue = 0;
            float count = 0;

            //Upside
            if (row - 1 >= 0)
            {
                //Upside-left
                if (col - 1 >= 0)
                {
                    aRed += blur[row - 1][col - 1].rgbtRed;
                    aGreen += blur[row - 1][col - 1].rgbtGreen;
                    aBlue += blur[row - 1][col - 1].rgbtBlue;
                    count++;
                }
                //Upside-same
                if (col >= 0)
                {
                    aRed += blur[row - 1][col].rgbtRed;
                    aGreen += blur[row - 1][col].rgbtGreen;
                    aBlue += blur[row - 1][col].rgbtBlue;
                    count++;
                }
                //Upside-right
                if (col + 1 <= width - 1)
                {
                    aRed += blur[row - 1][col + 1].rgbtRed;
                    aGreen += blur[row - 1][col + 1].rgbtGreen;
                    aBlue += blur[row - 1][col + 1].rgbtBlue;
                    count++;
                }
            }
            //Same
            if (row >= 0)
            {
                //Same-left
                if (col - 1 >= 0)
                {
                    aRed += blur[row][col - 1].rgbtRed;
                    aGreen += blur[row][col - 1].rgbtGreen;
                    aBlue += blur[row][col - 1].rgbtBlue;
                    count++;
                }
                //Same-same
                if (col >= 0)
                {
                    aRed += blur[row][col].rgbtRed;
                    aGreen += blur[row][col].rgbtGreen;
                    aBlue += blur[row][col].rgbtBlue;
                    count++;
                }
                //Same-right
                if (col + 1 <= width - 1)
                {
                    aRed += blur[row][col + 1].rgbtRed;
                    aGreen += blur[row][col + 1].rgbtGreen;
                    aBlue += blur[row][col + 1].rgbtBlue;
                    count++;
                }

            }
            //Downside
            if (row + 1 <= height - 1)
            {
                //Downside-left
                if (col - 1 >= 0)
                {
                    aRed += blur[row + 1][col - 1].rgbtRed;
                    aGreen += blur[row + 1][col - 1].rgbtGreen;
                    aBlue += blur[row + 1][col - 1].rgbtBlue;
                    count++;
                }
                //Downside-same
                if (col >= 0)
                {
                    aRed += blur[row + 1][col].rgbtRed;
                    aGreen += blur[row + 1][col].rgbtGreen;
                    aBlue += blur[row + 1][col].rgbtBlue;
                    count++;
                }
                //Downside-right
                if (col + 1 <= width - 1)
                {
                    aRed += blur[row + 1][col + 1].rgbtRed;
                    aGreen += blur[row + 1][col + 1].rgbtGreen;
                    aBlue += blur[row + 1][col + 1].rgbtBlue;
                    count++;
                }
            }

            // Copy blur pixels in main image
            image[row][col].rgbtRed = round(aRed / count);
            image[row][col].rgbtGreen = round(aGreen / count);
            image[row][col].rgbtBlue = round(aBlue / count);
        }
    }
    return;
}