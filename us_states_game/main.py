import turtle
import map
import map_data
import pandas


def save_leftover_states(all_states: list, correct_guesses: list):
    leftover_states = set(all_states).difference(set(correct_guesses))
    pandas.DataFrame({"state": list(leftover_states)}).to_csv("leftover_states.csv")


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=725, height=491)
    screen.bgpic("blank_states_img.gif")
    game_map = map.Map()
    game_map_data = map_data.MapData()
    states_count = game_map_data.get_count()
    correct_guesses = []
    score = 0

    while len(correct_guesses) < states_count:
        answer = screen.textinput(title=f"{score}/{states_count} States Correct",
                                  prompt="What's another state's name?").title()

        if "Exit" == answer:
            save_leftover_states(game_map_data.get_states(), correct_guesses)
            break

        coordinates = game_map_data.get_coordinates(answer)

        if coordinates:
            game_map.draw_text(text=answer, coordinates=coordinates)

            if answer not in correct_guesses:
                correct_guesses.append(answer)

            score += 1


main()
