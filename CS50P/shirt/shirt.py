import sys
from PIL import Image, ImageOps


def main():
    # Check if any issue with command-line argument
    check()

    shirtImg = Image.open("shirt.png")

    try:
        with Image.open(sys.argv[1]) as image:
            # Crop/Resize the original image
            image = ImageOps.fit(image, shirtImg.size)
            # Paste shirt.png onto original image
            image.paste(shirtImg, shirtImg)
            # Save new image
            image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    inputFile = sys.argv[1].split('.')
    outputFile = sys.argv[2].split('.')

    if inputFile[1] != "jpeg" and inputFile[1] != "jpg" and inputFile[1] != "png":
        sys.exit("Incorrect Format")

    if outputFile[1] != "jpeg" and outputFile[1] != "jpg" and outputFile[1] != "png":
        sys.exit("Incorrect Format")

    if inputFile[1] != outputFile[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
