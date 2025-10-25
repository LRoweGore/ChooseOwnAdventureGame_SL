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

if st.session_state.scene == "start":
    st.write("Would you like to start a new adventure?")
    
    if st.button("Start New Adventure", on_click=go, args=("wake_up",)):
        st.session_state.history = []
    
    if st.button("No"):
        st.write("Journey another day then...")
        

# Scene: wake_up > crossroads
elif st.session_state.scene == "wake_up":
    st.write("You awake in your car, and as you prepare to start the car up and leave, you peer over at your fuel, it's empty... not an ideal situation. With no clue where you are, you decide to leave the car and see a dirt path ahead of you, you follow it.")
    if st.button("Continue", on_click=go, args=("crossroads",)):
        pass

# Scene: crossroads
elif st.session_state.scene == "crossroads":
    st.header("Crossroads")
    st.write("As you continue following the path, you approach a crossroads, do you go left or right?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Left", on_click=go, args=("left_path",)):
            pass
    with col2:
        if st.button("Right", on_click=go, args=("right_path",)):
            pass

# Left path branch (lake > island > chalice or path_to_house)
elif st.session_state.scene == "left_path":
    st.write("You take the path left, making your way past what looks like a small lake, with an island in the middle. There seems to be something there.")
    col1, col2 = st.columns(2)
    if col1.button("Check the Island", on_click=go, args=("island_chalice",)):
        pass
        
    if col2.button("Ignore the Island", on_click=go, args=("ignore_island",)):
        pass

elif (st.session_state.scene == "ignore_island"):
    st.write ("You decide you don't want to check the island and continue forward on the path.")
    col1, col2 = st.columns(2)
    if col1.button("Continue", on_click=go, args=("path_to_house",)):
        pass
        
    if col2.button("Take the right path", on_click=go, args=("right_path",)):
        pass

elif st.session_state.scene == "island_chalice":
    st.write("You walk into the lake, trudging forward through the waist-high mud and water. As you reach the small island, you spot what looks like a chalice placed on a small altar. You move towards it.")
    col1, col2 = st.columns(2)
    if col1.button("Pick up the Chalice", on_click=go, args=("chalice_pick",)):
        pass
        
    if col2.button("Leave it", on_click=go, args=("chalice_leave",)):
        pass

elif st.session_state.scene == "chalice_pick":
    st.write("You pick the chalice up, as you examine the chalice, it appears to be intricately designed, a crown, a boy, and lions decorate it.")
    st.write("When the light catches it, the chalice glows gold. That's when you notice a liquid resides within it, you smell it, a sweet aroma, it smells like roses.")
    st.write ("Do you drink from the chalice?")
    col1, col2 = st.columns(2)
    
    if col1.button("Yes, drink it", on_click=go, args=("dead_from_chalice",)):
        pass
        
    if col2.button("No, don't drink", on_click=go, args=("",)):
        pass

elif st.session_state.scene == "chalice_dont_drink":
     st.write("You hesitantly put the chalice down resisting the urge of the sweet aroma, and head back through the cold, muddy water.")
    
     col1, col2 = st.columns(2)

    if col1.button ("Continue on main path", on_click=go, args=("path to house",)):
        pass

    if col2.button ("Take the right path", on_click=go, args=("right_path",)):
        pass

elif st.session_state.scene == "chalice_leave":
     st.write("You ignore the temptation to pick up the Chalice, and walk back through the cold, muddy water.")
     col1, col2 = st.columns(2)
     if col1.button("Continue on main path", on_click=go, args=("path_to_house",)):
         pass

     if col2.button("Take right path", on_click=go, args=("right_path",)):
         pass
    
# Separated the death logic into its own scene for cleaner navigation
elif st.session_state.scene == "dead_from_chalice":
    st.write("Unable to resist the sweet smell, you drink from the chalice, gulping down every last drop. As the last drop rolls down your throat, you take a moment, smacking your lips savouring the last remnants on your taste buds.")
    st.write("Suddenly, you drop the chalice and it clatters as you drop it to the ground.")
    st.write("Your eyes begin to burn, and you struggle to catch your breath as your airways gradually close, you begin to panic, and start clawing at your throat.")
    st.write("You've been poisoned. You collapse to the floor in a heap, the cold, wet ground a momentary relief from the pain coursing through your body. You gasp your last breath.")
    st.write ("You are Dead.")
    play_sound("sounds/roc.wav")
    if st.button("R to Restart", on_click=restart):
        pass


# Right path branch (shed)
elif st.session_state.scene == "right_path":
    st.write("As you walk along the right side of the path, you notice a small shed, well built, and a little aged but standing strong.")
    col1, col2 = st.columns(2)
    if col1.button("Go inside the cabin", on_click=go, args=("cabin_inside",)):
        pass
        
    if col2.button("Ignore the cabin", on_click=go, args=("path_to_house",)):
        st.write("Test")
        pass

elif st.session_state.scene == "cabin_inside":
    st.write("You go inside the wooden cabin, and inside you notice a number of old tools littered about. On a workbench, opposite the exit, you notice a chest on the table.")
    col1, col2 = st.columns(2)
    if col1.button("Open the chest", on_click=go, args=("chest_death",)):
        pass
    
    if col2.button("Don't open the chest"):
        st.write("You leave the cabin.")
        if st.button("Continue", on_click=go, args=("path_to_house",)):
            pass
elif st.session_state.scene == "chest_death":
        st.write ("You reach toward the chest, and as your hand brushes the chest, before you have any time to react, it lunges at you. Its teeth sink into your arm and within seconds, you can no longer move your body. You've been paralysed and feel no pain either.")
        st.write ("You fall to the floor, and the mimic chomps away at your flesh. What was a minute feels like an eternity, then everything turns to black. You are dead.")
        play_sound("sounds/ds_go.wav")
        if st.button("R to Restart", on_click=restart):
            pass

# Path to house
elif st.session_state.scene == "path_to_house":
    st.write("You continue walking down the path, it's still quite foggy but you can make out what appears to be a house. It is protected by a large gate. You approach the gate.")
    st.write("As you approach a gust of wind clears the fog, and the house becomes more visible. The house looks like something straight out of a horror movie, a rotting wooden structure, the windows dark and empty, vines encompassing most of the house. The air feels heavy now, and you have a decision to make.")
    st.write("Do you enter the house?")
    col1, col2 = st.columns(2)
    if col1.button("Yes, enter", on_click=go, args=("inside_house",)):
        pass
    if col2.button("No, don't enter"):
        st.write("Your initial thoughts to turn away are probably correct, but you suddenly feel a looming presence.")
        st.write ("Suddenly, there's a loud clang to your left where a rusty intercom sits, and a yellow gas spills out and fills the space around you.")
        st.write ("You breathe it in, and before you can react, you're compelled to completely change your mind about entering the house, you walk towards the house as if under a spell... reminds you of a movie")
        st.write ("You try the front door of the house, it's open. You take a few steps forward inside, and a chill wind hits you.")
        st.write("A panic overcomes you, and you snap out of the trance you were in but as you turn to leave, the front door slams shut. A voice fills the air 'The way is shut'. With no way back, you survey the area around you. You notice a door on your left, a red ruby jewel embedded in the centre of the door. The right a door with a blue sapphire jewel embedded in the centre of its door.")
        st.write("You try the front door of the house, it's open. You take a few steps forward inside, and a chill wind hits you.")
        if st.button("Continue", on_click=go, args=("inside_house",)):
            pass

elif st.session_state.scene == "inside_house":
    st.write("You try the front door of the house, it's open. A panic overcomes you and then the front door slams shut. You notice two doors: one with a red ruby, one with a blue sapphire.")
    if st.button("Open Blue Door", on_click=go, args=("blue_path",)):
        pass
    if st.button("Open Red Door", on_click=go, args=("red_path",)):
        pass

# Blue path
elif st.session_state.scene == "blue_path":
    st.write("You push the door open, and you're hit with a blast of light, and an aroma of meat, roasted vegetables and mead! A large banquet appears.")
    if st.button("Eat at the banquet"):
        st.write("You eat and feel satisfied. You spot a large covered painting. Do you unveil it?")
        if st.button("Unveil the painting", on_click=go, args=("red_path",)):
            play_sound("sounds/lotr.wav")
            st.write("A melody plays and gives you hope. You leave towards the Red Ruby Door.")
        if st.button("Don't unveil", on_click=go, args=("red_path",)):
            st.write("You decide not to unveil it and head to the Red Ruby Door.")
    else:
        if st.button("Ignore the food", on_click=go, args=("red_path",)):
            pass

# Red path
elif st.session_state.scene == "red_path":
    st.write("You approach the Red Ruby Door and enter a museum-like room with displays. Inside is a doll in a cabinet. Do you open it?")
    if st.button("Open the cabinet"):
        st.write("You pick up the doll, feel a presence, the doll disappears, cabinet starts to close, you see a shadow... Two claps and you are dead.")
        play_sound("sounds/clap.wav")
        play_sound("sounds/myneck.wav")
        if st.button("Restart", on_click=restart):
            pass
    if st.button("Close the cabinet"):
        st.write("You close the cabinet, proceed through the museum and head down into a basement where you spot a desk and a painting.")
        
        col1, col2 = st.columns(2)
        if col1.button("Check the Painting"):
            st.write("A painting features a grotesque scene — nothing else here so you approach the desk.")
            if st.button("Go to Desk", on_click=go, args=("desk",)):
                pass
        if col2.button("Check the Desk", on_click=go, args=("desk",)):
            pass

# Desk
elif st.session_state.scene == "desk":
    st.write("As you walk over to the desk and examine it, you sift through the notes on the table — research notes on occult topics. Something falls and you spot a key by your foot. You open a drawer and find a book that has a face.")
    if st.button("Interact with the Book", on_click=go, args=("book_interaction",)):
        pass

# Book interaction
elif st.session_state.scene == "book_interaction":
    st.write("You stare at the book. You can open it from the Front, Back or Middle.")
    c1, c2, c3 = st.columns(3)
    if c1.button("Front", on_click=go, args=("front_book",)):
        pass
    if c2.button("Back", on_click=go, args=("back_book",)):
        pass
    if c3.button("Middle", on_click=go, args=("middle_book",)):
        pass

elif st.session_state.scene == "front_book":
    st.write("You open the book from the front. It's mostly unintelligible. Do you check the back or the middle?")
    if st.button("Middle", on_click=go, args=("middle_book",)):
        play_sound("sounds/pageflip.wav")
    if st.button("Back", on_click=go, args=("back_book",)):
        play_sound("sounds/pageflip.wav")

elif st.session_state.scene == "back_book":
    st.write("You open the book from the back. There are numerous symbols including a Leviathan Cross and the word 'Daemonium'.")
    if st.button("Front", on_click=go, args=("front_book",)):
        play_sound("sounds/pageflip.wav")
    if st.button("Middle", on_click=go, args=("middle_book",)):
        play_sound("sounds/pageflip.wav")

elif st.session_state.scene == "middle_book":
    play_sound("sounds/pageflip.wav")
    st.write("You turn to the centre of the book and read about a great evil sealed away. You read aloud 'Daemonium Sigillum' and the basement door bursts open. A great evil launches toward you. Suddenly you wake up — it was a dream.")
    st.write("You look to your left, your partner asks if you're okay... As you close your eyes again, the story ends.")
    play_sound("sounds/gameover.wav")
    st.write("---\nThe End\n---\nThank you for playing and your help with this mini-project!")
    if st.button("Restart", on_click=restart):
        pass

# Fallback
else:
    st.write("restarting.")
    if st.button("Restart", on_click=restart):
        pass
