import random

def filter_by_category(category, items, temp, style, color=None):
    return [
        item for item in items
        if item.category == category and item.matches(temp, style, color)
    ]

def recommend_combination(items, temp, style, color=None):
    top_choices = [i for i in items if i.category == 'top' and i.matches(temp, style, color)]
    bottom_choices = [i for i in items if i.category == 'bottom' and temp >= i.temp_range[0] and temp <= i.temp_range[1] and style in i.styles]
    shoes_choices = [i for i in items if i.category == 'shoes' and temp >= i.temp_range[0] and temp <= i.temp_range[1] and style in i.styles]
    if top_choices and bottom_choices and shoes_choices:
        return {
            'top': random.choice(top_choices),
            'bottom': random.choice(bottom_choices),
            'shoes': random.choice(shoes_choices)
        }
    return None

def print_outfit(outfit):
    print("\n🌟 Your Recommended Outfit:")
    emoji_map = {"top": "👕", "bottom": "👖", "shoes": "👟"}
    for part in ["top", "bottom", "shoes"]:
        item = outfit[part]
        print(f"{emoji_map[part]} {part.capitalize()}: {item.name}")
    

def random_mode(items):
    top_choices = [i for i in items if i.category == 'top']
    bottom_choices = [i for i in items if i.category == 'bottom']
    shoes_choices = [i for i in items if i.category == 'shoes']
    if top_choices and bottom_choices and shoes_choices:
        return {
            'top': random.choice(top_choices),
            'bottom': random.choice(bottom_choices),
            'shoes': random.choice(shoes_choices)
        }
    return None

def re_pick(candidates):
    return {
        'top': random.choice(candidates['top']) if candidates['top'] else None,
        'bottom': random.choice(candidates['bottom']) if candidates['bottom'] else None,
        'shoes': random.choice(candidates['shoes']) if candidates['shoes'] else None,
    }

