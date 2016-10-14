def get_sandwich(text):
    """
    Search for a string between two other words.
    bread: string that should be present twice
    inside: string that is between two bread instances
    """
    bread = 'chleb'
    is_bread = False
    inside = ''

    if text.count(bread) == 2:
        is_bread = True

    if is_bread:
        first_bread = text.index(bread)
        second_part = text[first_bread + len(bread) :]
        second_bread = second_part.index(bread)
        inside = second_part[: second_bread]

    return inside
