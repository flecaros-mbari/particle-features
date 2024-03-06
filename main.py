import cv2
import glob
import numpy as np
import click

# Define the Click command and options outside the __main__ block
@click.command()
@click.option('--area', default=False, help='Compute the area of the particles in the images.')
@click.option('--contours', default=False, help='Define the contours in the particles of the image.')

def process_images(area, contours):
    # Code to process images goes here
    print("Trying")

if __name__ == '__main__':
    # Call the command function when the script is executed
    process_images()
