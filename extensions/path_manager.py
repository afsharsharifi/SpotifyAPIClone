import os
import uuid


def get_extension_file(filename):
    return os.path.splitext(filename)[-1]


def create_profile_image_path(instance, filename):
    extension = get_extension_file(filename)
    num_id = uuid.uuid1()
    return f"profiles/{num_id}{extension}"


def create_songs_file_path(instance, filename):
    extension = get_extension_file(filename)
    num_id = uuid.uuid1()
    return f"songs/{num_id}{extension}"
