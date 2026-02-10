import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from image_processing import jigsaw

INPUT_FOLDER = "input"     
OUTPUT_FOLDER = "output"   
GRID_SIZE = 3              


def test_input_folder_exists():
    assert os.path.exists(INPUT_FOLDER), f"Input folder '{INPUT_FOLDER}' is missing"


def test_images_are_processed():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    processed_any = False
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            processed_any = True
            img_path = os.path.join(INPUT_FOLDER, file)
            success = jigsaw.create_jigsaw(img_path, GRID_SIZE, OUTPUT_FOLDER)
            assert success is True, f"Processing failed for {file}"

    assert processed_any, "No images found in input folder"


def test_output_files_created():
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            name = os.path.splitext(file)[0]
            output_file = os.path.join(OUTPUT_FOLDER, f"{name}_jigsaw.png")
            assert os.path.exists(output_file), f"Output file not created: {output_file}"


def test_invalid_image_path():
    result = jigsaw.create_jigsaw("nonexistent_image.png", GRID_SIZE, OUTPUT_FOLDER)
    assert result is None