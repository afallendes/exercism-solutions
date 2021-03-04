def convert(number:int):
    raindrop_sounds = ''
    if number % 3 == 0:
        raindrop_sounds += 'Pling'
    if number % 5 == 0:
        raindrop_sounds += 'Plang'
    if number % 7 == 0:
        raindrop_sounds += 'Plong'
    return raindrop_sounds or str(number)
