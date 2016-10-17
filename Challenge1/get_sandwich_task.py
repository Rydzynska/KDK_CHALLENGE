def get_sandwich(text):
    """
    Search for a string between two other words.
    bread: string that should be present twice
    inside: string that is between two bread instances
    """
    bread = 'chleb'
    is_bread = False
    inside = ''

    if bread in text:
        is_bread = True

    if is_bread:
        first_bread = text.find(bread)
        last_bread = text.rfind(bread)
        inside = text[first_bread + len(bread) : last_bread]

    return inside
