#include <math.h>
#include "helpers.h"

void swap(uint8_t *x, uint8_t *y);
void horizontally(int i, int j, int h, int w, RGBTRIPLE edges[h][w], int *gxR, int *gxG, int *gxB);
void vertically(int i, int j, int h, int w, RGBTRIPLE edges[h][w], int *gyR, int *gyG, int *gyB);

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

            /// Copy blur pixels in main image
            image[row][col].rgbtRed = round(aRed / count);
            image[row][col].rgbtGreen = round(aGreen / count);
            image[row][col].rgbtBlue = round(aBlue / count);
        }

    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Copy 'image' in temporary 2D array 'edges'
    RGBTRIPLE edges[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            edges[row][col] = image[row][col];
        }
    }

    //Take the average value and update the image
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            int gxRed = 0;
            int gxGreen = 0;
            int gxBlue = 0;

            int gyRed = 0;
            int gyGreen = 0;
            int gyBlue = 0;

            //Checking changes horizontally
            horizontally(row, col, height, width, edges, &gxRed, &gxGreen, &gxBlue);
            //Checking changes vertically
            vertically(row, col, height, width, edges, &gyRed, &gyGreen, &gyBlue);

            int GxR = round(sqrt(gxRed * gxRed + gyRed * gyRed));
            int GxG = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int GxB = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));

            //New value of pixel
            image[row][col].rgbtRed = (GxR > 255) ? 255 : GxR;
            image[row][col].rgbtGreen = (GxG > 255) ? 255 : GxG;
            image[row][col].rgbtBlue = (GxB > 255) ? 255 : GxB;
        }
    }
    return;
}

void horizontally(int i, int j, int h, int w, RGBTRIPLE edges[h][w], int *gxR, int *gxG, int *gxB)
{
    //Upside
    if (i - 1 >= 0)
    {
        //Upside-left
        if (j - 1 >= 0)
        {
            *gxR -= edges[i - 1][j - 1].rgbtRed;
            *gxG -= edges[i - 1][j - 1].rgbtGreen;
            *gxB -= edges[i - 1][j - 1].rgbtBlue;
        }

        //Upside-right
        if (j + 1 <= w - 1)
        {
            *gxR += edges[i - 1][j + 1].rgbtRed;
            *gxG += edges[i - 1][j + 1].rgbtGreen;
            *gxB += edges[i - 1][j + 1].rgbtBlue;
        }
    }

    //Same
    if (i >= 0)
    {
        //Same-left
        if (j - 1 >= 0)
        {
            *gxR -= 2 * edges[i][j - 1].rgbtRed;
            *gxG -= 2 * edges[i][j - 1].rgbtGreen;
            *gxB -= 2 * edges[i][j - 1].rgbtBlue;
        }

        //Same-right
        if (j + 1 <= w - 1)
        {
            *gxR += 2 * edges[i][j + 1].rgbtRed;
            *gxG += 2 * edges[i][j + 1].rgbtGreen;
            *gxB += 2 * edges[i][j + 1].rgbtBlue;
        }

    }
    //Downside
    if (i + 1 <= h - 1)
    {
        //Downside-left
        if (j - 1 >= 0)
        {
            *gxR -= edges[i + 1][j - 1].rgbtRed;
            *gxG -= edges[i + 1][j - 1].rgbtGreen;
            *gxB -= edges[i + 1][j - 1].rgbtBlue;
        }

        //Downside-right
        if (j + 1 <= w - 1)
        {
            *gxR += edges[i + 1][j + 1].rgbtRed;
            *gxG += edges[i + 1][j + 1].rgbtGreen;
            *gxB += edges[i + 1][j + 1].rgbtBlue;
        }
    }
    return;
}

void vertically(int i, int j, int h, int w, RGBTRIPLE edges[h][w], int *gyR, int *gyG, int *gyB)
{
    //Upside
    if (i - 1 >= 0)
    {
        //Upside-left
        if (j - 1 >= 0)
        {
            *gyR -= edges[i - 1][j - 1].rgbtRed;
            *gyG -= edges[i - 1][j - 1].rgbtGreen;
            *gyB -= edges[i - 1][j - 1].rgbtBlue;
        }

        if (j >= 0)
        {
            *gyR -= 2 * edges[i - 1][j].rgbtRed;
            *gyG -= 2 * edges[i - 1][j].rgbtGreen;
            *gyB -= 2 * edges[i - 1][j].rgbtBlue;
        }

        //Upside-right
        if (j + 1 <= w - 1)
        {
            *gyR -= edges[i - 1][j + 1].rgbtRed;
            *gyG -= edges[i - 1][j + 1].rgbtGreen;
            *gyB -= edges[i - 1][j + 1].rgbtBlue;
        }
    }

    //Downside
    if (i + 1 <= h - 1)
    {
        //Downside-left
        if (j - 1 >= 0)
        {
            *gyR += edges[i + 1][j - 1].rgbtRed;
            *gyG += edges[i + 1][j - 1].rgbtGreen;
            *gyB += edges[i + 1][j - 1].rgbtBlue;
        }

        if (j >= 0)
        {
            *gyR += 2 * edges[i + 1][j].rgbtRed;
            *gyG += 2 * edges[i + 1][j].rgbtGreen;
            *gyB += 2 * edges[i + 1][j].rgbtBlue;
        }

        //Downside-right
        if (j + 1 <= w - 1)
        {
            *gyR += edges[i + 1][j + 1].rgbtRed;
            *gyG += edges[i + 1][j + 1].rgbtGreen;
            *gyB += edges[i + 1][j + 1].rgbtBlue;
        }
    }
    return;
}