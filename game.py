import streamlit as st
import time
import os
import sys

    
# function to get resource path, helps when running script with Pyinstaller. 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# function to play audio 
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

# Navigation function
def go(next_scene, note=None):
    st.session_state.history.append((st.session_state.scene, note))
    st.session_state.scene = next_scene

# Restart function
def restart():
    st.session_state.scene = "start"
    st.session_state.history = []

# Small utility to show paragraphs with optional delays (non-blocking)
def write_paragraphs(paragraphs):
    for p in paragraphs:
        st.write(p)

# Game UI 
st.title("Lewis' Mini Text Adventure Game")

if st.session_state.scene == "start":
    st.write("Would you like to start a new adventure?")

    col1, col2 = st.columns(2)
    if col1.button("Start New Adventure", on_click=go, args=("wake_up",)):
        st.session_state.history = []
        pass
    
    if col2.button("No"):
        st.write("Journey another day then...")

    st.write("\n\n\n\n\n*Any and all sounds used belong to their respective copyright holders, this project is purely for educational purposes. The views, opinions expressed are those of myself Lewis Rowe, and do not reflect any other business or company I have an affiliation with.*")
        

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
        
    if col2.button("No, don't drink", on_click=go, args=("chalice_dont_drink",)):
        pass

elif st.session_state.scene == "chalice_dont_drink":
     st.write("You hesitantly put the chalice down resisting the urge of the sweet aroma, and head back through the cold, muddy water.")
     col1, col2 = st.columns(2)

     if col1.button ("Continue on main path", on_click=go, args=("path_to_house",)):
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
        
    if col2.button("Ignore the cabin", on_click=go, args=("ignore_cabin_path_to_house",)):
        st.write("You turn right back around, ignoring the cabin.")
        pass

elif st.session_state.scene =="ignore_cabin_path_to_house":
     st.write("You turn right back around, resisting any curiosity for the mysterious cabin, and head back to the fork in the road.")
     col1, col2 = st.columns(2)

     if col1.button ("Continue on main path", on_click=go, args=("path_to_house",)):
        pass

     if col2.button ("Take the left path", on_click=go, args=("left_path",)):
        pass

elif st.session_state.scene == "cabin_inside":
    st.write("You go inside the wooden cabin, and inside you notice a number of old tools littered about. On a workbench, opposite the exit, you notice a chest on the table.")
    col1, col2 = st.columns(2)
    if col1.button("Open the chest", on_click=go, args=("chest_death",)):
        pass
    
    if col2.button("Don't open the chest", on_click=go, args=("chest_leave",)):
        pass
            
elif st.session_state.scene =="chest_leave":
     st.write("You get a tingle down your spine which instinctively encourages you not to open the chest, and you leave the cabin, back down the path.")
     col1, col2 = st.columns(2)
     if col1.button("Continue", on_click=go, args=("path_to_house",)):
         pass    

     if col2.button("Take the left path", on_click=go, args=("left_path",)):
         pass
            
elif st.session_state.scene == "chest_death":
        st.write ("You reach toward the chest, and as your hand brushes the chest, before you have any time to react, it lunges at you. Its teeth sink into your arm and within seconds, you can no longer move your body. You've been paralysed and feel no pain either.")
        st.write ("You fall to the floor, and the mimic chomps away at your flesh, then everything turns to black. You are dead.")
        play_sound("sounds/ds_go.wav")
        if st.button("R to Restart", on_click=restart):
            pass

# Path to house
elif st.session_state.scene == "path_to_house":
    st.write("You continue walking down the path, it's still quite foggy but you can make out what appears to be a house which is protected by a large black gate.")
    st.write("As you approach the gate, a gust of wind clears the fog. The house looks like something straight out of a horror movie, a rotting wooden structure, the windows dark and empty, whilst vines encompass most of the house. The air feels heavy, and you have a decision to make.")
    st.write("Do you enter the house?")
    col1, col2 = st.columns(2)
    if col1.button("Yes, enter", on_click=go, args=("inside_house",)):
        pass
    if col2.button("No, don't enter", on_click=go, args=("dont_enter",)):
        pass

elif st.session_state.scene =="dont_enter":
        st.write ("Suddenly, there's a loud clang to your left where a rusty intercom sits, and a yellow gas spills out and fills the space around you.")
        st.write ("You breathe it in, and before you can react, you're compelled to completely change your mind about entering the house, you walk towards the house as if under a spell...")
        st.write ("You try the front door of the house, it's open. You take a few steps forward inside, and a chill wind hits you.")
        st.write ("A panic overcomes you, and you snap out of the trance you were in but as you turn to leave, the front door slams shut! You try the door but to no avail, your only choice is forward. You notice a door on your left, a red ruby jewel embedded in the centre of the door, and another door on the right with a blue sapphire jewel embedded in the centre of its door.")
    
        if st.button("Continue", on_click=go, args=("inside_house",)):
            pass

elif st.session_state.scene == "inside_house":
        st.write ("You try the front door of the house, it's open. You take a few steps forward inside, and a chill wind hits you.")
        st.write ("A panic overcomes you, and you snap out of the trance you were in but as you turn to leave, the front door slams shut! You try the door but to no avail, your only choice is forward. You notice a door on your left, a red ruby jewel embedded in the centre of the door, and another door on the right with a blue sapphire jewel embedded   in the centre of its door.")
        st.write ("Which door do you open?")
        col1, col2 = st.columns(2)
        if col1.button("Open the Sapphire Door", on_click=go, args=("blue_path",)):
            pass
        if col2.button("Open the Ruby Door", on_click=go, args=("red_path",)):
            pass

# Blue path
elif st.session_state.scene == "blue_path":
        st.write("You push the door open, and you're hit with a blast of light, blinded but you can still smell an aroma of meat, and roasted vegetables! You eyes begin to adjust, and your vision begins to clear up, you spot exactly what your nose smelt!")
        st.write("A large banquet, with Roasted Venison, Slow Roasted Pork Belly, Baked Apples, Honey Roasted Carrots, and Sweet Mead. Your stomach grumbles at the thought of trying some.")
        st.write("Do you eat at the banquet table?")
        col1, col2 = st.columns(2)
        if col1.button("Yes, eat", on_click=go, args=("eat_banquet",)):
            pass
        if col2.button("No, don't eat", on_click=go, args=("skip_banquet",)):
            pass

elif st.session_state.scene =="eat_banquet":
        st.write("You sit down at the table, overwhelmed by the choice, and not sure where to start, you grab the closest food item, scoffing it all down.")
        st.write("This might be some of the best food you've ever had, and just as you go take another bite, you can't, you feel like your stomach is about to burst!")
        st.write("Feeling satisfied, you rise up from the table, and look around you. You spot what looks to be a large object on the wall covered by a red fabric.")
        st.write("Do you go over and remove the fabric?")
        col1, col2 = st.columns(2)
        if col1.button("Remove fabric", on_click=go, args=("remove_fabric",)):
            pass
        if col2.button("Leave fabric alone", on_click=go, args=("leave_fabric",)):
            pass

elif st.session_state.scene =="skip_banquet":
        st.write("You decide you're not hungry, and resist the urge to eat.")
        st.write("Instead, you have a closer look around the room, and notice a large object on the wall, it is covered by a red fabric")
        st.write("Do you go over and remove the fabric?")
        col1, col2 = st.columns(2)
        if col1.button("Remove fabric", on_click=go, args=("remove_fabric",)):
            pass
        if col2.button("Leave fabric alone", on_click=go, args=("leave_fabric",)):
            pass
            
elif st.session_state.scene =="remove_fabric":
        st.write("You walk over to the large painting and pull the red fabric covering it. On the painting, a group of 9 sits at a banquet table, much like the one behind you.")
        st.write("1 older man and a smaller humanoid with mighty beards, 2 handsome men with dark hair, a pointy-eared humanoid with fair hair, 4 smaller humanoid creatures with rather large and hairy feet, seems familiar.")
        st.write("You peer around the painting, and you notice a small button on the bottom centre of the frame.")
        st.write("Do you press the button?")
        col1, col2 = st.columns(2)
        if col1.button("Press the button", on_click=go, args=("painting_button_press",)):
            pass
        if col2.button("Ignore the button", on_click=go, args=("painting_button_ignore",)):
            pass

elif st.session_state.scene =="painting_button_press":
        st.write("You press the button. A melody plays, and for some reason, it gives you hope.")
        play_sound("sounds/lotr.wav")
        if st.button("Continue", on_click=go, args=("painting_exit_happy",)):
            pass
elif st.session_state.scene =="painting_exit_happy":
        st.write("You leave the banquet room with a rekindled spirit and head towards the Ruby Door")
        if st.button("Open Ruby Door", on_click=go, args=("red_path",)):
            pass
elif st.session_state.scene=="painting_button_ignore":
        st.write("You decide to not press the button, and move on.")
        if st.button ("Go to Ruby Door", on_click=go, args=("red_path",)):
            pass

elif st.session_state.scene=="leave_fabric":
        st.write("You think it's best to leave the fabric alone.")
        st.write("Do you take another chance at the banquet table, or head over to the Ruby Door?")
        col1, col2 = st.columns(2)
        if col1.button("Indulge yourself", on_click=go, args=("eat_banquet",)):
            pass
        if col2.button("Go to Ruby Door", on_click=go, args=("red_path",)):
            pass

#red path
elif st.session_state.scene=="red_path":
        st.write("You head over to the Ruby Door, the encrusted jewel glistening as you approach. You push the handle for the door and enter the room.")
        st.write("You observe your surroundings, noticing you appear to be in some sort of museum, various books, scepters, and dolls in glass display cabinets.")
        st.write("You wander inward, and as you peer between each of the displays, you notice one of them is slightly ajar.")
        st.write("Inside is a doll, its got red hair, a blue floral dress, striped socks, black shoes, and a white apron which says 'I Love You'.")
        st.write("Do you open the cabinet and take a closer look at it or shut it?")
        col1, col2 = st.columns(2)
        if col1.button("Open it", on_click=go, args=("open_cabinet",)):
            pass
        if col2.button("Close it", on_click=go, args=("close_cabinet",)):
            pass

elif st.session_state.scene=="open_cabinet":
        st.write("You open the cabinet, and grab the doll, examining it all round, there doesn't seem to be anything out of the ordinary with it.")
        st.write("In that moment of safety, you feel a presence behind you, you quickly turn around, but nothing is there. You clench your fist, thus becoming aware your hands feel a little lighter. The doll is gone from your grasp.")
        st.write("Confused, you look around and as you turn back around to the glass cabinet, you see that the doll sits back in its place. That's when the cabinet starts to slowly close on its own.")
        st.write("You watch in bewilderment, and as it reaches a close, you catch your own reflection although something is amiss, a dark shadow is looming over you.")
        if st.button("Continue", on_click=go, args=("cabinet_death",)):
            pass

elif st.session_state.scene=="open_cabinet_2":
        st.write("The temptation is overwhelming, so you decide to head back to the cabinet")
        st.write("You open the cabinet, and grab the doll, examining it all round, there doesn't seem to be anything out of the ordinary with it.")
        st.write("In that moment of safety, you feel a presence behind you, you quickly turn around, but nothing is there. You clench your fist, thus becoming aware your hands feel a little lighter. The doll is gone from your grasp.")
        st.write("Confused, you look around and as you turn back around to the glass cabinet, you see that the doll sits back in its place. That's when the cabinet starts to slowly close on its own.")
        st.write("You watch in bewilderment, and as it reaches a close, you catch your own reflection although something is amiss, a dark shadow is looming over you.")
        if st.button("Continue", on_click=go, args=("cabinet_death",)):
            pass

elif st.session_state.scene=="cabinet_death":
        play_sound("sounds/ClapNeck.wav")
        st.write("Before you even have time to react. You hear 2 Claps and your neck snaps. You are Dead.")
        if st.button("Restart", on_click=restart):
            pass
        
elif st.session_state.scene=="close_cabinet":
        st.write("You decide to close the cabinet, you snag one last look at the doll and you think to yourself, 'maybe it was for the best'. You continue through the museum and come across a wooden door.")
        col1, col2 = st.columns(2)
        if col1.button("Enter the door", on_click=go, args=("basement_door",)):
            pass
        if col2.button("Actually, open the cabinet", on_click=go, args=("open_cabinet_2",)):
            pass

elif st.session_state.scene=="basement_door":
        st.write("You push down the handle, and swing the door open. It leads downwards, into a basement. With only one way to go, you head down the stairs.")
        st.write("When you reach the bottom, you look over to your right and spot a desk filled to the brim with papers, it has just enough room you could work on it due to a painting which takes up the rest of the space.")
        col1, col2 = st.columns(2)
        if col1.button("Check the desk", on_click=go, args=("the_desk",)):
            pass
        if col2.button("Look at painting", on_click=go, args=("the_painting",)):
            pass

elif st.session_state.scene=="the_desk": 
        st.write("You walk over to the desk and examine it, sifting through a large stack of written notes.")
        st.write("Upon examination, you notice these hastily scrawled notes are covering occult, demonic, and religious topics. Whilst flicking through, something falls from between the papers and clatters on the ground.")
        st.write("You scan around the floor searching for what fell, and by your foot you notice a key, and pick it up.") 
        st.write("You look around the desk to see if there's anything you can use the key on, and notice the desk has two drawers with keyholes. You attempt to pull them open but expectedly they're locked.")
        col1, col2 = st.columns(2)
        if col1.button("Open first drawer", on_click=go, args=("first_drawer",)):
            pass
        if col2.button("Open second drawer", on_click=go, args=("second_drawer",)):
            pass

elif st.session_state.scene=="first_drawer":
        st.write("You place the key into the keyhole, turn it, and open the drawer.")
        st.write("Inside is a small charm, it appears to be a puzzle box, golden and black in colour with unfamiliar markings.")
        st.write("You pop the charm onto your waist belt, and go to open the second drawer.")
        if st.button("Continue", on_click=go, args=("second_drawer",)):
            pass

elif st.session_state.scene=="second_drawer":
        st.write("You place the key into keyhole, and attempt to turn it, but the key gets a little jammed on rotation.") 
        st.write("On the second attempt, and with a little more force, the key turns and unlocks but it breaks in the process. Hopefully you won't need it anymore.")
        st.write("Pulling the drawer open, you can see a book, it appears to have a face. You pick it up and examine it closer, an eerie feeling comes over you, and you place it on the desk.")
        if st.button("Examine Book", on_click=go, args=("book_interaction",)):
            pass

elif st.session_state.scene=="book_interaction":
        st.write("You stare at the book, and it seems to stare back at you. You can open the book, do you decide to open the book from the Front, Back or Middle?")
        col1, col2, col3 = st.columns(3)
        if col1.button("Front", on_click=go, args=("front_book",)):
            pass
        if col2.button("Middle", on_click=go, args=("middle_book",)):
            pass
        if col3.button("Back", on_click=go, args=("back_book",)):
            pass

elif st.session_state.scene=="back_book":
        st.write("You open the book from the back. Across the pages here, there are numerous images and scribbles of what looks to be religious and occult symbols. You spot one you recognize, a 'Leviathan Cross' it's a double cross with an infinity sign, and underneath it, the words 'Daemonium'.")
        st.write("Ominous sign... pressing on, you decide to check the other areas of the book.")
        col1, col2 = st.columns(2)
        if col1.button("Front", on_click=go, args=("front_book",)):
            pass
        if col2.button("Middle", on_click=go, args=("middle_book",)):
            pass
            
elif st.session_state.scene=="front_book":
        st.write("You open the book from the front. You attempt to read it but it's mostly unintelligible text, you can't make out any of it, it's definitely not human language.")
        st.write("From somewhere, you hear a faint laugh, as if mocking you. Frustrated that you've just wasted time checking the front of the book.")
        st.write("Do you check the back, or middle of the book?")
        col1, col2 = st.columns(2)
        if col1.button("Back", on_click=go, args=("back_book",)):
            pass
        if col2.button("Middle", on_click=go, args=("middle_book",)):
            pass
elif st.session_state.scene=="middle_book":
        st.write("You turn to the centre of the book, on it appears readable text, something you can read for yourself, finally.")
        st.write("It reads, 'A great evil who once dwelled in the very domain you occupy, sealed away a millennia ago, by an unlikely hero using the words 'Daemonium Sigillum'.")
        st.write("Below that is a messily written note, 'Don't read this aloud!' Too late, you got ahead of yourself, finally reading something you understand.")
        st.write("The door to the basement bursts open! As you turn, a great evil launches itself towards you!")
        if st.button("Continue", on_click=go, args=("ending",)):
            pass

elif st.session_state.scene=="ending":
        st.write("In that very moment, you wake up, and scream out, sweating profusely... it was all a dream?")
        st.write("You look over to your left, and your partner looks at you and asks 'If you're okay'. You reply with an unconvincing 'yeah', and rest your head back on the pillow.")
        st.write("As you roll over and close your eyes, your partner does the same. Before they close their eyes, unbeknowst to you, they produce a wry smile...")
        st.write("The End")
        play_sound("sounds/gameover.wav")
        st.write("Thankyou for playing and your help with this mini-project!")
            
#If anything fails, we restart. 
else:
    st.write("restarting.")
    if st.button("Restart", on_click=restart):
        pass
