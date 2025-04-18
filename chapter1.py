# 1. Write a program to print Twinkle twinkle little star poem in python.
# problrm 1 start

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

#problem 1 end

# 2. Use REPL and print the table of 5 using it.
#problem 2 start

for i in range(11) :print("5 x {} = {}".format(i,5*i))

#problem 2 end

# 3. Install an external module and use it to perform an operation of your interest.
#problem 3 start

import pyttsx3
engine = pyttsx3.init()
engine.say("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.""")
engine.runAndWait()

#problem 3 end

# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.
#problem 4 start

import os
dir_location = input("Enter Directory path : ")
contnets = os.listdir(dir_location)
for i in contnets:
    print(i)

#problem 4 end

# 5. Label the program written in problem 4 with comments. 
#problem 5 start
#writing coments in above program
#problem 5 end

