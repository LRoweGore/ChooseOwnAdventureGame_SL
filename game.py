import streamlit as st
import time
import os
import sys

# Helper to get resource path (works with local files and PyInstaller)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Helper to play audio (Streamlit can embed audio widgets)
def play_sound(sound_relative_path):
    sound_path = resource_path(sound_relative_path)
    if os.path.exists(sound_path):
        try:
            with open(sound_path, "rb") as f:
                st.audio(f.read())
        except Exception as e:
            st.write(f"(Could not play sound: {e})")
    else:
        st.write("(Sound not found)")

# Init session state
if "scene" not in st.session_state:
    st.session_state.scene = "start"

if "history" not in st.session_state:
    st.session_state.history = []

# Navigation helper
def go(next_scene, note=None):
    st.session_state.history.append((st.session_state.scene, note))
    st.session_state.scene = next_scene

# Restart helper
def restart():
    st.session_state.scene = "start"
    st.session_state.history = []

# Small utility to show paragraphs with optional delays (non-blocking)
def write_paragraphs(paragraphs):
    for p in paragraphs:
        st.write(p)

# App UI
st.title("Lewis' Mini Text Adventure Game")

# Scene: start
if st.session_state.scene == "start":
    st.header("Welcome")
    st.write("Welcome to Lewis' Mini Text Adventure Game!")
    st.write("Would you like to start a new adventure?")
    col1, col2 = st.columns(2)
    if col1.button("Start New Adventure"):
        time.sleep(0.2)
        go("wake_up")
    if col2.button("Exit"):
        st.write("Journey another day then...")
        if st.button("Close / Restart"):
            restart()

# Scene: wake_up -> crossroads
elif st.session_state.scene == "wake_up":
    st.write("You awake in your car, and as you prepare to start the car up and leave, you peer over at your fuel, it's empty... not an ideal situation. With no idea where you are, you decide to leave the car and see a dirt path ahead of you, you follow it.")
    if st.button("Continue"):
        go("crossroads")

# Scene: crossroads
elif st.session_state.scene == "crossroads":
    st.header("Crossroads")
    st.write("As you continue following the path, you approach a crossroads, do you go left or right?")
    col1, col2 = st.columns(2)
    if col1.button("Left"):
        go("left_path")
    if col2.button("Right"):
        go("right_path")

# Left path branch (lake -> island -> chalice or path_to_house)
elif st.session_state.scene == "left_path":
    st.write("You take the path left, making your way past what looks like a small lake, with an island in the middle. There seems to be something there.")
    if st.button("Check the Island"):
        go("island_chalice")
    if st.button("Ignore the Island"):
        go("path_to_house")

elif st.session_state.scene == "island_chalice":
    st.write("You walk into the lake, trudging forward through the waist-high mud and water. As you reach the small island, you spot what looks like a chalice placed on a small altar.")
    if st.button("Pick up the Chalice"):
        go("chalice_pick")
    if st.button("Leave it"):
        go("path_to_house")

elif st.session_state.scene == "chalice_pick":
    st.write("You pick the chalice up. It smells sweet like roses. Do you drink from the chalice?")
    col1, col2 = st.columns(2)
    if col1.button("Yes, drink it"):
        st.session_state.scene = "dead_from_chalice"
    if st.session_state.scene == "dead_from_chalice":
        st.write("Unable to resist the sweet smell, you drink from the chalice, gulping down every last drop. As the last drop rolls down your throat, you take a moment, smacking your lips savouring the last remnants on your taste buds.")
        st.write("Suddenly, you drop the chalice and it clatters as you drop it to the ground.")
        st.write("Your eyes begin to burn, and you struggle to catch your breath as your airways gradually close, you begin to panic, and start clawing at your throat.")
        st.write("You've been poisoned. You collapse to the floor in a heap, the cold, wet ground a momentary relief from the pain coursing through your body.")
        st.write ("You are Dead")
        play_sound("sounds/roc.wav")
        if st.button("R to Restart"):
            restart()
    if col2.button("No, don't drink"):
        st.session_state.scene = "path_to_house"
        st.write("You resist the urge and head back through the cold, muddy water.")
    


# Right path branch (shed)
elif st.session_state.scene == "right_path":
    st.write("As you walk along the right side of the path, you notice a small shed, well built, a little aged but standing strong.")
    if st.button("Go inside the cabin"):
        go("cabin_inside")
    if st.button("Ignore the cabin"):
        go("path_to_house")

elif st.session_state.scene == "cabin_inside":
    st.write("You go inside the wooden cabin, and inside you notice a number of old tools littered about. On a workbench, opposite the exit, you notice a chest on the table.")
    if st.button("Open the chest"):
        st.write("Before you can react, it lunges at you. You've been paralysed and the mimic attacks. You are dead.")
        play_sound("sounds/ds_go.wav")
        if st.button("R to Restart"):
            restart()
    if st.button("Don't open the chest"):
        st.write("You leave the cabin.")
        if st.button("Continue"):
            go("path_to_house")

# Path to house
elif st.session_state.scene == "path_to_house":
    st.write("You continue walking down the path, it's still quite foggy but starting to appear within your view is a house. You approach the gate.")
    st.write("The house looks like something straight out of a horror movie... Do you enter the house?")
    col1, col2 = st.columns(2)
    if col1.button("Yes, enter"):
        go("inside_house")
    if col2.button("No, don't enter"):
        st.write("A gas fills the air and you decide to go in anyway...")
        if st.button("Continue"):
            go("inside_house")

elif st.session_state.scene == "inside_house":
    st.write("You try the front door of the house, it's open. A panic overcomes you and then the front door slams shut. You notice two doors: one with a red ruby, one with a blue sapphire.")
    if st.button("Open Blue Door"):
        go("blue_path")
    if st.button("Open Red Door"):
        go("red_path")

# Blue path
elif st.session_state.scene == "blue_path":
    st.write("You push the door open, and you're hit with a blast of light, and an aroma of meat, roasted vegetables and mead! A large banquet appears.")
    if st.button("Eat at the banquet"):
        st.write("You eat and feel satisfied. You spot a large covered painting. Do you unveil it?")
        if st.button("Unveil the painting"):
            play_sound("sounds/lotr.wav")
            st.write("A melody plays and gives you hope. You leave towards the Red Ruby Door.")
            if st.button("Continue to Red Door"):
                go("red_path")
        if st.button("Don't unveil"):
            st.write("You decide not to unveil it and head to the Red Ruby Door.")
            if st.button("Continue"):
                go("red_path")
    else:
        if st.button("Ignore the food"):
            go("red_path")

# Red path
elif st.session_state.scene == "red_path":
    st.write("You approach the Red Ruby Door and enter a museum-like room with displays. Inside is a doll in a cabinet. Do you open it?")
    if st.button("Open the cabinet"):
        st.write("You pick up the doll, feel a presence, the doll disappears, cabinet starts to close, you see a shadow... Two claps and you are dead.")
        play_sound("sounds/clap.wav")
        play_sound("sounds/myneck.wav")
        if st.button("Restart"):
            restart()
    if st.button("Close the cabinet"):
        st.write("You close the cabinet, proceed through the museum and head down into a basement where you spot a desk and a painting.")
        if st.button("Check the Painting"):
            st.write("A painting features a grotesque scene — nothing else here so you approach the desk.")
            if st.button("Go to Desk"):
                go("desk")
        if st.button("Check the Desk"):
            go("desk")

# Desk
elif st.session_state.scene == "desk":
    st.write("As you walk over to the desk and examine it, you sift through the notes on the table — research notes on occult topics. Something falls and you spot a key by your foot. You open a drawer and find a book that has a face.")
    if st.button("Interact with the Book"):
        go("book_interaction")

# Book interaction
elif st.session_state.scene == "book_interaction":
    st.write("You stare at the book. You can open it from the Front, Back or Middle.")
    c1, c2, c3 = st.columns(3)
    if c1.button("Front"):
        go("front_book")
    if c2.button("Back"):
        go("back_book")
    if c3.button("Middle"):
        go("middle_book")

elif st.session_state.scene == "front_book":
    st.write("You open the book from the front. It's mostly unintelligible. Do you check the back or the middle?")
    if st.button("Middle"):
        play_sound("sounds/pageflip.wav")
        go("middle_book")
    if st.button("Back"):
        play_sound("sounds/pageflip.wav")
        go("back_book")

elif st.session_state.scene == "back_book":
    st.write("You open the book from the back. There are numerous symbols including a Leviathan Cross and the word 'Daemonium'.")
    if st.button("Front"):
        play_sound("sounds/pageflip.wav")
        go("front_book")
    if st.button("Middle"):
        play_sound("sounds/pageflip.wav")
        go("middle_book")

elif st.session_state.scene == "middle_book":
    play_sound("sounds/pageflip.wav")
    st.write("You turn to the centre of the book and read about a great evil sealed away. You read aloud 'Daemonium Sigillum' and the basement door bursts open. A great evil launches toward you. Suddenly you wake up — it was a dream.")
    st.write("You look to your left, your partner asks if you're okay... As you close your eyes again, the story ends.")
    play_sound("sounds/gameover.wav")
    st.write("---\nThe End\n---\nThank you for playing and your help with this mini-project!")
    if st.button("Restart"):
        restart()

# Fallback
else:
    st.write("restarting.")
    if st.button("Restart"):
        restart()
