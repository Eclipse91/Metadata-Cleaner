import os
import json
import shutil
from datetime import datetime
import base64
from PIL import Image
from mutagen import File as MutagenFile
from pymediainfo import MediaInfo
from PyPDF2 import PdfReader, PdfWriter

def extract_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img.info
        return metadata
    except Exception as e:
        print(f"Failed to extract image metadata: {e}")
        return {}

def extract_audio_metadata(audio_path):
    try:
        audio = MutagenFile(audio_path)
        metadata = {k: str(v) for k, v in audio.tags.items()} if audio.tags else {}
        return metadata
    except Exception as e:
        print(f"Failed to extract audio metadata: {e}")
        return {}

def extract_video_metadata(video_path):
    try:
        media_info = MediaInfo.parse(video_path)
        metadata = media_info.to_data()
        return metadata
    except Exception as e:
        print(f"Failed to extract video metadata: {e}")
        return {}

def extract_pdf_metadata(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        metadata = reader.metadata
        return metadata
    except Exception as e:
        print(f"Failed to extract PDF metadata: {e}")
        return {}

def save_metadata_to_file(metadata, metadata_file_path):
    try:
        with open(metadata_file_path, 'w') as f:
            json.dump(metadata, f, indent=4)
    except Exception as e:
        try:
            # Encode the bytes objects
            metadata = encode_bytes_in_dict(metadata)
        except:
            print(f"Failed to save metadata to file: {e}")

def encode_bytes_in_dict(obj):
    if isinstance(obj, dict):
        return {k: encode_bytes_in_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [encode_bytes_in_dict(v) for v in obj]
    elif isinstance(obj, bytes):
        return base64.b64encode(obj).decode('utf-8')
    else:
        return obj

def remove_image_metadata(image_path, output_image_path):
    try:
        with Image.open(image_path) as img:
            img_data = list(img.getdata())
            img_without_metadata = Image.new(img.mode, img.size)
            img_without_metadata.putdata(img_data)
            img_without_metadata.save(output_image_path)
    except Exception as e:
        print(f"Failed to remove image metadata: {e}")

def remove_audio_metadata(audio_path):
    try:
        audio = MutagenFile(audio_path)
        audio.delete()
        #audio.save(output_audio_path)
    except Exception as e:
        print(f"Failed to remove audio metadata: {e}")

def remove_video_metadata(video_path, output_video_path):
    try:
        shutil.copy(video_path, output_video_path)  # Placeholder for video metadata removal
    except Exception as e:
        print(f"Failed to remove video metadata: {e}")

def remove_pdf_metadata(pdf_path, output_pdf_path):
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_pdf_path, 'wb') as f:
            writer.write(f)
    except Exception as e:
        print(f"Failed to remove PDF metadata: {e}")

def copy_file(src_path, dst_path):
    """
    Copies a file from src_path to dst_path.

    Parameters:
    src_path (str): The path of the source file.
    dst_path (str): The path of the destination file.
    """
    try:
        shutil.copy(src_path, dst_path)
        # print(f"File copied from {src_path} to {dst_path}")
    except FileNotFoundError:
        print(f"File not found: {src_path}")
    except PermissionError:
        print(f"Permission denied: {dst_path}")
    except Exception as e:
        print(f"Error occurred while copying file: {e}")

def results_configurator(file_name):
    '''
    Configure the folder where to put all the resulting files.
    '''
    results_directory = './results/'
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y%m%d_%H%M%S')
    folder_name = results_directory + formatted_datetime + '_' + file_name.replace('.','_')
    os.makedirs(folder_name, exist_ok=True)

    return folder_name
    
def list_files_in_current_folder():
    """
    Lists all files in the current directory.

    Returns:
    list: A list of filenames in the current directory.
    """
    try:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        return files
    except Exception as e:
        print(f"Error occurred while listing files: {e}")
        return []

def process_file(file_path, folder_name):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    file_extension = os.path.splitext(file_path)[1].lower()
    base_name = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(base_name)
    new_file_path = folder_name + '/' + file_path
    metadata_file_path = f"{new_file_path}_metadata.json"
    output_file_path = f"{new_file_path}_no_metadata{file_extension}"
    
    try:
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            metadata = extract_image_metadata(file_path)
            save_metadata_to_file(metadata, metadata_file_path)
            remove_image_metadata(file_path, output_file_path)
        elif file_extension in ['.mp3', '.flac', '.wav', '.ogg', '.m4a']:
            copy_file(file_path, folder_name)
            metadata = extract_audio_metadata(new_file_path)
            save_metadata_to_file(metadata, metadata_file_path)
            remove_audio_metadata(new_file_path)
        elif file_extension in ['.mp4', '.mkv', '.avi', '.mov']:
            metadata = extract_video_metadata(file_path)
            save_metadata_to_file(metadata, metadata_file_path)
            remove_video_metadata(file_path, output_file_path)
        elif file_extension == '.pdf':
            metadata = extract_pdf_metadata(file_path)
            save_metadata_to_file(metadata, metadata_file_path)
            remove_pdf_metadata(file_path, output_file_path)
        else:
            print(f"Unsupported file type: {file_extension}")
            return
        
        print(f"Metadata saved to: {metadata_file_path}")
        print(f"File without metadata saved to: {output_file_path}\n")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def main():
    files = list_files_in_current_folder()
    for file in files:
        if file in ['main.py', '.gitignore', 'requirements.txt', 'LICENSE', 'README.md']:
            continue
        folder_name = results_configurator(file)

        try:
            process_file(file, folder_name)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

