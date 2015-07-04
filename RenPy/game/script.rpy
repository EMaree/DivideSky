# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
####BACKGROUND IMAGES BEGIN###
#Purgatory Beach
image bg beachnight = "bgs/beach_night_no_moon.jpg"
image bg beachnightmoon = "bgs/beach_night_with_moon.jpg"
#British Apocalypse
image bg beech_road = "bgs/beech_road.jpg"
image bg the_wheel = "bgs/the_wheel.jpg"
#scaling wrong for below image
image bg buildings = "bgs/apocalypsemanchester.JPG"
#unused
image bg buildings = "bgs/apocalypse2manchester.JPG"
#Hull
image bg hullwoods = "bgs/hullwoodlands.JPG"
image bg hullwoods2 = "bgs/hullwoodlands2.JPG"
image bg humberbridge = "bgs/HumberBridgeNature.JPG"
#Murmuration
image bg murmuration = "bgs/Starling_murmuration.JPG"
image bg murmuration2 = "bgs/Starling_murmuration_2.JPG"

####CHARACTER IMAGES BEGIN####
#TYLER
image tyler neutral = im.Scale("Leo_Sprite/leo_neutral.png", 300, 500)
image tyler angry = im.Scale("Leo_Sprite/leo_angry.png", 300, 500)
image tyler blush = "Leo_Sprite/leo_blush.png"
image tyler frown = im.Scale("Leo_Sprite/leo_frown.png", 300, 500)
image tyler happy= "Leo_Sprite/leo_happy.png"
image tyler happyblush = "Leo_Sprite/leo_happy_blush.png"
image tyler sad = im.Scale("Leo_Sprite/leo_sad.png",300,500)
image tyler surprise = "Leo_Sprite/leo_surprise.png"

#EDEL
image edel neutral = im.Scale("Sophie_Sprite/Sophie_neutral.png",200,500)
image edel smile = "Sophie_Sprite/Sophie_smile.png"
image edel smirk = "Sophie_Sprite/Sophie_smirk.png"
image edel embarassed = "Sophie_Sprite/Sophie_embarassed.png"

#TONI

image Toni smile = im.Scale("Aya_Sprite/Aya_smile.png",200,500)
image Toni neutral = im.Scale("Aya_Sprite/Aya_neutral.png",200,500)
image Toni angry = im.Scale("Aya_Sprite/Aya_angry.png",200,500)


#DIEGO

# Declare characters used by this game.
define t = Character('Tyler', color="#c8ffc8")
define e = Character('Edel', color="#c8c8ff")

#MUSIC NOTES
# play music "Aid and Comfort.mp3" -- Tense, low beats, used for intro at beach. Electronic.
# for the way across: nice continuation from 'aid and comfort', maybe good theme for rival? Also good theme for tension/injury. Sounds like snow.
# maybe https://disparition.bandcamp.com/track/vortex-shedding for the Embassy? The little background ticking is nice, but not quite what I'm after.
# winter transitions into more winter: good for flying, and sad moments. Piano ambient.
# one road among many: climatic theme, a big building beat, very ominious.
# eliezers waltz = very spooky, very witnery, big reveals and angsty moments.
# the high king: for the ceremony of flight.
# hvar: very sad, and seagulls (so fits either beach or work). good for moments of angst and realisation. Also good for sad ends, bad ends, true ends.



# The game starts here. Prologue.
label start:
    scene black
    play music "Aid and Comfort.mp3"
    
    "I've only got one rule in life: I'm not going to kill myself. "
    "It's not a rule most people need. Not a rule most people have to repeat to themselves almost daily, writing it down, setting reminders, whispering it under their breath."
    "But I'm nineteen, with no job, no boyfriend, no future."
    "And I'm not going to kill myself."
    "The world is ending, and I'm not going to kill myself."
    "Angels are in the streets tearing people apart."
    "Angels are eldritch things with eyes where eyes never belong."
    "Angels are ruthless, killing saints and sinners alike. I’ve seen so many friends die already."
    #to do: make slow
    "I'm. Not. Going. To. Kill. Myself."
    scene bg beech_road
    "My little sister is dead..."
    "...whatever death even means these days."
    "I heard her screaming but saw nothing except blood, felt nothing except the breeze of wings beating and the gaze of a hundred eyes."
    "I'm not going to--"
    "I can't."
    "But this bloody world wants me dead. It’s ending around me, a slow and steady apocalypse. Hull is a bright mess of streetlights and burning buildings, The Deep is a jagged broken edge jutting out into the smoke. London’s lost, and soon all of England will be."
    "And I've been stabbed."
    
    scene bg the_wheel
    "Actually, I was stabbed a while ago. The heat of the sword cauterized the wound instantly. But something was punctured, and parts of me are leaking into parts they shouldn't." 
    "The creature that did it left soon after, fleeing in a flurry of white feathers. "
    "They always know when they’ve killed you. You know it, too, when they turn away."
    "Back when this all started, before I knew better, I would’ve begged with them. Sobbed and wailed and pleaded, the whole lot, in the hope that all those staring eyes would see pity. "
    "But two days into the end of the world, an angel murdered my sister in front of me."
    "Begging did nothing."
    "So I’m dying as quietly as I can. Easier said than done, really."
    "Big guy curled up in the street, bleeding all over my favourite suit. I was just trying to get to a job interview."
    "In the bloody Pound Shop."
    "Down the road, metal columns are groaning as an overloaded bridge starts to lean and sag down into the water, shedding cars like dead leaves in autumn. "
    #to do: make slow
    "Old Humber Bridge is falling down, falling down, falling down..."
    #to do: make slow
    "And I'm bleeding to death."

   #Chapter 1
   
    scene black
    with dissolve
    with Pause(2)
    "The pain stops."
	"One moment, white hot pain, and then… nothing."
    "Nothing, except the torn-up high street is gone."

    scene bg beachnight
    with fade
    
    "The narrow brick lanes and crammed-together buildings, shredded and burnt-out, have been replaced by a frozen beach."
    "I blink a few times, but it’s definitely there: frosted sands and iced-over shallows. My breath fogs in front of my face as I sit up."
    "So, this is being dead."
    "Kind of weird, actually."
    "I don’t feel very dead."
    
    show tyler sad at right
    
    t "Well. This isn’t exactly what I was expecting."
    "Angels exist, so I shouldn’t be surprised that the afterlife does too. But in a way, it’s disappointing. "
    "I’m tired. Real, bone tired."
    "I don’t fancy dying a second time, but I don’t want to pick fights with halo-hatted monsters, either."
    "I move away from the icy water and into the shadows of the cliffs. The beach is rocky here, and focussing on not breaking my ankle is a welcome distraction from the mess I’m in. "
    "I can see chapels on the clifftops, with crosses hanging squint on their roofs. There’s one scattered every few hundred metres."
    "I could check them, but I know better."
    show tyler frown at left
    "Something—someone—runs across the cliffs above me. I freeze, but it curves it path and heads straight for me."
    "I’ve been seen. "
    
    show edel neutral at left
    e "Be not afraid."
    show tyler angry at right
    "I can’t help myself. I laugh in her face."
    e "I am an angel of the Lord. And if I were you, I’d take off that pretty suit and prepare yourself. Things are about to get very painful."
    
    scene black
    with Pause(2)
    "END OF DEMO."
    return
