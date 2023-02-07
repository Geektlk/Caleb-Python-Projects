name = input('What is your name ?: ')
age = input('How od are you ?: ')
job = input('Where do u work ?: ')
name_of_university = input('Which university are you going to ?: ')
name_of_state = input('What is the name of the state u were born in ?: ')
religion = input('What is your religion ?: ')
passion = input('What are is your aspiration ?: ')
hobbies_1 = input('What are your hobbies 1 ?: ')
hobbies_2 = input('What are your hobbies 2 ?: ')
hobbies_3 = input('What are your hobbies 3 ?: ')

madlib = f'''Hi my name is {name}, I am {age} yrs old and I work at a {job} and I am an undergraduate of {name_of_university} university.
I was born in {name_of_state} state and I am a {religion}. I have to dream to be a {passion} and am willing to sacifice anything for it,
also my hobbies are: {hobbies_1}, {hobbies_2} and {hobbies_3} and sometimes I'm just want to kickback and relax, despite the stress I'll still press.'''

print(madlib)