# TODO: Add docstrings and comments

from Bio import Entrez

# Entrez.api_key = ""  # Add your API Key
Entrez.email = "aniketf@uw.edu"  # Add your email address


def get(operation, db, term):
    handle = None
    record = None
    if operation == "Search":
        handle = Entrez.esearch(db=db, term=term)

    elif operation == "Fetch":
        # Fetch the ids to using esearch and then perform efetch
        # handle = Entrez.efetch(db=db, term=term)
        pass

    if handle:
        record = Entrez.read(handle)
    
    return record
