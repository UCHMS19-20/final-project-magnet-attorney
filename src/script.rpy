# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Dan",image="protag")
define l = Character("Larry", image = "larry")
define unknown = Character("???")
define lop_teacher = Character("LOP Teacher", image = "lop_teacher")

# The game starts here.

init:

    # Resize all necessary images
    image opening_classroom = im.Scale("opening_classroom.jpg", 1280, 720)
    image protag neutral = im.Scale("protag neutral.jpg", 400, 520)
    image protag angry = im.Scale("protag angry.jpg", 400, 520)
    image larry neutral = im.Scale("larry neutral.jpg", 400, 520)

    # rename audio files

    # CHANGE THESE FILES WHEN YOU ADD MUSIC

    define audio.panic = "audio/God_Fury.mp3"
    define audio.l_theme = "audio/Put_On_Your_Dancing_pants.mp3"
    define audio.muffled_rock = "audio/Manhattan.mp3"

label start:

    # Draws a background.

    scene opening_classroom

    # Shows a character sprite.

    show protag neutral

    # These display lines of dialogue.
    # "p" is used here because I want the protagonist to speak
    # (p is defined as the character named "Dan" on line 4)

    p "{i}You know, maybe getting a LOP wasn’t so bad after all.{/i}"
    p "{i}I get time to study for upcoming tests and catch up on homework...{/i}"
    p "{i}And best of all, I finally get some peace and quiet!{/i}"
    p "{i}But where to start? I have notes due in history, a test in Calculus,
        a group project in English…{/i}"
    p "{i}Maybe I’ll start by organizing all my homework...{/i}"


    show protag neutral
    with fade

    p "{i}Okay, everything is in order. It’s time to study! I think I’ll start
        with…{/i}"

    menu:

        "History Notes":
            jump history_homework

        "Calculus Test":
            jump calculus_homework

        "English Project":
            jump english_homework



label history_homework:
    # ren'py require "$"s before python code that isn't in ren'py by default
    # the $ is used here to tell ren'py to use python to declare a variable
    $ homework = "history"

    p "{i}History will probably take the most time. I’ll start with this.{/i}"

    scene desk history

    jump tired



label calculus_homework:
    $ homework = "calculus"

    p "{i}I should probably brush up on my derivative and integrals before the
        test tomorrow.{/i}"

    scene desk calculus

    jump tired



label english_homework:
    $ homework = "english"
    p "{i}I don't want my group members to think I'm slacking off. I'll
        contribute to the project first.{/i}"

    scene desk english

    jump tired



label tired:

    p "{i}Phew, I’ve organized everything and it’s time to start!{/i}"
    p "{i}I wonder what time it is…{/i}"


    scene clock 1100

    p "{i}Wow, it’s only been 10 minutes! I have 50 minutes of productivity
        remaining.{/i}"
    p "{i}Now that I think about it, I am kinda tired…{/i}"
    p "{i}Maybe I’ll take a 5 minute nap before I start.{/i}"


    scene black
    with fade

    p "*sleepy sleepy*"
    unknown "*muffled noises*"
    p "*sleepy sleepy*"
    unknown "Bro! Wake up!"


    # Plays music
    play music panic

    if homework == "history":
        scene desk history
        with fade

    elif homework == "calculus":
        scene desk calculus
        with fade

    elif homework == "english":
        scene desk english
        with fade

    p scared "AAH! I’m sorry, I must have napped too long! I need to run to
        Physics!"

    scene opening_classroom

    p "Oh my god. What time is it?"


    scene clock 1115

    pause


    scene opening_classroom
    show protag angry

    p "..."

    hide protag angry
    show larry neutral

    l "..."

    stop music

    hide larry neutral
    show protag angry

    p "..."
    p "it’s only 11:15…"
    l "Yup."
    p "WHY DID YOU WAKE ME UP?"

    play music l_theme

    l "Because of the trial, bro! Remember?"
    l " You said we would figure it out today, at 11:10…"
    p "Oh, sorry, I completely forgot."
    l "Bro, I was looking all over for you. If you’re gonna cancel a meeting
        for nap time, could you at least let me know in advance?"
    p "Sorry, sorry."

    scene lop_teacher_desk
    show lop_teacher
    play music muffled_rock
    pause

    p "Excuse me, can I leave early? I have a meeting to go to. I can make this
        up next week."
    lop_teacher "..."
    lop_teacher "..."
    p "{i}She seems busy...{/i}"
    p "{i}She probably won't care if i just leave{/i}."


    jump courtroom



label courtroom:
    scene courtroom
    jump end



label end:

    # This ends the game.
    return
