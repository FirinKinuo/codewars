def cakes(recipe, available):
    return min({available[k] // recipe[k] for k in recipe if k in available}) if all(
        map(lambda x: x in available, recipe)) else 0
