import random_word_generator
def print_user_string(current_word_state,attempts_remaining):
    print('current user string state')
    for i in current_word_state:
        print(i,end=' ')
    print('')
    print('Attempts remaining {}'.format(attempts_remaining))

def game_play():
    selected_word=random_word_generator.pick_random_word()
    current_word_state=''
    for i in range(0,len(selected_word)):
        if(selected_word[i]=='a' or selected_word[i]=='e' or selected_word[i]=='o' or selected_word[i]=='i' or selected_word[i]=='u'):
            current_word_state+=selected_word[i]
        else:
            current_word_state+='_'

    attempts_remaining=5
    print_user_string(current_word_state,attempts_remaining)

game_play()