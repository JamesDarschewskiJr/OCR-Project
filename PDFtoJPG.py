import os
from pdf2image import convert_from_path

def convert_pdfs_in_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            images = convert_from_path(pdf_path)
            
            # Save each page as a JPG file
            for i, image in enumerate(images):
                output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_page_{i + 1}.jpg')
                image.save(output_path, 'JPEG')
            print(f'Converted {filename} to JPG.')

# Define the input and output folders
input_folder = '/home/darshewskijadmin@consilio.com/ExperimentalLLMs/asdf'
output_folder = '/home/darshewskijadmin@consilio.com/ExperimentalLLMs/LowResolutionMobyDickImages/FullMobyDick'

# Convert all PDFs in the input folder
convert_pdfs_in_folder(input_folder, output_folder)

print("All PDF files have been converted to JPG.")