def transcribe(text: str) -> str:
    """transcribe a DNA string to RNA
    
    Arguments:
        text {str} -- DNA text string
    
    Returns:
        str -- transcribed RNA string
    """
    transtab = {"A":"A", "C":"C", "G":"G", "T":"U"}

    return "".join(transtab[t] for t in text.upper())