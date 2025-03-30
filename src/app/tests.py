import mimetypes

def check_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    
    if mime_type:
        if mime_type.startswith('image'):
            return 'image'
        elif mime_type.startswith('video'):
            return 'video'
        else:
            return 'unknown'
    else:
        return 'unknown'

# Exemple d'utilisation
file_path = "test/fichier.jpg"
file_type = check_file_type(file_path)
print(f"Le fichier {file_path} est un(e) {file_type}.")
