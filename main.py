from clothing_items import clothing_items
from recommender import recommend_combination, print_outfit, random_mode

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['yes', 'no']:
            return answer
        print("Invalid input. Please enter 'yes' or 'no'.")

def get_user_input():
    print("🔍 Welcome to FitFinder!")
    mode = ask_yes_no("Do you want to use random mode? (yes/no): ")
    is_raining = ask_yes_no("Is it raining today? (yes/no): ")
    if mode == 'yes':
        return 'random', None, None, None, is_raining

    while True:
        try:
            temp = int(input("Enter today's temperature (°C): "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    valid_styles = ['casual', 'sporty', 'minimal', 'cute', 'business formal', 'smart casual']
    print(f"Available styles: {', '.join(valid_styles)}")
    while True:
        style = input("Enter your preferred style (choose from above): ").strip().lower()
        if style in valid_styles:
            break
        print("❌ Invalid style. Please choose from the list above.")

    while True:
        tone = input("Do you want to wear dark or light today? ").strip().lower()
        if tone in ['dark', 'light']:
            break
        print("❌ Invalid input. Please enter 'dark' or 'light'.")

    has_specific = ask_yes_no("Do you want to specify a color? (yes/no): ")
    if has_specific == 'yes':
        color = input("Enter a specific color (e.g. white, navy): ").strip().lower()
    else:
        import random
        light_colors = ['white', 'beige', 'cream', 'light grey', 'sky blue']
        dark_colors = ['black', 'navy', 'charcoal', 'dark brown', 'deep green']
        color = random.choice(light_colors) if tone == 'light' else random.choice(dark_colors)

    return 'custom', temp, style, color, is_raining


def main():
    mode, temp, style, color, is_raining = get_user_input()

    if mode == 'random':
        outfit = random_mode(clothing_items)
    else:
        outfit = recommend_combination(clothing_items, temp, style, color)
        if outfit is None:
            print("❌ Sorry, no outfit matches your preferences.")
            return

    print_outfit(outfit)

    from recommender import filter_by_category, re_pick
    if mode == 'random':
        top = [i for i in clothing_items if i.category == 'top']
        bottom = [i for i in clothing_items if i.category == 'bottom']
        shoes = [i for i in clothing_items if i.category == 'shoes']
    else:
        top = filter_by_category('top', clothing_items, temp, style, color)
        bottom = [i for i in clothing_items if i.category == 'bottom' and temp >= i.temp_range[0] and temp <= i.temp_range[1] and style in i.styles]
        shoes = [i for i in clothing_items if i.category == 'shoes' and temp >= i.temp_range[0] and temp <= i.temp_range[1] and style in i.styles]

    while True:
        again = input("Do you want a different combination? (yes/no): ").strip().lower()
        if again != 'yes':
            if is_raining == 'yes':
                print("☔️ Please remember to bring an umbrella and hope you have a nice day!")
            else:
                print("🌞 Hope you have a nice day!")
            break
        new_outfit = re_pick({'top': top, 'bottom': bottom, 'shoes': shoes})
        print_outfit(new_outfit)

if __name__ == '__main__':
    main()
