import re
class regexSearch:
    def create_folder_name(text):
        pattern = r'\b[A-Za-z0-9]+_[A-Za-z0-9]*' 
        match = re.search(pattern, text)
        return match.group()