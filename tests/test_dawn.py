import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from image_processing import dawn

INPUT_FOLDER = "input"     
OUTPUT_FOLDER = "output"   


def test_input_folder_exists():
    assert os.path.exists(INPUT_FOLDER), f"Input folder '{INPUT_FOLDER}' is missing"


def test_images_are_processed():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    processed_any = False
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            processed_any = True
            img_path = os.path.join(INPUT_FOLDER, file)
            success = dawn.apply_dawn_effect(img_path, OUTPUT_FOLDER)
            assert success is True, f"Processing failed for {file}"

    assert processed_any, "No images found in input folder"


def test_output_files_created():
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            name = os.path.splitext(file)[0]
            output_file = os.path.join(OUTPUT_FOLDER, f"{name}_dawn.png")
            assert os.path.exists(output_file), f"Output file not created: {output_file}"


def test_invalid_image_path():
    result = dawn.apply_dawn_effect("nonexistent_image.png", OUTPUT_FOLDER)
    assert result is False