label intro:
	scene weet warn
	$renpy.pause(4)
	scene weet cred
	$renpy.pause(2)
	scene weet logo
	$renpy.pause(2)
label en_NOP1:
	scene black
	scene bg op_snowywoods
	play music "bgm/Lullaby_of_Open_Eyes.ogg"
	"A light breeze causes the naked branches overhead to rattle like wooden windchimes."
	"This is a popular retreat for couples in the summer. The deciduous trees provide a beautiful green canopy, far out of sight of teachers and fellow students."
	"But now, in late winter, it feels like I'm standing under a pile of kindling."
	"I breathe into my cupped hands and rub them together furiously to prevent them from numbing in this cold."
	hi "Just how long am I expected to wait out here, anyway? I'm sure the note said 4:00 PM."
	"Ah yes... the note... slipped between the pages of my math book while I wasn't looking."
	"As far as cliches go, I'm more a fan of the letter-in-the-locker, but at least this way shows a bit of initiative."
	"As I ponder the meaning of the note, the snowfall gradually thickens."
	"The snowflakes silently falling from the white-painted sky are the only sign of time passing in this stagnant world."
	"Their slow descent upon the frozen forest makes it seem like time has slowed to a crawl."
#	play sound "sfx/rustling.ogg"
	"The rustling of dry snow underfoot startles me, interrupting the quiet mood. Someone is approaching me from behind."
	mystery "Hi... Hisao? You came?"
	"A hesitating, barely audible question."
	"However, I recognize the owner of that dainty voice instantly."
	"I feel my heart skip a beat."
	"It's a voice I've listened to hundreds of times, but never as more than an eavesdropper to a conversation."
	"I turn to face this voice, the voice of my dreams, and my heart begins to race..."
	scene white
	$renpy.pause(1)
	scene ev other_iwanako_start
	hi "Iwanako? I got a note telling me to wait here... it was yours?"
	"Dammit. I spent all afternoon trying to come up with a good line and that was the result."
	"Pathetic."
	"Iwanako" "Ahmm... yes. I asked a friend to give you that note... I'm so glad you got it."
	"A shy, joyous smile that makes me so tense I couldn't move a single muscle even if I tried."
	play music "bgm/blank.ogg"
	scene bg op_snowywoods
#	play sound "sfx/heart_single_slow.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.7)
#	play sound "sfx/heart_single_slow.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.7)
	"My heart is pounding now, as if it were trying to burst out from my chest and claim this girl for itself."
	scene ev other_iwanako_start
	hi "So... ah... here we are. Out in the cold..."
	"Once again, the wind stirs up the branches. The cacophonous noise is music to my ears."
	"Iwanako flinches ever so softly against the gust of wind."
	"As it passes, she rights herself, as if supported by some new confidence."
	"Her eyes lock with mine and she lazily twirls her long, dark hair around her finger."
	"All the while, the anxious beating of my heart grows louder."
	scene bg op_snowywoods
	"My throat is tight; I doubt I could even force a word out if I tried."
	"Iwanako" "You see..."
#	play sound "sfx/heart_single_slow.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.7)
	"Iwanako" "...I wanted to know..."
#	play sound "sfx/heart_single_slow.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.7)
#	play sound "sfx/heart_single_fast.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.2)
	"Iwanako" "... if you'd go out with me..."
	"I stand there, motionless, save for my pounding heart."
	"I want to say something in reply, but my vocal cords feel like they've been stretched beyond the breaking point."
	play music "bgm/Cold_Iron.ogg"
	"Iwanako" "... Hisao?"
	"I reach up to try to massage my throat, but this only sends spikes of blinding pain along my arms."
	"Iwanako" "Hisao?!"
#	play sound "sfx/heart_single_fast.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.8)
	"My whole body freezes, save for my eyes, which shoot open in terror."
#	play sound "sfx/heart_single_fast.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.95)
#	play sound "sfx/heart_single_slow.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.8)
#	play sound "sfx/heart_single_fast.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.85)
#	play sound "sfx/heart_stop.ogg"
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	$renpy.pause(0.8)
	"Iwanako" "HISAO!"
	"The beating in my chest suddenly stops, and I go weak at the knees."
	scene black
	"The world around me - the canopy of bare branches, the dull winter sky, Iwanako running towards me - all these fade to black."
	"The last things I remember before slipping away are the sounds of Iwanako screaming for help and the incessant clatter of the branches above..."
	$renpy.pause(1)
	play music "bgm/blank.ogg"
	scene weet title
	$renpy.pause(4)
	scene black
label en_NOP2:
	"It's been four months since my heart attack."
	scene bg hosp_room
	play music "bgm/Caged_Heart.ogg"
	"In that whole time, I can probably count the times I've left this hospital room unsupervised on one hand."
	"Four months is a pretty long time when you're left alone with your thoughts. So, I've had plenty of time to come to terms with my situation."
	"Arrhythmia."
	"A strange word. A foreign, alien one. One that you don't want to be in the same room with."
	"A rare condition. It causes the heart to act erratically and occasionally beat way too fast. It can be fatal."
	"Apparently, I've had it for a long time. They said it was a miracle that I was able to go on so long without anything happening."
	"Is that really a miracle? I guess it was supposed to make me feel better, more appreciative of my life."
	"It really didn't do anything to cheer me up."
	"My parents, I think, were hit harder by the news than I was. They practically had two hemorrhages apiece."
	"I had already had a full day by then to digest everything. To them, it was all fresh. They were even willing to sell our house in order to pay for a cure."
	"Of course there isn't a cure."
	"Because of the late discovery of this... condition, I've had to stay at the hospital, to recuperate from the treatments."
	"When I was first admitted, it felt as if I was missed..."
	"For about a week, my room in the ward was full of flowers, balloons and cards."
	"But, the visitors soon dwindled and all the get-well gifts began trickling down to nothing shortly after."
	"I realized that the only reason I had gotten so many cards and flowers was because sending me their sympathy had been turned into a class project."
	"Maybe some people were genuinely concerned, but I doubt it. Even in the beginning, I barely had visitors. By the end of the first month, only my parents came by on a regular basis."
	"Iwanako was the last to stop visiting."
	"After six weeks, I never saw her again. We never had that much to talk about when she visited, anyway."
	"We didn't touch the subject that was between us on that snowy day ever again."
	"The hospital?"
	"It's not really a place I'd like to live in."
	"The doctors and nurses feel so impersonal and faceless."
	"I guess it's because they are in a hurry and they have a million other patients waiting for them, but it makes me feel uncomfortable."
	"For the first month or so, I asked the head cardiologist every time I saw him for a rough estimate of when I'd be able to leave."
	"He never answered anything in a straightforward way, but told me to wait and see if the treatment and surgeries worked."
	"So, I idly observed the scar that those surgeries had left on my chest slowly change its appearance over time, thinking of it as some kind of an omen."
	"I still ask the head cardiologist about leaving, but my expectations are low enough now that I'm not disappointed any more when I don't get a reply. The way he shuffles around the answer shows that there is at least some hope."
	"At some point I stopped watching TV. I don't know why, I just did."
	"Maybe it was the wrong kind of escapism for my situation."
	"I started reading instead. There was a small 'library' at the hospital, although it was more like a storeroom for books. I began working my way through it, one small stack at a time. After consuming them, I would go back for more."
	"I found that I liked reading and I think I even became a bit addicted. I started feeling naked without a book in my hands."
	"But I loved the stories."
	"That was what my life was like."
	"The days became increasingly harder to distinguish from each other, differing only by the book I was reading and the weather outside. It felt like time blurred into some kind of gooey mass I was trapped inside, instead of moving within."
	"A week could go by without me really noticing it."
	"Sometimes, I'd pause in realization that I didn't know what day of the week it was."
	"But other times, all the things that surrounded me would painfully crash into my consciousness, through the barrier of nonchalance I had set up for myself."
	"The pages of my book would start to feel sharp and burning hot and the heaviness in my chest would become so hard to bear that I had to put the book aside and just lay down for a while, looking at the ceiling as if I was going to cry."
	"But that happened only rarely."
	"And I couldn't even cry."
	"Today, the doctor comes in and gives me a smile. He seems excited, but not very. It's like he is trying to make an effort to be happy on my behalf."
	"My parents are here. It's been a few days since I've last seen them. Both of them are even sort of dressed up. Is this supposed to be some kind of special occasion? It's not a party."
	"There is this ritual the head cardiologist has. He takes his time, sorting his papers, then setting them aside as if to make a point of the pointlessness of what he just did."
	"Then he casually sits down on the edge of the bed next to mine. He looks me in the eyes for a moment."
	"Doctor" "Hello, Hisao. How are you today?"
	"I don't answer him but I smile a little, back at him."
	"Doctor" "I believe that you can go home; your heart is stronger now, and with some precautions, you should be fine."
	"Doctor" "We have all your medication sorted out. I'll give your father the prescription."
	"The doctor hands a sheet of paper to my dad, whose expression turns wooden as he reads it quickly."
	"Dad" "So many..."
	"I take it from his hand and take a look myself, feeling numb. How am I supposed to react to this?"
	scene white
	show wallodrugs
	"The absurdly long list of medications staring back at me from the paper seems insurmountable. They all blend together in a sea of letters."
	"This is insane."
	"Side effects, adverse effects, contraindications and dosages are listed line after line with cold precision."
	"I try to read them, but it's so futile."
	"I can't understand any of it. Attempting to only makes me feel sicker."
	"All this... for the rest of my life, every day?"
	scene bg hosp_room
	"Doctor" "I'm afraid that is the best we can do at this point."
	"Doctor" "However, new medications are always being developed, so I wouldn't be surprised to see that list fade over the years."
	"Years... What kind of confidence booster is that? I'd have felt better if he hadn't said anything at all..."
	"Doctor" "Also, I've spoken with your parents and we believe that it would be best if you don't return to your old school."
	"What!?"
	"Dad" "Please, calm down, Hisao. Listen to what the doctor has to say..."
	"Calm down? The way he says it tells me he knew full well that I wouldn't like it. Am I going to be home schooled?"
	"Whatever of my concern shows, it's ignored."
	"Doctor" "We all understand that your education is paramount; however, I don't think that it's wise for you to be without supervision."
	"Doctor" "At least not until we're sure that your medication is suitable."
	"Doctor" "So, I've spoken to your parents about a transfer."
	"Doctor" "It's a school called Yamaku Academy that specializes in dealing with disabled students."
	"Disabled? What? Am I..."
	"Doctor" "It has a 24-hour nursing staff and it's only a few minutes from a highly regarded general hospital. The majority of students live on the campus."
	"Doctor" "Think of it as a boarding school of sorts. It's designed to give students a degree of independence, while keeping help nearby."
	"Independence? It's a school for disabled kids. Don't try to disguise that fact."
	"If it was really that 'free,' there wouldn't be a 24-hour nursing staff, and you wouldn't make a hospital being nearby a selling point."
	"Dad" "Of course, that's only if you want to go. But... your mother and I aren't really able to home school you."
	"Dad" "We went out there and had a look a couple of weeks back; I think you'd like it."
	"It looks like I really don't have a choice."
	"Doctor" "Compared to other heart problems, people with your condition usually tend to live long lives. You'll need a job one day and this is a good opportunity to continue your education."
	"This isn't an opportunity, don't call it an opportunity. Don't call it a goddamned opportunity."
	"Doctor" "Well, you should be excited at the chance to go back to school. I remember you wanted to return to school, and while it's not the same one..."
	"A special school. That's..."
	"An insult. That is what I want to say. It's a step down."
	"Dad" "It's not what you think. All of the students there are pretty active, in their own sort of way."
	"Dad" "It's geared towards students that can still get around and learn, but just need a little help... in one way or another."
	"Doctor" "Your father's right. And many of the graduates of the school have gone on to do amazing things. A person doesn't have to be held back by their disability."
	"Doctor" "One of my colleagues in another hospital is a graduate."
	"I don't care. A person doesn't have to be held back by their disability? That's what a disability is."
	"I really hate that something so important was decided for me. But what can I do about it? A 'normal' life is out of the question now."
	play music "bgm/blank.ogg"
	"It's funny, I had always thought my life was actually kind of boring, but now I miss it."
	"I want to protest. I want to blame this lack of reaction on shock, or fatigue. I could easily yell out something now - something about how I can go back to school anyway. But, no."
	"I don't say anything. The fact is that I know now it's futile."
	"I look around the room, feeling very tired of all this. The hospital, doctors, my condition, everything. I don't see anything that would make me feel any different."
	"There really isn't a choice. I know this, but the thought of going to a disabled school... what are those even like? As much as I try to put a positive spin on this, it's very difficult."
	"But let me try."
	"A clean slate isn't a bad thing."
	"That is all I can think of to get me through this. At least I still have something; even if it's a 'special school,' it's something. It's a fresh start, and my life isn't over. It would be a mistake to just resign myself to thinking that."
	"At the very least, I'll try to see what my new life will look like."
label en_A1:
	scene act 1
	play music "bgm/acttrans.ogg"
	$renpy.pause(10)
	scene bg school_gate
	play music "bgm/Fripperies.ogg"
	"The gate looked far too pompous for what it was."
	"In fact, gates in general seem to do that, but this one especially so."
	"Red bricks, black wrought iron and gray plaster, assembled into a whole that didn't feel welcoming at all."
	"I wondered if it looked like what a gate for a school should look like, but couldn't really decide. Probably no."
	"Of course I didn't want to get stuck on thinking about the gate for too long, so I entered through it with a brisk pace that felt surprisingly good."
	"Moving forward feels good."
	scene bg school_courtyard
	"So I walk towards the main building of Yamaku Academy with this brisk pace. I'm alone, as my parents are taking my stuff to the dorms, and there's supposed to be someone waiting for me."
	"The grounds are incredibly lush, filled with green."
	"It doesn't feel like the kind of grounds a school would have, more like a park, with a clean walkway going past trees and the smell of fresh-cut grass and all other park-like things."
	"Words like 'clean' and 'hygienic' pop into my mind. It makes me shudder."
	"I shake them off. Stay open-minded now. It's your new life. You have to take it as it comes."
	"That's what I tell myself."
	"A few big buildings loom behind the leafy canopies, too big and too many for just a school."
	"Everything seems off; it's different from what I thought I knew about schools."
	"It's an uncanny valley. Even though I was told this is my new school, in the back of my head it doesn't feel like one."
	"I wonder if the feeling is real or caused by my expectations of a school for the disabled."
	"Speaking of that, I don't see anyone else here. It's kinda eerie."
	"It makes me wish there was somebody here so I could anchor myself to something tangible instead of having this feeling that I stepped into another dimension."
	"The trees hum with the wind and the green hues flashing all around me catch my attention."
	"It makes me think about hospitals again, how they say that the operating rooms are painted green because green is a calming color."
	"So why am I feeling so anxious, despite all this greenery?"
	"..."
	"Only after I stand in front of the haughty main building, I surprise myself by realizing why the gate bothered me:"
	"It was the last chance I had to turn back, even if I had no life I could return to."
	"But still, after entering, there was absolutely no way I could go back any more."
	"Feeling nervous and with this realization set in my head, I open the front door."
	scene bg school_lobby
	"A tall man with bad posture notices me as I enter. We're the only people in the lobby, so it's only logical."
	show muto normal at center
	mu_ "You must be... Ni... Na... Niki?"
	hi "Nakai."
	hide muto normal
	show muto smile
	mu_ "So you are. Excellent. I'm your homeroom and science teacher. My name is Mutou."
	mu "Welcome."
	"We exchange a handshake that is neither firm nor sloppy, and he looks at his watch."
	hide muto smile
	show muto irritated
	mu "The head nurse asked you for a brief check-in visit, but there's no time for that now."
	hi "Oh. Should I go later?"
	hide muto irritated
	show muto normal
	mu "Yes, afternoon is probably fine. We should get going and introduce you to the rest of the class. They're waiting already."
	"Waiting for me? I don't really like being the center of attention, but I guess it's inevitable in a situation like this."
	"Somehow, not knowing what is waiting for me makes me feel really nervous."
	"Thinking of this, I almost miss what the teacher is saying."
label en_choiceA1:
	mu "Do you want to introduce yourself to the class?"
	menu:
		"Why?":
			jump en_A1a
		"Yeah, of course.":
			jump en_A1b
label en_A1a:
	hi "Why? Do I have to?"
	mu "Of course not. That's why I asked."
	hi "Right."
	mu "Let's go then."
	jump en_A1c
label en_A1b:
	$attractionSC  = attractionSC+1
	$a1bTrigger = true
	hi "Yeah, sure. I mean, isn't that normal?"
	mu "Of course. But not everyone likes to be at the center of attention."
	"I'm probably one of those people, but I guess I should be the one to give the first impression of myself."
	hi "Right, but it's no problem."
	mu "Let's go then."
	jump en_A1c
label en_A1c:
	scene bg school_staircase2
	"My heart is pounding in my chest and it keeps me thinking about my condition as I follow the teacher up the stairs."
	scene bg school_hallway3
	show muto normal at center
	"The third door down the third floor corridor is marked as the classroom for class 3-3."
#	play sound "sfx/dooropen.ogg"
	"Mutou opens the door and enters."
	$renpy.pause(1)
	hide muto
	mu "Good morning everyone, sorry I'm late again."
	play music "bgm/blank.ogg"
	"I hesitate for a split second at the door, freezing on the spot."
label en_A2:
	scene bg school_hallway3
	"Ah, get a grip! This is a big step, I know that... But there isn't any point to worrying so much about it, at least not this soon."
	scene ev hisao_class_left
	play music "bgm/School_Days.ogg"
	"I follow the teacher into the classroom and look around, partially so I won't have to meet the curious gazes of my new classmates."
	"It's pretty spacious; the ceiling is unusually high and there's lots of space left over around and inbetween the desks."
	"An entire wall taken up by blackboards and the high, old fashioned windows only make it seem larger."
	"The students' desks are just standard wooden desks with a shelf underneath for books and wooden chairs with metal frames. Simple and efficient."
	"I stop walking in front of the classroom and face the other students. They all look normal, like students in any other school. But then, why would they be here?"
	scene ev hisao_class_right
	"They're probably like me and have something wrong with them, only it's just not immediately obvious. Then, I notice that one of the girls seems to be missing the thumb of her right hand. It's a little jarring."
	"Despite the natural tendency to listen when someone's talking about you, I tune out the teacher's speech halfway through while he introduces me to the class."
	"I notice a flash of dark hair and see that someone is looking at me. A girl with really long, straight hair that is pretty eye-catching. As she sees me looking back at her, she covers her face with her hands as if it will make her invisible."
	"There is one boy with a cane leaning against the lockers at the rear of the class. It's weird seeing someone so young with a cane."
	"Another girl seems to be making some weird hand motions. Sign language? She peers at me over the rims of her glasses, then goes back to whatever she's doing."
	"She's kind of cute. So is the cheery-looking girl with pink hair sitting next to her. She's really hard to miss; I don't know how I didn't notice her the moment I walked in..."
	mu "...please welcome our newest classmate."
	"He claps his hands and so does everyone else, except one girl in the first row who has only one hand. I cringe a little, but hide it by bowing in thanks for this applause I did not deserve."
	if a1bTrigger == true:
		jump en_A2b
	elif a1bTrigger == false:
		jump en_A2a
label en_A2a:
	"After the applause, there is a brief silence that nobody seems to want to be responsible for breaking."
	"The teacher soon realizes that he should probably say something. He opens up with some unintelligible noise, shuts up as he loses his momentum, and then starts introducing me."
	"Nobody seems to be too interested."
	"Maybe I should've said yes to the self-introduction thing."
	"Probably realizing he doesn't know anything about me, he just ends up saying my name wrong again, and asks me to write it on the blackboard."
	"I do that, and turn back to face the class, feeling awkward."
	jump en_A2c
label en_A2b:
	"A collective silence tells me that I should open my mouth now."
	hi "So... I'm Hisao Nakai."
	"And after that?"
	hi "My hobbies are reading and soccer. I hope to get along well with everyone even though I'm a new student."
	"And after that?"
	"I'm being so boring. This is exactly like every self-introduction ever. I should say something more. Something more exciting."
	"I end up saying nothing, and the teacher picks up from there."
	"Everyone seems to be satisfied even with what little I said, though. A few girls are whispering to each other, throwing glances at me. It could've gone worse."
	"..."
	jump en_A2c
label en_A2c:
	"I listen to the teacher as he drones about getting along while letting my gaze sweep across the classroom."
	"Everyone seems to be listening to him intently and when he's done, they clap their hands again which feels like a weird thing to do."
	"The first row girl claps on this round, with her one hand against her other wrist that ends in a bandaged stump."
	"It makes me feel a little bad."
	scene bg school_scienceroom_right
	show muto normal at center
	mu "We're going to be doing some group work today, so that'll give you a chance to talk with everyone. Is that okay with you?"
	hi "Yeah, it's fine with me."
	show muto smile
	mu "That's good, you can work with Hakamichi. She is the class representative."
	mu "She can explain anything you might want to know. And who else would be able to do that better, right?"
	hide muto
	"How could I know?"
	"The teacher passes out the day's assignments and announces that we will be working in groups of three."
	"It hits me that I don't know who Hakamichi is. Slow. The teacher seems to catch my helpless expression."
	mu "Oh, right. Hakamichi is right there, Shizune Hakamichi."
	show misha perky_smile at center
	"As he calls out her name, the cute, bubbly looking girl with bright pink hair and gold eyes waves her hand at me. I take a seat next to her, by the window."
	hi "Hey, I guess you're Hakamichi, right? It's nice to meet you."
	play music "bgm/blank.ogg"
	show misha cross_laugh at center
	"Shizune" "Hahaha~!"
	"What? I'm caught off guard by her laughter."
	show misha hips_grin at center
	"Shizune" "It's nice to meet you, too! But~!"
	"(Not Shizune)" "It's nice to meet you, too! But~!, I'm not Hakamichi, I'm Misha! This is Hakamichi. Shicchan~!"
	play music "bgm/The_Student_Council.ogg"
	scene bg school_scienceroom
	show misha hips_grin at twoleft
	show shizu basic_normal at tworight
	"Giggling, Misha points to the girl next to her, the one I saw using sign language before. It looks like she has been staring at me this whole time. She nods once nonchalantly to show that she acknowledges my presence... but only barely."
	"She has short, yet carefully, neatly brushed hair, a pair of oval-shaped glasses balanced on the tip of a dainty nose, and dark blue eyes that seem to alternate every few seconds between analytical and slightly bored."
	hi "It's nice to meet you."
	show shizu behind_blank at tworight
	shi "..."
	show misha perky_smile at twoleft
	$renpy.pause(0.5)
	show misha sign_smile at twoleft
	$renpy.pause(0.5)
	show misha perky_smile at twoleft
	$renpy.pause(1)
	"She immediately looks at Misha, who smiles and makes a few quick gestures with her hands."
	show shizu adjust_happy at tworight
	$renpy.pause(0.5)
	show shizu behind_smile at tworight
	$renpy.pause(1)
	"Hakamichi nods and makes a few gestures of her own."
	"I start to wonder if the teacher was messing with me, saying things like 'you'll be able to talk to people' and 'who better to explain things to you.'"
	show misha hips_smile at twoleft
	mi "I can see you're a little confused, right?, right? But, I understand why you would think I was Shicchan!"
	mi "Shicchan is deaf, so I'm the person who translates things back and forth for her."
	show misha hips_grin at twoleft
	mi "I'm like an interpreter~! She says it's nice to meet you, too!"
	show shizu basic_normal2 at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "You're the new student, aren't you? Well, Shicchan, of course he is! If he wasn't, he would have been standing up there for no reason, right? Right~!"
	if a1bTrigger == true:
		jump en_A2d
	elif a1bTrigger == false:
		jump en_A2e
label en_A2d:
	mi "He seems like a very interesting person, doesn't he~!"
	jump en_A2f
label en_A2e:
	"Misha looks at me with a weird expression, then continues."
	mi "We don't know much about him, but maybe we'll find out later."
	"Maybe I should've introduced myself after all. Anything would've given a better first impression than the teacher's drone and fumbling with my name."
	jump en_A2f
label en_A2f:
	mi "We knew there was going to be a new student, but we didn't know you would be here today. So soon! Hicchan, right?"
	"Hicchan...?"
	show misha hips_grin at twoleft
	mi "Yup~! It fits, doesn't it?"
	"Did I say it out loud? It's just a surprise. I've never liked that nickname."
	hi "I don't really see how."
	show misha cross_grin at twoleft
	mi "It fits~! You look just like I imagined!"
	show shizu adjust_smug at tworight
	shi "..."
	show misha cross_laugh at twoleft
	show shizu adjust_happy at tworight
	mi "Hahahaha~! Yeah, you look just like a Hicchan!"
	hi "I wonder why everyone seems to think so..."
	shi "..."
	"Hakamichi taps her fingers on the desk to get Misha's attention. They gesture back and forth to each other excitedly, their hands a blur."
	show shizu adjust_happy at tworight
	show misha sign_smile at twoleft
	$renpy.pause(0.5)
	show shizu behind_smile at tworight
	show misha perky_confused at twoleft
	"Misha seems a little overwhelmed."
	show misha hips_grin at twoleft
	mi "Ahaha~! Er, sorry about that!"
	show misha hips_smile at twoleft
	mi "Shicchan wants you to know that she's the class rep, so if there is anything you need to know, you can feel free to ask her."
	show shizu behind_blank at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Do you like the school so far? We can show you around a little if you haven't had the time to walk around and..."
	$renpy.pause(0.5)
	show misha perky_smile at twoleft
	mi "Do you like the school so far? We can show you around a little if you haven't had the time to walk around and... familiarize?"
	$renpy.pause(0.5)
	show misha perky_confused at twoleft
	mi "Do you like the school so far? We can show you around a little if you haven't had the time to walk around and... familiarize? yourself with it!"
	"Misha stumbles with the hard word a bit, making it stick out in her otherwise fluid translation."
	hi "Thanks, that would be pretty helpful. Yeah, I just kind of came straight to class today."
	show shizu behind_frown at tworight
	shi "..."
	show misha hips_laugh at twoleft
	mi "Hahaha~!"
	show misha hips_smile at twoleft
	mi "That's no good! You should always try to learn as much as you can about where you're going before you go there. Not just with school, either~!"
	show misha hips_grin at twoleft
	mi "Always! Even if it's a trip to the convenience store! Really, Shicchan? Hahaha~!"
	show misha perky_smile at twoleft
	show shizu behind_smile at tworight
	"Learn about where you're going? I guess I didn't bother to do that, or just didn't care enough to do so."
	"I didn't look forward to this, even if I committed myself to go along with it half-assedly, but anyway."
	"I don't say anything, and Misha signs something that ends in a shrug. What was that? It seems like it was about me."
	"I feel like slumping over in my seat. Both of them are smiling, but that shrug hit me unexpectedly deeply."
	show misha perky_sad at twoleft
	mi "You look down, are you okay?"
	show shizu basic_normal at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Don't take it the wrong way, please~! I hate it when people are afraid to ask questions! That's how people learn things, by asking~!"
	mi "Asking for help is perfectly normal, as much as needing help! Stop looking like you just failed a test!"
	show misha cross_laugh at twoleft
	mi "Wahahaha~!"
	hi "All right."
	show shizu adjust_happy at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Ah, and another thing, you don't have to call Shicchan something so formal like 'Hakamichi' or 'class rep' all the time! Just call her Shicchan~!"
	play music "bgm/blank.ogg"
	show shizu adjust_blush at tworight
	shi "..."
	show misha hips_smile at twoleft
	mi "Ahaha~! Okay, maybe that's too casual. Maybe 'Shizune' would be more appropriate?"
	show shizu basic_normal2 at tworight
	shi "..."
	show misha hips_grin at twoleft
	play music "bgm/The_Student_Council.ogg"
	mi "Yup, yup~! 'Shizune' is fine!"
	hi "Heh. Okay, that would be a lot easier for me."
	"I feel a lot more at ease. Both of them seem so friendly, so I feel like an idiot for being so apprehensive earlier. Especially about Shizune, who I assumed would be all business."
	"Well, she still seems like that. Just less so, I guess."
	show shizu behind_frown at tworight
	shi "...!"
	show misha perky_confused at twoleft
	mi "Huh? Oh, right, we haven't even touched the assignment! We should start work now, or Shicchan will get mad."
	hi "The assignment is also kind of long, so we should start now if we want to finish it before the end of class."
	show misha hips_laugh at twoleft
	mi "Wahaha~! That too!"
	show shizu basic_frown at tworight
	shi "..."
	"Shizune glares at the two of us impatiently. I don't need to know sign language to understand that."
	hi "Okay, okay, I get the message."
	show shizu basic_normal at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "After class, we can take a walk around the grounds together. It's a nice day today! Okay~?"
	"The assignment is actually very challenging to get through, combining aspects of being both difficult and unnecessarily long."
	play music "bgm/blank.ogg"
	scene bg school_scienceroom
	"Still, we finish it a few minutes earlier than anyone else in the class, despite our late start. Shizune and Misha are really capable."
	"They're quite different, though. The class rep is as calm and professional as she looks, while Misha is a lot more playful and girlish. Not to mention a little more easily distracted."
	"To be honest, the two of them did most of the work. I feel guilty about that."
#	play sound "sfx/carillon.ogg"
	"The clock tower bells ring, signaling the end of the period. Time for lunch."
	scene bg school_hallway3
	"Without knowing what else to do, I follow Misha, who is beckoning me into the hallway and down the stairs."
label en_A3:
	scene bg school_staircase2
	"We descend even below the lobby where I met Mutou, down to the bottom floor."
#	play sound "sfx/crowd_indoors.ogg"
	scene bg school_cafeteria
	"Just like everything in this school, the cafeteria seems too spacious and oddly modern in contrast to the classic exterior."
	"Its big windows open to the courtyard, towards the main gate."
	show misha hips_grin at center
	play music "bgm/Ease.ogg"
	mi "It's the cafeteria~!"
	"Her enthusiastic statement of the obvious makes people around us stare, but Misha doesn't seem to care so we proceed to the line."
	hide misha
	"There is a rather long list of menu options, which seems great until I realize that many of them are to accommodate students who need special diets."
	"How nice. It almost feels like I'm back at the hospital, eating portions measured with scientific precision to meet the needs of the patients."
	"I pick something at random and follow Shizune to a table, sitting opposite of her."
	show misha hips_frown at twoleft
	show shizu basic_normal at tworight
	"As I nibble indifferently at the food I'd rather not eat, Misha pokes me in the side to get my attention and points to Shizune."
	show misha perky_smile at twoleft
	show shizu basic_frown at tworight
	shi "..."
	"I don't understand sign, so the point escapes me."
	"Maybe looking at a person who 'talks' to you is proper and polite?"
	show misha hips_smile at twoleft
	show shizu behind_blank at tworight
	mi "Do you want to know something?"
	hi "What?"
	show misha hips_grin at twoleft
	mi "About anything! We're your guides so you should ask if there is something~!"
label en_choiceA3:
	hi "Hmm, I wonder..."
	menu:
		with menueffect
		"The Library":
			jump en_A3a
		"Shizune's Deafness":
			jump en_A3b
		"(I know everything)":
			jump en_A3c
label en_A3a:
	$attractionHanako = attractionHanako+1
	hi "Oh, yeah. Is there a library in the school? Lately I've gotten into reading a lot so I'd like to check it out."
	"Misha gives the kind of frown that makes it clear she doesn't consider reading a healthy hobby, but then picks up her smile again."
	mi "There is~! It's in the second floor, we can show it to you sometime!"
	hi "Thanks."
	"I return to my food while the girls talk between themselves."
	jump en_A3d
label en_A3b:
	"Shizune intrigues me, and I kind of want to ask something about her."
	"But I can't really ask about something that personal, can I?"
	"Hmm..."
	"I can't come up with anything else to ask so I just focus on my food while the girls talk between themselves."
	jump en_A3d
label en_A3c:
	$attractionSC = attractionSC+1
	hi "I can't think of anything, really."
	show misha sign_smile at twoleft
	mi "Ooh! That means we've been good guides, doesn't it, doesn't it~?"
	"..."
	hi "Eeh... if you say so."
	show misha hips_grin at twoleft
	show shizu behind_smile at tworight
	"Misha positively beams, and so does Shizune after a quick translation."
	"I shake my head at their somewhat exaggerated enthusiasm, and shift my focus on the food."
	jump en_A3d
label en_A3d:
	"Misha and Shizune sign back and forth very animatedly, throwing sideway glances at me but Misha refrains from translating."
	"Maybe they are talking about secret girl stuff or something."
	"..."
	scene bg school_scienceroom
	play music "bgm/Daylight.ogg"
	"We arrive in the classroom early, but we're not the first."
	show hanako emb_downtimid at offscreenright
	"That dark haired girl I noticed before is slumped over her desk at the last row."
	show hanako defarms_shock at offscreenright
	"She jumps a little when Misha crashes into the room with the elegance of a rhino."
	"She shrinks deeper into her seat. I can feel her tension all the way from here, as if she were slowly turning into stone just from our presence."
	"Misha and Shizune either don't notice or don't mind it, as they walk directly past her to their seats and begin to converse."
	hide hanako
	"I'm left wondering about her, even when the classroom slowly fills with other students and finally, the teacher."
	"Getting into the rhythm of school feels strange; it's as if my brain remembers how this is done, but my body doesn't."
	"Towards the end of the class I start yawning and counting the minutes left."
	"I shouldn't be this tired on my first day of school."
	"Maybe it's the long time spent in the hospital that made me like this. I'm even feeling physically weak and lifeless."
#	play sound "sfx/carillon.ogg"
	"Before long, the final bell rings."
	"School is finally over for the day."
	"Beside me, Misha and Shizune are having a short conversation. After a bit of deliberation, Misha turns to me."
	show shizu behind_blank at tworight
	show misha perky_smile at twoleft
	shi "..."
	mi "Unfortunately we can't stay and show you around today, Hicchan. We've got to hurry already, since there is a lot of work for us to do."
	show shizu basic_normal2 at tworight
	shi "..."
	mi "You'll find your way around here, I'm sure of it."
	hi "Ah, wait! The teacher said I'd have to see the nurse. Where do I have to go?"
	show shizu behind_smile at tworight
	show misha hips_grin at twoleft
	mi "Is that so? We can at least show you that much~!"
	mi "Come on, the nurses have their own building, so we have to go outside."
	hide shizu
	hide misha
	scene bg school_hallway3
	"We join the flow of students making their way down the stairwell and outside, with the girls pointing out other senior classrooms in the same hallway as ours."
	scene bg school_courtyard
	"When we get outside, the girls make their way to the smaller building right next to the school."
	"It's built in the same style, so it looks like it's actually a part of the main building."
	show shizu behind_smile at tworight
	show misha perky_smile at twoleft
	shi "..."
	mi "This is the auxiliary building here. There's a lot of official and important stuff inside, like the Yamaku Foundation office and all the nurses' offices. They even have a swimming pool!"
	hi "How is that official?"
	show shizu behind_frustrated at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Don't be silly, Hicchan! It's for physical therapy of course."
	show misha sign_smile at twoleft
	mi "Anyway, all the nursing staff facilities are in there too. The head nurse's office is on the first floor."
	show misha hips_smile at twoleft
	show shizu behind_smile at tworight
	mi "You'll be fine from here, right~? We'll be going, then! See you tomorrow!"
	hi "Yeah, thanks. Bye."
	play music "bgm/blank.ogg"
	hide shizu
	hide misha
	"A whole building for stuff that has nothing to do with the actual education?"
	"I guess it's necessary for a place like this."
	scene bg school_nursehall
	"I walk in, hoping that this really will be only a quick visit like the teacher said."
	"On a white door on the left is a green cross with the text 'Head Nurse' and a nameplate."
#	play sound "sfx/doorknock2.ogg"
	"A voice from the inside responds to my knock almost immediately, but I can't quite make it out."
	"It sounded a bit like an invitation to open the door, so I invite myself further in."
#	play sound "sfx/dooropen.ogg"
	scene bg school_nurseoffice
	"The room is not large and it smells strange. A friendly-looking man turns around on his office chair to face me as I enter."
	"His desk is neat and tidy, but the bin under the table is overflowing with used medical utensils and there are at least a dozen coffee-cup rings lingering on the desk."
	play music "bgm/Ah_Eh_I_Oh_You.ogg"
	show nurse neutral
	nk_ "Hello there. What can I do for you today?"
	"He is young-looking and sort of rugged, but the dimples in his cheeks wash that impression away when he smiles."
	hi "Erm, are you the nurse?"
	show nurse grin
	"He smiles like a person who has heard this very same question hundreds of times."
	nk_ "Why yes, I am. It says so on the door, no?"
	nk_ "You can call me by my name or just 'the nurse' like everyone else."
	"Of course. I shake off my confusion, realizing I probably should grab his extended hand. His handshake is rather firm and friendly."
	hi "Right... err, I'm a new student and my homeroom teacher told me to come and meet you. My name is Hisao Nakai."
#	play sound "sfx/snap.ogg"
	"His eyes light up with revelation and he snaps his fingers."
	show nurse fabulous
	nk "Oh you're THAT Nakai. I was just reading your file in the morning."
	nk "Some kind of chronic arrhythmia and related congenital heart muscle deficiency, right?"
	"He gestures me to sit down in a vacant armchair in front of his desk."
	hi "Eh, yes."
	show nurse neutral
	nk "Good. Well, you've probably been briefed about the school enough, so I'll just go over this quickly."
	nk "We have all kinds of facilities available, mostly physical therapy and such."
	nk "There's always someone from my staff around, even at night, so never hesitate to call us if there is a problem."
	"The famous twenty-four-hour nursing staff."
	hi "Wow, this is like a hospital."
	nk "Well, not exactly. For instance, we don't do brain surgery here."
	"His joke feels so out of place that I'm left thinking why he even said it."
	hi "Yeah... just that it's really weird to have so many medical people at a school."
	nk "You'll get used to it."
	"I'm not so sure of that myself but I don't let the nurse know it."
	nk "Now, let me just find your file again..."
	"While he searches for something from his computer and shuffles stacks of papers around, I let my gaze wander around the room."
	"It's the epitome of generic, I'd like to say."
	"Beige walls and ceiling, dark gray laminate flooring, and all the equipment you'd expect from a school nurse's office."
	"Even the ridiculous educational posters are hanging on all four walls, reminding me to eat properly - three times a day and from all the food groups."
	show nurse grin
	"Smiling, the nurse draws a thick file from a stack of similarly thick files and opens it."
	nk "So, you already have medication for the arrhythmia, just remember to take your pills every morning and evening or it won't be much help."
	show nurse fabulous
	nk "Apart from that... do you do any sports? Rash stuff like... I don't know, boxing?"
	"He grins to his own joke but I don't."
	hi "Eh, well. I played soccer occasionally with some classmates."
	nk "All right, I'm afraid I'm going to have to recommend you refrain from doing that. At least, for the time being."
	hi "Oh."
	"My lack of reaction makes him raise an eyebrow, but really, I'm not too bothered by him forbidding me to kick a ball around."
	"I guess I never did it out of burning passion for the sport. Just to have something to do."
	nk "Any kind of concussion might be very dangerous to your heart and risking another attack is not a good idea."
	nk "Was the previous one caused by a sudden concussion to the chest area? There is no mention of the cause in your papers."
	hi "Err... not exactly."
	show nurse concern
	with charachange
	"I sidestep the question acceptably, and he glances at me over his papers, with a more serious expression on his face."
	nk "Still, you need to keep your body healthy so some exercise would do you good."
	nk "We have physical therapy and such available as I said, but I don't think you really need such heavy measures."
	nk "Just get some light exercise regularly."
	nk "Brisk walks or even light jogging, jumping rope, that sort of thing. Swimming, maybe? There's a pool here."
	hi "So I was told."
	show nurse neutral
	nk "You were? Very good."
	nk "At any rate, and I'm sure you've been told this before, you just need to take care not to overexert yourself."
	"He wags his finger to emphasize the point. No need really, I've heard this a thousand times already."
	show nurse concern
	with charachange
	nk "Absolutely no unnecessary risks. Take care of yourself."
	hi "Okay."
	"He goes over my papers one more time and sets them on the desk, obviously content."
	show nurse neutral
	nk "Good. That's it, then. Come meet me if you ever need something."
	hide nurse
	scene bg school_nursehall
	play music "bgm/blank.ogg"
	"I'm ushered out before I even realize it. A quick visit, indeed."
label en_A4:
	scene bg school_courtyard
	play music "bgm/Stride.ogg"
	"I end up standing in front of the main building and the auxiliary building, although to my eyes, they still look one and the same."
	"It's the first real look I get at the other students, so I watch people coming out of the school, going towards the gate or the dorms."
	"Everyone seems to know where they are going."
	"And I still keep thinking that most of them don't look too special for being students at a special school. Then again, neither do I."
	"Does that make me one of them? One of us?"
	"..."
	"I should go somewhere too, to prevent me from getting lost."
	"It's around dinnertime, but I feel tired instead of hungry."
	"The weariness in me only grows as I trudge towards the dorms, set a little way apart from the main building complex."
	scene bg school_gardens
	"There is a garden of sorts between the school and the dorms; shrubbery, flowers and that overbearing smell of fresh cut grass that fills the atmosphere."
	"It dawns on my tired mind that the smell feels novel because I haven't been outside at all for so long."
	scene bg school_dormext_start_left
	"The dorm building is big and made of red brick. Like the others, it feels way too pompous for what it is, so I push forward, going inside."
	scene bg school_dormhallground
	"It takes more time than necessary to fish out the key I was given from my pocket."
	hi "Room one-one-nine..."
	"Despite the ornate exterior, the inside of the dorm is fairly new, functional, and boring."
	"Just like in the main building, the halls and doors are wide to accommodate wheelchairs. The same goes for the elevators at the ends of the hallways."
	"I poke my head around the corner of the common room door."
	"Inside a few students are watching the television."
	"One nods and gives a quick 'hello' before turning back to the TV."
	"Seems that only the girls around here are sociable. I suppose that's perfectly fine with me."
	"I climb the stairs to the upper floor."
	scene bg school_dormhallway
	"Here, small corridors branch off from the main hallway."
	"Each of these minor halls seems to have a toilet and shower, as well as four rooms."
	"About halfway down the hall, I spy room 119."
	"The name plates on the rooms adjacent to mine are blank. I guess there are just two of us here."
#	play sound "sfx/doorknock2.ogg"
	play music "bgm/blank.ogg"
	"Light shines from below the door of room 117, so I knock lightly."
	hi "Hello, is anyone home?"
	"From inside, I hear a few movements, then the clicking of way more locks than I thought these doors had. After a moment the door squeaks open."
	show kenji tsun
	play music "bgm/Out_of_the_Loop.ogg"
	"A bespectacled boy is standing in the doorway. He is looking at me very intently through his extremely thick eyeglasses."
	ke_ "Who is it?"
	"Blind? No, at least not completely, why would he have eyeglasses if he was?"
	show kenji tsun_close
	"He leans closer to me until our noses are almost touching. His breath stinks of garlic."
	hi "Hisao Nakai... I'm moving into the next room. I thought I should introduce my..."
	show kenji happy
	"His face suddenly brightens in realization, and he stands back upright, thrusting his hand out in a smiling greeting, almost straight to my diaphragm."
	ke_ "Oh, 'sup dude? The name's Kenji."
	hi "Ah, hi."
	"I take Kenji's sweaty hand and shake it, still a little rattled by the sudden change of attitude and vehement welcome."
	ke "There were some suspicious-looking people going in and out of your room earlier."
	hi "It was probably my parents."
	show kenji tsun
	ke "Your parents? You sure? 'Cause they could've been some other people, too. You can't judge a book by its cover."
	"His out-of-place proverb is left hanging between us awkwardly as I try to think of some way to respond."
	hi "I'd say the chances are high enough."
	"He shudders and makes some exaggerated hand gestures."
	show kenji neutral
	ke "You're a brave man, Hisao."
	show kenji tsun
	ke "Me, I don't think I could trust the chances."
	ke "The only one I trust is myself."
	hi "Does that mean I shouldn't get to know you, either?"
	"He thinks about this for a while."
	show kenji neutral
	ke "A wise decision."
	show kenji happy
	ke "Damn, you are smarter than you look."
	ke "Probably."
	ke "What do you look like? I hope not smart."
	show kenji neutral_close
	"He squints his eyes and leans closer again, but I lean backwards to dodge it."
	show kenji tsun
	ke "Never mind, it doesn't matter."
	hide kenji
	play music "bgm/blank.ogg"
	"With that, he turns, fumbles around for a moment in search of the door handle,"
#	play sound "sfx/doorslam.ogg"
	"With that, he turns, fumbles around for a moment in search of the door handle, and shuts the door behind him."
	"I slide the key into the lock of the door marked 119."
	scene bg school_dormhisao
	play music "bgm/Nocturne.ogg"
	"Bleak beige walls, white linen, a desk made of some type of light wood. Ugly curtains."
	"It's no one's room; impersonal, like my hospital room was."
	"My bags are sitting at the foot of my bed, looking a lot emptier than they did this morning."
	"The closet is sitting open, stocked with my clothes."
	"Also, it seems that there are a number of school uniforms hanging there as well."
	"A note is pinned to the sleeve of one of the shirts."
	show note 01
	""
	hide note 01
	"Well, at least I don't have to worry about unpacking."
	"I kind of hoped I would have, then there would be something to do."
	"It's still too early."
	"I put the note down on the desktop and lie down on the bed, feeling drained."
	"Lying there makes me want to read something, but I have nothing with me."
	"I wonder if the hospital conditioned me for wanting to read whenever I have nothing to do."
	"The restless urge just keeps growing until I have to stand up."
	"Maybe it's stress or something."
	"I was pretty nervous about it before coming and for the entire day today too. I still am, I think."
	"Damn, I have to distract myself somehow, so I won't be this unnatural all the time."
	"Tomorrow, I'll go borrow some books from the library."
	"Yeah, I'll do that."
	"But for now..."
	show pills
	"The bottles of medications neatly arranged on my night table catch my eye."
	"I pick up one and shake it just to hear the contents rattle inside, and then read the glued-on pharmacy label."
	hide pills
	show note 02
	""
	hide note 02
	"It doesn't really say that, but it could just as well."
	"It's kinda twisted, having your life depend on chemicals like this. I resent it a little, but what choice do I have?"
	"With a sigh, I begin my new daily ritual of taking the right number of pills from each bottle, being careful to check the correct dosages."
	"..."
	"I lie down again, feeling hollow and uncertain, and after that I keep staring at the blank, unfamiliar ceiling for a long time."
	play music "bgm/blank.ogg"
	scene bg school_dormhisao_ni
	"It doesn't start looking any more familiar, not even after darkness falls and long shadows draw across my room like fingers."
	"The sheets feel slightly more comfortable, warm and nest-like against the chill that passes for room temperature here."
	"Soon the lighter shade of darkness that is the ceiling looks like every ceiling does at night, and it becomes the only thing I recognize any more."
	"The night beckons me to sleep, and I feel the coldness of unfamiliarity and fear creeping up my spine once again."
	"I keep drifting further away from the world I knew."
	scene black
	""
label en_A5:
	scene bg school_dormhisao
	"I wake up in a strange room."
	"Solid morning light shimmers against the light gray ceiling. I had forgotten to draw the curtains closed last night."
	"I?"
	"This is my room, isn't it?"
	play music "bgm/Raindrops_and_Puddles.ogg"
	"My room..."
	"This is the third room this year that I'm supposed to call 'mine.'"
	"Various things around here remind me that indeed, it's me who is supposed to be the one living here."
	"My bags on the floor, my new school books on the desk."
	"My numerous medications on the night table."
	"I stare at the bottles for a moment, deliberating, until I open a bottle, shake out a pill and pop out a tablet from a foil sheet."
	"I down them with a chaser of water without thinking about the chemistry."
	"My uniforms are in the closet."
	"I slink out from under the sheets and stretch my back before dressing up."
	"Putting on a new school uniform feels like dressing in someone else's clothes."
	"The artificial smell of generic detergent invades my nose, but the feeling of fresh cloth against my back is a good one, a natural one."
	"It feels like a school uniform, as it should. It's not much different from what I used to wear before."
	"That goes for other things too. So far, this place seems more or less like a normal school."
	"Except for the people."
	"I think back to my talk with Kenji yesterday, Misha's constant laughter, and Shizune's sweeping sign language gestures."
	"Well, I've only met three students so far. Maybe they aren't that normal, but I'm sure others are."
	"Or, perhaps, people like them are what passes for normal around here?"
	"Yeah, what does pass for normal around here? What do people do?"
	"I didn't see a lot of kids hanging around after classes yesterday, so maybe there are clubs. If so, I wonder if I should join one."
	play music "bgm/blank.ogg"
	scene bg school_scienceroom_right
	"All through class, the question remains on my mind, so I decide to ask Shizune about it when we split into groups."
	"After all, she did say if I had anything I wanted to know, I should ask her."
	show shizu behind_blank at center
	shi "..."
	show shizu basic_normal at center
	shi "..."
	show shizu cross_wut at center
	"She crosses her arms and shifts her gaze slowly to Misha, who looks more preoccupied with trying to grind the eraser of her pencil down so that the top is perfect and evenly flat."
	show shizu cross_angry at center
	shi "..."
	scene bg school_scienceroom
	show shizu cross_angry at tworight
	show misha hips_grin at twoleft
	play music "bgm/Fripperies.ogg"
	mi "Ahaha~! Sorry, sorry, Shicchan~! Is there something you wanted from me?"
	show shizu basic_angry at tworight
	show misha perky_confused at twoleft
	mi "Oh~... I see! Hm... That's a good question, Hicchan."
	"My first thought is that means she doesn't know, which is worrying. Maybe I'm being too negative. Well, anyway, Misha, please don't prove me right."
	show shizu basic_normal2 at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Oh, that's right! Everyone is encouraged to join a club. A lot of people do so because there isn't really anything else to do."
	mi "There are also school events, like the festival coming up in a few days. Almost every student in the school tends to help out with it, doing whatever."
	show misha hips_grin at twoleft
	mi "So~! You actually transferred in at a busy time... maybe you can help out, too~!"
	hi "Sure."
	hi "What's the festival about?"
	show misha perky_confused at twoleft
	"Misha freezes."
	show misha hips_laugh at twoleft
	mi "...Wahahaha~! I don't know, Hicchan, the truth is it's a local event, and I'm not from this area, so..."
	show misha sign_confused at twoleft
	$renpy.pause(0.8)
	show shizu behind_blank at tworight
	$renpy.pause(0.8)
	show misha perky_confused at twoleft
	$renpy.pause(0.8)
	show shizu adjust_smug at tworight
	$renpy.pause(0.8)
	"She starts signing desperately to Shizune, asking her to bail her out. Shizune adjusts her glasses at the end of an oddly grandiose flourish and starts signing hard and heavy."
	show shizu adjust_happy at tworight
	shi "..."
	show misha sign_confused at twoleft
	mi "Huh? Oh."
	show misha hips_grin at twoleft
	mi "Who cares?"
	show misha hips_smile at twoleft
	"Misha puffs out her chest as she shouts Shizune's words out at me with a disproportionate amount of pride."
	"Too loud. I can see heads turning to look in our direction."
	hi "Not so loud..."
	show shizu basic_normal at tworight
	shi "..."
	show misha hips_frown at twoleft
	mi "Human beings evolve with each new generation! The ideals and beliefs behind a festival will inevitably change with time!"
	show shizu behind_frown at tworight
	shi "...!"
	show misha hips_grin at twoleft
	mi "Now, it's about delicious fried food and amusing little games that you play to win prizes~! Hahahaha~!"
	"The teacher clears his throat very loudly, batting his long wooden pointer against his other palm like a baton. He shoots a pointed gaze at us."
	show misha sign_sad at twoleft
	"Finally noticing where we are, Misha stifles a yelp and quickly quiets down. Shizune doesn't seem embarrassed at all, though, brushing it off without a care."
	show shizu basic_angry at tworight
	shi "..."
	show misha perky_confused at twoleft
	mi "We are in the middle of class, and should start working."
	show misha perky_smile at twoleft
	mi "That's right, Shicchan~!"
	show shizu basic_sparkle at tworight
	$renpy.pause(1)
	show misha sign_smile at twoleft
	mi "What? That's right~! Hicchan, are you asking because you're interested in joining a club?"
	show shizu behind_blank at tworight
	show misha perky_smile at twoleft
	"It could have been my eyes playing tricks on me, but I think I saw a suspicious glance exchanged between them. Misha's tone has also changed, although it does that every other word, anyway."
	hi "Yeah, I was thinking about it."
	"Misha and Shizune look at each other again."
	play music "bgm/blank.ogg"
	"I'm about to ask what they have in mind when something dark flutters in my peripheral vision, catching my attention."
	"Out of the corner of my eye, I see the girl with long, dark hair get up from her desk and slip silently towards the door."
	"It doesn't seem like she was working in any group, and no one seems to notice her but me."
	"I glance at the teacher, who's also looking at the dark-haired girl go."
	"Why doesn't he say anything?"
	show misha perky_confused at twoleft
	mi "Hicchan? Is something wrong?"
	"Do I look as uneasy as I feel?"
	"Or was Misha just looking at me looking after the girl who left?"
	hi "No, nothing."
	show shizu basic_happy at tworight
	shi "..."
	show misha hips_smile at twoleft
	mi "Okay~! Well, like we were asking, you don't have any plans for lunch today, do you?"
	"'I thought I would go to the library and pick up some books.'"
	hi "...Not really."
	show misha hips_grin at twoleft
	mi "Do you want to have lunch together then?"
	hi "Sure."
	show shizu behind_smile at tworight
	shi "..."
	show misha cross_laugh at twoleft
	mi "Yay~! Wahahaha~! Okay, Hicchan~! Perfect!"
	hide misha
	hide shizu
	"The rest of class passes uneventfully. The girl with the long hair never came back."
	"Before I have the time to put any more thought into where she could have gone, the teacher informs us that it's time to stop working."
	show shizu basic_frown at center
	"Shizune looks more than a little annoyed that we only just barely managed to finish all our work on time. I'm just glad we finished it at all; it's not a contest or anything."
	show shizu behind_frown at center
	shi "..."
	scene bg school_scienceroom_left
	show shizu behind_frown at tworight
	show misha hips_smile at twoleft
	play music "bgm/Generic_Happy_Music.ogg"
	mi "Yes it is, Hicchan!"
	hi "Impossible."
	mi "Really?"
	hi "Really."
	"I've noticed this before, but it's kind of funny how Misha is always moving her hands and signing not only everything she says, but what anyone else is saying at any given time."
	"Obviously, it must be so Shizune can understand it. Her eyes dart back and forth between Misha's hands and me."
	"I don't know who I'm supposed to be looking at. I'm talking to Misha, but that might be wrong; maybe I should face Shizune. I'm used to looking in the direction of the person whose voice I'm hearing, but really..."
	"Shizune can't hear me, but it would be disrespectful to talk to her only through Misha. Then again, isn't that what she's doing? No, she's at least looking at me. This is all very confusing and will take some time to get used to."
	hi "It's not a contest, because contests are competitions over a prize. If there's no prize on the line, it's not really a contest."
	show shizu basic_happy at tworight
	"Shizune's eyes flash dangerously with a competitive glare. She stares at me, as if surprised that I'm challenging her. I think maybe this is a contest to her."
	"I never noticed before how dark and blue her eyes are; it's truly an alluring gaze."
	shi "..."
	show misha perky_smile at twoleft
	mi "Are you sure, Hicchan?"
	hi "Very sure."
	show shizu behind_smile at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Hahaha! You're wrong, Hicchan. Because~!, I don't want to be the slowest one in the class. Therefore, what's on the line is my confidence in my abilities, and the prize is the satisfaction of proving them."
	show misha hips_laugh at twoleft
	mi "Wahahahaha~!"
	show shizu adjust_happy at tworight
	"Shizune pushes her glasses up the bridge of her nose in a very matter-of-fact way."
#	play sound "sfx/normalbell.ogg"
	hide shizu
	hide misha
	"I'd argue more, but the bell rings, and she quickly gets up and picks up her bag, looking at me expectantly."
	scene bg school_hallway3
	"I had almost forgotten that I was supposed to have lunch with them."
	show misha hips_smile at twoleft
	show shizu behind_smile at tworight
	$renpy.pause(0.5)
	show shizu adjust_happy at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Where do you want to eat?"
	hi "The cafeteria?"
	show misha hips_laugh at twoleft
	mi "Hahaha~! That's so plain... Okay~! Let's go!"
	"Plain? Well I guess..."
	play music "bgm/blank.ogg"
	"At my old school, I liked to eat outside, near the back of the building. It was a good spot, but I didn't find it until near the end of my freshman year."
	"I wonder if there is a similar place to eat here. Misha seems to imply as much."
	hide misha
	hide shizu
	scene bg school_cafeteria
	"Shizune and Misha pull me towards the cafeteria, which is surprisingly not packed. Maybe some students favor eating in classroom or outdoors. I saw some of my classmates had boxed lunches."
	"After we finish eating, Misha picks up where we left off earlier."
	play music "bgm/The_Student_Council.ogg"
	show misha perky_smile at twoleft
	show shizu behind_smile at tworight
	mi "So, Hicchan, you wanted to know about clubs and stuff, right?, right~?"
	show shizu adjust_happy at tworight
	shi "..."
	mi "Right, Shicchan! Okay, I guess it makes sense to ask first."
	show misha hips_smile at twoleft
	"Exchanging little nods of confirmation, they turn to face me again and Misha straightens her posture as if she is about to deliver a speech."
	mi "Hicchan, do you have anything you're really interested in?"
	hi "I used to play soccer, but I'm not really into it. I don't follow the teams and players or anything like that."
	hi "As of late, I usually just read a lot."
	show misha perky_smile at twoleft
	mi "Hm... There is a book club, right, Shicchan? Right! But~! It seems like they have all the members they can possibly have right now. Sorry, Hicchan... It's a really popular club."
	show shizu basic_happy at tworight
	shi "..."
	mi "Ah, okay! But, more to the point, Hicchan, does this mean that you don't have anything already in mind?"
	hi "Not really."
	show shizu adjust_happy at tworight
	shi "..."
	show misha cross_laugh at twoleft
	mi "Good! Great~! That's great, Hicchan! Really great! Hahaha~! Wahahahaha~!"
	hi "Why's it so great?"
	show misha cross_grin at twoleft
	show shizu adjust_happy at tworight
	mi "No reason."
	mi "Well, Hicchan, other than clubs and the upcoming festival, there is one other thing..."
	show misha hips_laugh at twoleft
	mi "Student Council!"
	"I see. I didn't know this school had a Student Council. That was a very melodramatic setup, though, just to tell me that."
	show shizu adjust_blush at tworight
	"I'm pretty sure the two of them know this, because Shizune looks a little embarrassed about it, and Misha is laughing."
	"Shizune quickly retakes control of the discussion, in a manner of speaking. After all, it's still Misha who has to voice whatever she says."
	show shizu behind_smile at tworight
	shi "..."
	show misha cross_grin at twoleft
	mi "Hahaha~! Hm? Right, right... Hicchan, maybe you should join the Student Council! They could use more people~. Yes! Definitely! You should definitely join!"
	hi "Why?"
	show misha cross_smile at twoleft
	mi "Well, for one, we could hang out every day, Hicchan~! Shicchan and I are both in the Student Council."
	show misha perky_smile at twoleft
	mi "Actually, Shicchan is the president."
	"Hm..."
	"I'm starting to get the suspicion that Shizune and Misha might not exactly be the most unbiased people to talk about this with."
	"As if reading my mind, Shizune quickly adjusts her glasses and signs something to Misha."
	show shizu adjust_happy at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Hahaha~! Of course, we're not trying to get you to join just because we would obviously benefit from you joining the Student Council and therefore have an incentive to try and get you to�"
	hi "So, you're admitting that�"
	show shizu behind_blank at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Ahaha~! No! We admit nothing~! I mean, Hicchan, of course it would be nice if you joined, and we'd appreciate it."
	mi "But even without all that, joining the Student Council shows a healthy interest in the workings of one's school."
	mi "Yup~! It's true, Hicchan. Besides, don't you want to spend time with us after school, Hicchan?"
	"I can't tell if she is being genuine or if this is just really good acting. Both of them seem to be trying hard to look their cutest, although they are already pretty cute to begin with."
	hi "Well..."
	show shizu adjust_happy at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "So it's settled, then. Welcome to the Student Council, Hicchan~!"
	hi "What? No. No!"
	show misha perky_sad at twoleft
	mi "Awww... See, Shicchan? Of course it wouldn't go so easily."
	show shizu adjust_smug at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Yup! That's right, though, it would be boring if it went that smoothly. Oh well~! Shicchan owes me candy now!"
	hi "You were betting on it? Hey, my life is not a game here!"
	show shizu basic_happy at tworight
	"Shizune seems very intrigued by this when Misha signs it to her. The aggressive glint returns to her eyes."
	shi "..."
	show misha cross_laugh at twoleft
	mi "Wahaha~! That's interesting, Hicchan. Let's play a game!"
	hi "That's not what I said."
	show misha hips_grin at twoleft
	mi "How about Rich Man, Poor Man, Hicchan? If you lose, you have to join the Student Council~!"
	hi "No, absolutely not."
	show misha perky_sad at twoleft
	mi "Aw~, why not?"
	hi "Well, because you two both have the same incentive, and therefore the same goal, which is to get me to join the Student Council, right?"
	show shizu adjust_smug at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Yup!"
	hi "Yeah, that isn't my goal. But what this means is that both of you can team up and I'll be at a clear disadvantage. So, I will have to decline."
	show shizu basic_angry at tworight
	shi "..."
	show misha hips_frown at twoleft
	mi "Hicchan! I'm very offended! Are you saying you don't trust us, and that we would pull something so d�dis�in�gen�u�ous...? That makes me sad..."
	hi "Sorry?"
	"It's hard to tell where Shizune's influence ends and Misha's thoughts begin."
	show shizu behind_frown at tworight
	shi "..."
	mi "In order to atone for hurting a young girl's feelings, you should definitely join the Student Council!"
	hi "No!"
	show misha hips_smile at twoleft
	mi "How about a game of paper football, instead of Rich Man, Poor Man?"
	hi "Paper football?"
	show misha hips_grin at twoleft
	mi "Yeah~! It's a game they play in America~! You make a paper triangle, and then you try to shoot it past goalposts that the other player makes with their fingers!"
	mi "Isn't it cool~? It's the ultimate form of competition between two people, Hicchan~!"
	show shizu basic_normal at tworight
	shi "..."
	mi "...And it's also played by elementary and middle school children, Shicchan? Wahaha! That means it's a game that really separates the boys from the men!"
	hi "More like the boys from the slightly older boys. Anyway, I'm not going to play that either. Just the fact that you know about it means you're probably surprisingly good at it."
	show misha cross_laugh at twoleft
	mi "Hahaha~! Yeah yeah~, that's true! How did you know, Hicchan?"
	show shizu behind_frown at tworight
	show misha cross_grin at twoleft
	"Shizune frowns at Misha, telling me that she probably wasn't supposed to admit that so readily."
	"I wouldn't say that I'm happy with their attempts to get me into the Student Council, but I'm a little curious about what the Student Council does here."
	"I've never been on one before, or even known anybody who was a member, so it interests me. I also kind of like Shizune and Misha, so maybe it wouldn't be so bad."
	show shizu behind_blank at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Okay, Hicchan, how about Risk? The game of world domination!"
	hi "I don't know what that is."
	show misha hips_smile at twoleft
	mi "It's really fun, Hicchan. You fight for control of the world, with armies and everything."
	"Sounds like Shizune would be good at it."
	mi "If you want to play, we can after school."
	show shizu basic_normal at tworight
	shi "..."
	mi "Ah, really, Shicchan? We can play just for fun, Hicchan. Shicchan hasn't played in a long time, so if you want to, there are no strings attached~!"
	hi "Well, okay..."
	show misha perky_smile at twoleft
	mi "Okay! Okay, okay~! Perfect~! We'll see you after school in the student council room, then, Hicchan!"
	hi "Wait, why there?"
	show misha hips_grin at twoleft
	mi "Because~! That's where we keep the game."
	show misha cross_laugh at twoleft
	mi "Wahahahaha~!"
	"I grimace to tell them how much I do not like this, but it's more for show than anything."
	"So in the end I agree, but only after getting Shizune to acknowledge that I don't mean anything concrete just by accepting to take a look around and play a game with her."
	"Lunch ends, and we go back to class."
	hide shizu
	hide misha
	play music "bgm/blank.ogg"
	scene bg school_scienceroom
	show hanako def_worry at offscreenright
	""
	hide hanako
	"During afternoon classes, the long haired girl comes back and sits down in her seat without a word."
	"Again, no one seems to notice, or if they do, no one says anything. I want to ask Misha about it, but I don't want to be nosy."
label en_A6:
	scene bg school_lobby_left
	show shizu behind_smile at tworight
	show misha hips_grin at twoleft
	play music "bgm/Ease.ogg"
	"After school, Shizune and Misha quickly find me by the first floor lobby and latch onto me, covering each flank in case I might try to escape."
	"I feel a little offended, but I'd been considering it. Nevertheless, I'm a bit disturbed that enough people have made a break for it in the past that they're on their guard."
	hi "What's with the escort? This doesn't make me feel very comfortable."
	"In fact, it makes me feel like a dangerous prisoner being transported to his cell."
	show misha cross_laugh at twoleft
	mi "Wahahaha! What's wrong, Hicchan?"
	show shizu adjust_smug at tworight
	shi "..."
	show misha cross_grin at twoleft
	mi "That's right, we're just going to go play a game of Risk, remember?"
	"I don't know, Misha, this all seems a little sinister to me. I start thinking that when we sit down to play the game, they'll tie me down and torture me until I agree to join the Student Council."
	"Well, that's highly unlikely, but still... For some reason, it just seems like it would be so plausible..."
	hide misha
	hide shizu
	$renpy.pause(0.2)
	scene bg school_lobby_right
	"Getting to the student council room is as simple as turning two corners from where we started."
	hi "What? That's it? This makes you guys being so on top of me seem a little silly."
	show shizu basic_normal2 at tworight
	show misha perky_smile at twoleft
	shi "..."
	show misha hips_smile at twoleft
	mi "That's not true, Hicchan, Shicchan says that when their life is threatened, people have shown the capability to pull off superhuman bursts of speed."
	hi "'Life is threatened'?"
	show shizu behind_smile at tworight
	"Her expression unchanging, Misha signs something amusedly to Shizune, who makes a baffling face and puts her hands behind her back, looking pleased with herself."
	show misha hips_grin at twoleft
	mi "Mm~ hm hm hm~..."
	"Misha feigns deafness and hums cheerily. Stop that, I know you heard me; you have no excuse, unlike Shizune."
#	play sound "sfx/dooropen.ogg"
	hide misha
	hide shizu
	scene bg school_council
	"Shizune opens the door to the student council room. It's a very plain, sparsely decorated room, although it is quite large, maybe even a little larger than a classroom."
	"There's a big table in the center surrounded by chairs, and a smaller desk prominently placed in the back that I assume is Shizune's. There are a few regular desks and chairs stacked to one side, as well. Extras, perhaps?"
	"Aside from the tables and chairs, the room doesn't have much else to offer. Just a couple of filing cabinets and bookshelves stacked with old school records and documents. Not much else. In fact, nothing else."
	"This is... a pretty bleak room. They could at least put a potted plant in here, or something. But the most noticeable thing that this room doesn't have is other people."
	hi "Are we early?"
	show shizu behind_blank at tworight
	show misha hips_smile at twoleft
	shi "..."
	show misha hips_grin at twoleft
	mi "No~."
	hi "What do you mean 'no'? Does it mean nobody else is coming today?"
	show shizu adjust_smug at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Yeah, that's right~."
#	play sound "sfx/snap.ogg"
	show shizu basic_happy at tworight
	"Before I manage to ask why that's the case, Shizune claps her hands together very energetically."
	show shizu adjust_happy at tworight
	shi "..."
	show misha hips_smile at twoleft
	mi "Hicchan, let's play Risk! Come on, you promised, didn't you? You have to~!"
	show misha hips_grin at twoleft
	mi "Hahaha~! Okay okay okay~! Do you want to know the rules? We can explain to you while we set everything up!"
	hide shizu
	"While Misha is talking, Shizune takes out what looks like a board game from behind one of the filing cabinets and throws it on the table."
	"Actually, this looks kind of interesting."
	show shizu adjust_frown at tworight
	"After Misha spends a little too long for her liking running through the basics with a somewhat vague and confusing tutorial, Shizune cuts in and declares the game has started with a decisive motion, slicing her arm through the air."
	"Shizune's aggressiveness is rubbing off onto me. I start feeling more competitive than I intended to be when I agreed to this."
	show misha perky_smile at twoleft
	show shizu basic_normal2 at tworight
	play music "bgm/Hokabi.ogg"
	"Halfway into the game, while I try to ponder how to defend against Shizune's assault from two fronts, she breaks my concentration by drumming her fingers on the table to get my attention."
	show shizu behind_frown at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Hicchan, Shicchan wants you to know that you are taking too long to make a move."
	show misha hips_smile at twoleft
	mi "Shicchan also says that she will let you keep Australia if you agree to join the Student Council~!"
	hi "I thought this was a game with no strings attached."
	"Just the fact that she would dangle that over my head as an offer means that she knows I care about the outcome of this game."
	hi "And anyway: No!"
	show shizu adjust_smug at tworight
	shi "..."
	mi "Shicchan admires your fighting spirit and would be a benevolent dictator who will spare your people if you agree to join the Student Council~!"
	show misha cross_laugh at twoleft
	mi "Hahahaha~!"
	show misha cross_grin at twoleft
	hi "You're so competitive, Shizune."
	show shizu adjust_happy at tworight
	"She seems to take this as a compliment."
	hi "I would expect the Student Council president to be a little more magnanimous."
	show misha perky_confused at twoleft
	mi "Mag�nan�i�mous...?"
	"She doesn't seem to know what the word means or how it's signed, so she pulls out a piece of paper and writes it for Shizune, who in return signs it back to Misha."
	"Misha presses her index fingers against her temples, as if trying to physically imprint the word into her memory."
	show shizu basic_happy at tworight
	shi "..."
	"Suddenly, Shizune bursts into a flurry of gestures. Misha looks daunted by the pace of her heated signing."
	show misha sign_confused at twoleft
	mi "Ah, wait, please slow down, Shicchan... Um, Hicchan~! Shicchan says you're going to lose!"
	hi "Tell her I will crush her world empire with my rebellion."
	mi "Ah... Okay..."
	show shizu basic_sparkle at tworight
	"Those eyes of hers shine with childlike mischief."
	show shizu basic_happy at tworight
	shi "..."
	show misha cross_smile at twoleft
label en_choiceA6:
	mi "She says you have no chance if you keep playing like this, no you won't~!"
	menu:
		"Attack aggressively!":
			jump en_A6a
		"Play defensively.":
			jump en_A6b
label en_A6a:
	$attractionSC = attractionSC+1
	"She is either really mocking me, or trying to trick me."
	"I have nothing else to lose, though, so I might as well try something different."
	"Maybe if I spread out my forces and try to control more territories, I can recoup the advantage."
	"Shizune seems to focus on conquering whole nations, so maybe I can sacrifice my hold on continents to gain more small countries."
	"It's worth a shot."
	"A few turns later, I end up losing the game anyway."
	show shizu adjust_smug at tworight
	"Shizune adjusts her glasses victoriously and allows herself to tentatively pump a fist in the air in celebration."
	shi "..."
	show misha cross_grin at twoleft
	mi "I win, I win~! Yay~!"
	hi "There's no need to translate that, it was pretty clear."
	show misha hips_grin at twoleft
	mi "Wahaha~! Don't look so sad, Hicchan~! You were really giving it your best, that's what I thought!"
	mi "Sometimes, your best just isn't good enough, though~. If anyone knows that, it's me~! You did very well for someone who just learned how to play today!"
	show shizu behind_smile at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Hicchan, you attacked Iceland and North America at the same time, that's a very daring move. Shicchan is impressed~!"
	shi "..."
	show shizu adjust_smug at tworight
	mi "The mark of great people is that they are daring, and that they can follow through~! You're already halfway there; isn't that great, Hicchan?"
	show shizu adjust_happy at tworight
	shi "..."
	mi "That isn't enough though; just potential isn't enough! There is no point to potential if you don't take the first step, and there is no point to that if you don't keep going. I want to see more."
	show misha perky_confused at twoleft
	mi "You're right, Shicchan~, but, that's so demanding..."
	shi "..."
	mi "..."
	show shizu basic_normal2_close at tworight
	play music "bgm/blank.ogg"
	"Shizune leans forward, suddenly looking a lot less playful and more like the serious person I expected her to be from the start."
	shi "..."
	show misha hips_smile at twoleft
	mi "Hicchan, would you like to join the Student Council?"
	"She really doesn't waste any time, does she? But..."
	"It's only my second day of school, so I'm hesitant about committing to something so early."
	"I haven't even taken a look at any other clubs yet."
	"But spending time with Shizune and Misha doesn't seem like something I would hate."
	"I still need more time to think about it before I decide for sure."
	hi "Maybe. I'll get back to you on it."
	play music "bgm/The_Student_Council.ogg"
	show shizu behind_blank at tworight
	shi "..."
	show misha hips_frown at twoleft
	mi "Okay, Hicchan~! But, I hope you're not just saying that so we don't feel bad."
	hi "No, really."
	show misha perky_smile at twoleft
	mi "Really~?"
	show misha hips_grin at twoleft
	mi "Hicchan, if you're going to say that, you're saying that it is definitely the truth, and there can't be any~ mistaking it~!"
	hi "I know, I know. I guess I should have my revenge for losing, at the very least."
	show shizu basic_sparkle at tworight
	"Shizune smiles at that in a mischievous way that feels like twisting the knife in the wound of my loss."
	jump en_A6c
label en_A6b:
	"It's likely that she's just trying to psych me out."
	"Looking at the board again, I have a pretty good defense set up, and I'm not going to wreck it doing something reckless."
	"A few turns later, I lose the game anyway."
	show shizu adjust_smug at tworight
	"Shizune adjusts her glasses victoriously and allows herself to tentatively pump a fist in the air in celebration."
	shi "..."
	show misha hips_grin at twoleft
	mi "Wahahaha~! Hicchan, you lost when you allowed me to take North America."
	show misha perky_confused at twoleft
	mi "I mean, Shicchan, not me."
	show shizu behind_frown at tworight
	play music "bgm/blank.ogg"
	shi "..."
	show misha perky_smile at twoleft
	mi "Getting control of North America is ambitious, because it provides a five army bonus, but you can attack it from three fronts, so you must defend them all~!"
	show shizu behind_frustrated at tworight
	shi "..."
	mi "I thought you'd have more guts. How disappointing."
	mi "Ambition, Hicchan, your play needs to be more daring! Ambition, ambition~!"
	show shizu basic_frown at tworight
	shi "..."
	mi "I was really excited when you took South America, but then you switched to playing defensively just because you gained a small advantage. That's no good, Hicchan."
	mi "You didn't take enough risks, and when you did, you didn't follow through. That's terrible, Hicchan."
	"Damn, what's it to her if I played too carefully? There's no need to rub it in my face."
	show shizu basic_normal2_close at tworight
	shi "..."
	mi "I wonder if you'd even be any good for the Student Council..."
	play music "bgm/School_Days.ogg"
	"What's this, reverse psychology?"
	hi "I guess I don't have to worry about joining or not in that case."
	shi "..."
	mi "Giving up just like that? I expected more of you."
	"Seriously, is Shizune trying to taunt me into joining the council?"
	"Besides, I don't even want to join. It's only my second day, I can't make that kind of commitment."
	"I haven't even taken a look at any other clubs yet. And these two, they're a little weird."
	hi "Fine, I'll consider joining the council, but I want to take a look at the clubs before I decide."
	show misha perky_confused at twoleft
	mi "Really, Hicchan? You're not just saying that to make us feel better?"
	hi "Yeah yeah, I'm just not sure that I want to."
	show misha perky_sad at twoleft
	mi "Aw..."
	show shizu behind_frown at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Okay, Hicchan, but we're not going to give up so easily. You said 'maybe'; there's still a chance you'll come around~!"
	show shizu basic_angry at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Come on, we could really have fun! We could play more Risk and maybe one day you could beat me, unless we graduate before that."
	hi "That doesn't make me feel any less reluctant about joining, you know."
	show shizu behind_blank at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Wahaha~! Surely you are not that horrible at board games? Maybe we can play a game you know then, to give you a handicap."
	hi "I might have said that just to make you feel better, after all."
	show misha perky_sad at twoleft
	mi "Awww, that's cold, Hicchan..."
	jump en_A6c
label en_A6c:
	"I take a glance at the clock on the wall and realize I've spent far longer playing Risk than I expected."
	hi "Sorry, I think I have to go. I wanted to go to the library. It's not closed yet, is it?"
	show shizu behind_blank at tworight
	"Shizune scratches her head and gestures at Misha."
	"How hard can it be to determine whether the library is open? There's a clock right there on the wall."
	shi "..."
	show misha perky_confused at twoleft
	mi "It should be, unless the librarian is absent."
	mi "I think you're right, Shicchan."
	show misha hips_smile at twoleft
	mi "We... think the library is open. It's on the second floor; can't miss it. Do you want us to show you where it is?"
	hi "No thanks, it's okay. See you tomorrow."
	show misha hips_grin at twoleft
	mi "Bye bye!"
	play music "bgm/blank.ogg"
label en_A7:
	scene bg school_staircase2
	$renpy.pause(1.5)
	scene bg school_hallway2
	"One flight of stairs up and I run into problems."
	"The second floor hallway is a carbon copy of the third floor one."
	"Wide, of course; and plain, like only hallways can be."
	"The problem is that the library's whereabouts are not as easily determined as one would think."
	"The classrooms are marked with signs stating which class they belong to, but then there is a plethora of other, unmarked rooms."
	"Is the library one of them? Or is it just somewhere down the hallway?"
	"I bet on the latter and choose my direction at random."
	"After I turn around the corner, an unmarked door draws my attention because it's not closed."
	"It's not open either though, just barely ajar so that I can see it's open and nothing else."
	"It would make sense for the library door to be invitingly open, and while this one is not quite that, it's good enough."
	"At the very least it means that someone is inside and I can ask for directions no matter how embarrassing that is."
	"I gingerly push on the center of the door with my fingertips, every muscle in my arm ready to pull back at a moment's notice."
	"The feeling of being an outsider to this school can't be shaken from my mind, so much so that I instinctively fear doing something wrong by entering."
#	play sound "sfx/door_creak.ogg"
	"The door slowly creaks as if groaning from a deep sleep, though is much easier to open than I'd anticipated."
	"Leaning over and poking my head ever further inside to gain sight of the room as fast as possible, the meek 'Hello...?'' on my lips is quickly snatched away."
	scene white
	play music "bgm/Concord.ogg"
	scene ev lilly_tearoom
	"..."
	"This is... not as I was expecting."
	"I mindlessly let the door open to its full extent, taking in the sight of the solitary figure taking center stage in the otherwise abandoned room."
	"The situation steals my voice, leaving me standing at the doorway staring at the beautiful girl."
	"Evidently having taken her time to assess the situation, the girl gently puts down her teacup and opens her eyes, but doesn't look at me."
	scene ev lilly_tearoom_open
	li_ "Hello there. May I help you?"
	"Staring directly in front of herself, the movements of her lips seem to break the silence rather than the words."
	"However it's the soft, measured voice that reminds me she's a being separate from the room itself."
	"Not only is she likely the tallest girl I've ever laid eyes on, but even among the foreigners I've met she's strikingly distinct."
	hi "Uh, hi. Sorry for intruding, I was just... kind of lost."
	"She takes a moment to formulate a response before speaking. Every action she takes feels as if it's carefully choreographed beforehand."
	li_ "Care to take a seat?"
	"...unexpected, considering that I'm intruding upon her."
	hi "Ummm... thanks."
	"I slowly step towards another seat opposite her, the girl resting the teacup and saucer on the wooden table inbetween."
	"The way she doesn't track my movements with her head is telling... that, and the slight cloudiness to her eyes means she must be at least partially blind, like Kenji."
	"Come to think of it, her voice doesn't have any detectable accent either. I guess she must be half-Japanese."
	"As I take my seat, her composure takes me slightly off-guard. Her air of relaxed confidence makes the silence entirely comfortable."
	scene ev lilly_tearoom
	"The calming atmosphere is so very different from the student council office."
	li_ "I take it you're a new student to Yamaku?"
	hi "Ah, yeah. I just transferred in yesterday."
	"I get the distinct feeling my speech patterns don't match the formality of hers, accentuated by her restrained bow of greeting."
	"One which I hasten to match, before realizing the futility of the action."
	scene ev lilly_tearoom_open
	li_ "I'm Lilly Satou. Pleased to meet you..."
	hi "Hisao. Hisao Nakai."
	"She gives a nod before gesturing roughly in the direction of her teacup."
	li "Would you care for a drink?"
	hi "Sure."
	"As much as it pains me, I can't keep step with her formality in the proceedings."
	"She gives a kind nod, taking the request in stride."
	scene bg school_miyagi
	"Without another word, she steps off the chair and prepares a second cup of tea from a collection of supplies laid out along a shelf."
	"A brush here, a brush there, her left hand often lightly touching the side of whichever container she's pouring into... it seems to be a process she's followed dozens of times before."
	"As I lean sideways to see around her back, she seems to use her long, dainty finger to measure the right amount of water in the cup."
	"It's one thing to see the different disabilities the students in my class have, but it's quite another to see how everyone seems to adapt."
	"Shizune and Misha have no problem working together to communicate to me, and Lilly herself seems to have workarounds for problems I'd never thought of."
	"While I feel slightly guilty about her doing the work, she seems pleased to be following the 'correct' process of the offerer preparing the drink."
	li "So,"
	"Her soft voice brings me out of my silent observance."
	show lilly basic_smile
	li "Which room were you looking for? It's not often this classroom is visited after school."
	hi "The school library. Shizune and Mi� I mean, some classmates, told me it was on this floor."
	"She finishes pouring water into the teacup as she nods, a small metallic tapping coming from the teacup indicating it being stirred."
	li "I'm aware of Miss Hakamichi, as are most students. To be with them means you're in class 3-3, no?"
	hi "That's right. In the science room with Mutou."
	show lilly basic_giggle
	"She gives a small giggle before setting down the teaspoon and slowly walking towards the table, teacup and saucer in hand."
	li "He's quite a character. I imagine you'll come to like him; most do."
	scene bg tearoom_lillyhisao_noon
	show tearoom_hisao smile
	show tearoom_lilly smileclosed
	"As she sets down the tea, I gently take it and have a sip. I'm really more of a coffee person, but this seems like a rather bad moment to bring it up."
	"Nonetheless, the smell's quite nice. I hardly think it'd be hard to choke down."
	show tearoom_hisao relief
	hi "Thanks, Satou. It tastes really nice."
	show tearoom_lilly ara
	"She smiles and quickly waves her hand in front of her face."
	li "Lilly, please. There's no need to be too formal."
	"She says this in spite of her exceedingly well-bred speech. Oh well."
	"I guess I should try and ask her about herself, as it really does seem as if she's catering to me."
	show tearoom_hisao smile
	hi "So which class are you from? I imagine it's one of the third-year classes."
	show tearoom_lilly smileclosed
	li "Correct, I'm in class 3-2; which is on the third floor, same as yours. It's taught by Miyagi, and is specifically for both blind and partially blind students."
	hi "I see."
	hi "I see. Ah, I mean, uh, s-sorry..."
	show tearoom_hisao oops
	"I feel like slapping myself for the faux-pas. Looking at her face, though, she doesn't seem in the least bit put off by it."
	show tearoom_lilly ara
	li "My my, there's no need to change your speech on my account."
	show tearoom_hisao unsure
	hi "Ah, sure. Sorry, I guess I'm really showing my newness here."
	show tearoom_lilly weaksmile
	li "An environment like this would be a big change, so I can't fault you for it. While the same can't be said for everyone, many have come to terms with their conditions."
	"A category which would include her, it seems. All too ready to jump ship from this particular topic, I segue into another."
	show tearoom_hisao smile
	hi "Do you come here to drink tea often? It's a really nice place."
	"Thinking on it, this might be her version of the place behind my school that I liked to have lunch at."
	show tearoom_lilly smileclosed
	show tearoom_hisao think
	li "I come here fairly often during lunch times. My duties as class representative don't leave enough time for an 'official' club, so a friend and I use this room for having tea."
	"Class representative, huh?"
	"Compared to Shizune, her mannerisms seem to be almost completely opposite. While Shizune's blunt and fiercely driven, Lilly seems relaxed and calm, almost aloof."
	"Come to think of it, she might be useful for a less biased view of the school's clubs."
	hi "What kinds of clubs are there to join?"
	show tearoom_lilly thinking
	li "Hmm... the more popular ones are the track and field club, which uses the field near the school during lunchtimes, the baseball club, and the book club in a room near the library."
	li "There are also numerous small ones too, though, such as the art and music clubs."
	"At a time when I'm just wanting to get on my feet, rushing into a club right away seems slightly unappealing."
	"I wonder if this school shares the same rule as my old one..."
	hi "Is it compulsory to join a club?"
	show tearoom_lilly smileclosed
	li "It isn't, though it is encouraged."
	show tearoom_hisao sigh
	hi "Ah, good. That's a relief."
	play music "bgm/blank.ogg"
	show tearoom_lilly giggle
	"I've really let down my guard around this girl to let such a thing slip out. The fact seems to slightly amuse her."
	"Not wanting my tea to get cold, I finally start drinking it as Lilly does the same."
	scene bg tearoom_lillyhisao_sunset
	show tearoom_hisao outside
	show tearoom_lilly smileclosed
	play music "bgm/Afternoon.ogg"
	"As I look over to the window over her shoulder, I notice the light coming into the room has a distinctly orange tint."
	"Even here, time doesn't stand still."
	hi "Huh, the time's gone quickly."
	show tearoom_lilly thinking
	li "Sorry?"
	"Right. She's blind. Of course she can't see the sun setting."
	show tearoom_hisao smile
	hi "It just looks like the sun's starting to set."
	"It seems to come as a surprise for her. I guess she must have lost track of the time."
	show tearoom_lilly weaksmile
	li "Sorry, Hisao. I didn't mean to keep you from the library for so long."
	"I quickly move to allay her concern."
	show tearoom_hisao calm
	hi "Ah, no, it's okay. The library's still open, isn't it?"
	"She pauses, and takes a moment to think on it."
	"It's probably something I should've asked Shizune when I had the chance, but Lilly seems likely to know in any case."
	show tearoom_lilly thinking
	$renpy.pause(0.25)
	show tearoom_lilly smileclosed
	$renpy.pause(0.25)
	li "True. It's open until six-thirty during weekdays."
	"A quick glance at my watch confirms I have well enough time to get there."
	show tearoom_hisao smile
	hi "Hmm, I might get going in that case. It's been nice talking with you, Lilly."
	show tearoom_lilly smileclosed
	"She smiles and gives a deep nod, her hands still neatly folded on the table in front of her."
	li "It was my pleasure."
	show tearoom_lilly thinking
	li "Oh, come to think of it... shall I show you to where the library is?"
	hi "I couldn't possibly ask for more help. I should be able to find it all right."
	"Well, unless my navigational skills fail me.{w} Which they seem to have a habit of doing."
	show tearoom_lilly smileclosed
	li "It's all right, I was going to be talking to the librarian there in any case. I could introduce you."
	"This gets better and better. It's pretty hard to deny her offer."
	hi "If you're sure, then that'd be great. Thanks."
	scene bg school_miyagi
	show lilly cane_smile at center
	"As she stands up to follow me, she takes hold of a straight, retractable cane that had been slipped in the handle of her bag on the floor."
	"Compared to the cane the boy in my class had, Lilly's looks much thinner and longer. His must be for support, whereas Lilly's is for navigation."
	"Together we leave the peaceful room and enter the empty hallway on the way to the library."
	play music "bgm/blank.ogg"
	scene bg school_hallway2
	"Side by side, my pace carefully slowed to match hers, we slowly walk through the hallway."
	"It doesn't take long for us to arrive at the door to the warm-looking room, apparently situated in the center of the floor rather than either wing."
	hi "Ladies first."
	show lilly cane_smileclosed at center
	"She gives an appreciative smile at the gesture, taking the lead as we file in."
	hide lilly
	scene bg school_library_ss_right
	play music "bgm/Fripperies.ogg"
	"To the left is the wooden library counter, with the library proper being on the right."
	"It easily dwarfs my old school's library, with the distinct smell of old books giving the place an almost old-world air."
	"There don't seem to be a lot of students here. Considering the time, it isn't a big surprise; everyone's probably either in the school grounds or the dorms."
	show lilly cane_smileclosed at center
	li "Yuuko, are you here?"
	"She says it to thin air since the librarian doesn't seem to be present and of course Lilly can't see this."
	"What's unexpected is that it draws a reaction."
#	play sound "sfx/impact.ogg"
	show lilly cane_surprised at center
	"Something from under the counter thuds against it, followed by a quiet wail."
	mystery "Awwww."
	scene bg school_library_ss
	show lilly cane_weaksmile at twoleft
	show yuuko neutral_down at tworight
	"The origin, apparently the librarian, quickly crawls out and bounces up to extremely rigid attention."
	show yuuko neurotic_up at tworight
	yu_ "Hi, Lilly. How can I help you?"
	"Her voice is strained in a failing attempt to sound casual and she's rubbing the back of her head."
	li "Good afternoon. What happened just now? I heard a strange sound."
	show yuuko worried_up at tworight
	yu_ "It's nothing, I just hit my head."
	yu_ "See, I dropped an eraser under my desk and while I was looking for it a pencil dropped and when I was looking for both of them you came and surprised me..."
	show lilly cane_sad at twoleft
	li "Are you all right? I'm sorry, I couldn't know�"
	show yuuko neurotic_up at tworight
	yu_ "It's okay! It's okay, sorry for making you worry."
	show yuuko smile_down at tworight
	show lilly cane_weaksmile at twoleft
	yu_ "This is nothing, I've had worse happen to me."
	"She's quick to reverse Lilly's apologies, almost frantically trying to push aside the possibility that she could be in any way inconvenienced by bashing her head on the counter."
	yu_ "Yes... worse things have happened, hehehe..."
	"The girl fidgets with her fingers as Lilly doesn't seem to drop her concerned expression, and then she shuffles some papers around the counter for no reason."
	"A little shorter than Lilly, replete with glasses, freckles and a very troubled look, she seems to fit a library perfectly."
	show yuuko happy_down at tworight
	yu_ "Ah, Lilly! Did you get my message?"
	show lilly cane_reminisce at twoleft
	li "Message... hmm..."
	show lilly cane_smile at twoleft
	li "Oh, the two imported books that arrived?"
	yu_ "Right! Right! They finally came! I can't believe it took so long, but�"
	"Amidst her celebrations, partially for managing to change the topic I'm sure, she notices me from the corner of her eye and freezes on the spot when she does."
	show yuuko panic_up at tworight
	show lilly cane_weaksmile at twoleft
	yu_ "Oh no, I'm sorry for not noticing you before!"
	yu_ "Did you need to check out a book? Or return one? I'm sorry! I'm sorry!"
	"The way she can so quickly shift between moods is a little unsettling."
	show yuuko worried_up at tworight
	show lilly cane_smileclosed at twoleft
	li "He's with me. Yuuko, this is Hisao, a new student. Hisao, this is Yuuko, the school librarian."
	hi "Pleased to meet you."
	show yuuko neutral_down at tworight
	yu "Hisao. Right. Hisao. Pleased to meet you, too. Hisao."
	"For a second she visibly attempts to engrave the name on her mind so she won't forget."
	li "Yuuko often arranges to import foreign books in Braille for me."
	li "Would you like to tell Hisao a little something about the library?"
	"Lilly's innocent suggestion is met with an expression of abject terror."
	show yuuko panic_up at tworight
	yu "I... Please Lilly, I can't. I don't know what he could be interested in. This is too much responsibility."
	"How it's any responsibility at all I don't get, but her objection is so sincere I don't doubt for a second that she would rather disembowel herself on the spot than tell me where the light novels are."
	show lilly cane_sleepy at twoleft
	li "But..."
	hi "So, there are a lot of books in Braille here?"
	"I attempt to save the day by asking the first thing that pops into my head. It seems to work at least partially, as Yuuko seems to... not exactly relax, but at least look slightly less tense."
	show yuuko smile_down at tworight
	show lilly cane_weaksmile at twoleft
	yu "Well... I think about a third or a fourth of Yamaku's library is either in Braille or audio."
	"Makes sense, given all the blind students that'd be here."
	hi "If it's only that, how come this library is so big in the first place?"
	yu "Ummm, well, we get a lot of new books regularly because the library is adequately endowed. That's probably why."
	show yuuko neurotic_up at tworight
	yu "They spend more on new books than on my salary, and then I have to organize and shelve all of them."
	show yuuko worried_up at tworight
	yu "It's so troublesome and they weigh so much, I wish I could quit this job."
	"..."
	"A very awkward silence follows this revelation of too much information."
	hi "Umm, I'll go check the aisles then, if you don't mind."
	"It's probably best for all of us if she doesn't keep talking to me."
	show lilly cane_smileclosed at twoleft
	li "Very well. Meanwhile, Yuuko, I would have those books if it's all right with you."
	play music "bgm/blank.ogg"
	hide yuuko
	hide lilly
label en_A8:
	scene bg school_library_ss
	"My first impression was right; the library is surprisingly big."
	"Ambling down the narrow aisles, I study the spines of the books in random order, occasionally sliding one out to read the blurb, taking it with me if it looks good."
	"In a few moments I have a respectable stack of books in my arms."
	"I guess I'll never be stuck for choice in here."
	"The normality of the library sinks in. Sure, there are large-print and Braille books scattered throughout, but it is what it is: a library."
	"It's as if the calm mood from the room I had tea with Lilly in snuck with us in here, unless it was here to begin with."
	"Something about that puts me at ease, just like before."
	"I reach the end of the aisle and find a collection of desks, set up for study or personal reading. Going a little further, though, I discover a nice quiet corner at the back."
	"While the rest of the library has the odd student sitting at a desk either reading or stealthily sleeping, the back is pretty much deserted."
	"As I glance around, I see someone who I recognize sitting on one of several beanbags."
	scene ev hana_library_read
	play music "bgm/Everyday_Fantasy.ogg"
	"It's the dark-haired girl from my class. The one who snuck out of the classroom earlier."
	"She's reading a book, keeping it close to her face which makes her look like she's really into it."
	"From the way she was acting today, I had her pegged as more of a delinquent than a bookworm. In fact, her mysterious disappearance from the class raises all sorts of whys in my head."
	"Intrigue floats slowly but surely towards the surface, and before I know it I'm walking towards the mysterious long-haired girl."
	"I guess there's no harm in introducing myself as I would with anyone else. She's a classmate after all."
	"Walking over to another beanbag, I take a seat and lay my books beside it."
	scene ev hana_library_gasp
	"The girl starts, looking scaredly up at me from underneath her fringe."
	"This is the first time I've seen her this close. Underneath her long, dense bangs, I can see that part of her face, at least a third if not a half, is pretty badly scarred."
	"My eyes are immediately drawn to the scars, subconsciously peeking past her hair until they meet her own eyes."
	"For a second, I am shocked, and divert my eyes to the book in her hands, before I realize that looking away probably only makes it worse."
label en_choiceA8:
	"It takes too many seconds to collect myself and remember what I walked up to her for."
	menu:
		"Hi! I'm Hisao Nakai.":
			jump en_A8a
		"I didn't mean to startle you.":
			jump en_A8b
label en_A8a:
	$a8aTrigger = true
	hi "Hi! I'm new here. Hisao Nakai. We're in the same class."
	"..."
	hi "Umm... I just transferred here the other day. Maybe you don't remember?"
	"..."
	if a1bTrigger == true:
		jump en_A8aa
	elseif a1bTrigger == false:
		jump en_A8ab
label en_A8aa:
	hi "I did a self-introduction too."
	"..."
	jump en_A8ab
label en_A8ab:
	scene ev hana_library
	"The girl still doesn't say a word, but simply stares at me, wide-eyed."
	hi "I'm still getting used to the place so I'm trying to meet as many people as I can."
	hi "So, er... what's your name?"
	ha_ "H... Hanako..."
	"Her speech is stuttering and so quiet that it is barely audible even in the still library."
	"Somehow I think that my 'delinquent' impression of her was wrong."
	hi "Hanako, eh? So what are you reading?"
	scene bg school_library_ss
	show hanako emb_downtimid at center
	"She gently tips the book backwards so that I can read the title, at the same time hiding her face behind it."
	"She must have noticed me staring before."
	hi "'Life of Pi'? I've never heard of it before. What's it about?"
	ha "A boy... and a tiger..."
	ha "...on a boat..."
	"I can see this taking some time."
	hi "Sounds interesting. Is it any good?"
	"She nods from behind the book, but stays silent."
	"She looks kinda tense. A bit like Yuuko earlier, but in a different way. More like... petrified with terror, I'd say."
	"So the mystery delinquent girl turned out to be anything but, and she is quivering in a way that makes it look like she is mortally afraid of me."
	"The only way out of this, as far as I can tell, is to try to get a normal conversation going."
	hi "Is it a library book? I'm looking for new ones to read, but there's just so many..."
	show hanako emb_sad
	ha "N-no. It's mine."
	hi "Oh. So... do you come here often?"
	play music "bgm/blank.ogg"
	"..."
	show hanako emb_blushtimid
	"A huge, huge blush spreads on Hanako's face and her eyes widen far larger than I thought it was possible for eyes to do."
	"Uh-oh. Did she interpret my lame attempt at small talk as a feeble attempt to pick her up?"
	hi "I mean... ehh... I didn't mean it like that..."
	jump en_A8c
label en_A8b:
	$attractionHanako = attractionHanako+1
	hi "Sorry, I didn't mean to startle you."
	ha_ "It... it's okay."
	"The girl certainly doesn't look like it's okay, but I let it slide."
	hi "So, umm... do you mind if I sit here?"
	"She seems to be very uncertain whether it's okay or not for me to sit, but finally she nods, just a little."
	scene ev hana_library
	ha_ "O... okay."
	scene ev hana_library_read
	"I take the seat next to her, and she hides herself behind her book."
	"'Life of Pi'... Never heard of it."
	hi "So, errr... sorry again for startling you. I'm Hisao."
	scene ev hana_library
	"She looks up from her book, stalling a little before replying."
	ha_ "I... know."
	ha_ "We... are in the same... same class."
	"Her speech is stilted and so quiet that it is barely audible even in the still library."
	"Somehow I think that my 'delinquent' impression of her was wrong."
	ha_ "H-H-Hanako. I'm... Hanako."
	play music "bgm/blank.ogg"
	"..."
	"I resist the urge to say 'that's a nice name' just to have something to say, but really, it's the only thing that I can think of."
	"I feel like an idiot. Everyone here must be used to being different to each other, and here I am being all bothered and fussed about that kind of thing."
	hi "Don't let me interrupt your reading. I'll... just check these books if you don't mind."
	"She nods a little, and sighs a little sigh of relief."
	"..."
	scene ev hana_library_read
	"So I try to read the covers and the introductions of the books I picked up and she buries her face in her book."
	"Uncomfortable silence consumes us."
	"My eyes still wander to her direction, and I sneak peeks at her flowing hair and the scars it's hiding."
	scene ev hana_library
	$renpy.pause(0.5)
	scene ev hana_library_read
	"After a while I realize that she's doing the same, and only pretending to immerse in 'Life of Pi.'"
	scene ev hana_library
	$renpy.pause(0.5)
	scene ev hana_library_read
	"Her gaze is not inquisitive at all though, it darts around like a scared rabbit."
	scene ev hana_library
	"When our gazes finally meet, the chain reaction is unstoppable."
#	play sound "sfx/impact.ogg"
	scene bg school_library_ss
	show hanako def_worry at center
	"She stands up forcefully from the beanbag and takes a deep breath."
	jump en_A8c
label en_A8c:
	ha "I..."
	ha "I... I..."
	hi "I...?"
	show hanako defarms_strain at center
	ha "Ivegottogodosomething!"
	hide hanako
	"Without warning, Hanako takes off and runs towards the counter."
	"Her hare-like takeoff catches me so off guard that I don't manage to go after her until she has a good head start."
	show lilly cane_smileclosed at twoleft
	show yuuko neutral_down at tworight
	play music "bgm/Stride.ogg"
	"By the time I reach the counter she is nowhere to be seen."
	"Lilly and Yuuko are happily chatting away."
	"Knowing that I won't be able to catch Hanako myself, I approach the girls."
	hi "Hey, did you see... er... notice a girl run past here?"
	show yuuko smile_down at tworight
	yu "Um, maybe... what did she look like?"
	hi "Long, dark hair. Kinda shy. She had... well... some scars... on her... face."
	show lilly cane_surprised at twoleft
	li "You wouldn't be talking about Hanako, would you?"
	hi "Yeah, that's her. I saw her reading and tried to talk to her, but I think I scared her off or something."
	show lilly cane_sad at twoleft
	li "Oh dear. Yuuko, would you excuse me, I had better try and find her."
	show yuuko neurotic_up at tworight
	yu "S-sure. I'll just hold onto these until you come back."
	hi "Um, what's going on?"
	li "I'm sorry, but I'll have to explain it to you some other time."
	hi "Right. I'll see you later then..."
	hide lilly
	show yuuko neurotic_up at center
	scene bg school_library_ss_right
	"Lilly hastily grabs her cane and hurries out of the library, leaving me alone with Yuuko."
	hi "I don't think I'll ever get the hang of this place."
	hi "Did I do something wrong?"
	show yuuko smile_down
	yu "What did you do?"
	if a8aTrigger == true:
		jump en_A8d
	elseif a8aTrigger == false:
		jump en_A8e
label en_A8d:
	hi "Nothing! I just... talked to her. Tried to get to know her. Didn't even manage to get started."
	show yuuko worried_up
	"Yuuko sighs and looks awfully bothered, even more so than she did before."
	yu "I guess you weren't 'wrong' so much as 'tactless.'"
	hi "Tactless?"
	show yuuko smile_down
	yu "That girl is a bit of a special case. It's like she never really talks to anyone."
	hi "Isn't that a bit... strange?"
	yu "I wonder... It's just how she is, I think."
	"Yuuko doesn't sound all that convincing. Then again, maybe this is just the norm around here."
	"Everyone has their own problems, or else they wouldn't be here."
	"Perhaps I was being a little tactless after all."
	jump en_A8f
label en_A8e:
	hi "Nothing! I was just looking for some books and then she got this fit and ran off."
	hi "The most offending thing I can think of was that I might've looked at her general direction a few times."
	show yuuko worried_up
	yu "Well, she is a very timid girl."
	yu "You have to be very careful around her. She can be very jumpy, I think, and she's not accustomed to talking with other people."
	hi "Isn't that a bit... strange?"
	yu "I wonder... It's just how she is, I think."
	"Yuuko doesn't sound all that convincing. Then again, maybe this is just the norm around here."
	"Everyone has their own problems, or else they wouldn't be here."
	jump en_A8f
label en_A8f:
	hi "But how should I deal with these people? Forcing myself to act overly casually only makes me feel phony."
	hi "Like I was supposed to be ignoring the elephant in the room."
	show yuuko neurotic_up
	"Yuuko fidgets, looking like she wants to say something to that, but resists it."
	yu "I think it's an elephant only if you feel that way."
	"I guess she doesn't have a good sense of self-restraint. It makes me smile, and she blushes heavily."
	show yuuko panic_up
	yu "W... what? Did that sound stupid?"
	hi "No no, it sounded really wise. I guess you're right. It's more about me than anyone else."
	show yuuko smile_down
	"Neither of us has anything to add so Yuuko fills the silence by shuffling some papers around."
	"People who have papers on their desks really like doing that."
	yu "Did you find any books? I should be closing soon. I mean this library should be closing. But I have to do it. I hope that's not too inconvenient for you."
	hi "Oh. Yeah, I want some books, but I left them over there because..."
	hi "...I'll just go get them."
	"I fetch my stack of books from beside the beanbags where Hanako and I were sitting and return to the counter."
	show yuuko neutral_down
	yu "Wow. You read a lot, don't you?"
	hi "I surprise myself with that too, honestly. At least, when I really think about it."
	hi "I had a lot of free time earlier this year, so I just kind of... started reading books to fill that time. I couldn't do much else."
	yu "I see."
	"But she doesn't say anything else, and just checks out my books for me."
	"I guess this is what they call 'tact.'"
	play music "bgm/blank.ogg"
label en_A9:
	scene bg school_dormhallway
	"Holding the library books with one arm, I trawl my pocket for the key to the door."
#	play sound "sfx/dooropen.ogg"
	"A sudden sound from behind startles me, making me nearly drop the books I'm carrying or the key that I almost managed to get into the lock."
	mystery "Who is it?"
	play music "bgm/Out_of_the_Loop.ogg"
	show kenji neutral at center
	"I turn around to see who is talking to me. It's Kenji. He seems to be in a friendly mood, although the light glinting off his glasses in the dark gives him a sinister look."
	hi "It's just me."
	"This makes him pause and lick his lips nervously."
	show kenji tsun
	ke "Who is me? I don't know anyone called me. Are you some new guy again?"
	"His voice is suddenly strained and quick."
	hi "Yes... but we've met before. Yesterday."
	ke "I don't think so, I would remember someone who I met only yesterday. ...When was that? What day is it today?"
	"I try to ignore him. Is he joking or what?"
	ke "Prove that we've met before!"
	hi "You live across the hall. You're Kenji."
	show kenji rage
	"Kenji jumps back, his eyes filled with an uncomprehending fear."
	ke "How do you know my name? Damn, this can only mean one of two things: Either we have met, and you are telling the truth, and I just can't remember it, or you are a spy."
	"He pauses."
	show kenji tsun
	ke "A psychic spy."
	"His eyes dart around me, trying to peek into my room, although it's hard to believe he can see anything through those thick glasses."
	"His mood swung from friendly to manic in less than a minute."
	hi "I'm not psychic."
	ke "How do I know that? I'm not a mind reader."
	"Kenji points a finger in my face damningly."
	show kenji rage
	ke "...Unlike you!"
	hi "Stop that, man. We met yesterday. What's wrong with you? I live in this room."
	ke "Lies. If you think you can pass as Hisao because I'm legally blind you are sorely mistaken."
	ke "You don't even look like him. I mean, the resemblance is real, real slim. Maybe at a distance, but who do you think you're kidding?"
	"I want to grab him by the shoulders and shake him. Exasperated, I rub my eyes and let out a heavy sigh."
	show kenji tsun
	ke "Stay there."
	show kenji tsun_close
	"Kenji comes closer, one careful step at a time. I stay still, lest he assault me physically, although I doubt he could do much damage even if he did."
	show kenji happy_close
	ke "Oh, wait, I see it now. Damn, it really is you."
	"Sighing again, and then once again for good measure, I step backwards, just in case."
	show kenji happy
	ke "What's up, man? You don't look too good. I think. Something wrong?"
	hi "I don't know. Just had something stupid happen to me. A few stupid things, actually. Even if you discount this one."
	hi "I can't get a proper touch on other people here, and I have no idea if it's because of me or because of them."
	"I don't know why I'm telling this to Kenji. It's not like we've had any contact either."
	ke "That's rough, dude. Yeah, I'm sorry about calling you a psychic spy and all, but you can never be too careful."
	show kenji tsun
	ke "It's the hard reality we live in."
	"I'm slowly starting to think that Kenji isn't necessarily living in the same reality as the rest of us."
	ke "You see? This is how it is, this world. There is no justice. You see? Even when I lose, I win, because I don't lose the lesson."
	hi "...What does that even mean?"
	ke "It doesn't matter."
	"He dismisses it flatly with a wave of his hand."
	show kenji happy
	ke "So what happened? Why the long face? Do you have a long face?"
	hi "Eh, it's nothing. I just scared some girl off accidentally. Literally too, she actually ran away from me."
	hi "Was my fault, really, I think. I'm not really... used to all this yet."
	show kenji tsun
	ke "A girl? A cute one?"
	"Cute? That's a hard question. She had a nice body and really beautiful hair... but the face..."
label en_choiceA9:
	"I guess it could go either way."
	menu:
		"She was cute.":
			jump en_A9a
		"She wasn't cute.":
			jump en_A9b
label en_A9a:
	$attractionHanako = attractionHanako+1
	hi "Yeah, cute I guess."
	ke "I knew it!"
	jump en_A9c
label en_A9b:
	hi "Not exactly cute, no."
	ke "Hmm..."
	jump en_A9c
label en_A9c:
	ke "There are a lot of cute girls here. A strangely disproportionate amount... I believe this is one of the dark secrets of this school."
	ke "I tried to warn you man, but did you listen..."
	"I don't remember any such warning."
	hi "Dark secrets?"
	ke "Yes, dark secrets. Extremely dark. Like a black hole."
	ke "Have you noticed that the number of girls in this school is slightly but significantly higher than the number of boys? It's like 60-40."
	"He turns his head to the left and stares off into the distance at nothing."
	ke "Why is it like this? I mean, to the untrained eye, it doesn't appear to be that bad, but that is a full 20%%."
	ke "One would think that a school with such a huge pool of women would be a man's dream. But no!"
	play music "bgm/blank.ogg"
	show kenji neutral
	ke "What I am about to tell you could blow your mind. Are you ready?"
	"I don't know where this is going, but I think I won't be missing much by cutting out now."
	hi "No, I am not ready."
	"I only get as far as turning the doorknob before Kenji starts talking again, showing that he doesn't really care if my mind is blown or not."
	show kenji tsun
	play music "bgm/High_Tension.ogg"
	ke "I believe that this school is a battleground. The site of a feminist infiltration."
	ke "This disparity in the number of men to women is a clear sign of how far they have come. In case this cold war turns hot, they will have superiority in numbers."
	ke "Just another skirmish in the eternal war against the forces of the feminists... They're everywhere. In Japan, women outnumber men. It's not a 60-40 split, but it's only a matter of time, man..."
	ke "Even in America, women are the majority by a hair. They're building up their numbers. In the past, the buildup of a military has always been the clearest sign of imminent war."
	ke "Japan is just the first step. Our economy is badass, and the country itself is small and isolated, yet a huge part of the Pacific in terms of political value."
	ke "The perfect target. They are so cunning... As expected of women."
	ke "Soon, the day will come, when..."
	"Kenji's voice trails off ominously."
	show kenji neutral
	ke "That is why you can't trust them. They will string you along, and then kill you, just as they killed me. You will end up just like me."
	play music "bgm/blank.ogg"
	hi "Oh, hell no..."
	"I can't stop myself from blurting it out."
	show kenji tsun
	play music "bgm/Out_of_the_Loop.ogg"
	ke "Hey! What the hell does that mean?!"
	hi "You said it, not me."
	"It's the best I can think of."
	ke "So? You're not supposed to say something like that! Damn, so rude."
	show kenji neutral
	ke "Where was I? Oh, yeah, vast feminist conspiracy."
	hi "Stop it. Stop! I lost you way, way back there somewhere. Somewhere around �feminist infiltration.�"
	show kenji happy
	ke "Too hard to follow? It's cool, I have some graphs and stuff in my room. And puppets. You like puppets?"
	hi "No puppets."
	ke "You don't like puppets, okay. Graphs are still cool, though, right?"
	"He speaks energetically, responding almost before I'm done talking, moving his hands in an animated way as he continues to rant on."
	"This is too strange. I had him pegged as relatively normal, but it's clear that I was wrong."
	ke "Something on your mind, dude?"
	hi "Just thinking about what it's like to be the last sane man in an insane world."
	show kenji tsun
	"Kenji frowns, looking deeply upset."
	ke "You mean that's you? That can't be, because I'm the last sane man in an insane world. That is my dream, you can't just steal a man's dream."
	ke "What the hell, there can't be two last sane men. It would invalidate that whole �last� part... and that part is kind of important."
	ke "There can only be one, like in that foreign movie where there could only be one, and in the end there is only one dude left, because that was the point."
	"I have never seen anyone talk so heatedly and so defensively about absolutely nothing before."
	show kenji neutral
	ke "Anyway, if you wait here, I can get my graphs. I also have a list of the other dark and complex conspiracies that this school holds, as tangled as..."
	ke "Quick, finish my analogy for me. Be a pal."
	hi "I'm going to go to bed now. It's extremely late."
	show kenji tsun
	ke "That doesn't sound like an analogy. But whatever."
	show kenji happy
	ke "I like you, you seem like a cool dude."
	show kenji tsun
	ke "Most people don't understand what I'm talking about when I try to explain the vast feminist conspiracy to them. Denial is a terrible thing."
	ke "Later."
	hide kenji
	play music "bgm/blank.ogg"
	"He claps me on the back and then vanishes into his room so quickly and quietly it's like he didn't even open the door but instead walked right through it like a ghost."
	scene bg school_dormhisao_ss
	"I don't know if I can fully digest what just happened, so I give up and just go to my room, kicking off my shoes before falling facefirst into bed."
	"It takes me some time to relax and get up so I can get started on homework."
	"It's because the sheets are cool and comforting against my cheeks, and it feels good just lying there with my eyes closed."
	"This school is like some kind of bizarre and surreal island. It's isolated on top of a mountain, and each person is stranger than the last."
	"I just can't seem to fit in. What irony, one would think that fitting in a place that's made for people who are unfit for anywhere else would be easy."
	hi "Maybe I'm trying too hard."
	"Although I say that, it doesn't help take the edge off, and the words are left echoing off my empty walls."
	"I guess it's not as bad as I expected, though. This place really is more a school and less a hospital pretending it's a school than I thought it would be."
	"If nothing else, the scenery is beautiful."
	"I open one eye, seeing the schoolbooks and bottles of pills arranged side-by-side on my desktop."
	"Maybe this place is too much like a normal school, after all."
	scene black
	""
label en_A10:
	play music "bgm/Fripperies.ogg"
	scene bg school_scienceroom
	"I feel very tired this morning, probably because yesterday itself was a very tiring day. On top of that, I woke up far earlier than necessary."
	"After saying hi to Shizune and Misha, I start doing the work as instructed from the board. It already looks like today is going to be heavy."
	"I don't have a problem with that now, though. Shizune and Misha might jump on me trying to get an answer about whether or not I've decided to join the Student Council, even if it's just one day."
	"I wouldn't put it past them to try, and I don't have an answer for them if they do. So, this situation is convenient for me."
	"About ten minutes into class, Hanako walks in and takes a seat, but no one looks at her. The teacher doesn't even comment on her lateness."
	"He does, however, stop us to say that we're going to break into groups again."
	show shizu behind_smile at tworight
	show misha perky_smile at twoleft
	"I turn my head and see that Shizune and Misha are looking at me. Shizune gives me a smile that is equal parts cute and menacing. This is a smile that says 'We have you now. There is no escape.'"
	show misha hips_grin at twoleft
	mi "Hicchan~, it looks like we're together again! Yay yay~!"
	show misha hips_grin_close at twoleft
	show shizu behind_smile_close at tworight
	"Misha leans sideways while Shizune pushes her desk closer to mine. There really is no escape now unless I were to jump through the window."
	"Jumping out the window isn't the best option, sadly."
	show shizu adjust_smug_close at tworight
	shi "..."
	show misha hips_smile_close at twoleft
	mi "What's wrong, Hicchan?"
	show shizu adjust_happy_close at tworight
	shi "..."
	show misha perky_smile_close at twoleft
	mi "Oh... Hicchan, have you been thinking about what you said yesterday? You said that you would think about joining the Student Council, didn't you?"
	show misha hips_grin_close at twoleft
	mi "It's okay, Hicchan. We were talking about it after you left, and it would be rude to expect you to already have an answer for us this early, right? Right~!"
	show misha cross_laugh_close at twoleft
	mi "Hahahahahaha~!"
	"I'm so happy you two are able to have a laugh at my expense, and even more pleased to know that you both know how crazy the two of you can be."
	show shizu basic_normal2_close at tworight
	show misha perky_smile_close at twoleft
	"Now that that's over, Shizune snaps back into serious mode and smacks today's assignment with the back of her hand in an overly dramatic and important way."
	"When I actually look at the stuff, it's mostly just reading. In fact, there are only two problems."
	"I almost want to say something about how her rush to get started seems a bit much, considering the small amount of work. In fact, Shizune probably knows how little there is, and simply doesn't care."
	"Yeah, it seems like the workload doesn't matter to her as much as the fact that there is work; the actual amount is unimportant. She approaches everything with the same level of ambition."
	scene bg school_scienceroom_left
	show hanako emb_downtimid at right
	show shizu basic_normal2_close at twoleft
	show misha perky_smile_close at left
	play music "bgm/blank.ogg"
	"While I'm reading, I let my eyes wander around the room and catch Hanako trying her hand at solving the problems. It looks like she's working alone."
	"I can't remember seeing her working with other people before."
	"Thinking back to how shy she is, it's understandable."
	hi "Hey, that girl over there..."
	show misha perky_confused_close at left
	mi "Huh? Who, Hicchan?"
	hi "Her. Hanako. Over there. Does she always work alone?"
	mi "I think so, Hicchan. Do you feel sorry for her because she's alone?"
	hi "I was just thinking that maybe she could work with us, or something."
	show misha perky_sad_close at left
	mi "Hmmmm... No, I don't think that would be a good idea, Hicchan."
	hi "Why not?"
	mi "Shicchan wouldn't get along with her."
	hi "Why?"
	show misha perky_confused_close at left
	"Misha shuffles around the question, letting out a laugh that sounds very strange; it's nervous, but still has that lilting up-and-down quality present in everything she says."
	mi "Just because, Hicchan."
	"By now, Shizune has noticed our conversation, and it makes me realize again how Misha has been signing everything she has been saying this whole time."
	show shizu basic_frown_close at twoleft
	shi "..."
	show misha perky_sad_close at left
	mi "What, Shicchan? The friend of my enemy is my enemy? That sounds so harsh, I'm not going to say that."
	hi "You said it anyway."
	show misha hips_grin_close at left
	mi "I know, Hicchan, it's fine if you overhear~!"
	"I wonder if this is Misha's way of keeping things fair, since without her, I wouldn't be able to understand a thing Shizune is saying, and vice versa."
	"Is that also why she signs all the time, so there is never a conversation Shizune will be left out of?"
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha perky_smile_close at left
	mi "Anyway, we should start on the problems now, Hicchan."
	hide misha
	hide shizu
	hide hanako
	scene bg school_scienceroom
	play music "bgm/Daylight.ogg"
	"We finish with time to spare, and I decide to ask if there are any alternatives to the cafeteria, as frankly, the food so far has been subpar."
	"This sends Shizune and Misha arguing among themselves about their favorite restaurants. All of them are downtown, so I don't think we have time to go all the way there. And what about the bill?"
	"Are they arguing just for the fun of it?"
	"Maybe. They seem so distracted by it that they don't even notice the start of the actual lunch break."
	"I look over my shoulder towards the back of the classroom."
	show hanako emb_downtimid at tworight
	"She seems to be studying her notes from the previous class."
	"It's an odd sight; everyone else in the class is busying themselves with the lunch break."
	"Socializing, gossiping, rearranging desks, the ones with actual boxed lunches mixed in and chattering like everyone else, only interrupted by short bouts of eating."
	"But, when I watch Hanako, it feels that I'm the only one who can see her. Almost as if she was invisible; sort of hiding in plain sight."
	"Is she being bullied? Is she isolating herself from the rest of the class on her own accord?"
	show hanako emb_timid at tworight
	$renpy.pause(0.6)
	show hanako emb_downtimid at tworight
	"I see her look over her shoulder towards the classroom's rear door."
	"Come to think of it, she hasn't turned a page since I've started watching her."
	"I guess she's waiting for someone."
	if attractionSC > 1:
		if attractionHanako > 1:
			jump en_choiceA10a
		elseif attractionHanako < 2:
			jump en_choiceA10b
	elseif attractionSC < 2:
		if attractionHanako > 1:
			jump en_choiceA10c
		elseif attractionHanako < 2:
			jump en_A10a
label en_choiceA10a:
	"What to do..."
	menu:
		"Read my book.":
			jump en_A10a
		"Go talk with Hanako.":
			jump en_A10b
		"Wait for Shizune and Misha.":
			jump en_A10c
label en_choiceA10b:
	"What to do..."
	menu:
		"Wait for Shizune and Misha.":
			jump en_A10c
		"Read my book.":
			jump en_A10a
label en_choiceA10c:
	"What to do..."
	menu:
		"Read my book.":
			jump en_A10a     
		"Go talk with Hanako.":
			jump en_A10b
label en_A10a:
	play music "bgm/blank.ogg"
	"I do what I always do when I don't know what to do."
	"Like now."
	"I've already started on one of the books I borrowed yesterday, and took it with me to school to fill the empty moments between classes."
	hide hanako
	"I find the page that I creased a corner of to mark the spot I left yesterday night, and pick up from there."
	"Misha and Shizune are still arguing heatedly, probably about restaurants still."
	"If I joined them, I'd just get caught up in that, or worse, get grilled about joining the Student Council."
	"Misha isn't speaking aloud since there is nobody who'd need to hear what they are talking about."
	"But why does she tend to sign things even when Shizune doesn't need to understand what's being said, or even more strangely, when Shizune is not around at all? What an odd conflict of habits."
	"I find it hard to focus on the book, and besides, the lunch break beckons me to leave the dullness of the classroom. I do so, heading down for the cafeteria."
	"Misha and Shizune, having come to a conclusion of one kind or another, follow in my wake though still talking in their animated fashion."
	jump en_A11
label en_A10b:
	$a10bTrigger = true
	"I still feel bad for making her run away yesterday, so I'd better say something."
	scene bg school_scienceroom_left
	show hanako emb_downtimid
	hi "Um, hey there, Hanako."
	show hanako def_shock
	ha "H... Hisao?"
	"Well, at least she remembers my name."
	hi "Hey... I just wanted to apologize for yesterday."
	hi "I didn't mean to startle you or anything."
	hi "I'm just new here and thought I should get to know my classmates."
	show hanako basic_bashful
	"As Hanako looks up at me, I notice her scarring once more."
	"It's a little bewildering that you can barely notice it from across the room, but it's so noticeable from close up."
	show hanako cover_bashful
	ha "T... that's okay."
	ha "It... it was my fault."
	hi "Nah, that wasn't anyone's 'fault,' it just kind of happened."
	hi "So, are you waiting for someone? I saw you looking at the door before..."
	show hanako basic_normal
	ha "Y-yes... Lilly."
	hi "Oh, you mean Lilly the blind girl?"
	"Hanako only nods in response, and I can't help but wonder if defining people through their disabilities is a faux pas of the worst kind or just normal here."
	"I guess that explains why Lilly took off after her yesterday."
	hi "She seems like a nice girl. Are you two friends?"
	show hanako basic_bashful
	ha "Y-yes."
	show hanako basic_distant
	"As if hoping for Lilly to appear, she checks over her shoulder again."
	play music "bgm/blank.ogg"
	"I think I'm making her nervous again."
	hi "I hope I'm not disturbing you right now..."
	show hanako basic_bashful
	ha "N-no, that's not it."
	ha "It's just easier if Lilly doesn't come here..."
	hi "Oh, because it's hard to get around the classroom?"
	show hanako basic_distant
	ha "Not... really."
	"Hanako's gaze drifts past my shoulder and towards Shizune."
	hi "Shizune?"
	"Hanako nods again."
	hi "What about her? Don't they get along?"
	"Hanako shakes her head. Clearly this is something she doesn't want to talk about."
	"It does make a strange sort of sense, Shizune and Lilly not getting along so well."
	"Communication between the two would be all but impossible. It's hard enough talking to Shizune through Misha, even when you can see whose hands are 'talking.'"
	"Hanako is so focused on Shizune that I am the first to notice Lilly at the door."
	hi "Oh, she's here now."
	show hanako defarms_shock
	"Hanako spins around to confirm this. Upon seeing Lilly, she moves quickly to the door."
	scene bg school_scienceroom
	show lilly cane_weaksmile at twoleft
	play music "bgm/Concord.ogg"
	show hanako emb_smile at tworight
	ha "Lilly..."
	show lilly cane_smile at twoleft
	li "Ah, Hanako. Good morning. Is the president here?"
	show hanako emb_downtimid at tworight
	ha "Y-yes."
	show hanako basic_distant at tworight
	"Hanako glances over her shoulder at Shizune again, as if to confirm she can't hear them even though that's impossible."
	show lilly cane_sad at twoleft
	li "I suppose we'd best be off, then."
	"Lilly's sigh and tone of what seems like frustration makes me raise an eyebrow. I guess there's some kind of enmity between the two."
	"It's intriguing, but that's not really something I'd ask about. I'm sure if they wanted me to know, then they would tell me."
	"It's only my third day here; I should be trying to make friends, not finding out why people are enemies."
	"Still, it's a little funny to find out that this school has little feuds, just like my old high school."
	"Even if people are more tolerant of others, they're still going to get on each other's nerves."
	hi "Hey Lilly. How are things? I'm sorry I made you run off yesterday..."
	show lilly cane_surprised at twoleft
	li "Oh my, is that Hisao? I didn't realize you were here..."
	"It seems that Lilly is a little embarrassed about being so frank in front of me."
	show hanako emb_sad at tworight
	ha "S-sorry Lilly. I thought you realized..."
	show lilly cane_weaksmile at twoleft
	li "No, it's all right, Hanako."
	li "Hisao, please don't worry about yesterday. It was just a misunderstanding."
	hi "If... you say so. I'm still working this place out."
	show lilly cane_smile at twoleft
	li "Well then, I think you'll find most people here a lot more forgiving than elsewhere."
	li "If you are feeling a little confused, please don't be afraid to ask questions."
	hi "Sure, I'll remember that."
	show hanako emb_timid at tworight
	ha "Um... Lilly..."
	show lilly cane_weaksmile at twoleft
	"Lilly gives a small nod of acknowledgment."
	li "I'm sorry Hisao, but we must be off."
	"Hanako really doesn't look all that comfortable here right now, and Lilly still seems a little embarrassed."
	"I wonder if my apologies really made any impact."
	hi "Mind if I accompany you two?"
	show lilly cane_smile at twoleft
	"I know I'm kinda pushing it, but... Lilly hmms quietly, still smiling."
	show lilly cane_weaksmile at twoleft
	li "I'm sure that we could accommodate you, can't we, Hanako?"
	show hanako emb_downsad at tworight
	$renpy.pause(0.6)
	show hanako basic_worry at tworight
	"She looks at Lilly, then at me, and then she freezes, wide-eyed."
	ha "S... sure."
	show lilly cane_cheerful at twoleft
	li "Well then, shall we go?"
	"I'm sure Lilly wouldn't do this so easily if she saw how scared Hanako looks, but it can't be helped now."
	"Declining after the deal is sealed would only cause confusion and problems."
	play music "bgm/blank.ogg"
	jump en_A11c
label en_A10c:
	$a10cTrigger = true
	hide hanako
	show misha sign_smile at twoleft
	show shizu adjust_happy at tworight
	"Misha and Shizune are still arguing about their choice for lunch place, incomprehensible for a pair of high school students who have to take a taxi at least to make it to downtown and back in time."
	hi "Haven't you finished, already?"
	show misha hips_grin at twoleft
	mi "Oh, sorry Hicchan! Were you waiting for us?"
	show shizu behind_smile at tworight
	shi "..."
	show misha hips_smile at twoleft
	mi "You don't have any plans?"
	hi "Plans?"
	mi "For lunch?"
	hi "Well, I don't, so I thought I could hang with you guys."
	show misha sign_smile at twoleft
	$renpy.pause(0.6)
	show misha perky_smile at twoleft
	"Misha smiles victoriously at my lack of plans, and excitedly translates my response to Shizune."
	show shizu adjust_smug at tworight
	shi "..."
	show misha hips_grin at twoleft
	play music "bgm/blank.ogg"
	mi "If you don't have anything specific planned out, do you want to eat lunch with me and Shicchan? Ah, we're going to go to town for lunch, though... Don't worry, Hicchan, it's not that far."
	hi "Sure, I'll come with you."
	"And with that, we leave the classroom."
	jump en_A11
label en_A11:
	scene bg school_hallway3
	"Just around the corner of the hallway something hits me in the chest with the force of a runaway train."
	jump en_A11a
label en_A11a:
#	play sound "sfx/impact.ogg"
	scene black
	hi "Ouch..."
	play music "bgm/Standing_Tall.ogg"
	scene ev emi_knockeddown_face
	"Opening my eyes, I see a pair of saucer-like green eyes looking up at me."
	scene ev emi_knockeddown
	"They belong to the perpetrator, a short girl who bumped into me and has now fallen down onto the hallway floor."
	"She wears a PE uniform and a very worried frown. The former strikes me as a rather strange thing to have on during a lunch break."
	"...More striking than that, though, is that she doesn't have legs."
	show ev emi_knockeddown_legs
	"Or she does, but they are not flesh and bone. Her pale and very much flesh-and-bone thighs end in shins and feet made of some black metallic or plastic-like material."
	"They look disturbingly artificial and unnatural. It almost makes me forget that my chest is hurting."
	scene ev emi_knockeddown
	"The girl winces a little, rubs her nose and jumps up."
	scene bg school_hallway3_left
	show emi sad_depressed_gym at center
	emi_ "Aw man... Hey, are you all right? I'm sorry about that, really!"
	emi_ "I wasn't looking where I was going, and you just came out of nowhere. Sorry... Sorry!"
	"She's looking really apologetic, in the hurt puppy way of looking apologetic."
	"I quickly forget about being angry or anything, since hurt puppies are my weak spot."
	play music "bgm/blank.ogg"
	hi "It's okay. Don't worry about it... ouch..."
#	play sound "sfx/heartfast.ogg"
	hide emi
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	show emi sad_depressed_gym at center
	$renpy.pause(0.7)
	"I say that, but there's a stinging pain growing in my chest, and I know that this is about the biggest possible danger for my condition."
	"Don't overexert yourself, don't forget your medication and most of all, don't get hit in the chest."
#	play sound "sfx/heartslow.ogg"
	hide emi
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	show emi sad_depressed_gym at center
	$renpy.pause(0.7)
	"I try to rub my solar plexus to chase the pain away, holding my breath in an attempt to hear my heartbeat."
#	play sound "sfx/heartslow.ogg"
	hide emi
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	show emi sad_depressed_gym at center
	$renpy.pause(1.7)
#	play sound "sfx/heartslow.ogg"
	hide emi
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	show emi sad_depressed_gym at center
	$renpy.pause(1.7)
#	play sound "sfx/heartslow.ogg"
	hide emi
	show heartattack alpha
	$renpy.pause(0.1)
	hide heartattack alpha
	show emi sad_depressed_gym at center
	$renpy.pause(1.7)
	"It seems normal..."
	show emi basic_shock_gym
	emi_ "Hey, should I get a nurse?"
	play music "bgm/Standing_Tall.ogg"
	"The worried, high-pitched voice of the girl snaps me out of it."
	"I stare at her for a few seconds dumbfounded, until I realize that I probably looked worse off than I really was, doubled over myself and looking all tense."
	"Damn, I'm overly worried about my heart."
	hi "Err... no need, I'm fine."
	"Managing to say something in response, I pull myself upright, feeling my sore ribs one last time, and take a deep breath."
	"She just knocked the wind out of me. Big time. But it's nothing more than that."
	show emi basic_hes_gym
	emi_ "You sure you're okay? I hit you pretty hard."
	hi "It's okay. I said I was fine, and nothing's broken. No harm done."
	show emi basic_happy_gym
	emi_ "That's good! I was--"
	if a10bTrigger == true:
		jump en_A11d
	elseif a10bTrigger == false:
		jump en_A11b
label en_A11b:
	"I feel a hand on my shoulder at the same time the girl's eyes widen in horror and whatever she was saying gets interrupted by a very horrified?"
	show emi basic_hes_gym
	emi_ "Eep!"
	scene bg school_hallway3
	show emi basic_hes_gym at right
	show shizu cross_rage at 2four
	show misha hips_smile at left
	"I don't have time to look behind me because Shizune is already shoving me aside and stomping over to the girl, signing furiously at her."
	show misha hips_grin at left
	mi "Miss Ibarazaki, I saw that. Running in the halls is strictly forbidden."
	"Misha translates, right on Shizune's tail, but her voice is girlishly playful, not full of the divine fury Shizune's arm movements would seem to call for."
	show emi basic_closedsweat_gym at right
	emi_ "Er, sorry, I was just going to get some stuff, and I was in a kind of a hurry."
	show shizu adjust_angry at 2four
	shi "..."
	show misha hips_smile at left
	mi "You've been told this a thousand times before. Your reckless behavior endangers other students, and even worse, it's explicitly against the school regulations."
	show emi sad_depressed_gym at right
	"The girl blushes and starts to fidget nervously like a little child caught misbehaving."
	"It's so cute I find myself smiling."
	emi_ "I know that! I? I, um, I was just..."
	show shizu cross_angry at 2four
	shi "..."
	show misha cross_smile at left
	mi "Make sure that this will not happen again... although I'm sure telling you this is futile, and only causes me further headache when you choose to ignore the regulations."
	show misha cross_grin at left
	mi "Got that, Emi?"
	show emi sad_annoyed_gym at right
	"The small girl sticks her tongue out in response."
	show emi basic_hes_gym at right
	emi "Aaah!"
	emi "I gotta go!"
	emi "Teacher'll have my head! I promised to help with printouts, but I went running instead! Sorry, but I've gotta change and everything!"
#	play sound "sfx/emisprinting.ogg"
	play music "bgm/blank.ogg"
	hide emi
	"Before Misha or Shizune or I can say anything, she's already bolted from where she was a second ago, almost halfway towards the stairwell."
	scene bg school_hallway3_right
	show shizu cross_angry at tworight
	show misha cross_grin at twoleft
	play music "bgm/School_Days.ogg"
	"Shizune looks like she's about to go nuclear on the spot, so I smile at her in a vain attempt to calm her down."
	show shizu basic_frown at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "Are you okay, Hicchan? That Ibarazaki girl is always like that, causing trouble to others."
	hi "You know, I'm pretty certain Shizune wouldn't call me 'Hicchan.'"
	show misha hips_grin at twoleft
	mi "Never mind, never mind!"
	"..."
	hi "Yeah, anyway, I'm okay. Just got the wind knocked out of me."
	show shizu basic_normal at tworight
	shi "..."
	show misha cross_grin at twoleft
	mi "That's great, Hicchan!"
	"I wouldn't call that great, but I let it slide this one time."
	if a10cTrigger == true:
		jump en_A11x
	elseif a10cTrigger == false:
		jump en_A11y
label en_A11x:
	show shizu adjust_happy at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "So, let's hurry, Hicchan~! To have lunch!"
	show misha hips_grin at twoleft
	mi "We promise it'll be great!"
	hi "I'll take your word for it. What kind of a place is it?"
	hi "A restaurant, or something?"
	show shizu behind_smile at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "It's a teahouse, Hicchan~!"
	"A teahouse... that sounds kind of fancy."
	show shizu adjust_smug at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Why are you looking at your wallet, Hicchan? It's okay, if you don't have any money we'll cover for you~!"
	hi "That's really nice of you. Thanks."
	show misha hips_smile at twoleft
	mi "It's okay, Hicchan! After all, we're friends, right, Hicchan?"
	"It's only been three days. Are we really friends that quickly?"
	"Heh. But, hearing that makes me happy."
	show shizu behind_blank at tworight
	shi "..."
	show misha sign_smile at twoleft
	mi "Ah, it's only for today, though, and only if you accept right now! Do you want to go, Hicchan?"
	"I start wondering if this is some kind of trap. Is this Misha's suggestion or Shizune's? This is important. I'm still a little apprehensive about the possible motives of a girl whose favorite pastime is the game of world domination."
	"No, I'm just being paranoid. Actually, they have grown on me already, and I do have to go to town sometime. So why not now, with them?"
	"I've never actually been to a teahouse before. All my expectations are from what I've seen about them on TV. But those are period dramas, and these are modern times. It might just be a regular cafe, and they're just calling it a teahouse."
	"Either way, I'm curious about that, too, so there's another reason for me to join them."
	hi "Sure."
	show misha hips_grin at twoleft
	show shizu behind_smile at tworight
	mi "That's great, Hicchan~! That's great, that's great! Yay~!"
	"Misha hops up and down briefly to show how happy she is, which causes a few heads to turn towards us. Shizune opts for a polite, tiny clap that lasts for all of two seconds before she goes back to looking stoic as usual."
	show shizu behind_blank at tworight
	hi "Would it kill you to be a little happier, Shizune?"
	show shizu basic_normal2 at tworight
	shi "..."
	show misha cross_laugh at twoleft
	mi "Oh? I wasn't aware that Hicchan was a king. Hahahaha~!"
	show shizu adjust_smug at tworight
	"Shizune pushes her glasses up as Misha delivers her message totally without sarcasm. I guess it would sting more if she could say it with the intent Shizune meant behind it, so for once I'm happy to have Misha as a barrier between us."
	hi "I'm not telling you to jump for joy just because I'm having lunch with you. I'm not that arrogant."
	show shizu adjust_happy at tworight
	show misha cross_grin at twoleft
	play music "bgm/blank.ogg"
	"She seems to accept this, and we head for town with Shizune leading the way."
	jump en_A12
label en_A11y:
	show shizu basic_normal2 at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "We have to run now, there is an important student council meeting regarding the festival. And we finally decided where to eat~!"
	show shizu behind_blank at tworight
	shi "..."
	show misha hips_smile at twoleft
	mi "Too bad you can't join, but this lunch meeting is only for council members."
	show misha hips_grin at twoleft
	mi "We can take you there some other time! Oh, but that'd be like a date, wouldn't it?"
	show misha hips_laugh at twoleft
	mi "Wahaha~!"
	hide misha
	hide shizu
	play music "bgm/blank.ogg"
	"The girls leave for downstairs."
	"I didn't manage to get far from the third floor hallway before all this commotion struck, literally. I should get going as well."
	scene bg school_scienceroom
	"The lunch and the afternoon class pass uneventfully."
	"I read most of the book I had started yesterday, and eat some of the mostly inedible offerings of the cafeteria."
	"The class is tiresome."
	jump en_A15
label en_A11c:
	scene bg school_hallway3
	"So we leave, all three together."
	show hanako emb_downtimid at center
	show lilly cane_smile at twoleft
	"Lilly walks beside the wall, letting her cane gently tap against it every now and then. Hanako comes along right beside her, so close that she is practically half-hugging her as they go."
	"Although it must make her walking that much harder, Lilly takes it in stride."
	show hanako defarms_shock at center
	"As we turn around the corner of the hallway, something hits me in the chest with the force of a steam train. Hanako shrieks a little and my vision briefly goes black."
	jump en_A11a
label en_A11d:
	show lilly cane_listen at left
	show hanako defarms_worry at right
	li "Hisao, what happened?"
	"She's not quite up to speed for obvious reasons, but she sounds very worried. More than what the situation deserves, really."
	hi "Someone just bumped into me, nothing serious. Just winded."
	show emi excited_sad_gym
	emi_ "Er, sorry, it's my fault. I was just going to get some stuff, and I was in a kind of a hurry."
	show lilly cane_weaksmile at left
	show hanako def_worry at right
	li "That 'someone' here is Emi, isn't it?"
	show emi basic_hes_gym
	"The little girl coughs quietly and shuffles her plastic or metallic feet, looking down at them before saying anything."
	show emi basic_closedgrin_gym
	emi "Hi, Lilly. Hanako."
	"I guess the girls know each other."
	show lilly cane_sad at left
	show hanako def_worry at right
	li "Do please try to be more careful. You might be sturdy enough to endure these sorts of accidents, but there are people who aren't."
	show emi sad_depressed_gym
	"The girl blushes and starts to fidget nervously like a little child caught misbehaving."
	"It's so cute I find myself smiling."
	emi "I know that! I? I, um, I was just..."
	show emi basic_hes_gym
	show lilly cane_surprised at left
	show hanako defarms_shock at right
	emi "Aaah! I gotta go!"
	emi "Teacher'll have my head, I promised to help with printouts but I went running instead! Sorry, but I've gotta change and everything!"
#	play sound "sfx/emisprinting.ogg"
	play music "bgm/blank.ogg"
	hide emi
	"Before any of us can say a thing, Emi has already bolted away, leaving the hallway eerily quiet."
	hi "Does that kind of thing happen often around here?"
	scene bg school_hallway3
	show lilly cane_concerned at twoleft
	show hanako def_worry at tworight
	li "There are more rules in Yamaku than usual for running in corridors."
	show lilly cane_listen at twoleft
	li "...but that rarely stops Emi, it seems."
	show lilly cane_weaksmile at twoleft
	"She shakes her head weakly and offers a slight, composed smile."
	li "I don't think there's anything we can do to stop her, I'm afraid. Shall we be off, then?"
	hide lilly
	hide hanako
	"Lilly heads off along the hallway, and Hanako hurries after her."
	"The route to the room the two use for tea is fairly simple to retrace, being still fresh in my mind from yesterday."
	jump en_A13
label en_A12:
	scene bg suburb_roadcenter
	play music "bgm/Afternoon.ogg"
	"Watching her walk in front of me, I notice that she walks very quickly, taking long, heavy, determined strides."
	"Maybe if we were traveling through a snowstorm it would make sense to walk like that, but it's a perfectly clear day. Anyway, it's making me feel exhausted just watching her."
	scene bg suburb_shanghaiext
	"We arrive at the teahouse in what Misha says is 'record time,' likely because of Shizune's blazing pace. I feel a little let down seeing that it's not a huge feudal-era building with mats on the floor and women in kimonos pouring the tea."
	"It actually is more like a cafe, as I thought. Not that it's a bad thing. It looks very nice."
#	play sound "sfx/storebell.ogg"
	scene bg suburb_shanghaiint
	"As soon as I walk through the doors, someone zooms in front of us, as if they had been lying in wait the entire time."
	show yuukoshang closedhappy_down at center
	yu "Welcome! Thank you for patronizing this establishment!"
	"The top half of her body drops forward in a bow that looks like an axe chopping through wood."
	"I'm surprised to see it's none other than Yuuko, the librarian."
	hi "Hey, I didn't know you worked here."
	show yuukoshang smile_down
	yu "Oh... Yes, I do. I'm a waitress... I've been working here for one year, six months, and two weeks now... Thank you for choosing to come here, is there anything I can do for you?"
	scene bg suburb_shanghaiint_left
	show yuukoshang smile_down at twoleft
	show shizu behind_smile at right
	show misha hips_grin at tworight
	mi "Hi, Yuu-chan~!"
	show yuukoshang neutral_down at twoleft
	yu "Hello."
	hi "Misha, you both know her too?"
	show misha perky_smile at tworight
	mi "Of course, Hicchan~! Yuu-chan works in the library, after all~! I don't go there often myself, but Shicchan knows her! And~!, we both come here a lot, so it's like we see her all the time!"
	show yuukoshang neurotic_up at twoleft
	yu "Um... Yes... Should I get you your usuals? And... if there is anything you would want, please feel free to tell me at any time."
	hi "You don't have to be so formal, we all know each other."
	"It's also pretty empty today, so she can afford to take it easy."
	"I was hoping she would stop looking so nervous, but my words have the opposite effect."
	show yuukoshang panic_up at twoleft
	yu "No... I'm a waitress, this is my job, I have to... do it properly."
	show shizu adjust_happy at right
	shi "..."
	show misha hips_smile at tworight
	mi "Okay, okay~! That works for Shicchan! Yuu-chan, please get Shicchan what she usually gets, and I'll have some green tea with milk and honey."
	hi "No pressure."
	show yuukoshang neurotic_up at twoleft
	yu "Um, yes... but... this is my job, and... there is always pressure. I'm sorry, I'm arguing with a customer... Sorry! Sorry, sorry!"
	"Yuuko takes another hundred-mile-per-hour bow. I decide to give up and join Shizune and Misha at a table."
	hide shizu
	hide misha
	hide yuukoshang
	"As soon as I sit down, Yuuko comes by looking even more upset than before."
	show yuukoshang panic_up at center
	yu "I'm sorry! I'm really, really sorry, I forgot to take your order... I'm... not attentive to customers, that's not right... I'm sorry... If there is anything I can do to make up for it, please tell me..."
	scene ev shizu_shanghai
	shi "..."
	mi "It's okay, Yuu-chan, Hicchan didn't order anything, so it's not your fault, don't be upset."
	"It's true. I guess I should order now, but I don't really know what this place serves, and there doesn't seem to be a menu."
	hi "Yeah, she's right. I'll have some coffee, and... a sandwich, if you have one. Whichever sandwich you think is the best tasting one here, because Shizune is paying for my meal."
	scene ev shizu_shanghai_borednormal
	"Shizune frowns and gives me alternating looks of surprise, indignation, and bemusement, unable to decide between the three."
	shi "..."
	scene ev shizu_shanghai_boredlaugh
	mi "Hicchan, just how much money do you have in your wallet? It can't be that little, right?, right? We should split the cost three ways, to make it fair~! Yeah, I won't accept anything else~!"
	"Misha turns to Yuuko."
	show ev shizu_shanghai_borednormal
	mi "Yuu-chan, Shicchan says she wants three of whatever is the most expensive item on the menu~."
	hi "No!"
	show ev shizu_shanghai_boredlaugh
	mi "Hahaha~! Just kidding, Hicchan..."
	scene bg suburb_shanghaiint
	show yuukoshang neurotic_up at center
	yu "Um... okay, I think that the turkey sandwich is the most delicious sandwich... And it comes with free soup... A good employee would try to recommend the item that there is the most of, though... or the most expensive item..."
	show yuukoshang worried_up
	yu "Am I bad at my job?"
	hi "No! That sounds good, I'll have that. And some coffee."
	show yuukoshang smile_down
	yu "Okay."
	hide yuukoshang
	""
	show yuukoshang neutral_down at center
	"She comes back a few minutes later with our drinks and my sandwich. Shizune seems to be fine with just her tea, while Misha also ordered a parfait. I don't know why, because I can't imagine many other things that would go worse with tea."
	"Oh well. I take a bite out of my sandwich. It's very good."
	scene ev shizu_shanghai
	shi "..."
	mi "Hicchan, have you thought about joining the Student Council?"
	play music "bgm/blank.ogg"
	hi "Huh?"
	show ev shizu_shanghai_borednormal
	shi "..."
	mi "Don't talk with your mouth full, Hicchan..."
	scene bg suburb_shanghaiint_left
	"I wash my food down with a sip of coffee, which is also surprisingly good. But now's not the time to remark on how this place has good food."
	hi "You said you understood it was too early to expect me to make a decision this quickly! That was like three hours ago!"
	play music "bgm/Generic_Happy_Music.ogg"
	scene bg suburb_shanghaiint_right
	show shizu adjust_smug_close at center
	shi "..."
	scene bg suburb_shanghaiint
	show shizu adjust_smug_close at twoleft
	show misha hips_grin_close at tworight
	mi "A man should be decisive, Hicchan!"
	show shizu behind_blank_close at twoleft
	shi "..."
	show misha perky_smile_close at tworight
	mi "You really should join the Student Council, Hicchan. Come on, it'll be fun!"
	hi "People always say 'come on, it'll be fun' about things that are never, ever fun."
	show shizu behind_frown_close at twoleft
	shi "..."
	show misha cross_grin_close at tworight
	mi "Don't you believe me, Hicchan?"
	"Is it Shizune saying that or Misha? What a cute expression; but the effect is somewhat jarring, like she has split personalities."
	hi "Uh..."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha hips_frown_close at tworight
	mi "Hicchan, that's depressing. We just want to spend time with you..."
	show shizu behind_smile_close at twoleft
	shi "..."
	show misha hips_grin_close at tworight
	mi "That's right, Shicchan! Yeah, that's a good point too!"
	show shizu adjust_smug_close at twoleft
	shi "..."
	mi "Yup, this is beneficial to everyone, it solves all our problems~."
	show shizu behind_frown_close at twoleft
	shi "..."
	show misha perky_sad_close at tworight
	mi "Yeah, I also thought Hicchan would appreciate it... That makes me sad."
	"Suddenly I feel really left out."
	hi "It's rude to talk about someone without letting them in the conversation."
	show shizu adjust_happy_close at twoleft
	"Shizune adjusts her glasses, laughing to herself."
	shi "..."
	mi "Aw, but it's true, Hicchan~! And you would be helping us out, membership has been really low this year."
	hi "How low?"
	show misha sign_confused_close at tworight
	mi "Ah, that's a secret, Hicchan."
	hi "No, I want to know how low it was. How low is 'low'?"
	mi "Ahaha..."
	hi "Five?"
	show shizu behind_blank_close at twoleft
	shi "..."
	hi "Lower?"
	show misha perky_sad_close at tworight
	mi "Well..."
	hi "Zero?"
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha hips_grin_close at tworight
	mi "Wahaha~! Hicchan, that isn't important. What matters is that the number is low, and that is why we would appreciate you giving us a hand, especially with the festival coming up so soon, and it looking to be a busy year ahead in general."
	hi "So you're not going to answer my question?"
	show shizu adjust_smug_close at twoleft
	shi "..."
	mi "No~."
	"I sigh and straighten up in my chair, trying to look as defiant as possible, because this seems like a big issue and I do not want to let it go that easily. I feel silly, like a blowfish."
	hi "Fine, at least tell me this: How many people are in the Student Council? Total?"
	show shizu behind_blank_close at twoleft
	shi "..."
	show misha perky_smile_close at tworight
	mi "Um, well, Hicchan, we're definitely undermanned, but we have enough members to get the job done. Yup, yup~!"
	hi "It's not just the two of you, is it?"
	show misha cross_laugh_close at tworight
	mi "Hahaha~! Hicchan, that's funny~!"
	show shizu basic_normal2_close at twoleft
	shi "..."
	show misha cross_smile_close at tworight
	mi "But~! It's definitely not just us."
	hi "Are you sure? Are you absolutely sure?"
	show misha cross_grin_close at tworight
	mi "Yup~!"
	"I stare at them both, trying to see if they will slip up and confirm my worst fears."
	show misha perky_sad_close at tworight
	"Misha frowns, looking uncomfortable, but that is probably because I'm staring at her."
	show shizu basic_happy_close at twoleft
	"Shizune, on the other hand, returns my gaze with one of her own. Maybe she is challenging me, peering at me over the rims of her glasses like that. So teasing; and surprisingly immature, like a little girl beckoning someone to play with her."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha perky_smile_close at tworight
	mi "Hicchan, your two cute student council representatives have been trying to make you feel welcome and are even treating you to lunch. You should show your gratitude by joining the council so you can at least help them out."
	mi "Yeah, it would be great if you could just file some papers for us, and... the festival is coming up, and we have to build some stalls for the games and food, just a few, so if you were there, it would be a lot easier for us..."
	show misha perky_sad_close at tworight
	mi "Please, Hicchan?"
	"What an interesting good cop-bad cop routine."
	"I'll give it a shot. Why not?"
	"Just a shot."
	hi "Okay, I'll give it a trial run. It doesn't mean I'm joining, or anything definite, just that I'll help out a little, and then I'll see. And this makes us even for lunch, I'm not doing this because I want to."
	show misha perky_smile_close at tworight
	show shizu basic_frown_close at twoleft
	"I finish off the last of my sandwich, and this makes Misha notice for the first time in a while that she has a parfait. She starts digging in, much to Shizune's chagrin, because I can tell from the way she plays with her fingers that she had a lot to say."
	play music "bgm/blank.ogg"
	show shizu behind_blank_close at twoleft
	"Every time I look at Shizune, she looks back with such focus and intensity. This time is no exception. Her face is expressionless; maybe she is thinking. Eventually, it gives way to a smile."
	show shizu adjust_happy_close at twoleft
	shi "..."
	"She signs something, and obviously, I can't understand it at all. She has to know that. Then, she does it again, a childish playfulness showing through in the speed and energy of her gestures."
	show shizu adjust_smug_close at twoleft
	shi "..."
	show shizu adjust_happy_close at twoleft
	hi "Misha, what did she say?"
	show misha perky_confused_close at tworight
	mi "...?"
	"Misha looks up from her parfait, torn between wanting to help out and going back to eating."
	hi "What does this mean?"
	"I try my best to make the same movements with my hands that Shizune did. I come to realize quickly that this isn't very easy. Imagine doing this all day, as your only means of communication."
	show misha perky_smile_close at tworight
	mi "Hmm~... Sorry, Hicchan, I can't tell you."
	hi "Why not? Is it an insult?"
	show misha hips_grin_close at tworight
	mi "No, Hicchan, I can't tell you because~!, it means something nice."
	"Something nice, huh? Well, they've gone back to their tea and food, so I guess this conversation is over for now."
	hide misha
	hide shizu
	"I don't really understand. But this makes me wish that I could. Maybe I could even try learning sign language. This school might have courses for it."
	"Would I really do that? I think about it as I finish the rest of my coffee. I wonder why I'd even be motivated to think about it."
	"I'm enjoying myself so much that I don't even notice that we were supposed to be back in class ten minutes ago."
	"Even if I were to start heading back to school right now, it would take at least... thirty minutes? Maybe. I can't risk running fast with my condition, so it would take at least that long to get there."
	"Well, ten minutes late already as I am, it wouldn't matter even if I could teleport."
	show shizu behind_blank_close at twoleft
	show misha perky_confused_close at tworight
	mi "Something wrong, Hicchan?"
	hi "I just realized lunch break ended ten minutes ago. It's only my third day, and I'm already going to miss a class."
	play music "bgm/Hokabi.ogg"
	show shizu adjust_smug_close at twoleft
	shi "..."
	show misha hips_grin_close at tworight
	mi " Yup~! You are already late."
	hi "Hey, that's not funny, so are you! And, aren't you two in the Student Council? You're setting a bad example."
	show misha perky_sad_close at tworight
	mi "Hicchan is so moral..."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha sign_smile_close at tworight
	mi "But~! Hicchan is right, he is late for class, and~ it looks like you're cutting too, Hicchan, because you're not making an effort to go."
	mi "As your student council representatives, we're going to have to do something about this and make sure you're punished for it~!"
	hi "But you two dragged me out here, this is all your fault. Take responsibility!"
	show shizu behind_frown_close at twoleft
	shi "..."
	show misha hips_smile_close at tworight
	mi "Hicchan, we were just taking a prospective student council member out to try and recruit him. It's business, business~! But~! You're not a member of the council, so there's no excuse!"
	hi "Yes, there is. That prospective student council member is clearly me."
	show shizu basic_happy_close at twoleft
	shi "..."
	show misha hips_grin_close at tworight
	mi "Yes~! Are you going to join the Student Council, Hicchan?"
	"Shizune raises her teacup haughtily and wags her outstretched pinky finger up and down."
	show shizu behind_blank_close at twoleft
	shi "..."
	show misha perky_smile_close at tworight
	mi "Hicchan, if only you were a member of the Student Council... But~! You can still join now, Hicchan! If you join now, you won't be in any trouble at all, and we'll be able to take many more nice excursions like this all the time! It'll be fun~!"
	"I start to think that, maybe, this was all an elaborate set-up leading up to this moment. Maybe Shizune lured me out here, banking on the possibility that I'd lose track of time and be forced into this situation."
	"Diabolical. ...Well, considering what I know of her, I should have been more on my guard. But to admit that I got myself into this, even slightly, would be unforgivable."
	"I try to read Shizune's intentions in her eyes, but she just returns my stare blankly. Innocently. She takes a sip of tea, like she is mocking me."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha sign_smile_close at tworight
	mi "By the way, Hicchan, I didn't plan this at all, things just happened to work out this way~!"
	"I was almost about to drop my theory as paranoia, but this puts a new spin on things. I almost fall over in awe. So it really was an elaborate set up, from the very beginning, all just to burn me and force me to join the Student Council."
	show shizu adjust_smug_close at twoleft
	shi "..."
	show misha cross_laugh_close at tworight
	mi "Ahahahaha~! You look so nervous, Hicchan~! Did you really think we were tricking you this whole time?"
	hi "You're not?"
	show misha perky_sad_close at tworight
	mi "Hicchan, you really thought...?"
	show shizu behind_frown_close at twoleft
	"Misha frowns, looking heartbroken. Shizune quickly frowns as well, following her lead. How synchronized. Two of a perfect pair. They must be twins."
	shi "..."
	mi "Shicchan says she's flattered, Hicchan, but doing that kind of thing would be a grossly inappropriate abuse of power, and imposing on your free will~! And~! It would be blackmail, too! Shicchan would never do anything like that, never!"
	"I think about asking Misha, 'Are you sure?' but resist the urge to."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha perky_smile_close at tworight
	mi "Anyway, Hicchan, what Shicchan said is true. Since you're with us, and we're doing student council work, it's okay if we miss a class or two."
	show shizu basic_normal_close at twoleft
	shi "..."
	show misha perky_confused_close at tworight
	mi "Not that this is a good excuse to do so..."
	shi "..."
	show shizu behind_blank_close at twoleft
	mi "...Or one that should be used more than three times a month..."
	show shizu basic_normal_close at twoleft
	shi "..."
	mi "Or something that can or should be abused..."
	show shizu adjust_happy_close at twoleft
	shi "..."
	show misha hips_grin_close at tworight
	mi "So~! We must definitely, definitely return to class! Eventually~!"
	show misha cross_laugh_close at tworight
	mi "Wahaha~!"
	"Shizune waves Yuuko over and points to her empty teacup, indicating that she wants another one, as Misha scrambles to finish her parfait so she can order something else. Maybe I should as well."
	"I am still hungry, and the portions here are a little on the small side. Most importantly, Shizune is paying for everything. With that in mind, I ask Yuuko for another sandwich."
	scene bg suburb_shanghaiext
	play music "bgm/blank.ogg"
	"By the time we leave the tea shop I've missed not just one class, but two."
	scene bg suburb_roadcenter
	"Shizune and Misha seem content to let the whole day pass by, stalling for even more time by suggesting a tour of the town that turns out to cover a two block radius from where we start."
	scene bg school_scienceroom
	"Eventually, we do go back to school, and the rest of the day is business as usual. When classes are over, Shizune and Misha pack their bags and leave the room before me. Come to think of it, this is the first time they've left me alone."
	"It's strange, I almost miss them. The room empties quickly, and I'm the last one out the door."
	scene bg school_lobby
	"When I try leaving the lobby, however, an arm lowers itself in front of me like a toll bridge gate, stopping me in my tracks."
	show shizu behind_blank at center
	shi "..."
	hi "Oh, hi Shizune."
	scene black
	"A pair of hands from behind cover my eyes, followed by a sharp burst of laughter."
	mi "Hi, Hicchan~! Guess who!"
	"Misha asks the question completely without sarcasm, meaning she doesn't think that I instantly knew it was her for many obvious reasons."
	hi "I wonder who it could be? Well, it's definitely not Misha..."
	mi "Hahaha~! It is!"
	play music "bgm/The_Student_Council.ogg"
	scene bg school_lobby_right
	show shizu behind_blank at tworight
	show misha hips_grin_close at twoleft
	"Misha swings around to stand in front of me, beside Shizune."
	show shizu basic_normal2 at tworight
	shi "..."
	show misha cross_smile_close at twoleft
	mi "Hicchan, are you busy right now?"
	hi "Busy going to my room, yeah. See you two tomorrow!"
	show bg school_lobby_right
	show shizu behind_blank_close at tworight
	show misha perky_smile at twoleft
	"I try to make a break for it, but Shizune is too agile to get past. As someone who used to play soccer, this is embarrassing. Not to mention that this behavior is drawing some odd looks. I should just quit while I'm ahead."
	show shizu adjust_happy_close at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "Hicchan, could you please go upstairs and get a few things for us from the art room?"
	hi "Why me?"
	show misha cross_laugh at twoleft
	mi "Hahaha~! Shicchan thinks that if the art teacher sees us, he will say hi, and she doesn't like him!"
	hi "Ignore him."
	show shizu behind_blank_close at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "She tried, but even though Shicchan is deaf, he'll try to say 'hi~!' anyway!"
	hi "Run away?"
	show shizu cross_angry_close at tworight
	shi "..."
	show misha perky_smile at twoleft
	mi "I never run!"
	"A tone of finality so strong that I can pick it up even through Misha. I can see there is no use pursuing this further with Shizune."
	hi "Misha, why can't you get them?"
	show misha sign_smile at twoleft
	mi "Stairs make me dizzy, Hicchan!"
	show shizu basic_normal_close at tworight
	hi "..."
	"Shizune nods, as if to confirm it."
	show misha perky_sad at twoleft
	mi "Please, Hicchan? We need these things to build stalls for the festival, and you said you would help out a little, right?, right?"
	"I really shouldn't, but I guess just this once would be all right."
	hi "Okay."
	show shizu adjust_happy at tworight
	shi "..."
	show misha hips_grin at twoleft
	mi "That's great, Hicchan! Thank you~!"
	show misha perky_smile at twoleft
	mi "This is what we need!"
	"She holds out a piece of paper for me to take."
	"I'm sure this list was made by Shizune. It's handwritten, but each letter is perfectly formed and uniform, as if it were typed. Not just that, but it's exhaustively detailed, complete with numbers, bullet points, and even little checkboxes."
	"What it boils down to is that she wants paint, paintbrushes, posterboard, and an easel. Just different types and specific numbers of each. I wonder how I'm going to carry all of this stuff down the stairs without breaking my neck."
	jump en_A16
label en_A13:
	play music "bgm/Raindrops_and_Puddles.ogg"
	scene bg school_miyagi
	"Lilly and Hanako quickly go about the business of making lunch."
	"Before I can even open my small bag of food, Lilly's busying herself with her thermos and teabags as Hanako is setting out both their lunchboxes."
	show lilly basic_smile at center
	hi "So, is this what you meant by coming here almost every day?"
	show lilly basic_smileclosed
	li "Yes, Hanako and I usually have lunch here. It suits both of us, so we ended up using this room regularly."
	"After seeing Hanako's reactions to me over the past couple of days, I can understand why that is a boon. That, and Lilly being able to get some quiet away from her class as well."
	"I take my seat last, after Lilly's poured the tea for us and sits down."
	scene bg tearoom_everyone_noon
	show tearoom_hisaoe lsmile
	show tearoom_lillye smileclosed
	show tearoom_hanae sad
	"The more time I spend with these two girls, the more I think they're a perfect foil to Misha and Shizune."
	"Even without a voice, Shizune is direct and brash, and Misha seems to get along with everyone. On the other hand, Lilly is soft-spoken and relaxed while Hanako seems to be the shyest girl I've ever met."
	li "So, how are you faring in Yamaku, Hisao? You seemed a bit flustered before."
	show tearoom_hisaoe sigh
	hi "Apart from getting lost every now and again, and being crash-tackled outside my classroom? Fine I guess..."
	show tearoom_lillye smileclosed
	show tearoom_hanae shy
	ha "You... you looked pretty hurt before. Are you really... okay?"
	"For a brief moment, I consider telling Hanako and Lilly about my condition but then, I hold it back."
	"I can't tell why, but for some reason I feel uncomfortable talking about it to these relative strangers, even if they have been pretty friendly."
	show tearoom_hisaoe hrelief
	hi "Yeah, it's nothing. I was just a bit startled."
	show tearoom_lillye thinking
	show tearoom_hanae sad
	show tearoom_hisaoe lthink
	"Judging from the two girls' expressions, I don't think that they're buying it. But, in what I assume is their way of respecting my privacy, they don't press the matter."
	"I guess that is one of the unwritten rules around here; 'don't ask.' Even if people's conditions are obvious, like Hanako's, there's still bound to be a story involved."
	"Everyone has things that they don't feel comfortable speaking about, and I think everyone here recognizes that."
	show tearoom_hisaoe lsmile
	hi "So, uh... how long have you been in this school? You both seem to know your way around pretty well."
	show tearoom_lillye smileclosed
	li "Hmm... well, I've been here since the start of high school, but only moved into the dormitories a year ago."
	li "Hanako joined at the start of high school as well, and moved to the dormitories when she did, if memory serves me right."
	show tearoom_hanae shy
	ha "That's right. Since... high school."
	hi "So you've known each other since then?"
	show tearoom_lillye ara
	li "Since I moved, yes. Hanako lives next door to me, so it's only natural, right?"
	ha "R-right."
	show tearoom_hisaoe calm
	hi "Yeah, of course."
	"Living next to someone is probably reason enough to befriend them, though I'm guessing that Lilly's blindness played a part in it as well."
	"I can't imagine Hanako easily making friends with someone who has to deliberately avoid looking at her scars."
	"With the immediate conversation dried up, we start to eat our lunch."
	scene bg tearoom_everyone_noon
	show tearoom_hisaoe lsmile
	show tearoom_lillye weaksmile
	show tearoom_hanae sad
#	play sound "sfx/warningbell.ogg"
	"It isn't long before the bells are signaling the end of the break. Like me, the girls pack up their lunches as efficiently as they set them out."
	show tearoom_lillye smileclosed
	li "I guess I'd better be off. Are you going to go with Hisao, Hanako?"
	show tearoom_hanae shy
	show tearoom_hisaoe hthink
	"Hanako looks up at me, and for a second I can see that she is considering skipping class, maybe just to avoid walking to the classroom with me."
	show tearoom_hanae sad
	ha "Y-yes."
	"I don't know what to think of it. Hanako really is delicate to the point of breaking if looked at in the wrong way. It makes me a bit nervous too, but I push the feeling aside, trying to be as natural as I can."
	show tearoom_hisaoe hsmile
	hi "We should hurry then. Class has already started by the sound of it."
	"Lilly gives a nod of farewell as she bends down to take her cane, Hanako and I filing out before her."
	scene bg school_hallway3
	"We walk quickly down the empty halls to our respective classes."
	"As we reach the door to Lilly's 3-2 classroom, she turns towards me."
	show lilly cane_smileclosed at twoleft
	show hanako emb_timid at tworight
	li "Hisao, thank you for sharing lunch with us today."
	hi "My pleasure, Lilly."
	hide lilly
	play music "bgm/blank.ogg"
	scene bg school_hallway3_left
	show hanako emb_timid at center
	"And with that, we part ways; Lilly entering her classroom and leaving Hanako and I to make off to our own. She's still looking like she wants to run away."
	hi "So, do you really want to go back to class now?"
	show hanako basic_worry
	ha "Y-yes."
	hi "Okay then."
	"I feel like I should say something more to her, but it's hard to come up with anything that would be appropriate and safe enough."
	"And Lilly was right; the more time we spend out here, the more explaining we have to do."
#	play sound "sfx/dooropen.ogg"
	"I open the rear door to the class, and walk in."
	scene bg school_scienceroom
	show muto irritated at center
	"The teacher looks up at me, and opens his mouth to say something."
	show muto normal
	"However, as Hanako follows me in and closes the door, he simply nods to us and continues his lecture."
	"This is the third time that Hanako has had her truancy practically ignored. There's definitely something going on here."
	hide muto
	"We make our way to our seats, and I notice that Misha and Shizune are both missing as well."
	"I wonder if it is some form of informal agreement with the staff, or if it's a 'perk' afforded to the unique students of this school?"
	"Trying to make as little disturbance as I can, I extract the relevant textbooks from my bag and start catching up."
	"The class goes on quietly."
	jump en_A15
label en_A15:
	scene bg school_scienceroom
	"The teacher seems like an okay person despite the weird first impression I got, and the material is relatively interesting."
	"However, the way he teaches is really bizarre. It's as if he expects that everyone is a natural genius."
#	play sound "sfx/normalbell.ogg"
	play music "bgm/Afternoon.ogg"
	"When the final bell sounds, I realize that there is still a lot of time left in the day, and I'm left wondering what to do."
	"It's odd, at the hospital I had 24 hours a day of free time, but here filling the considerably shorter hours feels difficult."
	"Everyone else leaves, and I'm left alone with the teacher."
	"Mutou is examining the assignment sheets we were working on earlier, marking them with a red ballpen."
	"Raising his eyes from his papers briefly, he notices me and furrows his brow."
	show muto normal at center
	mu "What is it, Nakai?"
	"I jump at him addressing me, but I guess it's natural to spark some conversation since there is nobody else around."
	hi "Umm... nothing. Thinking about what I'd do after school."
	"The teacher slowly puts the cap on the pen he is holding and arranges his papers into a stack, clacking it against the desk twice."
	"He seems very methodical and for a brief moment I'm reminded of Shizune, but the teacher is more unhurried and relaxed, much more routined."
	mu "You have no plans?"
	hi "No. I considered joining a club, but don't know what kind of club would interest me."
	mu "Go observe a meeting of someone else's club. Might pique your interest."
	hi "I guess..."
	hi "I just..."
	"But I don't know how to continue from there."
	show muto irritated
	"Mutou looks at me in a way that makes me quickly want to take the words back to avoid a conversation."
	"But I can't, so I have to forge ahead."
	hi "I just don't know how to deal with people. I mean, the other students."
	hi "I'm talking to people and everything, so it's not that I'd be isolated or anything."
	hi "I just don't know what to think about... the disabilities. It's like... it feels that I'm being impolite if I pay attention to them, and it's weird to ignore them."
	hi "Damned if I do, damned if I don't."
	"The teacher scratches his cheek absentmindedly, looking very unresponsive."
	show muto normal
	mu "These things are only an issue if you make them one."
	mu "You can talk normally with someone, even if they are blind or something."
	show muto smile
	mu "Try to look behind the superficial. There's not a single student here who isn't just a normal kid behind whatever they might seem at first glance."
	"He says the same thing as Yuuko did."
	"I know they're right, but it's hard. How can you not consider for example Shizune's deafness, when the only way to communicate with her is to talk through Misha?"
	"Or Hanako... it's not like you can ignore her face."
	hi "But..."
#	play sound "sfx/doorslam.ogg"
	play music "bgm/blank.ogg"
	show muto irritated
	"I'm interrupted by the door of the classroom suddenly slamming open."
	scene bg school_scienceroom_left
	show muto irritated at twoleft
	show misha hips_grin at tworight
	with ease
	play music "bgm/Generic_Happy_Music.ogg"
	mi "Teacher~!"
	"Misha crashes in, hand straight in an enthusiastic greeting, her voice loud and lively enough to wake the dead from their graves."
	"She starts towards the teacher's desk with her bouncing step, hands energetically swinging with the rhythm."
	"Mutou, visibly dismayed at the interruption and Misha in general, slumps in his chair."
	mu "Mikado."
	"Misha stops in her tracks and looks around cluelessly, as if she's sensing from his tone that something's wrong but has no idea what."
	show misha perky_confused at tworight
	mi "Yes~?"
	mu "We have talked about volume control before."
	show misha perky_smile at tworight
	mi "Yes~!"
	"But she doesn't lower her voice at all, and the teacher just rubs his eyes."
	mu "So, what is it?"
	show misha perky_sad at tworight
	mi "I... we need help! We are running out of supplies for the festival stands!"
	show misha sign_sad at tworight
	mi "This is a distress!"
	"She waves a pink slip of paper she's holding around."
	mu "So... go get more supplies from the art room. What's the problem with that?"
	show misha perky_sad at tworight
	mi "Plywood! Plywood is always the problem! Last time we wanted more there was only a little, but that time we just took it all and went with that."
	mi "Now there's like none left there, so do you know where there is some?"
	mu "I don't understand. How would I know?"
	show misha perky_confused at tworight
	mi "Shicchan... I mean the president thought that a teacher would know if there is plywood. Was she wrong?"
	"Mutou looks like he is in great pain, frowning with his entire essence, and Misha doesn't get it at all."
	"Looking at the two of them communicate is terrible, like looking at a man being tortured by drilling his skull open while blasting pop music at full volume at the same time."
	mu "I'm afraid I have no idea if there is any plywood in the school, let alone where it would be if there was any."
	show misha perky_sad at tworight
	mi "Awww... what should I do?"
	mu "Perhaps try to find Mr. Nomiya? I'm quite sure he would know where to find everything you need."
	mu "You'd have to pry them from his cold, dead hands, but that's a different matter."
	mi "Aaaah! I don't have time! We are so busy!"
	"She holds her head with both of her hands, looking as despairing as it's possible for a person like her. Without even noticing, she crumples the note she's holding against her hair."
	mi "I shouldn't even be fetching these things, there is so much to do and we are falling behind the schedule!"
	show muto smile at twoleft
	play music "bgm/blank.ogg"
	"Mutou looks at her gravely and then, suddenly smiles. Smiling doesn't really fit his face. I think it'd be better if he didn't."
	mu "I wonder if you could get some temporary help?"
	show muto normal at twoleft
	"He switches to staring at me focusedly, with a hard expression, as if trying to say 'go make some friends.'"
	"..."
	hi "Eehhh... I guess I can give you a hand."
	play music "bgm/Hokabi.ogg"
	show misha hips_grin at tworight
	mi "You can? Thanks, Hicchan, you are really nice!"
	show misha sign_confused at tworight
	"She pauses, does a double take and then points at me with her finger, yelping 'Ah!' and looking very puzzled."
	mi "Come to think of it, what's Hicchan doing here? Class is over, you should be having fun~!"
	mu "We just had a little chat."
	show misha perky_sad at tworight
	mi "Oh no! It's not detention is it? Are you in trouble, Hicchan?"
	hi "No, I'm not."
	mi "Is Hicchan in trouble, teacher?"
	mu "No, he's not."
	"Mutou sighs deeply and I feel that I have to help Misha to get her off the teacher's back."
	hi "So what do you need?"
	show misha hips_smile at tworight
	mi "Here's a list. I can try to find the plywood from somewhere if there's none in the art room."
	"She offers me the note she's holding. I take it, hesitating a bit."
	hi "I said I'd help you, but this has no implications on whether I'm joining the council or not."
	show misha perky_sad at tworight
	mi "Awww...."
	show misha hips_grin at tworight
	mi "Still, thanks, Hicchan. Try to be quick, we are in a stall-building streak now, we must hurry hurry hurry!"
	hide misha
	"She bounces out of the classroom, leaving me and the teacher looking at each other with something that feels like a silent agreement."
	scene bg school_scienceroom
	show muto normal at center
	mu "Well, there you have it, Nakai. You have something to do now."
	"Please don't sound so smug."
	"Looking at the list with a number of items ranging from paint to plywood, all written with small, neat handwriting that is undoubtedly Shizune's, I heave a sigh."
	hi "I'll be going then."
	play music "bgm/blank.ogg"
	"Waving the long list limply at the teacher, I exit to the hallway."
	jump en_A16
label en_A16:
	scene bg school_hallway3
	"The classrooms closest to ours are designated belonging to classes 3-1 and 3-2 on the right side, and 3-4 on the left side, each door looking exactly the same."
	"Further down the corridor still with identical doors, are rooms that I didn't think were used for classes."
	"I guess the art room is not a classroom as such."
	"I carefully push open the furthest door, and peek in."
	scene bg school_classroomart
	"It's a classroom, but it seems rather badly kept or not in use. Am I in the right place?"
	"Desks and chairs are all around the room, a thin layer of dust settled on them. There are some easels in the corner so at least this looks like the right place."
	"The room is flushed in sunlight from the big windows, shadows creeping all over the desks."
	"Specks of dust are dancing in the stagnant air, making the beams of light almost visible."
	"Jokingly, I call into the empty room."
	hi "Anybody ho--"
	"Something catches my eye and I stop mid-sentence."
	scene ev rin_eating
	play music "bgm/Parity.ogg"
	"Sitting on a desk is a short-haired girl; curiously wearing a boy's uniform, with a fork between her toes, a morsel of food stuck firmly on the end."
	"This odd way of dining seems to be caused by her apparent lack of hands, but her presence here is what takes me aback even more."
	"How did I miss her before? She's sitting in a corner very still, but I still somehow took her as a part of the furnishing or a statue at first glance."
	"I'm not being too observant today, as a whole."
	"The girl seems to be frozen in place, staring at me with her huge eyes like a rabbit in headlights."
	"She's staring at me, her mouth wide open, ready to accept the fork."
	"I'm staring at her, my mouth wide open, suddenly remembering I didn't finish my sentence and trying to think if I should."
	"This weird stalemate keeps us both stunned into silence, punctuated only by the wall clock ticking rhythmically."
	rin_ "Hello."
	"The girl stuffs the forkful in her mouth, and is now staring at me expectantly while chewing. This is a bit awkward."
	hi "Umm... hello. I was told to pick up some supplies from here. For some festival stalls I think. I didn't think there would be someone here."
	rin_ "There isn't. That's why I came here, too."
	"She picks up another forkful."
	hi "Doesn't that mean you're here, then?"
	scene bg school_classroomart_left
	show rin relaxed_surprised at center
	"She raises her eyebrows as if she was suspecting my observation was false."
	rin_ "You are pretty observant. I guess it does. But who are you?"
	"This girl is pretty straightforward, isn't she?"
	hi "I'm Nakai, Hisao Nakai. I just transferred in on Monday."
	show rin basic_absent
	rin_ "I'm Rin. Tezuka Rin. Rin Tezuka."
	show rin basic_deadpandelight
	rin "I won't shake hands with you, but at least we know who we are now."
	rin "That's very nice."
	"Her deadpan manner of talking makes it hard to determine whether she's joking about shaking hands or not."
	"It kinda bothers me, joking about these matters doesn't feel appropriate at all."
	show rin relaxed_nonchalant
	"While I'm trying to figure what's appropriate and whether this girl is, she seems to have lost interest in me and is now gazing yearningly back at her food."
	show rin basic_deadpan
	rin "Can I continue my lunch? If you don't mind me, I won't mind you."
	rin "If you need to get your stuff, the supplies are at the back."
	hi "Go right ahead. But... lunch? School's already over for the day."
	show rin basic_awayabsent
	rin "What word would you use then? There is no word for a meal you eat after lunch but before dinner, right? It bothers me very much too, but I don't really know what I should say."
	hi "I don't think you are supposed to eat a meal between lunch and dinner to begin with."
	show rin negative_spaciness
	rin "But I'm hungry now and my delicious boxed lunch would go to waste otherwise."
	show rin basic_delight
	rin "I have curry. It's very delicious."
	"With much decisiveness, Rin once again picks up the fork between her toes and with at least as much impoliteness, she points it straight at me."
	scene ev rin_eating
	rin "So, Nakai, what brings you to this place?"
	hi "Like I said, I was told to look for these things."
	play music "bgm/blank.ogg"
	rin "No, the school. From outside you look fine. Is your problem inside?"
	"I come to a full stop, opening my mouth but not getting a word out."
	hi "I..."
	rin "I can guess. I am good at guessing. Better than most people."
	"Rin cuts me off before I can answer her question, or skirt around it somehow. I don't know which I would've done."
	"I froze in front of this issue again. I haven't even told anyone here about my condition, or maybe it's only because it hasn't really come up."
	"I do get the feeling that not making issues of this is a part of the social code here, as the teacher said."
	"I wonder if the people here could relate? Probably not any better than any normal person could."
	"I can't relate to Shizune's circumstances, or Lilly's, either."
	scene bg school_classroomart_left
	show rin basic_absent at center
	"Naturally, while I go through this in my head, Rin keeps considering what my condition could be, with an overtly contemplative look on her face."
	"She puts her fork between her lips and leans back, looking at the ceiling as if the answer was written up there."
	"A beam of light illuminates her face from the window side, creating a mask of dark shadow on the other side."
	show rin basic_lucid
	rin "I don't think it's anything in your head, and something in your guts would be boringly ordinary, like this lunch of mine. And less delicious."
	show rin basic_deadpandelight
	rin "The problem must be in your pants!"
	play music "bgm/Parity.ogg"
	"This messed-up Sherlock Holmes kind of statement and the sheer lack of tact it was delivered with catches me completely off guard."
	"I think I might've reeled back even physically as Rin's eyes widen in revelation and astonishment."
	show rin relaxed_surprised
	rin "So I was right! There's something wrong with your tackle, isn't there?"
	"Still partially in shock but recognizing the need to reply something, I spit out the first thing that I can think of."
	hi "No! Nothing like that. I have a heart problem. Arrhythmia."
	"..."
	"I said it. More like blurted it out, but I said it."
	show rin negative_spaciness
	"The girl in front of me purses her lips together and glowers at me, looking very disappointed."
	rin "How boring. Trouble in the pants would have been much more scandalous."
	"What's with this reaction?"
	hi "I'm sorry to let you down."
	show rin basic_awayabsent
	rin "I forgive you. Just, I collect people and a person with, you know, that kind of problem would've been really great."
	hi "Collect people?"
	show rin basic_absent
	rin "People with different problems."
	hi "Huh, so you just... like, go around asking people what's wrong with them?"
	show rin basic_deadpannormal
	rin "Pretty much."
	hi "I see."
	"..."
	play music "bgm/blank.ogg"
	hide rin
	"With little left to say, Rin resumes her lunch and the conversation dies away, but I keep thinking about what was said."
	"It's the first time I told anyone else about my condition. All the other people have either known about it already, or heard about it from someone else."
	"Or didn't need to know about it, like every other student here, so far."
	"Should I have told it as a natural part of introductions? Is it expected of me?"
	"'Hi, I'm Hisao. I have a very serious heart condition.'"
	"Is that how I'm supposed to go around introducing myself from now on?"
	"As if our disabilities would define us. What a disgusting thought."
	"Or maybe this Tezuka girl just has an unnatural interest in such things."
	play music "bgm/Raindrops_and_Puddles.ogg"
	scene bg school_classroomart_right
	show rin basic_awayabsent at right
	"As I walk to the back of the room to pick up the items on Misha's list, a chance opens to study Rin from the corner of my eye."
	"Her hair is a burnt auburn, almost orange, and cropped short. Long hair would probably be impossible with no arms."
	"The boy's uniform and the lack of arms make her look very thin, almost scrawny."
	"She is not particularly pretty except for her murky green eyes which flicker restlessly from below her short bangs, even when she eats."
	"The distance and the shadows make it seem like they don't reflect sunlight at all, but instead absorb all of it within them like deep wells."
	"She moves her feet almost as deftly as a normal person would use their arms."
	"However, I can see how this sight could discomfort people, especially while eating. It makes me feel a bit uncomfortable at least."
	"I hesitate to think about the word 'unnatural' but it's too late now, isn't it?"
	"I keep searching the cabins and shelves for Misha's things, but after enough time passes the silence grows too uncomfortable, so I try to force some conversation out of this strange girl."
	hi "So, do you always eat alone and this late? Or do you get the occasional visitor?"
	scene bg school_classroomart_left
	show rin basic_absent at center
	rin "Visitors... maybe you are my first occasional visitor. But I don't always eat alone either."
	rin "Sometimes I eat with a certain person on the roof, if she's not horsing around."
	hi "Horsing?"
	show rin basic_deadpan
	rin "She likes to do sports."
	hi "Oh."
	"And that's all I can think of to say."
	"Both of us fall silent again as Rin forks the last bits of her meal to her mouth."
	"I look down at my haul and double check it with Misha's list. It seems I have everything except plywood."
	hi "Umm... so, I think I have all the things now."
	show rin basic_deadpannormal
	rin "That's very nice for you. Don't feel obliged to stay. I was about to take a nap anyway."
	rin "You need to do whatever you are going to do with that stuff anyway, right?"
	show rin relaxed_surprised
	rin "Or perhaps you like to watch girls sleeping?"
	hi "Ehh..."
	"I'm not sure what to make of this, but Rin looks serious."
	hi "Even if I did, I think I have to be going."
	hi "I... I'll catch you around, Tezuka."
	show rin basic_absent
	rin "You can call me Rin."
	show rin basic_awayabsent
	rin "I feel that our relationship is at this point good enough to warrant this much."
	"I was already turning to make my exit, but she draws me back in."
	hi "Fine, then I'm Hisao."
	show rin basic_deadpannormal
	rin "Then you are."
	"..."
	"Rin looks at me hard in the eyes but that intimidating feeling you get when someone stares at you isn't there."
	"It's like she's actually not looking at me at all."
	"She blinks a couple of times, and I can't figure out why a pause like this just popped between us out of nowhere."
	show rin basic_deadpandelight
	rin "See you later, Hisao."
	"There is something like a tiny smile there in her face, maybe."
	scene bg school_hallway3
#	play sound "sfx/doorclose.ogg"
	"I quietly back out of the room. As I shut the door in front of my face, I whisper to myself."
	hi "What an intriguing person..."
	"From inside, I hear a muffled, sing-song voice:"
	rin "I heard tha~t!"
	play music "bgm/blank.ogg"
label en_A17:
	scene bg school_hallway3
	show misha hips_grin_close
	mi "What did she hear?"
	play music "bgm/Generic_Happy_Music.ogg"
	"I jump at the sudden appearance of Misha, who I had not heard approaching despite the completely empty hallway."
	"Somehow she had gotten to jumping distance of me without making a sound. Creepy. It briefly reminds me of Kenji's nutty theory about a global feminist conspiracy, but I push that thought aside."
	show misha hips_grin_close at twoleft
	show shizu behind_blank at tworight
	"Shizune, standing slightly behind Misha, looks aloof as she couldn't have heard the remark that drew Misha's attention, but Misha is visibly excited."
	show misha perky_confused_close at twoleft
	mi "No wait, more importantly, who is in there? There's no club meetings today."
	"She tries to curiously peek past me, even though the door prevents her from seeing anyway."
	hi "What are you doing here?"
	mi "You took so long that we had to come check what's wrong. That's no good, Hicchan~"
	show misha hips_frown_close at twoleft
	"She wags her finger at me scoldingly."
	mi "I found plywood, but everything else is still missing because you are tardy."
	hi "Oh, sorry. Err... I got the things here, was just going to bring them."
	show misha cross_frown_close at twoleft
	mi "I think you were up to some mischief, Hicchan~! Who was in there with you, I wonder..."
	"Misha signs something quickly to Shizune, pointing at her own ear a couple of times."
	show shizu basic_angry at right
#	play sound "sfx/dooropen.ogg"
	"Shizune immediately pushes her way past me and opens the door into the classroom I just left."
	"I can only imagine the shock she is experiencing."
	"With Shizune's diligence and attitude, the insolence of daring to deface school property by sleeping on top of it must be too much to bear."
	show shizu basic_frown at right
	"And indeed, she stares at Rin, frozen in place apart from the slight but noticeable trembling of her shoulders, from suppressed rage I'm sure."
	"Instead of blowing up, Shizune just takes a few deep breaths, adjusts her glasses and slams the door shut, turning to sign furiously at Misha."
#	play sound "sfx/doorslam.ogg"
	show shizu cross_angry at right
	"Maybe she did blow up but I can't understand it."
	show shizu behind_frown at right
	"She shoots a very loaded stare at me too, as if it was somehow my fault that Rin is sleeping on one of the tables."
	"I hope she's not getting any funny ideas about the reason of my tardiness."
	rin "Hello."
	"Rin's voice comes from the other side of the door and it takes a few eyeblinks to realize she might have trouble opening it."
#	play sound "sfx/dooropen.ogg"
	"I open the door to find Rin directly behind it, looking at us with a half-interested, half-sleepy face."
	show shizu basic_frown
	show rin relaxed_sleepy at right
	rin "Hello."
	shi "..."
	show misha cross_frown at twoleft
	mi "Miss Tezuka, what do you think you were doing? You absolutely are not permitted to use school property for such... err, disgraceful? activity!"
	show rin negative_confused at right
	rin "It sure is suddenly very crowded in here. I didn't know I was this popular."
	"It's hard to say whether she's happy or unhappy about this turn of events."
	"At any rate she ignores Shizune/Misha's scolding so they have no choice but to drop the issue."
	show shizu behind_frown
	"Shizune taps Misha's shoulder, points at Rin and makes some quick signs."
	shi "..."
	show misha sign_smile at twoleft
	mi "Popularity aside, please don't do that any more."
	show shizu basic_angry
	shi "..."
	show misha hips_grin at twoleft
	mi "Anyway, how is your project going? Will it be done for the festival?"
	show rin basic_awayabsent at right
	"Rin looks at them blankly, apparently at ease under the pressure Shizune's cold stare is putting on her."
	rin "I keep wondering about that myself too."
	show shizu behind_frustrated
	shi "..."
	mi "And...?"
	show rin relaxed_boredom at right
	rin "Will think about it harder."
	"As Misha signs her reply to Shizune her face turns into an unsatisfied frown."
	show shizu basic_frown
	shi "..."
	show misha hips_frown at twoleft
	mi "Miss Tezuka, please try to take this seriously. It'll be a disaster if the wall looks like someone threw up their lunch onto it."
	show rin basic_absent at right
	"Rin nods assertively."
	rin "Will think more seriously."
	show misha cross_grin at twoleft
	"Misha actually giggles at that, but Shizune doesn't, not even after translation."
	hide shizu
	hide misha
	"She just shakes her head, takes the materials from me and takes off with Misha in tow."
	show rin basic_deadpanupset at right
	"Rin frowns thoughtfully as she looks after the retreating student council duo."
	rin "How rude."
	rin "It's true though, I must finish my project before the weekend. There will be dire consequences if I don't."
	rin "The end of the world as we know it. Like weekends usually are, but more dire."
	rin "Much more dire."
	show rin relaxed_nonchalant at right
	rin "Maybe I'll postpone my nap. To unforeseen future."
	hide rin
	play music "bgm/blank.ogg"
	"I am about to ask what project she has and what are these apocalyptic consequences, but she walks back into the art classroom."
	rin "Since you have nothing to do, would you give me a hand?"
	scene bg school_classroomart
	show rin basic_absent
	rin "This paint can doesn't fit into my bag but I need it."
	"She kicks lightly at a huge can of paint that's lying on the floor next to the table she was sitting and sleeping on."
	"It lets out a dull clang."
	"Being the gentleman I am, I naturally pick it up."
	"Heavy."
	hi "Yeah, sure. Where do you need to take it?"
	show rin basic_awayabsent
	rin "Away."
	hide rin
	"And with that, she takes off to the hallway, me and the paint can following since there's little choice for either of us."
	scene bg school_hallway3
	"The hallway is quiet and empty now with Shizune and Misha gone, so we too leave towards the stairwell at the other end."
	scene bg school_staircase2
	"Every ten or fifteen or twenty steps I have to change the can from one hand to another because the thin handle cuts into my palm. At least it keeps my arms from tiring too fast."
	"Rin strolls on beside me with an uneven pace that I have trouble matching, or maybe I am walking weird because of the extra weight."
	"It seems one of us is constantly walking too slow or too fast, and I can't figure out which."
	scene bg school_lobby_right
	"Two flights of stairs below, trouble appears in the form of the head nurse and his fox-like grin."
	show nurse grin at center
	play music "bgm/Ah_Eh_I_Oh_You.ogg"
	nk "Ah, Mr. Nakai, what a happy coincidence! Tezuka too, of course."
	scene bg school_lobby
	show nurse grin at twoleft
	show rin basic_awayabsent at tworight
	"He nods courteously to Rin who does not acknowledge him back, then turns to me because obviously it's me who he had some business with."
	show nurse concern at twoleft
	nk "There is something I forgot to mention on Monday."
	"I nod and wait impassively because I can't even begin to guess what he forgot. The feeling of the handle delving deeper into my skin doesn't make me feel enthusiastic about this interruption, either."
	nk "It's about your medications. Since you haven't been that long on your current medications there might be some unexpected side effects, which might require adjusting dosages or even changing to another kind of medication."
	show nurse neutral at twoleft
	nk "So we will do a few tests regularly, but what I'd want is for you to keep an eye on everything in your condition that feels off, if you get what I mean."
	nk "Nausea, headache, anything. And come see me if something happens."
	show rin basic_absent at tworight
	hi "All right."
	show nurse fabulous at twoleft
	show rin basic_awayabsent at tworight
	nk "So how are you? Everything fine?"
	"I give up and drop the can to the floor before answering him. Apparently this takes longer than my biceps can handle."
	"I'm about to say something generic as an answer, but then I realize how often I've done that lately."
	"Other people have asked me that too. Teachers and students here. My parents, visitors, nurses, doctors at the hospital."
	"Everyone seems to be concerned about that. It's natural for a hospital, not so much for a school. Except this school."
	"This is a small school, and both the student base and the faculty seem to be very tightly knit."
	"At least that's the feeling I'm getting."
	"And this is not the kind of school that gets transfer students too often."
	show rin basic_absent at tworight
	"The thought sends shivers up my spine, but I give a generic answer, anyway."
	"..."
	show nurse grin at twoleft
	show rin basic_awayabsent at tworight
	nk "That's great. Also, one other thing."
	show nurse fabulous at twoleft
	nk "My sources tell me that you've been at neither the school track nor even the pool, so I'd like to know if you have taken up exercising as I asked."
	"Of course I haven't, but his way of inquiring gives me the feeling that I should've been running my ass off on the track since the very first day."
	show rin basic_absent at tworight
	hi "You have people spying on me?"
	show nurse grin at twoleft
	show rin basic_awayabsent at tworight
	nk "Not as such. I just happen to know a few people. But that's not the issue here, so don't try to slip out of it."
	show rin basic_absent at tworight
	hi "Well, I was actually just doing some improvised weight lifting, as an exercise."
	"I pick up and lift the can up and down a few times like some sad imitation of a bodybuilder, even though it's weighing down on my arms painfully."
	show nurse neutral at twoleft
	show rin basic_awayabsent at tworight
	"The stupid grin disappears from his face for a second, then comes back like it was never gone."
	show nurse grin at twoleft
	nk "Tezuka, would you give us a second?"
	play music "bgm/blank.ogg"
	hide rin
	scene bg school_lobby_right
	show nurse neutral_close
	"The nurse grabs me by the shoulder without waiting for Rin's permission which he didn't need in the first place and drags me aside."
	show nurse concern_close
	nk "When I told you to exercise I wasn't joking."
	nk "I understand that you are still on your first week and all, but please don't ignore the importance of this."
	nk "The reason I'm coming down this hard on you is that habits are not easy to form."
	nk "The more you slip and postpone, the harder it'll be. It's the same with everything, like dieting."
label en_choiceA17:
	nk "Can you promise me to be more serious about this from now on?"
	menu:
		"Yes.":
			jump en_A17a
		"Maybe.":
			jump en_A17b
label en_A17a:
	hi "Yeah, I promise. Definitely."
	jump en_A17c
label en_A17b:
	hi "Maybe, no... I mean..."
	"He gives me a nasty sort of look when I say that, making me try to take back the word."
	hi "I mean, I don't know... I'm still trying to get used to the school."
	hi "I'll promise to try though."
	nk "You're not being very convincing there, Hisao. Tip number one: medical professionals are not amused if you take their advice lightly."
	"What's up with him? As if a day or two would make that much of a difference."
	"I didn't do anything at the hospital either."
	hi "Yeah, okay. Sorry."
	jump en_A17c
label en_A17c:
	"He studies me for a moment and then shrugs, smiling again."
	play music "bgm/Ah_Eh_I_Oh_You.ogg"
	show nurse neutral_close
	nk "Okay. That's more like it."
	nk "If you go to the school track tomorrow morning, you'll meet my 'spy,' who probably has no qualms offering consultation to you if you want to jog a bit."
	hi "Consultation?"
	show nurse fabulous_close
	nk "See you around."
	play music "bgm/blank.ogg"
	hide nurse
	scene bg school_lobby_left
	show rin basic_awayabsent
	"He leaves with a wave of his hand and no answer, and I walk to Rin who has been waiting, idly leaning against the hallway wall and staring at the pale lighting fixtures in the ceiling."
	"Even when I approach, she doesn't move her eyes off them."
	rin "Are you getting medications for your heart thingy?"
	hi "Were you listening?"
	"It comes out more accusatory than I intended, accidentally lashing out on her."
	"But even so, I don't really want to start talking about it. I just met her, I don't know her. It's not her business."
	"The nurse seems to be happily ignorant about confidentiality too, talking about that kind of thing in public."
	"But it's not Rin's fault, is it?"
	"I look up at her, suddenly feeling a bit guilty, but Rin is just staring past my shoulder quizzically, her head tilted like a bird's."
	"Sigh."
	"I don't know why this is so hard for me. It feels like there is some inexplicable lock that prevents me from being more upfront about this."
	hi "...yeah. They're for my heart."
	show rin basic_absent at center
	rin "Will they make you better?"
	hi "...no, not really."
	hi "They just make me a little less worse."
	"Rin keeps looking at me for a while longer, and she neither says anything further, nor displays any kind of emotion I could discern."
	"I'm thankful that she doesn't. I think I'm still not quite used to all this."
	"At the hospital it was easy, but I still haven't sorted my feelings about having to live a 'normal' life with this disability."
label en_A18:
	play music "bgm/Air_Guitar.ogg"
	scene bg school_courtyard
	"We leave the main building, and Rin leads us onwards towards the dorm."
	scene bg school_dormext_start
	"We stop at the small patch of greenery in front of the dorm building."
	"The dorm is built on a slightly elevated ground, with a wall and a few trees that everyone has to circle around every time they come or go. It's probably the only inconvenient design in the school."
	"The entire wall, made of the same kind of bricks as the building itself, has been covered with some sort of a painting."
	"Most of it is still mere sketches, quick lines drawn with black and white against the gray plastering that covers almost the entire length of the wall, but some places look a bit more finished."
	"There are human faces and legs and hands, I can't quite say what the painting as a whole might portray."
	"Stacks of what seem to be paint cans are arranged in piles on the ground, beside the wall."
	show rin basic_awayabsent at tworight
	rin "See, the left side is hardly off the ground yet."
	show rin basic_deadpannormal at tworight
	rin "It's because I couldn't get in the mood yesterday so I gave up and went to meditate instead. Then it was suddenly morning."
	show rin negative_spaciness at tworight
	rin "I have to work on it, but the guys from art class are helping with the negative spaces and base surfaces whenever, which is a problem."
	rin "It's easier to paint big areas if there are a lot of people, with hands."
	show rin basic_deadpan at tworight
	rin "The reach is better, and it's faster too."
	"She goes on a tangent of a tangent, waving a little with her arm, or whatever of it there actually is, to demonstrate even though I got the point already."
	"The white cotton of her sleeve flaps around, and it makes me think it could look sadder than it does."
	"But it makes me feel out of place, like almost every tangible reminder of the student base's... special properties has in the past few days."
	"This girl doesn't notice my dreary feelings of course, or the fact that she lost me a while ago already... and just keeps on blabbering."
	rin "...so that's why I'm trying to figure out if there is something I need to figure out and then figure that out before it's too late and all hope is lost."
	hi "Why would the hope be lost?"
	show rin basic_awayabsent at tworight
	rin "Because paint has to be painted and then it has to dry and then it has to be painted over with another kind of paint."
	show rin basic_absent at tworight
	rin "It takes time."
	"She finally stops, apparently thinking she made some kind of a statement that makes sense."
	"I think it's best to start from the top."
	hi "So, this is your project? You did... this?"
	show rin basic_deadpan at tworight
	rin "Yes. Yes."
	hi "All of it?"
	rin "Yes."
	hi "Nice. But..."
	"I stumble with my words, suddenly feeling like I've walked straight into the mine field of political incorrectness."
	show rin basic_deadpanamused at tworight
	rin "It's ok, you can say it. I probably won't get mad."
	"I blush really hard. I don't really know what would be the right thing to say, if any. It feels that I'm way more sensitive than Rin is, though."
	"This is really awkward."
	show rin basic_deadpansurprised at tworight
	rin "Don't you want to ask?"
	hi "...How do you paint without hands?"
	show rin basic_amused at tworight
	rin "See, I'm an easy person to talk to, right? With my feet."
	hi "I almost guessed that already, but isn't that hard to do?"
	show rin basic_delight at tworight
	rin "You're good at guessing. Anyway, I don't think it is. But maybe I'm used to it by now."
	"I can't get my mind around the fact that she could be an artist, but seeing how adept she was using her feet to eat I figure painting might not be a problem either."
	"Neither of us has anything more to add to the subject."
	show rin basic_awayabsent at tworight
	rin "The afternoon light works pretty well. I was afraid it would look too flat but it's not like that after all."
	show rin basic_absent at tworight
	rin "I think it's actually pretty interesting. I wanted to see what it looks like in dim light. Do you think it's flat?"
	hi "Eeeh well, paintings tend to be flat."
	show rin basic_deadpan at tworight
	rin "Not like that flat. You know, flat. Like some people are, no substance, no meat where there should be some."
	rin "I know a few girls who--"
	hi "Okay I get it. But I couldn't really tell, I'm not that good with art. I can't name many artists or artistic terms."
	hi "So I don't really have anything to say."
	show rin relaxed_nonchalant at tworight
	"Rin shrugs her shoulders at that, saying 'suit yourself' without saying it and looks up at the sky as if trying to look for something up there."
	rin "I didn't think I'd get any actual work done but if you give me a hand with the paints I could do a little before it's too dark."
	show rin basic_awayabsent at tworight
	rin "I wanted to get a halogen lamp like the ones they have at the sports track but there aren't any."
	"Rin sure is quick to recruit my help, as was Shizune. It really makes me feel that the festival is such a big project that every pair of hands is needed."
	hi "Why not? I'm not really sure if I can be of any help, though."
	show rin basic_absent at tworight
	rin "It's just mixing some paints, you can do that. Probably. Do you have motor control problems, like you know, those people who have some?"
	show rin basic_deadpan at tworight
	rin "Cerebral palsy, maybe?"
	hi "Not that I know of."
	show rin basic_deadpanamused at tworight
	rin "I get it. Heart thingy has nothing to do with that."
	"She gives me a sly look for no reason."
	hi "No, it doesn't."
	show rin basic_amused at tworight
	rin "Let's do it then."
	hide rin
	play music "bgm/blank.ogg"
	"So she sits on an empty wooden box and very naturally picks up a wide brush between the toes of her bare right foot."
	"I open a few of the cans and pour some of the contents into shallow bowls for mixing."
	"The thick paints flow lazily from the can to the bowl, like syrup."
	"I mix them, creating funny, hypnotic looking swirl patterns that melt quickly into each other to form a new monotone hue."
	"Rin sets to work, every now and then asking me for a hand with something or the other."
	"..."
	"Finding different brushes is easy enough, but mixing the paints to be the exact tone this girl is apparently seeing in her head is a frustrating ordeal."
	"She wants precision down to the last milliliter before she is satisfied, but her instructions are obscure at best."
	play music "bgm/Everyday_Fantasy.ogg"
	scene bg mural_start
	show rin basic_deadpan_close at tworight
	rin "Add half a splash of green."
	show rin negative_spaciness_close at tworight
	"I crouch down to pick up the can of bright green."
	show rin basic_deadpan_close at tworight
	rin "The other green. This green."
	show rin negative_spaciness_close at tworight
	"I carefully pour some of the other green paint into the mixing bowl."
	show rin basic_deadpan_close at tworight
	rin "No, that's almost a whole splash. More white."
	rin "Is green a good color to add?"
	hi "No idea. You're the artist here."
	show rin basic_deadpanamused_close at tworight
	"A hint of smile appears in the corners of her mouth."
	rin "Do you lack an opinion?"
	hi "No, it's just that I have no idea."
	show rin basic_deadpandelight_close at tworight
	rin "It's OK, because I just got an idea. Add more white."
	"With this exclamation I pour a minuscule amount of white into the bowl and mix it. It looks slightly... whiter."
	show rin basic_deadpanupset_close at tworight
	rin "That's not good. It has to be like... like the color when you wake up and you 'know' that you saw the meaning of life in your dream but can't remember it."
	rin "Maybe it's yellow..."
	show rin negative_spaciness_close at tworight
	"..."
	"Despite the impossibility of mixing a color like the change of seasons or any other nonsense that's being imposed on me, I find myself enjoying it more than I thought I would."
	stop music fadeout 7.0
	scene bg school_dormext_start_ss
	"Seeing a painting being born on the plastered wall feels like magic."
	"I spend the moments I have between mixing paints crouching down on the paving and just looking at her work."
	"It feels slightly intrusive at first, like breaking some imaginary intimacy, but Rin doesn't seem to mind the least bit. Maybe it's just in my head."
	"Her entire presence emits a completely different air as she patiently works the details, adding layers of paint on top of other layers of paint, steadily moving her foot across the wall to add new shapes."
	"When I manage to produce a passable mixture of paint, the rare smile on her face is oddly rewarding."
	"Apart from the few words when discussing paint mixes, neither of us says a word for the longest time."
	"And even those short discussions soon evolve into a shorthand, both of us developing and using weird impromptu code words for various paints and hues."
	"As if there was some need to conserve words and breath and sound."
	scene bg school_dormext_half_ni
	"We stay there late into the evening until it becomes too dark to paint properly."
	scene black
label en_A19:
window hide None
scene black
with dissolve
play sound sfx_alarmclock
stop ambient
show bg school_dormhisao
with openeye
play music music_dreamy fadein 2.0
window show
"The sound of an alarm pulls me out of a fitful slumber and into the unpleasant state of wakefulness."
"I linger under the blanket for a few minutes, gathering energy to rise up while making excuses as for why I already haven't."
"Honestly, I wouldn't mind staying here for all day. School is surprisingly exhausting after a long pause, and the culture shock still has not faded, I think."
"Still, despite getting an impression that skipping class is easy here, I don't think they are going to let me get away that easily."
"And the nurse is bound to keep breathing down my neck with the talk of exercising as well."
"So eventually I do rise up, swallow the morning medications and put on my old soccer clothing."
"Thanks to my condition, I was exempted from taking part in gym classes at Yamaku, so I didn't get issued with a gym outfit."
"I'd order some to cover such a contingency, but wearing my old soccer clothes is kind of nostalgic."
"I can't use them for that any more, so maybe they can get a new life this way. A bit like me."
label en_A19a:
"After all, if I'm going to start taking care of myself, I can't afford to slack around. I'll start from the basics."
"Basics which include keeping the rest of my body in shape along with what little I can do to strengthen my heart."
"Maybe then I can go back to something approaching a normal life; or at least something where I'm less likely to fall over dead at any minute."
stop music fadeout 2.0
label en_A19b:
"Seems a bit stupid to me, really."
"But I suppose this way at least I can tell the nurse honestly that I'm doing something about my health."
"Not that I was ever much of a runner to begin with."
"Can't hurt to try, I guess."
stop music fadeout 2.0
label en_A19c:
show bg school_track
with locationskip
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_emijogging fadein 0.1
"I'm surprised to discover that I'm not the only one present at the track."
"Not just that, but it's a face I've seen before."
"The prosthetic-legged girl who bowled me over in the hallway yesterday is running on the track lithely, like a half-mechanical gazelle."
"What was her name again? It was a short one, but I can't remember."
"She seems to be running laps at a somewhat easy lope, her prosthetic legs clacking rhythmically on the hard track surface."
"I wonder what reason she has for running this early in the morning. Maybe it's something akin to mine, and the nurse is oppressing the poor girl to jog just like he is oppressing me."
"I certainly wouldn't be here if it weren't for my health, and his prompting me to do so."
"And even with things being like they are, it's only because I wanted to get it out of the way early."
"The fact that I would be less likely to encounter someone who would witness my pitiful attempts to get in shape was merely a happy accident."
"I'd leave, but it seems that my former assailant noticed me on her last lap."
"She waves at me cheerfully and jogs over."
show emi basic_grin_gym at Slide(0.7,0.5,0.5,0.5,1.0,_ease_in_time_warp)
with charaenter
stop ambient
emi_ "Good morning! Your name is Hisao, right?"
play music music_emi fadein 2.0
"She grins, seemingly pleased that she'd remembered my name."
show emi basic_closedgrin_gym at center
with charachange
emi_ "You may not remember me."
show emi basic_grin_gym
with charachange
emi_ "Emi? I knocked you over in the hall yesterday."
label en_A19i:
show emi excited_circle_gym
with charachange
emi "“Miss Ibarazaki?”"
"She imitates Misha “imitating” Shizune, failing to get the same kind of subdued lilt into her high-pitched voice."
label en_A19j:
hi "How could I forget such a er, blunt introduction?"
show emi sad_shy_gym
with charachange
"Emi has the decency to look vaguely apologetic for a moment before giggling."
show emi sad_grin_gym
with charachange
emi "Yeah, sorry about that. Again."
hi "Hmm, well, so long as you don't make a habit of it, I suppose I'll be fine."
show emi basic_happy_gym
with charachange
emi "Great!"
"I'm not sure she realized I was joking."
hi "So the “spy-consultant” the nurse was talking about… is that actually you?"
show emi basic_closedgrin_gym
with charachange
emi "That's right!"
hi "Oh."
hi "I was expecting someone from the nursing staff, to be honest."
show emi basic_confused_gym
with charachange
emi "What, are you saying I don't look like I could be a spy?"
hi "No, this is more like a relief. I was afraid he would have someone to watch my every move."
hi "Unless you are here to do exactly that."
show emi excited_laugh_gym
with charachange
emi "No, I'm here for my own reasons, the nurse just asked me if I had seen “a messy-haired transfer student who looks like he's kinda lost” around the track."
hi "So why are you down here?"
"Emi strikes a dramatic pose."
show emi basic_happy_gym
with charachange
emi "Training!"
hi "For what?"
show emi basic_closedhappy_gym
with charachange
emi "Track!"
hi "Ah, I see. You're on the track team, then?"
"Emi nods enthusiastically."
show emi excited_proud_gym
with charachange
emi "Yep! I'm one of the better runners, too!"
"And modest about it, too."
show emi basic_grin_gym
with charachange
emi "Hey, you should join up!"
emi "It's good exercise, you know."
"I think that much activity is probably out of the question for me."
hi "Nah, I'm not even sure that I really like running all that much."
hi "Plus I'm just not into organized sports, you know?"
"It's true. I never even really got that much into soccer."
"I mean I'd run around with my friends and all, but that was really the only reason I ever played."
"It wasn't for the glory to be found on the field, that's for sure."
"Emi seems to understand my meaning."
show emi basic_confused_gym
with charachange
emi "I see, I see. Not that into the whole organization thing."
show emi excited_proud_gym
with charachange
emi "But now that you're here, I guess we're going to run together, huh?"
hi "What? Er, sure, I guess."
"Emi seems pleased."
show emi excited_joy_gym
with charachange
emi "Are you going to warm up?"
hi "Real men don't warm up."
show emi basic_annoyed_gym
with charachange
emi "Oh no, you always should warm up! Bad Hisao!"
show emi excited_proud_gym_close
with characlose
"She scolds me enthusiastically, but then smiles and leans closer."
emi "I hate warming up too."
show emi excited_laugh_gym_close
with charachange
"She laughs suddenly."
emi "Heck, and I don't even have to stretch my legs!"
play sound sfx_gymbounce
show emi gymbounce
with charadistant
"As if to confirm her statement she bounces up and down a couple of times, giving a passing impression of standing on a pair of springs. Her legblades seem to be quite elastic."
emi "Let's go!"
stop music fadeout 1.0
play ambient sfx_emijogging fadein 0.3
scene bg school_track_running
with locationchange
"So we both take off around the track, and I can immediately see that she wasn't lying about being good at running."
"Emi moves fluidly, throwing herself into the run with a sort of wild abandon."
"I find myself concentrating more on running properly."
label en_A19d:
"Hands spread, right?"
"And something about hitting on the balls of your feet, rather than the heels…"
"I try to match my stride to Emi's, but it's pretty difficult."
"Apparently I'm not very good at it."
"Maybe Emi could help me with that sometime."
label en_A19e:
"Frankly, I don't remember if there's any particular form for running, but I can't help but feel like I'm doing it wrong, somehow."
"I feel awkward in comparison to Emi, who never seems to break stride."
"…"
"I don't think I want to do this any more."
label en_A19f:
"I'm really not feeling up to more than a couple of laps today, and slow to a walk pretty quickly."
scene bg school_track_on
with Dissolve(4.0)
"Emi keeps running, and doesn't seem to notice I've stopped until she passes me a second time."
stop ambient
"She quickly skids to a halt, breathing steadily in contrast to my own somewhat gasping demeanor."
play music music_emi fadein 2.0
show emi basic_confused_gym at center
with charamoveinleft
emi "Finished already?"
"I hang my head ruefully."
hi "Heh, yeah."
hi "I'm not in very good shape right now."
show emi basic_grin_gym
with charachange
"Emi nods, and then grins at me again."
"She seems to do a lot of smiling."
emi "Well, the important thing is you started, right?"
show emi excited_amused_gym
with charachange
emi "Next time, you just have to try to hold out longer, and then longer, and longer, and eventually you'll be great!"
hi "I'll keep that in mind."
hi "But I think right now I'm going to go get ready for class."
hi "Shouldn't you?"
"Emi shrugs unconcernedly."
show emi basic_grin_gym
with charachange
emi "Nah, I've got plenty of time."
"I notice that she's not wearing a watch."
hi "Are you sure?"
"Another careless shrug."
emi "Not really… but I've got to finish my routine!"
show emi basic_closedgrin_gym
with charachange
emi "See you later, Hisao!"
hi "Er, yeah. See ya."
stop music fadeout 5.0
play ambient sfx_emisprinting
hide emi
with easeoutleft
stop ambient fadeout 2.0
label en_A19g:
"I'm not sure whether this morning's experiment was a success or a failure, but I'll admit that I do feel slightly good about getting out there this morning."
"And like Emi said, I just need to keep at it in order to get better, right?"
"Practice makes perfect, or something like that."
"It's nice at least to feel like I've taken some semblance of control over my own health."
"I'll have to try to keep this up."
scene black
with locationskip_in
label en_A19h:
"Apart from feeling more tired than before, I don't think I accomplished anything today."
"I'm so out of shape it's embarrassing."
"The whole thing might have been a waste of time. I'll find some other way."
scene black
with locationskip_in
label en_A20:
scene bg school_dormext_half
with locationskip_out
"I head back to the dorms to wash and change into my uniform, trying to resist the urge to take a really long and hot shower."
"I'm tired from all the running, so I just want to unwind, but I don't want to break my slowly building routine of getting to school before the morning rush."
scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip
"After taking a long shower anyway, I dry myself off and get out of the stall to put on my clothes."
show kenji silhouette_naked at center  behind steam
with charaenter
"Out of nowhere, a shadow appears within the mist, looming and radiating malicious intent. It bursts through the fog."
play music music_kenji fadein 0.3
hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange
ke "Sup?"
hi "What are you doing here? What the hell, you scared me! What's your problem?!"
show kenji tsun_naked
with charachange
ke "I should be asking you that. I've been looking for you all over the place, man."
hi "What do you mean “all over the place”?"
"I want to ask if he's been looking for me like that, stark naked, but hold my tongue back."
"I finally realize I'm still naked too and quickly hold up my shirt in front of me, but Kenji doesn't seem to notice a thing."
"His glasses are fogged up. But then, why doesn't he wipe them off? Is his vision so bad it's like he's perpetually seeing through fog?"
ke "You know, your room, and… Yeah, that's it. Hey, I mean, I still had to get up, though. Whatever. It's not important. Can I borrow some money?"
show kenji neutral_naked
with charachange
"He puts on an innocent face and looks away, trying very hard to look very casual. It doesn't work; he's as transparent as his windowpane-sized glasses."
"Talking neutrally like this, wearing nothing, feels awkward."
"Actually, somehow it's even more awkward to be naked in front of someone when they can't see me being naked. To say nothing of the fact that he's naked as well."
"I try to brush the feeling off, with little success."
hi "Money? Sure."
show kenji happy_naked
hide newsteam
with charachange
ke "Awesome."
hi "Wait, why do you need it?"
show kenji tsun_naked
with charachange
ke "Ehhhh…"
show kenji neutral_naked
with charachange
ke "Can't you just give it to me because I had the good will not to run through your pockets while you were in the shower? I could have, but I exercised restraint. And in the end, isn't it the thought that counts? Come on, be a pal."
"This makes no sense. If it's the thought that counts, I should withhold payment, since his thoughts were so clearly impure and his intentions are probably even more sinister since he can't tell me what they are. I say as much to him."
show kenji tsun_naked
with charachange
ke "I'm offended man, but if that is your game, then fine, I guess I have no choice. I want to order a pizza, and I already have most of the cost of the pizza. I need your help for the rest."
hi "I get some of that pizza too, right?"
ke "No."
hi "Are you serious?"
show kenji neutral_naked
with charachange
ke "Yeah. I would give you some, but you have class, you don't have time to eat a pizza."
hi "What about you?!"
ke "I'm not going to class, I have to wait for the pizza and pay the guy. And then eat it. It's not easy. You have to obtain the pizza stealthily. If you don't, everyone will see you. And the pizza. And they will ask for a slice."
show kenji tsun_naked
with charachange
ke "It's a hard world out there. Everyone wants a piece. Then you're left pizzaless in an unforgiving world. It's happened before, that's how I know."
ke "Every day, I plan my vengeance, so that when the people who wronged me order a pizza, I will be there. Ever vigilant!"
"Kenji strikes a dramatic pose, completely without irony."
show kenji neutral_naked
with charachange
ke "But yeah, I only need like 400 yen. Please! You're my only hope! I can't go outside and buy my own pizza, it's too far!"
ke "I try not to go out unless it's absolutely necessary. Let me tell you what happened the last time I went out without carefully planning it out in advance."
ke "I was outside. I can't remember what I was doing. Something. Standing? Maybe wondering how I got there."
show kenji tsun_naked
with charachange
ke "And then, out of nowhere, it happened."
ke "Like a flash of lightning, splitting the sky, like how you split a sandwich into two equal pieces to make it more manageable to hold and eat, a bird crapped on my head."
ke "It was the second most shocking moment of my life."
hi "What was the first?"
"He ignores me and keeps going. I want to grab him and shake him. Is he just trying to keep momentum? I'll go with that, even if it's more likely he just didn't hear me."
ke "It was like in the openings to some kind of anime show, you know how there is always a part where the main dude is fighting his rival, and they fly at each other and clash swords and there's like, big dramatic colored auras and zoom?"
show kenji neutral_naked
with charachange
ke "It was like that, but with poo."
hi "Okay."
show kenji happy_naked
with charachange
ke "So yeah, I need some money. Please? Don't leave me hanging, man. I only need like 1000 yen."
hi "I thought it was 400."
ke "Okay."
hi "What?"
ke "I'll pay you back, I swear."
hi "You better, that's what it means to borrow stuff."
show kenji neutral_naked
with charachange
ke "I don't know when I'll be able to pay you back."
hi "You have one week."
show kenji tsun_naked
with charachange
ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh……"
"Kenji winces and makes a noise like a dying cow, a particularly disturbing fact given that his baton is conducting freely."
ke "You're not supposed to be so tight assed about money between brothers in arms, man. Men have it bad enough as it is. Did you know that male porn stars only make about half of what female porn stars make?"
hi "That doesn't mean anything unless you're a porn star."
ke "So maybe I am a porn star, on the side, struggling to make ends meet as I fight the feminist agenda, and you can't even spot me your crumbs, you bastard. Nobody understands. Nobody."
"Wouldn't feminists be against pornography in the first place?"
hi "This feminist agenda stuff again?"
ke "This stuff is important. I can see that you don't give a shit, but this is serious, here. Feminists… are a dangerous enemy, make no mistake. You take them lightly, and you'll wake up in the morning with a knife in your back, bam! Out of nowhere!"
hi "How do you wake up in the morning if someone stabbed you in your sleep?"
show kenji happy_naked
with charachange
ke "Women are terrible at stabbing things."
hi "I thought you just said don't take them lightly."
show kenji neutral_naked
with charachange
ke "Well, I mean don't take them lightly for the big things. Individually they're not a threat, but if there was some kind of war, like a big war, with men on one side, and the feminist forces on the other side, it would be pretty ugly."
show kenji tsun_naked
with charachange
ke "And that day will come, when the feminists come out of their central top secret worldwide feminist headquarters, and say “It's on now, motherfuckers!”"
hi "You're being ridiculous, there's no big worldwide feminist headquarters building, where would they even hide that? I mean, it'd have to be massive, you couldn't hide that on Earth, someone would notice a big fortress with women only in it."
show kenji happy_naked
with charachange
ke "Who said it was on Earth?"
"I turn away from Kenji and start practicing frowning faces in a mirror so that I can figure out what kind of frown will best express my emotions. He can't see me from this distance anyway."
"Which, unfortunately, means that he just keeps on ranting without any regard to sense or sensibility."
show kenji tsun_naked
with charachange
ke "Yeah, there is a war going on. A war not many know about, but it's a great one that will one day boil over, and encompass all of the known world. Then, we will have to pick sides. We will have to make a stand. In fact, it's happening right now."
ke "Imagine it, the bloody battlefield. A vicious conflict without end."
ke "I almost gave up, when I thought this cause was silly… When I grew tired of the bleakness of our fight… When I mistook the time the power went out for a feminist raid and thought the end was near…"
ke "But then I realized that if I gave up, it would all be over, and I was like, “whoa” and knew I had to get serious. Because I am the last sane man in an insane world. It's about duty."
hi "Must be a pretty crappy movement if it all hinges on one naked guy, ranting in a bathroom at another naked guy."
show kenji neutral_naked
with charachange
ke "So can I have the money?"
"He's blocking the way out, it's getting cold because I'm still naked, and I want to go to class, so I agree to spot him the money."
show kenji happy_naked
with charachange
ke "Awesome. Thanks, dude. We should go bowling later on."
hi "Bowling?"
ke "Yeah, it's the ultimate sport. There are almost no women bowlers either, making it also the manliest sport."
ke "Should I wear my pink bowling shirt with matching shoes or the pastel green with flower accents?"
hi "There are bowling clothes?"
show kenji neutral_naked
with charachange
ke "Maybe."
hi "Anyway, you had better pay me back."
ke "I can pay you back in stuff, right?"
"I don't have the time to ask him to elaborate on what that means."
hi "I don't know. I have to get to class, you're kind of in the way."
show kenji tsun_naked
with charachange
ke "Oh. Sorry. Yeah, I don't want to hold you up, and I have some stuff to do myself. The time has come."
hi "The time for what?"
show kenji happy_naked
with charachange
ke "I just like saying that."
ke "Okay, now the time has really come."
hi "For what?"
show kenji tsun_naked
with charachange
ke "I have to use the bathroom. Get out of it."
hi "I was just going to! And what does that mean? It's a big bathroom."
ke "So? I have to be alone or I can't go. The pressure…"
hi "Okay. What if someone else comes in?"
ke "…"
ke "I'll think of something."
"I give him my practiced frown and it looks kind of silly reflected in his glasses. He either doesn't notice or doesn't see, anyway, so I get dressed and run back to my room, feeling as though an eternity has passed since I woke up."
stop music fadeout 2.0
scene bg school_dormhisao
with locationskip
"That is time I will never get back. I'll get him for this somehow."
"But right now, I have to get to class."
label en_A21:
scene bg school_scienceroom
with locationskip
play music music_normal fadein 2.0
"I'm the first person in class today, although I think I'm a little too early. Then again, sitting alone here for twenty minutes sure beats having to suffer that time with Kenji."
"The combination of fatigue, frustration and boredom starts making me feel very tired."
"I black out for a second, waking up when my head hits the surface of my desk. Rubbing my forehead, I realize this is as good a reason as any to stay up for now and stop coming to class so early later."
"Eventually, I hear a tapping noise outside in the hallway, and Lilly's tall figure appears in the doorway. She's not in this class, so she must have some other business. Maybe she's looking for Hanako."
"Lilly stops at the door, looking hesitant as if she was a vampire who can't come in unless invited. I consider doing so because she looks rather lonesome standing there."
"She steps in on her own accord though, after straightening her skirt and shirt collar as if it was of importance to look prim when entering our classroom."
show lilly cane_concerned at left
with charamoveinleft
li "Excuse me."
"She calls into the quiet classroom with a probing, delicate voice. I realize the silence might unnerve her because of her blindness so I break it."
hi "Good morning, Lilly."
show lilly cane_surprised at left
with charachange
show lilly cane_surprised at center
show bg school_scienceroom at bgright
with charamove
li "Hisao? Good morning. I didn't hear you come in."
"I wonder if she thinks it's suspicious I didn't say anything to her before. It's likely. If I were to tell too big a lie now, it would sink me."
hi "Well, I was already here, just asleep until now."
show lilly cane_listen
with charachange
li "Oh. Have you seen Hanako today, by any chance?"
hi "No, she seems to come in only just before the bells ring… or after that. Do you want me to tell her something for you?"
show lilly cane_weaksmile
with charachange
li "No, it's fine. It's strange, but I think we're the only two people in the school right now. I didn't hear anyone else on my way here."
hi "I shouldn't have gotten up so early today, I guess."
show lilly cane_smile
with charachange
li "You're chastising yourself for doing something that other people should? Punctuality is a good thing. I think so, anyway."
show lilly cane_concerned
with charachange
li "It's a very busy morning today. The festival is coming up soon, and today is the deadline for event registration, budget reports, and any other official paperwork."
show lilly cane_weaksmile
with charachange
li "It could be that everyone is trying to complete the necessary forms at the last minute. Maybe that is why it's so quiet today."
play sound sfx_doorslam
show lilly cane_surprised
with vpunch
mi "Hi~ hi~!"
show shizu behind_blank at offscreenright
show misha hips_grin at offscreenright
with None
show lilly cane_surprised at left
show misha hips_grin at center
show shizu behind_blank at right
show bg school_scienceroom at bgleft
with charamove
hide misha
show misha hips_grin behind shizu
with None
"Misha pops into the room with Shizune as if on cue, shouting with a loudness that makes Lilly visibly flinch."
show misha hips_smile
with charachange
mi "Hi, Hicchan~!"
hi "Hi."
show shizu behind_smile
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Look, it's the class representative~! Hello~!"
show lilly cane_smile
with charachange
"Lilly smiles, probably amused by Misha's - or Shizune's - use of the word “look.”"
show lilly cane_smile
with charachange
li "Good morning."
show shizu adjust_smug
with charachange
shi "…"
show misha cross_smile
with charachange
mi "Of course, you're not the representative of this class, right, right~?"
show lilly cane_weaksmile
with charachange
li "I'm not."
"Lilly seems a little more guarded in her answers to Shizune than she was with me the other day. I guess they really don't get along at all."
"Then I realize that Lilly might actually not know Shizune is present and she's trying to detect whether or not she is, to know who she is talking to."
"For all she knows, she's talking to Misha, but knowing that she and Shizune are practically inseparable, she might expect Shizune being the one that actually “talks.”"
"Damn, how complicated. I decide to help Lilly out, for my own peace of mind more than anything else."
hi "You're here early, Shizune."
show shizu basic_angry
with charachange
shi "…"
show misha hips_frown
with charachange
mi "You were here even earlier than us!"
"Misha puffs out her cheeks angrily. Why is she getting angry? Does she feel emotions on Shizune's behalf, too?"
"It's not that weird, though, that Shizune didn't like my little comment. It's true, I was here earlier than them, so me saying something like that could definitely be misinterpreted as anything."
"Especially to Shizune, who doesn't have the benefit of hearing tone to gauge intent."
"Before I can start weighing whether or not I should apologize, Shizune has already moved on."
show shizu adjust_smug
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Class rep~! It's a good thing you're here~! We have to talk."
show shizu behind_frown
with charachange
shi "…"
show misha hips_grin
with charachange
mi "The festival is coming up in three days, right? Every other class has already handed in their projected budget reports for their events! Even the first-years! Except you~!"
show misha cross_laugh
with charachange
mi "Wahaha~!"
show lilly cane_surprised
with charachange
li "There is still time to hand it in, isn't there?"
stop music fadeout 2.0
show shizu cross_angry
with charachange
shi "…"
show misha cross_frown
with charachange
mi "Today! The deadline is today! You're certainly taking your time, aren't you? If I had it my way, I'd have had all of the necessary paperwork days ago, but someone~! had to say “the deadline, please extend it~!”"
show lilly cane_displeased
with charachange
li "Yes, that was me. Planning something on this scale is not a small task, and a week is too small a time frame to expect a whole class to work out such a complex issue completely."
show shizu adjust_angry
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Do you want to know what's harder than distributing the funds for one class' event? Handling the same matter for every class in the school and then some~! The one who does that is me!"
"Misha puts her hands on her hips and stands up straight. Wow, she is really getting into the role. Lilly doesn't look like she's very amused, though."
hi "Hey, Shizune, aren't you being a little too hard on her? There's still a whole day left."
show lilly cane_weaksmile
with charachange
li "Please, Hisao. It's all right."
"Lilly seems happy I'm taking her side, but a bit conflicted that I might not think she can take care of herself."
show lilly cane_listen
with charachange
li "If this is about the budget, then I'm disappointed you think I have forgotten about it. I understand how important it is."
show shizu behind_frustrated
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Then~! Can I have it, please?"
hi "Shizune, she might not have it on her at this exact second."
show lilly cane_displeased
with charachange
li "It's not here right now. I asked two students to take care of it for me. Students from my class."
"She emphasizes the last sentence much to my surprise. She knows about Shizune and Misha's efforts to rope me into the Student Council?"
"I guess word must've gotten around, so now she's using me as ammo against Shizune. This just gets better and better…"
show shizu cross_angry
with charachange
shi "…"
show misha hips_frown
with charachange
mi "It was your responsibility~! A budget report isn't something you should just be delegating away; as class rep, it's your job to be on top of things! This kind of disregard for proper procedure is really just terrible~!"
show lilly cane_listen
with charachange
li "They completed it, being capable of doing so, but the students have been sick recently, so they could not come to school and give it back to me. If you want, I will apologize on their behalf for getting sick."
show misha hips_grin
with charachange
mi "Okay~!"
"Although Misha misses Lilly's little jab entirely, Shizune doesn't, and she seems torn between being offended by Lilly's daring and jumping for joy at the prospect of a challenge."
show shizu behind_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Lilly, don't they live here at the school? That's a five minute walk, you know~."
mi "What could they possibly have that prevents them from taking five minutes out of their busy lives… to drop off something that will affect the enjoyment of their entire class?"
show shizu adjust_angry
with charachange
"Lilly opens her mouth to say something, but Shizune closes the gap between them and starts signing furiously, waving her hands around like an orchestra conductor."
"Misha tries her best to convey the same passion, but can't seem to lose her normal cheerful tone. The result is interesting and somewhat surreal."
shi "…"
show misha cross_frown
with charachange
mi "And what's with that attitude~? I said that it's not something you should be delegating away; are you the class representative or aren't you?"
show misha hips_frown
with charachange
mi "Tell me the names of those two students, they should have your job if you can't even handle something this simple yourself."
show lilly cane_displeased
with charachange
li "One form isn't the full extent of what I am supposed to take care of."
"Lilly's tone is growing slightly impatient, but she is doing a good job of not letting Shizune see how unsettled she is becoming. She's playing her cards close to her chest."
"Shizune, on the other hand, wraps her fingers cheerfully along the edge of her glasses, knowing Lilly can neither hear nor see how excited she is."
show shizu adjust_smug
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Of course, you do so much, class rep~! It must be so difficult being you~!"
show lilly cane_listen
with charachange
"Lilly tightens her lips at Misha's words, clearly understanding the intent behind them even though Misha delivers them without even a hint of the sarcasm which they were meant to have."
"Shizune and Lilly don't like each other, that much is clear, but this seems a little much. It seems like Lilly has had enough and is ready to push back."
play music music_tension
$ wdt_off(False)
scene black
with Dissolve(0.2)
show showdown_lilly_slice at Transform(xanchor=0.0, xpos=1.0, yalign=0.0)
show showdown_shizu_slice at Transform(xanchor=1.0, xpos=0.0, yalign=1.0)
with None
play sound sfx_draw
show showdown_lilly_slice at Transform(xalign=0.0, yalign=0.0)
with slice_in
with Pause(0.2)
play sound sfx_draw
show showdown_shizu_slice at Transform(xalign=1.0, yalign=1.0)
with slice_in
with Pause(0.2)
play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 3.0, color="#FFF")
play sound sfx_slide2
show ev showdown_large:
    pause 0 size (800,600) crop (0, 0, 2400, 1800) subpixel True
    easeout 0.2 crop (280, 100, 800, 600)
with None
window show
li "I was actually just discussing the budget report before you came by. You must be very talented to have finished all your student council duties so quickly that you can track me down to make sure I don't forget my own."
play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None
mi "Are you accusing me of slacking off? It seems like you're confusing me with yourself~!"
play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None
li "I don't think so. That would be a very difficult thing for me to do; comparing myself to you."
play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None
mi "You're right, the difference between us is like heaven and hell."
play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None
li "And it's not hard to guess which one you might represent."
$ _window = False
play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")
window show
"The air between them ripples with the heat of their enmity. Well, not really. They can't disguise it any more, though. Even Misha looks like she's beginning to understand the real nature of this conversation."
stop music fadeout 5.0
scene bg school_scienceroom
show lilly cane_listen at left
show misha perky_confused at center
show shizu basic_angry at right
with flash
shi "…"
show misha sign_confused
with charachange
mi "Hicchan~! Don't you slack off either~!"
hi "What are you talking about?"
show shizu basic_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Aren't you taking part in the festival, Hicchan? You are, aren't you? Then~! I hope you're going to do a lot more to make sure it goes smoothly than this person~!"
label en_choiceA21:
menu:
    with menueffect
    "I don't understand why Shizune is suddenly getting mad at me."
    "Don't drag me into this! I've done my part!":
        return m1
    "Hey, come on. Cut me and Lilly some slack…":
        return m2
label en_A21a:
hi "Why am I being dragged into this, again? I've done more than enough, I think."
hi "If you're angry with Lilly, that has nothing to do with me."
show lilly cane_reminisce
with charachange
li "Now, wait just a second… are you implying the president is more right in scolding me than yourself?"
"Ah damn, I think I could've worded that better."
hi "No, I don't know about that but… I mean…"
show shizu behind_frown
with charachange
shi "…"
show misha perky_confused
with charachange
mi "What are you saying, Hicchan?"
hi "It's just that I hardly think it's fair you can say that, seeing that I've helped you guys."
"The mood has changed. This is like a showdown between two gunfighters now. Well, it was like that before too, but this time Shizune's focus is on me."
"And so is Lilly's, though she keeps quiet. I'm afraid I inadvertently pissed her off."
show shizu cross_angry
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Are you saying I'm wrong?"
"What a dangerous situation."
hi "It's too early to argue with you. …Yes, I think it's unfair of you to get on my case."
show shizu behind_frustrated
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Hicchan, you want too much~! But~! You have a point. Okay, okay okay~! You're not lazy, Hicchan."
show misha hips_laugh
with charachange
mi "Hahaha~!"
"Shizune pushes her glasses up with her thumb, almost approvingly."
show shizu adjust_happy
with charachange
shi "…"
show misha perky_smile
with charachange
mi "That's good! If you're not useless, you shouldn't let anyone say you are~! But the next time I say it, it'll really be because you are disappointing me like Miss Class Rep here, so don't let this go to your head!"
show lilly cane_displeased
with charachange
"Lilly takes the jab silently, a venomous visage frozen on her face."
show misha hips_smile
with charachange
mi "Class rep~! Shicchan says: “Don't forget that report, please~!”"
li "I won't."
show lilly cane_listen
with charachange
li "Would that be all?"
show misha hips_grin
with charachange
mi "Yup~!"
li "Then, good day to you all."
"Her voice would cut the air of the classroom into half, if it was more tangible."
hide lilly
with charaexit
"Lilly leaves the room, understandably in a bad mood but still managing to be as poised and calm as usual."
show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove
hi "Shizune, you really did go a little too far today."
show misha perky_smile
with charachange
mi "It's true, Shicchan, just a little~."
"If I had been expecting Shizune to grudgingly admit I have a point there as well, I think I was expecting too much. She doesn't respond."
show shizu basic_normal2
with charachange
shi "…"
show misha cross_laugh
with charachange
mi "Hahaha~! Shicchan thinks you should mind your own business."
show misha hips_smile
with charachange
mi "Hicchan, we have a few last minute things to take care of before class~! We might be late, so~! Can you please cover for us?"
hi "Yeah."
show misha cross_grin
with charachange
mi "Perfect~! Yay~! Okay~! Thanks, Hicchan!"
hide misha
hide shizu
with charaexit
"They walk outside even though there are only ten minutes left before the bell will ring, signaling the start of class."
label en_A21b:
hi "Hey, I'm the new guy, remember?"
hi "It's not like I could've done much, even if I wanted."
show lilly cane_displeased
with charachange
li "That's right, you shouldn't expect a transfer student to jump right into it on his first week."
"Lilly taking my side feels oddly comforting so I decide to back her up too."
hi "Yeah you're being unreasonable with us both."
show shizu behind_frustrated
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Excuses, excuses. Miss Class Rep has had plenty of time to deal with her report."
mi "And we repeatedly offered you a position to help with the student council work, but you refused to commit yourself to making the festival a success."
hi "Yeah, but as I said back then, I'm not sure if…"
"I don't have time for this right now; no matter what I do, it will mean being drawn into a confrontation with Shizune, and that is what she wants."
hi "Whatever. Forget it."
label en_A21c:
"I turn my back at them."
hide shizu
hide misha
with charaexit
show lilly cane_displeased at center
show bg school_scienceroom at bgright
with charamove
hi "Lilly, class is going to be starting soon, so we can talk more later. I'll tell Hanako you were looking for her."
"I can feel Shizune freezing. Maybe this is the first time she has ever been ignored in such a blunt manner."
show lilly cane_smile
with charachange
li "Thank you, Hisao. I'll leave now, then."
"She gives me the sweetest smile I've seen all week, and turns on her heels to make her exit."
hide lilly
with charaexit
"As soon as Lilly walks out the door, I suddenly start feeling reluctant about turning to face Shizune."
"I can feel her eyes burning into my back, and can't bring myself to look at her. She must be furious. I keep expecting Misha to say something to alleviate the tension, but it really is wanting too much."
"In the end, I go back to my seat and listen to the sound of Shizune's footsteps as she marches out of the room. She doesn't return until a few minutes before class."
label en_A21d:
hide shizu
hide misha
hide lilly
with charaexit
"I turn my back at them."
"I get back to my seat and shut my ears from the finale of the argument between Lilly and Shizune."
"Eventually, Lilly leaves our classroom and Shizune and Misha seat themselves, without talking to me."
"I can feel Shizune's eyes burning into my back. She is probably angry at me, but I'm just as angry with her."
"I don't get why she had to drag me into the argument."
label en_A22:
scene bg school_scienceroom at bgleft
with shorttimeskip
play music music_daily fadein 0.5
"Hanako doesn't come to the morning class at all, leaving her seat looking empty and lonely in the back of the classroom."
"I have to tell her that Lilly was looking for her if I see her later."
"After the events of this morning, class is pretty boring in comparison. I turn the pages of my textbook lazily."
"We've been covering the same amount of pages each day, so reading ahead is more or less giving myself a preview of what tomorrow's lesson will be about."
"The clock at the front of the room sounds unbearably loud. The teacher hasn't said anything in over seven minutes, instead opting to cover the board in rows and rows of equations taken directly from the book."
"The rhythmic clashing of chalk on blackboard seems to synchronize perfectly with the ticking of the clock."
show misha cross_smile_close at offscreenleft
with None
show misha cross_smile_close at Transform(xpos=0.1, xanchor=0.5)
show bg school_scienceroom at center
with charamove
"I start to copy down the equations just to pass the time, not noticing Misha's head poking over my shoulder until she is almost on top of me."
hi "What are you doing?"
"I try to strike a balance between being quiet enough to not draw attention to myself but loud enough to draw hers."
show misha cross_grin_close
with charachange
show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove
mi "What are you doing, Hicchan~?"
"Panic shoots through me as Misha starts talking at her normal volume, and I sputter out a hasty reply, still keeping my voice down despite the fact that she just blew any hope of being discreet I may have had."
hi "I'm copying down that stuff, what are you doing? Why so loud?"
show misha perky_confused_close
with charachange
mi "Aw~, really? But it's all in the book… That's why no one else is copying it down~!"
hi "I know, why are you so loud?"
show misha hips_grin_close
with charachange
mi "Why are you so quiet, Hicchan? It's hard to hear you."
"I look around to see if anyone is noticing our conversation and it's pretty obvious that everyone has, even the teacher."
show shizu behind_smile at right
with charamoveinright
"Shizune smiles coyly and I start to wonder if Misha is doing this because she told her to."
"Is it because of what happened between her and Lilly earlier?"
"This is what I get for trying to be reasonable? For trying to take the middle path? Shizune is way too prideful, although by now I should know to expect that kind of behavior from her."
hi "Why are you doing this?"
show misha perky_confused_close
with charachange
mi "Huh?"
"Misha is totally oblivious to the awkward stare the teacher is giving both of us, while trying to balance her textbook on one finger. For a brief second it looks as if things could get ugly, but the teacher simply looks away, as if it's not worth the trouble."
"I guess this is a good thing, and I slump back in my seat in relief."
scene bg school_scienceroom at bgright
with shorttimeskip
"The rest of day passes by uneventfully, and this time I'm able to appreciate that it does."
play sound sfx_normalbell
"When the bell rings, I'm not in a hurry, so I stay for a while, reviewing what we covered in class today. I prefer to leave last anyway, so I don't have to deal with crowding in the hallways."
"I notice Shizune and Misha have also stayed behind, talking to someone from another class."
"Shizune's signing so fast that her hands make noises like swords cutting through the air."
"Misha is trying desperately to keep up, but it's clear she can barely manage to even understand her."
"I put my head down. Whatever they're discussing, it looks like serious business. Probably way over my head. Not just that, but Shizune also seems angry, although it could just be her normal severity making it appear so."
"Shizune signs to the point where her wrists crackle, and Misha struggles to spit it out in word form."
"Sometimes she trips over herself like she's dealing with tongue twisters. And then on top of that, she has to sign back anything the other girl says."
"Seems like a rough job."
"Misha looks tired, like she's about to faint."
"Luckily for her, their business is soon finished and the girls sit down on their seats again."
show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter
mi "Uwaaah! I'm so tired!"
"She's hanging her head limply on her desk, looking exhausted."
hi "Festival preparations must be tough for you."
"Indeed, the people in this school seem to be taking the festival very seriously. Whenever I see people idling around before and after classes they're always talking about their plans for it."
"It's kind of neat to see everyone being so enthusiastic about it."
"I'm probably the only one who doesn't have something to do."
show shizu basic_normal
show misha perky_confused
with charachange
"Shizune starts signing at me and Misha perks up, looking at her hands with slightly unfocused eyes."
show shizu behind_frown
with charachange
shi "…"
"She signs with harsh, heavy, dramatic strokes."
"Misha translates her signing into speech for me."
"She does it so well it's almost like Shizune is actually speaking, transmitting her thoughts directly through Misha."
show misha cross_frown
with charachange
mi "Well, we're in the Student Council, you know, so we're pretty busy."
hi "Sarcasm?"
show misha perky_confused
with charachange
mi "Huh?"
"The tone of Shizune's actions make me think she is “speaking” with disdain, but Misha interprets it normally, replacing whatever intent may have been there with her own chipper twist on things. It's still disorienting, I don't think I'll ever get used to it."
hi "Never mind."
hi "How could I forget, with you two trying to get me to join at least twice a day?"
show misha cross_laugh
with charachange
mi "Hahaha~! But, Hicchan, some could say the work is too much."
show shizu basic_normal2
with charachange
show misha perky_sad
with charachange
mi "It'd be nice if students were to show a little more support for their leadership, some appreciation to the ones who are working so hard to make it all possible."
show shizu behind_frown
with charachange
show misha perky_smile
with charachange
mi "Maybe, for example, a little help. That's asking too much, is it? Yep~! Help would be appreciated~! From students like you~!"
show shizu adjust_angry
with charachange
show misha hips_frown
with charachange
mi "If students would show their dedication and school spirit, and offer some help, well, I don't exactly need it…"
show shizu behind_smile
with charachange
show misha hips_smile
with charachange
mi "But I wouldn't necessarily refuse it… So~! it would be nice if someone would…"
stop music fadeout 2.0
show shizu adjust_blush
show misha perky_confused
with charachange
mi "Oh? Hello~!"
show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright
play music music_pearly fadein 1.0
"I look over my shoulder and see Hanako peering timidly into the classroom, most of her body hidden behind the door."
show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove
mi "Hey! Playing delinquent again?"
show hanako emb_blushtimid
with charachange
"Hanako blushes hard at Misha's straightforward jab, even if it was only in jest."
show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove
shi "…"
show hanako emb_downsad
with charachange
show hanako emb_downsad at Transform(xanchor=0.5, xpos=0.97)
with charamove
"Shizune stares at her probingly, causing Hanako to look down and start backing away to the point where only her fingers can be seen wrapped nervously around the edge of the door."
"Maybe she is showing her dislike of Hanako by association of her dislike of Lilly."
"It appears so, and Hanako probably knows it as well."
"They seem to have momentarily forgotten about trying to get me to stay for the rest of the day."
hi "What is it, Hanako?"
show hanako emb_timid
with charachange
ha "H… has Lilly been here?"
mi "Sorry, Satou is not here. She, eh, came by in the morning though."
show hanako emb_downtimid
with charachange
"Hanako keeps looking uneasily at Shizune, who stares back at her with her usual studying gaze. What is she trying to do?"
"Of course Shizune isn't going to look away, and she is intimidating enough as it is, so I can only imagine how terrified Hanako would be."
"It is a little funny though, watching Hanako's reaction to Shizune's normal behavior. This is what happens when two people of two different extremes meet, it seems."
show hanako emb_timid
with charachange
ha "Do… do you know where she is?"
show shizu behind_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "If she has any sense in her head, she's in her classroom, working on their festival project. But who knows where that woman is loitering at."
label en_A22a:
show misha hips_grin at Transform(xanchor=0.5, xpos=0.15)
with charachange
mi "She might be slacking off somewhere, just like Hicchan~! Wahaha~!"
"Damn, what is it with Shizune and her need to point out stuff like this?"
label en_A22b:
scene bg school_scienceroom at bgleft
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.97)
with None
mi "She might be slacking off somewhere~! What a useless woman~!"
show hanako emb_downtimid
with charachange
hide hanako
with easeoutright
"Hanako nods quickly and retreats with haste, obviously to avoid any further contact with Shizune. Unfortunately, this turns their attention fully back to me."
stop music fadeout 2.0
show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove
show misha hips_grin
show shizu behind_smile
with charachange
mi "But Hicchan is not useless, right? Right? He said so himself~! Wahaha~!"
"I can see where this is going, and I do not want any part of it, not after that experience yesterday."
hi "Well, good luck with your preparations…"
"I start packing my bag, ready to make a break for the exit."
"Unfortunately I'm all the way on the other side of the room."
"The short distance to the doorway seems like a vast No Man's Land to me now."
show misha perky_smile
show shizu behind_blank
with charachange
play music music_shizune fadein 4.0
show bg school_scienceroom at bgleft
show shizu behind_blank at center
show misha perky_smile at Transform(xalign=-0.15)
with charamove
show bg school_scienceroom at center
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charamove
"Shizune and Misha both start maneuvering slowly in front of me, cutting off my route of escape in an unsettlingly cautious way that makes me think of ship-to-ship combat."
show misha hips_grin
with charachange
mi "I think Shicchan is saying that you should help us, Hicchan~!"
hi "Gee, I wouldn't know, she's so subtle."
show misha perky_confused
with charachange
mi "But~! that's the intent, so, please? I can't keep up, we have to actually build stalls for the festival, almost all of them all by ourselves, can you believe that?"
show misha perky_sad
with charachange
mi "Hammering boards together, over and over again, for hours, it's really hard!"
mi "I'm so used to it I was doing swinging motions in class, and I didn't even know it!"
"She bangs her desk a few times, imitating hammer blows."
mi "It's so repetitive, I can't stand it! And yesterday, I actually hammered all the boards on top of each other…"
mi "It was just a stack of boards all nailed together, and then I had to take it apart and do it all over again, and I got yelled at and laughed at~!"
hi "Uh…"
show misha perky_smile
with charachange
mi "So…"
show misha hips_grin_close
with characlose
"She clamps a hand down on my shoulder and grins, quickly running her tongue across her teeth mischievously."
mi "Do you have any plans for today, Hicchan?"
mi "I wonder if you do~."
hi "Sure I have plans…"
show misha perky_confused_close
with characlose
mi "Really~?"
mi "You're going to help us, right?"
"I notice her hands are moving constantly."
"She's signing everything we both say so that Shizune can understand."
"Shizune is being somewhat quiet today. Is she still angry? Well, probably at least a bit. I can see it in her eyes. But, this could also just be another way of trying to guilt me into lending her a hand."
"I have to find a way out of this."
hi "Hey, I should go now, to the library. You know, homework…"
hi "I should get going, shouldn't I? I have to be diligent, because I'm a new student, and all, so I have to make a good first impression, right? Yeah…"
hi "See you later, then!"
show misha perky_confused_close at offscreenleft
show shizu behind_blank at twoleft
show bg school_scienceroom at bgleft
with ease
hide misha
show misha perky_confused_close at offscreenleft behind shizu
show shizu basic_normal2 at offscreenright
show bg school_scienceroom at center
with ease_accel
show shizu cross_angry_close at tworight
show bg school_scienceroom at bgright
with ease_decel
"I turn to bolt for the door, but Shizune is blocking my path, her arms crossed over her chest and a stern expression on her face."
show shizu basic_angry_close
with charadistant
"She wags a finger tauntingly and begins signing to Misha with the manner of a squad leader giving directions to his fellow soldiers."
show shizu basic_angry
with charadistant
show misha perky_smile at twoleft
with charamove
mi "It didn't seem like you were in any rush to get to the library, Hicchan~!"
show misha hips_grin
with charachange
mi "That's right, Shicchan~, it does seem like he was probably going to slack off for the rest of the day."
show misha hips_laugh
with charachange
mi "Hahaha~! Wahaha~! You're surrounded~!"
show shizu behind_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Let's go to the student council room~!"
"She lets out a chuckle, and then breaks into laughter."
show misha cross_laugh
with charachange
mi "I'm sorry, Hicchan, I feel bad, but this works out for everyone, right?"
show shizu basic_normal2
with charachange
shi "…"
show misha sign_smile
with charachange
mi "That's right, Shicchan! Yes~, that's a good point too."
show shizu behind_blank
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Yes, this is beneficial to everyone, it solves all our problems."
show shizu basic_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Yeah yeah~!, I also thought he'd be more appreciative of our efforts."
show misha hips_frown_close
show shizu basic_frown_close
with characlose
"They pull themselves closer, as if they are about to pounce."
hi "Hey guys, two-on-one isn't very fair, is it?"
show shizu behind_blank_close
with charachange
shi "…"
"She keeps looking forward, impassive, then gives a sinister smile."
show shizu basic_sparkle_close
show misha hips_grin_close
with characlose
mi "Come on, we have a lot of work to do! Let's go to the student council room~!"
hi "Gee, I don't know…"
show misha cross_laugh_close
with characlose
"Misha laughs."
show misha hips_grin_close
with characlose
mi "Deja vu~?"
"She chortles, before letting out another laugh."
show misha cross_laugh_close
with characlose
mi "Hahaha, you know, my horoscope said it'd be a good day for me today."
show misha perky_smile_close
with characlose
mi "And now that you're going to help—{w=.5}{nw}"
show shizu adjust_smug_close
with charachange
"Shizune signs quickly to her."
show misha hips_grin_close
with charachange
mi "Right~!, I mean, now that you've decided to help us, completely of your own free will, I'll be able to take it easy! Lucky~, huh?"
"I open my mouth to say something but then realize there's no point."
"I refocus on trying to think of a way out of this. No, their actions are clearly deliberate, there's no sense in attempting to reason with them."
"You can't reason with madmen. I frown, and they don't even notice my discontent, further proving my suspicions."
"They seem pretty relaxed now. I guess they think they've already won, so they're letting their guard down."
stop music fadeout 2.5
"That's kind of arrogant."
"They pass forward in front of me as they move through the doorway,"
hide shizu
hide misha
with charaexit
"And I stealthily walk backwards back into the classroom as they step into the hallway, turning towards the stairwell."
"I let out a sigh of relief and quickly pack the rest of my stuff so I can make my escape."
play sound sfx_doorslam
"The classroom door slams shut."
play music music_running fadein 0.5
with None
show shizu cross_angry at offscreenright 
with None
with None
show misha cross_frown at offscreenleft 
with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease
shi "…"
mi "That wasn't very nice, there. Hahaha, you really got us good, though. Didn't he, Shicchan?"
show shizu behind_frown
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Right, right… …Hahaha!"
show misha cross_frown
with charachange
mi "What was that about? I thought you said you'd help us!"
mi "And then you bailed on us! And you thought you would get away with it, didn't you?"
show misha cross_laugh
with charachange
"The indignant expression vanishes and she begins to laugh hysterically, calming down only after an aggravated look from Shizune."
show misha cross_grin
with charachange
mi "Oh, ah… Yeah~, you thought you could get away with it! But, a criminal always returns to the scene of the crime!"
"I didn't even manage to leave the classroom in the first place. No, wait, I didn't even agree to help in the first place."
show misha perky_smile
with charachange
mi "Not very bright, are you, criminal? Thinking you can just shirk your duties like that… How low, Hicchan~!"
hi "I'm a criminal? What did I do? What's the charge? What am I guilty of?"
show misha hips_grin
with charachange
mi "That's for the courts to decide, criminal! I don't think we have to tell you that!"
show misha perky_smile
with charachange
mi "Besides, you're the criminal here, you know what you did!"
hi "Have you ever read “The Trial,” by Kafka?"
show misha hips_grin
with charachange
mi "No, what's that, Hicchan~? What does that have to do with this?"
hi "I read it a few months ago. It's about these people who run a kangaroo court on a guy who just wants to live his life. They refuse to leave him alone, and he can't fight the power."
show shizu basic_frown
with charachange
shi "…"
show shizu behind_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Hicchan, what does that have to do with anything?"
show misha sign_confused
with charachange
mi "Hey~!, what does that mean?"
"She turns back to me after signing back and forth for a lengthy amount of time."
show misha hips_frown
with charachange
mi "You know, we're both a little disappointed in you. You've let us down, Hisao."
show shizu basic_frown
with charachange
shi "…"
mi "Dropped the ball."
show shizu behind_frown
with charachange
shi "…"
mi "Left us hanging. And out in the cold~."
show shizu cross_angry
with charachange
shi "…"
show misha sign_smile
with charachange
mi "Is that any way to treat a person? To run away from your responsibilities, to abandon your comrades?"
show misha hips_frown
with charachange
mi "We think you owe it to us to honor your commitment."
hi "What? But I didn't commit to anything~!"
"My breathing catches in my throat and I momentarily start choking."
show shizu basic_frown
with charachange
shi "…"
show misha cross_smile
with charachange
mi "That's not true, Hicchan! You said you are not useless, you definitely said it, yes, definitely, definitely definitely~!"
show misha hips_grin
with charachange
mi "We are calling you on those words now~! You better prepare to show you are not a useless guy!"
mi "Your honor will be soiled forever if you try to get out of this~!"
mi "So for the rest of the day, we are going to hang out together, just the three of us, and work hard!"
show shizu behind_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "You can't fool us!"
mi "You should be happy, you're doing your school a great service. Ask not what your school can do for you…"
mi "But what you can do for your school!"
show misha cross_laugh
with charachange
mi "Hahaha!"
mi "Hahahahahahaha!"
"How depressing."
show misha cross_grin
with charachange
mi "Cheer up, cheer up, Hicchan!"
"She slaps me hard across the back with enough strength to knock the air out of my lungs. I gasp to breathe."
mi "Besides, aren't you happy you get to spend the day with two cute girls?"
show misha hips_laugh
with charachange
mi "Hahahaha!"
"I guess they are right. I did blurt those words out."
stop music fadeout 3.0
"Accepting my fate, I follow them to the student council room…"
scene bg school_council_ss
with shorttimeskip
play sound sfx_hammer
play music music_tranquil fadein 3.0
"…And hammer the final nail into the stall. It took all of the afternoon, and dinner time is nearly over. But it is done now."
show shizu basic_normal_ss at center
with charaenter
"Shizune pulls out a roll of measuring tape and a small level, and inspects it thoroughly."
show shizu behind_smile_ss
with charachange
"She smiles, looking pleased, then motions for Misha to come over."
show shizu adjust_happy_ss
with charachange
shi "…"
show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove
show misha perky_smile_ss at twoleft  behind shizu
with charaenter
mi "She says you did a very good job. In fact, you might actually have a gift for this."
show misha hips_smile_ss
with charachange
mi "Wow, I'm impressed, too. And that was fast, have you done this before?"
hi "No. Never."
hi "Never before."
hi "And I never will again."
show shizu behind_smile_ss
with charachange
shi "…"
mi "Well, our quota for the day is six stalls. In a few minutes, me and Shicchan should finish this one."
show misha hips_grin_ss
with charachange
mi "That means~… four more to go!"
show misha sign_smile_ss
with charachange
mi "We're making good time, she says~!"
show misha hips_grin_ss
with charachange
mi "Isn't this great fun?"
hi "What?"
"I could think of a million things I'd rather do, but I suppose everyone has to do their share for the festival, even me."
hi "You're both lucky that I'm helping you two out, if I really didn't want to, I could have gotten out of it easily."
show shizu basic_normal2_ss
with charachange
shi "…"
show misha perky_smile_ss
with charachange
mi "Really, Hicchan?"
show shizu adjust_smug_ss
with charachange
shi "…"
show misha cross_laugh_ss
with charachange
mi "Wahaha~! Shicchan thinks you are just running your mouth! Japanese people have no flight or fight reflex, Hicchan~!"
"Shizune tents her fingers deviously."
show shizu basic_happy_ss
with charachange
shi "…"
show misha hips_grin_ss
with charachange
mi "Definitely~! Definitely, definitely~! If you really wanted to escape, you would have taken immediate action~! That is how you know someone is serious; when they have no doubts, no regrets!"
show shizu basic_normal_ss
with charachange
shi "…"
show misha sign_smile_ss
with charachange
mi "Maybe it was a bad idea to tell you that, since now Hicchan knows what to do next time~."
"But, just the fact that she is all right with telling me this shows me that she doubts I'll be able to act on it."
"That only makes me want to do it more, and I almost want the opportunity to do so to arise again. But if that happens, she might get me again somehow."
show shizu behind_smile_ss
with charachange
shi "…"
show misha perky_smile_ss
with charachange
mi "Shicchan says she is happy now."
stop music fadeout 1.5
scene bg school_council_ni
with shorttimeskip
play music music_dreamy fadein 0.5
"Much, much later in the evening, we are looking at six completed stalls."
"With the pride of a job well done, we sit back and admire the fruits of our labor, not sharing a word between us. Just admiring."
"I realize I'm feeling quite thirsty."
hi "Hey, isn't there a vending machine out in the hall? They're on all day, right?"
show misha hips_smile at center
with charaenter
mi "Yeah, the drinks are very cheap, too. We usually get something from there on days like this."
"I dig around in my pocket, and find a single hundred yen coin."
hi "Is this enough? I'm feeling kind of thirsty."
show misha hips_grin
with charachange
mi "A hundred yen? You can get any drink in the machine with that."
hi "That's good, that's very good, then."
show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove
show shizu adjust_happy at tworight
with charaenter
shi "…"
show misha sign_smile
with charachange
mi "Ah, wait a second."
show misha hips_grin
with charachange
mi "Hm? What is it, Shicchan? Do you want him to get you a drink too? Hahaha!"
show shizu behind_smile
with charachange
shi "…"
show misha perky_smile
with charachange
mi "Hicchan, you've really helped us out, so today I - I mean Shicchan, will treat you."
show misha perky_confused
with charachange
mi "Hey, what about me?"
show shizu adjust_smug
with charachange
shi "…"
show misha perky_smile
with charachange
mi "What would you like? I'm feeling thirsty myself?"
show misha perky_confused
with charachange
mi "So am I!"
hi "Hm, I don't know. Anything's fine. I guess the melon soda."
show shizu behind_smile
with charachange
shi "…"
show misha perky_sad
with charachange
mi "Hey, wait, Shicchan! I also want a drink!"
hide shizu
with charaexit
show misha perky_sad at center
show bg school_council_ni at center
with charamove
mi "Aw…!"
show misha perky_confused
with charachange
mi "You know, it's times like this that I think she is just teasing me."
hi "That's probably it. I'm sure she'll get you something, right?"
mi "Yeah, she usually does. But… you never know…"
hi "Heh."
show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove
show shizu basic_normal2 at tworight  behind misha
with charaenter
"Shizune comes back with two melon sodas and a can of fruit juice."
"She hands me one of the sodas, and the other to Misha."
show misha hips_grin
with charachange
mi "Thanks, Shicchan~! I had total faith that you'd get me one, I knew I could count on you! Wahahaha!"
show misha perky_confused
with charachange
mi "But how did you know this was what I wanted? I usually get something else."
show shizu behind_smile
with charachange
shi "…"
show misha hips_grin
with charachange
mi "What? You knew I'd want to try it? And that I like these kinds of childish things? Hahahaha!"
show misha hips_laugh
with charachange
mi "Hahahaha!"
"I gesture my thanks to Shizune, who smiles and nods."
show shizu adjust_happy
with charachange
shi "…"
stop music fadeout 4.0
show misha sign_smile
with charachange
mi "Hey, Hicchan…"
hi "Yes?"
show shizu behind_smile
with charachange
shi "…"
show misha perky_smile
with charachange
mi "We've been spending a lot of time together. Already, in such a short time, we've done so much."
mi "We should both stop beating around the bush. What I'm trying to say is,"
"It sounds a lot like she's going to ask me out, but that can't be it. Nevertheless, my heart is beating like a jackhammer. Damn, this reminds me of another similar scene earlier this year."
"I try to say something, but my brains can't decide whether to stop her or to tell her to continue."
"I feel myself blushing all the way to the ears."
show shizu adjust_smug
with charachange
shi "…"
show misha hips_smile
with charachange
mi "What I'm trying to say is…"
show misha hips_grin
with charachange
play music music_ease
mi "Would you like to join the Student Council?"
hi "Ah, what a disappointment."
show misha cross_laugh
show shizu adjust_blush
with charachange
mi "Hahaha! Hahahaha! Hahahahaha! Wahaha! Hahahaha!"
mi "Did you think she wanted to ask you out, Hicchan?"
mi "Hahahaha! Hahaha! Hahaha! Hahahaha!"
mi "Hahahahahahahaha!"
"I feel very embarrassed right now, I can feel myself getting even redder in the face."
"Shizune also tries to hide a blush after Misha translates, and then puts a few sheets of paper in front of me."
show shizu behind_frustrated
with charachange
shi "…"
show misha cross_grin
with charachange
mi "So, how about it? All the paperwork is right here."
show misha cross_smile
with charachange
mi "And you are sitting down, anyway. You look very at home here. Drinks and everything~!"
show shizu basic_normal
with charachange
shi "…"
show misha hips_grin
with charachange
mi "What do you say?"
"She quiets down a little and asks again a little more solemnly."
show misha cross_smile
with charachange
mi "Hicchan, what do you say?"
show misha sign_smile
with charachange
mi "You don't exactly hate this, right?"
"I'm more than a little surprised by this sudden change of tone. I don't really know how to react to it."
"For one thing, she isn't shouting uproariously with no regard for tact."
"Before, I'm sure she knew already that I was going to say no."
"This time, she seems actually serious."
show misha perky_smile
with charachange
mi "I think maybe you should join. Not just because we could use your help, but, well, you're hanging out with us anyway."
mi "I think Shicchan would like it if you would join as well. It's not like you hate us or anything, right?"
show misha perky_sad
with charachange
mi "It wouldn't hurt if you joined. And I'd appreciate it if you would."
"She seems to be having a hard time getting her words out, which is strange for someone talkative like Misha."
"For some reason, I'm almost troubled by it."
show shizu behind_blank
with charachange
"My eyes drift over to Shizune, who stares back at me tentatively, absentmindedly cleaning her fingernails."
show misha perky_smile
with charachange
mi "If you don't want to join, I promise we won't ask again, but if you did, we would be really happy."
"Both Shizune and Misha seem to be unable to look me in the eye."
"I can't lie, the thought of being around two such cute girls is something that I couldn't possibly pass up."
"I'm not looking forward to this kind of work every day, but there should be less after the festival."
"At least, I hope so."
hi "All right. I guess it can't hurt, so, why not?"
show shizu adjust_happy
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Wonderful. Wonderful! Ahahaha~!"
"Shizune tents her fingers in satisfaction."
show shizu basic_happy
with charachange
shi "…"
show misha perky_smile
with charachange
mi "She'll fill everything out, Hicchan. Congratulations, you are officially a member of the Student Council now!"
hi "Great. I'm not looking forward to a lot of work."
hi "To be honest, I've never done any student council activities before."
hi "But maybe it'll be a positive experience?"
"Misha starts to clap, laughing exuberantly as she does."
show misha hips_laugh
with charachange
mi "Congratulations, Hicchan!"
show shizu adjust_smug
with charachange
shi "…"
mi "Congratulations!"
show shizu behind_smile
with charachange
shi "…"
mi "Congratulations!"
show shizu adjust_happy
with charachange
shi "…"
mi "Congratulations!"
hi "I get the message."
"I can't help but smile, finding such a display childishly cute."
show misha hips_grin
with charachange
mi "The Student Council is always busy, you know! But for today, we're done. See you tomorrow, Hicchan!"
show misha hips_smile
with charachange
mi "We still have work left, so we'll be counting on you!"
stop music fadeout 4.0
scene bg school_hallway3
with locationchange
"I leave the room, feeling totally wiped out. The grounds are totally deserted, and the school looks pretty ominous this late. The council office is the only window with lights on any more."
"Is this what the Student Council will be like? My body might not be able to take it."
label en_A23:
scene bg school_scienceroom at bgleft
with shorttimeskip
play music music_tranquil fadein 3.0
"Hanako doesn't come to the morning class at all, leaving her seat looking empty and lonely in the back of the classroom."
"I have to tell her that Lilly was looking for her if I see her later."
"After the events of this morning, class is pretty boring in comparison. I turn the pages of my textbook lazily."
"I have a bit of catching up to do, despite trying to keep up with my studies at the hospital, but I'm not feeling that enthusiastic about it."
"The clock at the front of the room sounds unbearably loud. The teacher hasn't said anything in over seven minutes, instead opting to cover the board in rows and rows of equations taken directly from the book."
"The rhythmic clashing of chalk on blackboard seems to synchronize perfectly with the ticking of the clock."
"I start to copy down the equations just to pass the time, even though they are right there in the text book."
scene bg school_scienceroom at bgright
with shorttimeskip
play sound sfx_normalbell
"When the bell rings, I'm not in a hurry because I have nothing to do, so I stay for a while, reviewing what we covered in class today. I prefer to leave last anyway, so I don't have to deal with crowding in the hallways."
"I notice Shizune and Misha have also stayed behind, talking to someone from another class."
"Shizune's signing so fast that her hands make noises like swords cutting through the air."
"Maybe there is pent up anger in there."
"Misha is trying desperately to keep up, but it's clear she can barely manage to even understand her."
"I put my head down. Whatever they're discussing, it looks like serious business."
"Shizune signs to the point where her wrists crackle, and Misha struggles to spit it out in word form."
"Sometimes she trips over herself like she's dealing with tongue twisters. And then on top of that, she has to sign back anything the other girl says."
"Seems like a rough job."
"Misha looks tired, like she's about to faint."
"Luckily for her, their business is soon finished and the girls sit down on their seats again."
show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter
mi "Uwaaah! I'm so tired!"
"She's hanging her head limply on her desk, looking exhausted."
"I'll use the opportunity to reconcile with Shizune a bit, without getting roped into the student council thing again, though I suspect that door is now closed for me."
hi "Festival preparations must be tough for you."
"Indeed, the people in this school seem to be taking the festival very seriously. Whenever I see people idling around before and after classes they're always talking about their plans for it."
"It's kind of neat to see everyone being so enthusiastic about it."
"I'm probably the only one who doesn't have something to do."
show shizu basic_angry
with charachange
"Shizune scoffs at me first, as if trying to decide whether to ignore or sneer at me, but in the end she starts signing without doing either."
show misha perky_confused
with charachange
"Misha perks up, looking at her hands with slightly unfocused eyes."
show shizu behind_frown
with charachange
shi "…"
"She signs with harsh, heavy, dramatic strokes."
"Misha translates her signing into speech for me."
"She does it so well it's almost like Shizune is actually speaking, transmitting her thoughts directly through Misha."
"She must've practiced it vigorously."
show misha cross_frown
with charachange
mi "Well of course, we're in the Student Council, you know, so we're pretty busy."
show shizu basic_frown
with charachange
shi "…"
show misha sign_smile
with charachange
mi "It's an important duty of ours, to ensure the success of the festival with all our strength."
show shizu behind_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "We would shame ourselves in front of the past student council generations if the festival were to fail."
show shizu adjust_angry
with charachange
shi "…"
show misha sign_smile
with charachange
mi "That's why there must be no flaws, no… errr I think that was “incumbrances,” no nothing that might make the festival short of perfect."
"Shizune's passionate speech and Misha's enacting are really oddly fitting of them."
stop music fadeout 2.0
show shizu adjust_blush
show misha perky_confused
with charachange
mi "Oh? Hello~!"
show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright
play music music_pearly fadein 1.0
"I look over my shoulder and see Hanako peering timidly into the classroom, most of her body hidden behind the door."
show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove
mi "Hey! Playing delinquent again?"
show hanako emb_blushtimid
with charachange
"Hanako blushes hard at Misha's straightforward jab, even if it was only in jest."
show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove
shi "…"
show hanako emb_downsad
with charachange
show hanako emb_downsad at Transform (xanchor=0.5, xpos=0.97)
with charamove
"Shizune stares at her probingly, causing Hanako to look down and start backing away to the point where only her fingers can be seen wrapped nervously around the edge of the door."
"Maybe she is showing her dislike of Hanako by association of her dislike of Lilly."
"It appears so, and Hanako probably knows it as well."
hi "What is it, Hanako?"
show hanako emb_timid
with charachange
ha "H… has Lilly been here?"
mi "Sorry, haven't seen Satou. She, eh, came by in the morning though."
show hanako emb_downtimid
with charachange
"Hanako keeps looking uneasily at Shizune, who stares back at her with her usual studying gaze. What is she trying to do?"
"Of course Shizune isn't going to look away, and she is intimidating enough as it is, so I can only imagine how terrified Hanako would be."
"It is a little uncomfortable, watching Hanako's reaction to Shizune's normal behavior. This is what happens when two people of two different extremes meet, it seems."
show hanako emb_timid
with charachange
ha "Do… do you know where she is?"
show shizu behind_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "If she has any sense in her head, she's in her classroom, working on their festival project. But who knows where that woman is loitering at."
label en_A23a:
scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None
hide hanako
with charamoveoutright
"Hanako nods quickly and retreats with haste."
stop music fadeout 2.0
show misha hips_grin
with charachange
mi "What were we talking about? Oh yeah, we are really working hard to make the festival happen."
"And driving other people insane along the way."
hi "Well, good luck with that."
"I stand up to leave, making my exit before either of them manages to berate me any more for slacking off."
scene bg school_hallway3
with locationchange
"The halls are somewhat quiet, as expected. Everyone must be in club meetings or at festival preparations. Or both."
"Shizune's words about being a slacker echo in my head."
"I feel a bit guilty about not contributing, but I seem to lack the resolve to do something concrete about the matter."
"For the festival, it's too late already unless I count helping Shizune and Misha which I naturally don't. And clubs… I don't know."
"Maybe I'm not a club type of a person."
play music music_soothing fadein 4.0
scene bg school_dormext_half
with locationskip
"Halfway through the way from the school building to the dorms I spot a figure in front of the dorms."
"It's Rin."
"It looks like she is working on her mural today too."
"I walk over to her, but she doesn't seem to notice me approaching."
scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange
"She's sitting on an upturned box, looking intently at the wall she is painting with a brush held between her toes."
"The mural has progressed considerably since yesterday but it's still only half-done as far as I can tell."
"More colors have appeared and the twisted human-like figures have spread and increased in number."
"I have to say, the style is quite eye-catching and very unique. Not that I would be knowledgeable about art by any measurable scale, but it's very nice-looking, nevertheless."
"I clear my throat to get her attention, but not startle her so that her concentration won't break."
rin "Wait."
"She doesn't even turn to check who it is."
"I'll wait."
stop music fadeout 6.0
"…"
"…"
"…"
"…"
with shorttimeskip
"…"
"Fifteen minutes later I decide that her concentration is indeed unbroken, and also that I have waited long enough to warrant poking her gently on the shoulder to remind her of my presence."
"Rin turns her head mechanically to my direction, ending up staring at my crotch level."
show rin basic_deadpan_close
with charachange
rin "Oh, it's Hisao."
play music music_rin fadein 0.3
"She can tell? I would feel a lot less uncomfortable if she would look at my face."
hi "An astute observation. Hard at work, I see."
"The conversation starts as if I hadn't been here for a quarter of an hour already, but it's not a concern. At least it starts."
hi "Looking good."
"It does, the layers of paint hiding other layers of paint, mixing and shaping the human figures really create an impressive look. But Rin looks miffed."
show rin basic_deadpanupset_close
with charachange
rin "You shouldn't comment on works in progress. Seven years of bad luck."
hi "Sounds terrible. I guess I'll take it back then."
"Still, it looks good. I wonder if I get fourteen years of bad luck for thinking that."
show rin basic_awayabsent_close
with charachange
"Rin turns back to look at her painting and pokes it with a big toe."
show rin relaxed_nonchalant_close
with charachange
rin "Could you mix some of this color? I am running out of it."
"She looks down at a half-empty bowl with the remains of the same pinkish paint in it."
"I didn't really intend to stay and help her with this project though… I guess I didn't intend to do anything much."
show rin basic_absent_close
with charachange
"I look at Rin, she looks emptily back at me."
hi "Just this once."
show rin basic_awayabsent_close
with charachange
"Rin picks up another brush and drenches it in another tone of pale red. There are dozens of similar bowls all around her working area. From the looks of this scene she could have been sitting there for hours."
"I wonder if she has. That would mean she'd have been skipping school though, which I of course wouldn't put beyond someone like Rin."
"I pour a little bit of white and red into the bowl, trying to match the color with the one already on the wall."
"I can't seem to get it right."
"It's really inconvenient of her to not mix enough in the first place. Getting it to be exactly the same tone will be impossible, but at least I can try to get as close as I can."
hi "Speaking of hard work, isn't that a huge workload for you too? It's such a big painting and all."
show rin basic_deadpan_close
with charachange
rin "Oh, I’m not old and bitter enough yet to think like that."
hi "I guess you aren't."
show rin basic_deadpannormal_close
with charachange
rin "You guessed right."
show rin basic_deadpancontemplation_close
with charachange
rin "Legs hurt though. They feel like slugs. Slugs made of sea slugs."
hi "Because of the position?"
rin "Yeah, I like doing it in a horizontal position more, if you know what I'm talking about."
rin "But it can't be helped. Can't ask the wall to lay down."
show rin negative_spaciness_close
with charachange
"Saying that, she stretches herself a little, bending her legs and back far more than a human should flex. It's astonishing how effortlessly she manages her body around."
show rin negative_annoyed_close
with charachange
show rin negative_spaciness_close
with charachange
"There is a small flinch in her otherwise blank expression - a hint of pain maybe - as she stretches out her calves."
"Rin must have stamina and dexterity far above a normal person to be able to live like she does, but she's wearing out working on this."
hi "Why push yourself so much? Take a break or something at least. Continue tomorrow if it's bad."
show rin basic_deadpannormal_close
with charachange
"This gives her a pause."
"A long one too, feeling like a mental yawn."
"…"
show rin basic_deadpan_close
with charachange
rin "I don't think so, Hisao."
rin "I'm not pushing myself."
hi "Sure looks like you are."
show rin basic_deadpannormal_close
with charachange
rin "No. It's not about pushing or pulling or anything related to that kind of thing."
show rin basic_awayabsent_close
with charachange
rin "There is this boy."
hi "A boy?"
show rin basic_absent_close
with charachange
rin "Yes."
hi "Where?"
show rin basic_deadpannormal_close
with charachange
rin "At the art club."
hi "Err… and?"
show rin basic_deadpan_close
with charachange
rin "He is blind."
hi "Oh. How can you paint if you are blind?"
show rin basic_awayabsent_close
with charachange
rin "No idea."
hi "So why is he there?"
show rin basic_absent_close
with charachange
rin "That's the point. He is there."
"She really should speak more than one word at a time to make this feel more like a discussion and less like an interrogation."
show rin basic_awayabsent_close
with charachange
rin "He can't really do anything that you'd call art, right? But he comes there anyway. And paints."
show rin basic_deadpannormal_close
with charachange
rin "Why?"
hi "I don't know. Why?"
show rin basic_deadpan_close
with charachange
rin "I don't know. That's why I asked."
hi "So?"
show rin basic_deadpannormal_close
with charachange
rin "He doesn't paint often but I think his paintings are very interesting."
hi "I'm sure they are."
show rin basic_lucid_close
with charachange
rin "I once tried that. Painting with eyes closed."
show rin basic_deadpannormal_close
with charachange
rin "Wasn't too interesting. And cleaning up the floor took ages. Didn't try again."
show rin basic_deadpandelight_close
with charachange
rin "But he is becoming better at sculpting."
hi "I see."
"Maybe she was trying to make a point with this. Maybe she forgot she had one."
hi "Seems like the art club is full of interesting people."
show rin basic_deadpan_close
with charachange
rin "Not really."
"Pretty blunt statement, and she totally missed the sarcasm."
hi "No?"
show rin basic_awayabsent_close
with charachange
rin "Just like I said. They are not very interesting. I usually don't have much interest in people who are not interesting."
show rin basic_absent_close
with charachange
rin "Maybe you have."
hi "Maybe."
"…"
show rin basic_awayabsent_close
with charachange
rin "But that boy is interesting."
show rin basic_lucid_close
with charachange
rin "Maybe I am like that boy, or maybe you are. Maybe everyone is."
rin "Doing things you can't do, just because you can."
"That's pretty deep I think, and tell that to her."
hi "You're a deep one."
show rin basic_deadpannormal_close
with charachange
rin "Nah. I'm a really shallow and thoughtless person. People say that to me all the time."
show rin basic_deadpanamused_close
with charachange
rin "Did you know I can only think of four things at the same time?"
hi "No, but now I do."
show rin basic_lucid_close
with charachange
rin "Right now I'm thinking of the second floor's girls' toilet, ice-cream-flavored ice cream, the middle toe, and a haircut."
show rin basic_awayabsent_close
with charachange
rin "I'm going to need a haircut."
show rin negative_spaciness_close
with Dissolve(0.1)
show rin basic_delight_close
with Dissolve(0.1)
show rin negative_spaciness_close
with Dissolve(0.05)
show rin basic_delight_close
with Dissolve(0.05)
show rin negative_spaciness_close
with Dissolve(0.05)
show rin basic_delight_close
with Dissolve(0.05)
show rin negative_spaciness_close
with Dissolve(0.1)
show rin basic_delight_close
with Dissolve(0.2)
"She shakes her head around vigorously, letting her short and messy hair ruffle wildly around. I can see that doing it is something she likes to do."
show rin basic_awayabsent_close
with charachange
"We fall silent as Rin treads around absentmindedly, poking some brushes around. The thought about the art club sticks in my head for a while longer."
"I'm feeling like I'm treading on very unknown territory with art. The way these meetings with Rin go, it's as though I'm starting a smoking habit or something. I should probably stop talking with her."
"It’s not like I dislike her, despite the confusion her being herself causes, and I don't dislike art either. I’ve even drawn for fun sometimes. I just don’t have a real creative drive, or any technical skill."
"So usually, if I were to draw something, I get white paper syndrome and just freeze completely."
"That, or I manage to draw something disfigured and promptly get frustrated at my inability to put the picture in my head down on the paper, then call it quits without really even trying to make an effort."
"Rin clearly doesn't have this problem… but she frustrates me in another way. Being with her is like looking into a mirror that doesn't reflect anything."
"It makes one question the sanity of the act."
show rin basic_absent_close
with charachange
"Rin sits down on her box, swaying from side to side, apparently comfortable with the uncomfortable silence. She is staring at me again, or maybe over my shoulder. I can’t quite figure out where her eyes are focused on."
"I'm thinking of leaving so she can carry on working undistracted and that I can do whatever I'm going to do alone. It's not like I have anything that must be done today…"
hi "Oh, shoot."
show rin basic_deadpan_close
with charachange
rin "Who?"
hi "Nobody, I just forgot to tell Hanako that Lilly was looking for her."
hi "Do you know her? From my class?"
show rin basic_deadpanamused_close
with charachange
rin "Oh, her. The Mystery Toilet Girl."
show rin basic_amused_close
with charachange
rin "That person is funny. I saw her going to the toilet five times during one recess three weeks ago. I'm sure it's the world record."
show rin basic_deadpandelight_close
with charachange
rin "It was very mysterious."
hi "That's why you call her Mystery Toilet Girl?"
show rin basic_absent_close
with charachange
rin "What other reason could there possibly be? Well, if there is, it's an eternal mystery. I didn't follow her in there."
"…"
show rin basic_awayabsent_close
with charachange
rin "Maybe it was the week before that? Could have been."
"…"
rin "Looking at her makes me hungry."
hi "Don't say that."
hi "At least, not around her."
show rin basic_deadpannormal_close
with charachange
"Rin turns to look at me blankly, as if she's not sure why I reproved her."
"But she doesn't acknowledge understanding any more than before, so I give up at this point."
hi "So do you want to go eat dinner then?"
show rin basic_awayabsent_close
with charachange
rin "No. Not yet."
"Rin has turned her hungry gaze back to the wall, looking slightly more energetic, or at least slightly less lethargic than she did before."
"It's as if the wall is an opponent she has to vanquish, something she must overcome before she can indulge in dinner."
"This is the feeling I get. A weird sense of empathy overcomes me and makes me smile a little to myself."
"For all her oddity, Rin is pretty cool after all."
hi "I'll be going anyway."
hi "Have fun."
stop music fadeout 3.0
"Rin has already grasped a brush and is dipping it into fresh paint, so of course she can't hear me any more or doesn't answer anything even if she does."
label en_A24:
stop music fadeout 6.0
scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None
show bg school_scienceroom at right 
show hanako emb_timid at right
show shizu behind_frown at offscreenleft
show misha hips_frown at offscreenleft
with charamove
hide misha
hide shizu
with None
hi "You need to find her? She was looking for you in the morning but I guess you have missed each other."
"She waits a little without answering the simple question, looking awfully like she's not sure if it's proper to answer such a question."
show hanako emb_blushtimid
with charachange
ha "Y…yeah."
hi "I can come with you."
hi "If it's okay."
show hanako emb_downtimid
with charachange
show hanako emb_blushtimid
with charachange
"Hanako nods fractionally, still on guard, her shoulders stiff like wood. I get the feeling that she might be more comfortable by herself after all, but it's too late to back off now."
"She has this really troubled expression she seems to wear almost constantly, one that makes me constantly be on guard myself. I wonder why."
"I kind of understand why she always seems to be so wary… or maybe more like, why there could be a person like her."
"But I still have no idea how I should act around such a person."
hi "It's dinnertime soon. Were you planning to eat with Lilly?"
show hanako emb_downtimid
with charachange
show hanako emb_blushtimid
with charachange
"She nods slightly."
"So she must have been trying to get in the cafeteria."
"Well, there's something of a dinner crowd, just like the cafeteria is crowded during lunch."
"It's not as bad because dinnertime is longer than lunch hour, but I can understand why Hanako could be discouraged from going in."
"I pick up my bag and we take our leave. Hanako skips a little to meet my initial pace, so I slow down to match her speed."
scene bg school_hallway3
with locationchange
"It doesn't take long for us to be walking at a comfortable pace down the hallway."
show hanako def_worry at right
with charaenter
"It almost feels like we're going for a stroll together; something that I can't say I've really done before with a girl."
"Hanako doesn't seem to be thinking the same thing though. Even though we are walking at the same pace, she never comes within arm's reach of me."
"I guess she's still a little uncomfortable around me. Given how shy she is, there doesn't seem to be much helping it, at least for now."
scene bg school_cafeteria
with locationchange
play music music_night fadein 3.0
"By the time we arrive at the cafeteria, there is not much of a crowd there, but Lilly is nowhere to be seen."
show hanako emb_downsad at center
with charaenter
"Hanako's head sinks even lower than usual."
hi "Have you looked somewhere else already?"
show hanako basic_worry
with charachange
ha "J-just at the library… I was reading…"
"So she does spend the classes she skips at the library."
hi "Ah, so not exactly a thorough search then. Well, if I had to guess, she'd be in her own class like Shizune said, right?"
show hanako cover_worry
with charachange
ha "R-right."
show hanako basic_normal
with charachange
"With the slightest of nods, Hanako agrees with my reasoning."
"God, she's being so awkward."
"It's like I need double layered silk gloves with padding to even begin interacting with her."
"Some small talk might help her become a bit more used to me. It isn't hard to tell that the silence between us is hovering on the edge of both our minds."
hi "So you and Lilly usually hang out together after class, right?"
show hanako emb_downtimid
with charachange
ha "Y-yes."
"I'm not quite sure what I expected from her answer, nor why I even asked the question. That much was rather obvious, after all."
"She doesn't seem like the type to cultivate a social circle, either, so I suspect that Lilly may well be her only friend."
hi "Must be a pain being in different classes, I'm guessing."
"She gives a sharp, almost reflexive nod. Compared to Lilly's careful thought about her actions and speech, Hanako hastens to make her answers as prompt and short as possible."
show hanako emb_downsmile
with charachange
ha "Lilly… comes by the classroom, though. Even when she's busy…"
"She gives a small smile as she says it, evidently appreciating the fact that Lilly goes out of her way to help her."
"It's pretty cute, really. There isn't any need to say more, both of us content that the discussion's reached an end."
scene bg school_staircase2
with locationchange
"As we ascend the stairs back to the lobby we are met by a group of students heading downstairs like a school of fish moving from one feeding area to another."
show hanako cover_worry_close at Transform(xanchor=0.4, xpos=0.0)
with easeinleft
"They seem to be keeping mostly to themselves, but before I can notice her doing so, Hanako has moved around behind me."
hi "Hey, are you all right?"
show hanako basic_worry_close
with charachange
ha "J-just keep going…"
hide hanako
with easeoutleft
"The students pass us without as much as a second glance, and Hanako takes up position to my side again as we enter the building, her momentary reprieve from her anxiety all but snatched away."
scene bg school_lobby
show hanako basic_normal at center
with locationchange
"Even as we climb towards the third floor, she doesn't seem to relax."
"It isn't as if I've never known a shy person before, or even shy girls, but Hanako seems to be pretty far beyond what I'd call normal in her fear of other people."
"If it weren't for Lilly acting as a mediator, I doubt Hanako would have even been able to walk beside me like this. She seems to completely shut down in the presence of others."
"The rest of the walk up to Lilly's classroom continues in strained silence, while I rue her inability to socialize at all."
scene bg school_hallway3
with locationskip
stop music fadeout 4.0
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0
"After we make our way up the stairs, the noise coming from Lilly's classroom is audible from halfway down the hallway. I wasn't expecting such a din at all."
hi "Well, I guess we found her…"
"This wasn't hard. Did Hanako come here first then come to me for backup, I wonder?"
"Well, if that's true, then at least she's starting to trust me a little. That can only be a good thing."
"Eventually, the two of us reach the door to class 3-2. With Hanako less than subtly positioning herself behind me, I open the door."
play sound sfx_dooropen
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play music music_another fadein 1.0
scene bg school_room32 at bgright
with locationchange
"Inside is a hive of activity, seemingly every student in the class talking at once as they work hurriedly on their separate tasks."
"Going by the paint cans, decorations and banners being made, it must be for the upcoming school festival."
"I guess my first priority should be finding Lilly…"
"…{w} There."
"Finding her among the din is surprisingly easy, not the least because of her looks."
"With a couple of students gathered around her as she stands at the front of the class, she seems to be in charge of the preparations, or at least busy organizing them."
"Carefully negotiating a path through the various students hunched over the floor for lack of desk space, I raise a hand entirely out of habit as we finally reach Lilly."
hi "Hi, Lilly."
show lilly basic_surprised at center
with charaenter
"She perks her head up as she breaks off talking to a noticeably smaller girl who must be her classmate, trying to listen as best she can."
li "Sorry, who…"
hi "Ah, sorry. Hisao. I have Hanako too."
show lilly basic_smile
with charachange
show lilly basic_smile at twoleft
show bg school_room32 at center
with charamove
show hanako basic_normal at tworight
with charaenter
ha "H-hi."
"She's pretty skittish. Considering the number of people around, it isn't too hard to work out why."
"Lilly takes a moment's pause to assess the situation before turning to the other student once again."
show lilly basic_smileclosed
with charachange
li "For the moment, just ask Moriya for his advice. Kenji's busy with painting one of the banners already."
"A quick nod and she bounces off, fingers carefully sliding along the wall's face for orientation."
$ renpy.music.set_volume(0.1,1.0)
"Wait… Kenji? That Kenji?"
"I quickly turn about, leaning to the side to see past Hanako."
"Sure enough, in a corner of the room, Kenji's hunched over a sheet of cloth as he paints it. His eyes remain only inches from the brush, reminding me of how close he had to be to make out my face when I met him."
$ renpy.music.set_volume(1.0,1.0)
show lilly basic_smile
with charachange
li "Sorry about that. Our class doesn't have many students with even partial eyesight, so they're in high demand."
"That's right, class 3-2 was specially for students with poor vision. Preparing for the festival must be pretty arduous for them."
hi "Need a hand? I could give you help if you need some. Maybe Hanako could too."
"A chance to set her mind on something would do her good, but I doubt she has the courage to ask outright. She quickly nods in affirmation afterwards, so I'm confident I made the right move."
"Lilly gives a noticeable sigh of relief."
show lilly basic_weaksmile
with charachange
li "Ah, that's good. This might actually get finished before everyone goes off to dinner, now."
show lilly basic_listen
with charachange
li "Would you be able to help the person painting the main banner? It's a big task for him to do, but nobody else can help."
hi "Kenji? Sure."
show lilly basic_surprised
with charachange
"She seems surprised that I know him. I can't really blame her."
li "I take it you've met?"
hi "Our rooms in the dorm are right next to each other. Hard to miss each other, really."
show lilly basic_ara
with charachange
li "Well, it's good to see you're getting friends so fast."
"Friend… I wonder if that's the right word to use for him."
"Hanako's silence during the proceedings reminds me of the reason I put her up to helping in the first place."
hi "We'll go help him then. He knows what needs doing, right?"
show lilly basic_smileclosed
with charachange
li "That's right. Just ask if you have any problems."
hide lilly
hide hanako
with charaexit
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")
"Chorusing in assent, Hanako and I begin another trek across the classroom."
"Kenji sits crouched on the floor, his gaze fixed on the white calico in front of him."
show kenji tsun at Transform(yanchor=0.45, ypos=1.0, xalign=0.5)
with charaenter
hi "Hey Kenji."
"…No answer. He continues dragging his paint-soaked brush along the large half-painted kanji that's sketched on the sheet in pencil."
hi "Kenji?"
show kenji tsun at center
with charamove
ke "Huh? What? Who is it?"
"If this is the way he treats class members, it's no small wonder he's working on this alone."
hi "It's me. Hisao. From the—{w=.5}{nw}"
ke "Right, right, I know that, man. What're you doing here, though?"
"His dismissive attitude annoys me."
"He must be the type to really get focused on his work, hating to be disturbed by anyone until he's done, I suppose."
show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove
show hanako cover_distant at tworight
with charaenter
"While we talk, the sound of Hanako's footsteps as she walks out from behind me reminds me that she's here."
hi "I was just going to help with the banner. Hanako and I, that is."
show hanako cover_worry
with charachange
ha "H… Hello…"
show kenji happy
with charachange
ke "Oh. Er, hey. I guess that's okay."
"As soon as Hanako enters the equation, his demeanor takes a complete about-face. His sudden faux-hospitality is slightly unsettling."
"Oh, right. Women. On second thoughts, this may not have been a great idea after all."
stop music fadeout 2.0
scene bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip
"Hanako and I grudgingly set ourselves down on the opposite side of the cloth banner to Kenji, noting the several small paint tins on the ground around it."
"Class 3-2… noodle stall?"
hi "You guys selling noodles at the festival on Sunday?"
show kenji happy_close
with charachange
ke "Yeah, some stalls outside. Or something."
"“Or something?” His noncommittal nature sparks a fair amount of suspicion on my behalf. The task at hand comes first, though."
hi "So how do you want to split this? We do borders while you do the text? Or do you want to switch and do the borders?"
show kenji tsun_close
with charachange
ke "Text is mine. You do borders."
"He has surprisingly strong feelings on the topic."
show hanako basic_distant_close
with charachange
"As I reach over to grab a brush, I notice Hanako's already debating between colors to use."
show hanako basic_normal_close
with charachange
show hanako basic_distant_close
with charachange
show hanako basic_normal_close
with charachange
"By the time I've put brush to cloth, she's already started on a delicate pattern. Looks like my idea of taking her mind off everyone around her worked."
"With a dark blue stroke, the three of us silently get to work."
"Not before Kenji takes advantage of Hanako's working to lean towards me and whisper conspiratorially, though."
show bg school_room32 at center
show kenji tsun_close at center
show hanako basic_normal_close at offscreenright
with charamove
show kenji neutral_close
with charachange
play music music_kenji fadein 0.5
ke "Okay man, why're you here?"
hi "Hanako just wanted some help to find Lilly, that's all."
show kenji tsun_close
with charachange
"He apparently disapproves of my motivations."
ke "I get it. It looks like I misjudged you."
show kenji happy_close
with charachange
ke "You're infiltrating them, aren't you? Going deep undercover?"
"I should have guessed. Letting the truth slip by him would probably be better than outright lying or annoying him, in any case."
hi "Is that why you're here?"
ke "Obviously. It sucks, but there's no better way to get intel than going in yourself."
show kenji tsun_close
with charachange
ke "We gotta stick together, man. This is a harsh school, a harsh world."
hi "Yes, very harsh."
"He misses my true meaning as he leans back, satisfied I'm sympathetic to his cause. I'd better get down to work."
stop music fadeout 2.0
stop ambient fadeout 2.0
scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip
ha "Finished."
hi "Looks like I am too. Good job."
"The two of us connect up the lines of our patterns, mine being as close a copy as I could manage of hers."
scene bg school_room32
with locationskip
"With a grunt, I lever myself up from the floor and look around."
play music music_dreamy fadein 4.0
"Aside from Hanako and myself, there's only Kenji left finishing off a sign as well as Lilly and a couple of students talking among themselves in the classroom."
"Looking at my watch, it's no surprise. It's getting pretty late."
hi "Need a hand?"
show hanako basic_normal at center
with charamoveinbottom
"I offer a hand to Hanako, which she uses to get herself up."
"As she does, I can't help but glance at her wrist; if her scars extend even to there, just how much of her body was burned?"
show hanako emb_downtimid
with charachange
"I feel a pang of guilt about it however as she quickly covers her wrist with her other hand."
hi "Looks good, doesn't it?"
show hanako emb_timid
with charachange
"She looks surprised for a moment before noticing that I mean the banner."
show hanako basic_bashful
with charachange
ha "It does… I guess."
"Her smile shows that she feels a slight sense of pride in the result, just as I do."
hide hanako
with charaexit
"With the floor significantly neater for the decorations being placed on desks and shelves, it's much easier to get to Lilly as we cross the room."
hi "We've finished the banner. I guess that's all that needs to be done?"
show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter
"Lilly gives an appreciative nod."
show lilly basic_smile
with charachange
li "Thank you Hisao, Hanako. If there's any way I can thank you…?"
hi "It's fine. Beats sitting in my room studying, at any rate."
show hanako basic_normal
with charachange
ha "I don't mind either."
"She nods, before suddenly remembering one last person."
show lilly basic_surprised
with charachange
li "Oh, is Kenji still here?"
"Just as I open my mouth, Kenji gives the answer from the other side of the room."
ke "Yeah, just finished."
"He carefully slides his sign onto an empty section of shelf to dry, before quickly walking past us and out the door."
show hanako basic_normal at center
show lilly basic_surprised at left
show bg school_room32 at bgleft
with charamove
show kenji neutral at Transform(xalign=1.15)
with charaenter
ke "Seeya man."
hi "Bye."
hide kenji
with charaexit
show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32 at center
with charamove
"The remaining two students say their goodbyes to Lilly before taking their cue to leave as well, leaving only the three of us."
hi "Well, I guess that's everyone."
show lilly basic_displeased
with charachange
li "I hope we don't have to do anything like that again."
hi "Working past schooltime?"
show lilly basic_concerned
with charachange
li "Indeed. The class's plans this year were ambitious. Maybe too ambitious."
show hanako emb_smile
with charachange
ha "The stalls look nice, though."
hi "She's right, it shows that a lot of work's gone into them."
show lilly basic_ara
with charachange
li "My my, I'm sure a lot of us would be glad to hear that. At least now there's not much work to do until the festival itself."
show hanako basic_smile
with charachange
ha "Umm… It's getting pretty late. Should we go?"
show lilly basic_smileclosed
with charachange
li "That's probably a good idea. Are you going back to the dorms as well, Hisao?"
hi "Yeah, I guess I'll tag along."
scene bg school_gardens2_ni
with locationskip
"The nighttime lighting really makes the gardens look quite different. Compared to the usual look of lush greenery, things are much more calm."
"Being that it's so late, the lack of students around probably helps. The odd one or two can be seen scurrying to and from the dorms trying to eke the most out of their approaching curfews, but no more."
"All that can be heard is our footsteps, in addition to Lilly's cane regularly gently tapping the ground in front of her."
"It's nice to finally be able to relax a bit after the mad rush during school."
"Without even noticing it, I let out a small yawn."
show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter
li "Tired?"
hi "Yeah. Still getting used to the flow of things, I guess."
hi "The… uh… thing… with Shizune took me kind of off guard, though."
"I grit my teeth a little at the candid mention of their rather public spat. That said, I do want to sort out what in the world was behind it."
show lilly cane_displeased_ni
with charachange
li "Ah… about that…"
li "I'm sorry about it being so public. Shizune and I… go back some ways."
label en_A24c:
"Her voice seems slightly irritated as she remembers Shizune, and on second thought, possibly my part in the proceedings."
show lilly cane_listen_ni
with charachange
li "I would appreciate it if you didn't help her. The last thing she needs is urging on."
"Well, that confirms my suspicions at the time. I pissed her off."
"That said, while I may have inadvertently fed her to the dogs, I couldn't know and therefore am in no position where I'd need to apologize."
"A couple of minutes of strained silence pass by between us, Hanako's eyes darting left and right."
"Giving up on the prospect of any kind of apology, Lilly surrenders the fight and changes the topic."
label en_A24d:
"Her voice seems slightly irritated as she remembers Shizune, obviously unwilling to discuss it any further."
show hanako basic_distant_ni
with charaenter
"I glance to Hanako for her views on this, but her expression is, unsurprisingly, evasive and difficult to read."
"Either way I guess her apologizing for it is something, even if my curiosity goes unanswered."
label en_A24e:
show lilly cane_weaksmile_ni
with charachange
li "I'll be glad once the festival is over, in any case."
"The change of topic's welcome, clearing the thickening air quickly."
hi "I can imagine. My old school's festivals were a lot more low-key than this."
show lilly cane_smileclosed_ni
with charachange
li "Yamaku stresses the idea of a school community, so the staff likes to make our festivals and such special occasions."
hi "And yet the students are the ones who do the work. What an unfair world."
show lilly cane_giggle_ni
show hanako emb_emb_ni
with charachange
"Hanako and Lilly both chuckle in agreement, savoring the fact that none of the staff are around to hear our grumbling."
show lilly cane_smile_ni
show hanako basic_smile_ni
with charachange
li "I suppose coming from a strict all-girls school helped me a bit with Yamaku. Compared to there, Yamaku is much more relaxed."
"That'd go a way towards explaining her well-bred speech and behavior, in any case."
scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip
"As we come up to the dormitories, it eventually comes time to leave for our respective rooms."
hi "See you Lilly, Hanako."
"The two both give polite nods before setting off to the women's dorms, just next to the guys'."
stop music fadeout 4.0
hide lilly
hide hanako
with charaexit
"As is to be expected of such an arrangement, there's a staff member casually patrolling around outside to prevent any nighttime shenanigans."
"Walking past him, I quickly stretch my arms and rub my neck, both quite sore after having worked on the floor for so long, before walking to my room."
"It feels good to actually have direction, though. After so long in the hospital, the everyday facts of studying, homework and teachers seem almost a blessing."
"I guess if things continue like this, my time at Yamaku might turn out okay."
label en_A24a:
scene bg school_dormhisao_ni
with locationskip
"Adhering to the nurse's nagging voice in the back of my head, I set my alarm clock to wake me up early enough to go jogging again."
"I made a promise and I'm going to keep it. Besides, Emi is bound to rat on me if I don't show up."
"But it's not all that bad."
$ suppress_window_after_timeskip = True
scene black
with shuteye
label en_A24b:
scene bg school_dormhisao_ni
with locationskip
"I'm feeling tired so I set my alarm clock to wake me up as late as I can afford, while still making it to the first class."
"The nurse's voice is almost nagging in the back of my head about morning jogs. I make a resolution to make up for it by going for a walk after school tomorrow."
"Emi won't care either way, I bet."
$ suppress_window_after_timeskip = True
scene black
label en_A25:
window hide None
scene black
with dissolve
play sound sfx_alarmclock
scene bg school_dormhisao
with openeye
window show
"My morning alarm goes off, and I flail about uselessly for a while until I remember that I'd decided to give morning runs another shot."
"I don't know if this was my greatest idea, but I'm determined to keep going."
"This is about my health, after all."
"Sure, things haven't been great lately for me, but that hasn't made existence so intolerable that I'm not going to try everything I can to stay healthy."
"Besides, it's all about asserting some kind of control over this thing, right?"
"If I can manage that, well, I can manage anything."
"At least that's what I keep telling myself."
scene bg school_track
with locationskip
play ambient sfx_emirunning fadein 0.3
"Once again, it would appear that I'm not alone in my run."
"Emi has apparently been here for some time."
"It looks like she's already worked up a good sweat."
"Just when the hell does she come down here, anyway?"
stop ambient fadeout 0.3
show emi basic_grin_gym at center
with charaenter
play music music_emi fadein 0.5
emi "Oh, it's you!"
show emi basic_closedgrin_gym
with charachange
emi "I'm surprised to see you again!"
hi "Why's that?"
show emi basic_grin_gym
with charachange
emi "Well, not many people actually manage to come back for a second try."
show emi basic_annoyed_gym
with charachange
"She frowns, seemingly annoyed by a passing thought."
emi "Like the rest of the track team, for instance."
emi "Still, it was only supposed to be on a volunteer basis, so it's not that big of a shock."
emi "And I guess it's pretty early in the morning…"
"A shrug, and suddenly it appears that she's forgotten what she was talking about."
show emi basic_happy_gym
with charachange
"The frown disappears entirely, and she seems to snap back to her previous train of thought."
emi "So! Come on, then!"
hi "What?"
show emi excited_proud_gym
with charachange
emi "You're here to run again, right?"
hi "Well, yes."
show emi basic_closedhappy_gym
with charachange
emi "So come on!"
scene bg school_track_on
with locationchange
"I find myself suddenly grabbed and yanked onto the track."
play ambient sfx_emijogging fadein 0.3
scene bg school_track_running
with locationchange
"Things seem to be set on mirroring yesterday's run."
"That is, I seem to be struggling, while Emi moves with an effortlessness that I find enviable."
"It's incredibly bothersome, to be so easily worn out."
"I know I should be patient, work toward things gradually, but…"
"It's difficult to stay positive about this."
"We round the track and start on our second lap."
play ambient sfx_emirunning
"Emi seems to have grown impatient keeping pace with me, and begins to pull away."
"This is where I gave out yesterday."
label en_choiceA25:
menu:
    with menueffect
    "Will I be able to do more?"
    "Go for it.":
        return m1
    "Take it easy.":
        return m2
label en_A25a:
stop music fadeout 10.0
"I let Emi go with her own pace, and she doesn't show mercy, pulling half a lap ahead of me in an instant."
"I don't blame her."
"I mean, it's not as if I'm really putting up any sort of real fight out here, is it?"
"Instead, I'm just running at a steady pace, which is what I should be doing, right?"
"There's no need to go pushing my limits at this stage of the game."
"God, is this even worth it?"
scene bg school_track_on
with locationchange
"As we finish the second lap, I break off again."
"Emi keeps going, and it almost seems to me that she's disappointed."
"Well, that's stupid."
"I don't have anything to prove to her - come to think of it, I've got nothing to prove to myself, either."
"I'm just fine the way I am."
"And what I'm not is a runner."
"This was probably a bad idea."
"Maybe there's something else I can do instead of this."
"Getting up this early sucks, anyway. There's got to be some other way to keep healthy."
"Walking, maybe. Nice afternoon walks."
"Yeah, that sounds good. Running isn't for me."
stop ambient fadeout 2.0
scene bg school_track
with locationchange
"I wave to Emi and head back to my room."
"I'll think of something else later."
label en_A25b:
"What am I doing here?"
"Am I really just going to fold and let Emi pull ahead?"
scene bg school_track_running
with locationchange
"I speed up."
"The second lap's done quickly, and without even considering it I keep going."
"Emi looks back over her shoulder at me and grins."
show emi excited_proud_gym at twoleft
with charaenter
emi "Still going?"
hi "Wouldn't *pant* want you *pant* to think I'm outta shape *pant*"
show emi excited_laugh_gym
with charachange
hide emi
with charamoveoutleft
play ambient sfx_emipacing
"Emi laughs - without breaking her stride, no less - and speeds up even more."
"Well, if this is the way we're going to play things…"
"I increase my own pace as well."
"I can feel my lungs burning, and my legs are starting to question just what the hell I think I'm doing."
"Lactic acid screams in my muscles, but I close my ears."
"I can't let myself fall behind, because that would be a loss."
"The rational voice in my head inquires mildly just when we started playing a game."
"I'd answer it, but I'm having a lot of trouble thinking at present."
"She's so {b}fast{/b}."
"How the hell does she keep it—{w=.5}{nw}"
stop music fadeout 0.2
play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)
hide heartattack alpha
with Dissolve (0.2)
"It's like a string pulling at my chest, a choking feeling of narrowness and pain."
"Before I can think of anything else than “Oh shit,” the track disappears from under my feet."
scene bg school_track_on:
    pause 0 xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch
"I stumble, one hand shooting down to clutch at my chest, the other hitting the track to keep me from falling on my face."
stop ambient fadeout 0.2
"Emi whirls around and her eyes widen."
emi "Hisao!"
play ambient sfx_emisprinting
"She yells at me, sprinting from the other side of the track."
show emi basic_shock_gym:
    pause 0 xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright
stop ambient fadeout 0.1
emi "What's wrong?"
hi "Nngh—Nothing, just…"
play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)
hide heartattack alpha
with Dissolve (0.2)
"Keep your breathing steady."
"Calm down. Don't panic."
play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)
hide heartattack alpha
with Dissolve (0.2)
"Don't panic."
show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:
        pause 0 "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None
emi "Do you need me to get the nurse?"
show black
with shuteyefast
scene black
with None
"I close my eyes, shutting out the outside world."
play sound sfx_heartfast
show heartattack
with Dissolve (0.1)
hide heartattack
with Dissolve (0.3)
with Pause(1.0)
play sound sfx_heartslow
show heartattack
with Dissolve (0.1)
hide heartattack
with Dissolve (0.7)
"My heart struggles to regain its rhythm."
"Slowly, the pain in my chest begins to subside."
"Soon it's gone like nothing happened."
"It was… nothing? No, something happened there."
play music music_rain fadein 2.0
scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye
"I open my eyes again and glance at a very worried Emi."
hi "I think I'm fine."
"My voice sounds weird even to myself, oddly even and matter-of-fact. It makes Emi frown."
show emi sad_annoyed_gym_close
with charachange
emi "I don't think you are."
"She seems to come to a decision, and nods to herself."
show emi basic_annoyed_gym_close
with charachange
emi "Right. You're coming with me."
emi "You've got to see the nurse."
with vpunch
"Emi grabs my arm and drags me up. I feel a bit wobbly, but I refuse the shoulder Emi offers for support."
"Honestly, I'm a little ashamed by my own weakness."
"I'd really rather not have Emi concerned about me, but it seems to be too late."
"Heck, I'd really rather not have anyone concerned about my condition, though at this point, it seems to be too late for that as well."
"I'd like to be able to deal with the whole thing on my own, without being a bother to anyone else."
"While I'm wishing for things, I'd rather not have this condition in the first place."
stop music fadeout 1.0
scene bg school_nurseoffice at bgleft
with locationskip
show emi basic_shock_gym at tworight
with easeinright
emi "Nurse!"
"Emi crashes into his office without knocking, but it doesn't alarm the nurse in the least."
play music music_nurse fadein 0.5
show nurse grin at twoleft
with charaenter
nk "Good morning, sunshine. What's up?"
"Sunshine? Anyway, he calmly sips from his coffee mug but lays it down after following Emi's gaze to me looming in the doorway."
show nurse fabulous
with charachange
nk "Hisao? What brings you here?"
show emi excited_sad_gym
with charachange
emi "We were running and he stumbled over and started grabbing at his chest and I thought I'd come get you and make him wait there but he said he was okay but then I thought you should see him anyway and—{w=1.5}{nw}"
show nurse concern
with charachange
nk "Easy there, Emi. Calm down."
show nurse neutral
with charachange
nk "Hisao, what happened?"
hi "I don't know. We were running, and then my chest started hurting like that time before, but it went away after a few seconds."
hi "It was just a flutter or something."
show nurse concern
with charachange
"The nurse frowns, as if to say that “just a flutter” is some kind of oxymoron."
nk "I didn't mean quite this when I suggested to get some exercise. You've got to be more careful, Hisao."
hi "I was being careful, I just…"
"Come to think of it, “I just got into a race with a member of the track team” doesn't seem as well reasoned as I thought it would."
nk "You just what?"
hi "Er… that is…"
hi "I was racing Emi."
nk "Emi, is this true?"
show emi basic_hes_gym
with charachange
"Emi fidgets, looking adorably contrite."
emi "Um, well…"
show emi basic_closedsweat_gym
with charachange
"Finally she can't seem to bring herself to say it aloud, and merely nods."
"The nurse sighs and rubs at his forehead with one hand tiredly."
nk "Emi, you've got to be more sensitive to the limits of others!"
nk "I don't know if he told you, but Hisao has a bad heart, and getting him to race you was incredibly irresponsible."
hi "Er, actually I started it."
"The nurse is stunned by my statement."
nk "You WHAT?"
hi "We were just running, and Emi started to pull away, and so I uh, sped up to catch her."
"The nurse stares at the ceiling, mutters a prayer for patience to some god or another, and looks back down at the both of us."
nk "So you're {b}both{/b} stupid."
nk "That's a comfort, I guess."
nk "Now come on, Hisao. I've got to make sure your heart's not going to explode or something."
show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove
hide emi
with None
"I dutifully obey and follow him to the adjacent room where we ascertain that I am, in fact, not going to keel over and die."
nk "So how does it feel?"
hi "I don't know. Nothing much. Tired, but it might be just from the exercise."
nk "You should stay here for a few hours and rest, and we'll see how you feel after that."
"I am not going to object, so I lie down on the infirmary bed."
stop music fadeout 2.0
scene bg school_nurseoffice at left
with shorttimeskip
"A thoroughly miserable Emi comes in after getting an earful from the nurse in the other room."
"I couldn't hear what he said through the closed door, but I'm sure it wasn't pleasantries."
show emi sad_depressed_gym at center
with charaenter
play music music_dreamy fadein 0.5
emi "Look, I'm really, really sorry."
emi "I should've been more careful."
hi "Hey, you didn't know. It's not your fault."
"She looks awfully down and sorry, and my reassurances don't do anything much to cheer her up."
emi "I want to make it up to you."
"Again with that decisive nod."
show emi sad_shy_gym
with charachange
emi "So you have to come to lunch with me."
emi "I'll bring it for you, okay? Something really really good!"
"I start with a “You don't have to…” but then shut up and just nod at her when I see her face."
show emi excited_proud_gym
with charachange
emi "Good!"
show emi basic_grin_gym
with charachange
emi "We meet on the roof."
hi "We?"
show emi basic_closedgrin_gym
with charachange
emi "Yep! The weather's nice now, so the roof's a great spot for lunch, you know."
hi "I see."
show emi sad_shy_gym
with charachange
emi "You'll come, right?"
emi "You wouldn't deny me the chance to make it up to you?"
hi "Of course not."
show emi excited_joy_gym
with charachange
emi "Great! See you there!"
hide emi
with charaexit
with shorttimeskip
"I stay afloat somewhere between asleep and awake, feeling completely drained."
"Not only my body, but all of me is limp and paralyzed, apart from my senses."
"I swallow with difficulty and then try to lie as still as I can, which in this state is not a very hard thing to do."
"The nurse is shuffling around on the other side of the curtains he drew to give me privacy. I can see his shadow shifting about in the sunlight."
"He has opened the window of his office. It's windy outside."
"The clean white curtains flutter in the breeze in a heavy, lazy motion, like waves. Light sifts through them slowly, half absorbing into the fabric."
stop music fadeout 5.0
scene darkgrey
with shuteye
"I close my eyes. The breeze on my face feels like the soft fabric of the curtains."
"I listen to the sound of my heartbeat for a moment, trying to shut out the sound of the nurse tapping away on his computer, and my own heavy breathing."
"It's steady."
"Damn it, not even a week and I end up like this again. I really screwed up this time. Should've known better than to play the half-baked sports star in front of a real one."
"And why did I try to act brave, like that heart flutter was no big deal, even when it was obvious that it was?"
"It was just a reflex, to push it away, to keep it inside."
"I didn't want it to happen."
"I didn't want Emi to see it."
"Aaah…"
"Stupidstupidstupid."
"I have to be more careful, or I will end up in the hospital again, or worse."
"…"
"That's my final thought before I give in to the tiredness."
scene black
with Dissolve(1.0)
window hide Dissolve(2.0)
with Pause(2.0)
scene bg school_nurseoffice at left
with openeye
window show
play music music_daily fadein 6.0
"I fell asleep. For how long? What time is it?"
"I'm feeling a little lightheaded and I keep blinking compulsively."
show bg school_nurseoffice at center
with charamove
"Pushing the curtain aside, I squint my eyes against the unfiltered light pouring in from the window. The texture of the canvas feels nothing like the wind did before."
"The nurse looks up from his work, sitting exactly where he was before."
show nurse fabulous at center
with charaenter
nk "How are you feeling?"
"I can't really tell, so I don't answer anything. I'm feeling kinda groggy from falling asleep at such a weird time, hopefully I don't look too weird."
hi "What time is it?"
"Me croaking the question to gain some orientation. The nurse looking at his wristwatch before answering."
"Things seem to happen in slow motion."
show nurse neutral
with charachange
nk "Quarter past ten."
"I try to think for a moment what that means but I'm not really sure."
show nurse concern
with charachange
nk "You didn't answer my question, Hisao."
hi "Oh. Fine."
show nurse neutral
with charachange
nk "Climb down from that bed then, and let’s see how you are doing. Don’t…"
$ renpy.music.set_volume(0.5, 0.2, channel="music")
show bg school_nurseoffice as dizzy_bg behind nurse:
    pause 0 xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate 6 zoom 1.05 alpha 0.5
show nurse neutral as dizzy_fg:
    pause 0 xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate -4 zoom 1.05 alpha 0.5
with Pause(0.4)
show bg school_nurseoffice as dizzy_bg behind nurse:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0
show nurse neutral as dizzy_fg:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0
"I try to do exactly that, only to sway dizzily when I move too fast. The nurse moves to support me by an arm and sighs."
show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange
nk "…stand up too quickly, is what I was going to say. Just sit there, I’ll check your pressure to make sure."
$ renpy.music.set_volume(1.0, 2.0, channel="music")
"My good intentions sure lasted for a long time. I shut up, embarrassed with myself, while the nurse gets busy with an old-fashioned contraption and my arm. After a couple of minutes, he puts it away, looking neither pleased nor unhappy."
show nurse neutral
with charachange
nk "You’re all right. Head stopped spinning?"
hi "Yeah."
nk "Good. And how are the contents doing?"
show nurse concern
with charachange
nk "You didn’t show very good judgment out there, Hisao."
"I swallow the retort I was going to make. It’s what I was thinking myself, but hearing it stated by somebody else makes me want to protest."
"What he’s saying is not pleasant to hear. Doesn’t make him any less right."
hi "No, sir."
show nurse neutral
with charachange
"He nods, still looking as neutral as he was before."
"It would be easy to be angry at him if he said “Told you so” or something, but he doesn’t."
nk "I can try and help you to keep your health, but ultimately the last call lies with you. Hopefully this little episode will be something that’ll remind you of that."
show nurse fabulous
with charachange
nk "Here, a note for your teacher. To avoid an interrogation."
"I take the slip of paper he's offering and then make my leave as I can't think of anything else to say, nor even really want to."
show nurse neutral
with charachange
nk "Stay out of trouble, you hear me? I don't think it was anything but a scare, but next time could be different."
"I hear you."
scene bg school_nursehall
with locationchange
stop music fadeout 4.0
"There is some way to get to the school building straight from the auxiliary building, but I'm not keen to find out and possibly get lost, so I go out from the exit that I know works."
scene bg school_courtyard
with locationchange
"I stop at the stairs of the auxiliary building, deliberating for a moment between going to the dorms to get my books and stuff and going straight away to the class."
"The sun stings my eyes, so I head towards the dorms."
label en_A26:
window hide None
scene black
with dissolve
scene bg school_dormhisao
with openeye
with Pause(0.2)
scene bg school_dormbathroom
with locationskip
window show
"I wake up and take a hot shower."
label en_A26a:
scene bg school_dormhisao
with locationskip
"Back in my room, the first thing I see is the familiar row of medication bottles lined up on top of my dresser, and it makes me depressed, as usual."
"It's annoying. I thought I was okay. I thought I had made my peace with this thing, gotten over it."
"But what I really did… I allowed myself to forget that I have a problem. Being here really reminds me of the reality, and trying to fight against it just hurts."
"Reflecting on it is only going to do so much. I've done this before, for months. It seems like it's time to get over it."
"If I allow myself to forget that my life is definitely not going to be as long as those of others, I won't get anywhere."
"My life may be different from others. But it is a life in progress."
"That is how I'll rationalize it."
"I down the usual handful of pills, trying to push the sudden dreary feeling out of my head. Then I prepare to head out to class early, as usual."
scene bg school_dormhallway
with locationchange
"As I step into the hallway, I notice Kenji coming around the hallway corner, stealthily making his way over to his own room with a large bag. As he sneaks past me soundlessly like a ninja hiding in plain sight, I call out to him."
hi "Hey."
show kenji neutral at center
with charaenter
play music music_kenji fadein 0.5
"He jumps at the sound of my voice."
ke "Oh, hey, man. I didn't notice you there. I'm really tired."
"I think it's more like he didn't see me, but that's not the issue."
hi "Where have you been this early? Shopping?"
show kenji tsun
with charachange
ke "Nah, I wasn't shopping. Sometimes I have to visit… the math teacher. Yeah, I figured it would be a good idea to find out when the next exam is, since he tells you in advance if you want."
hi "So then, what's in the bag?"
show kenji neutral
with charachange
ke "I thought I'd go shopping while I was outside. I need supplies to continue the fight against the vast feminist conspiracy."
hi "Uh, okay."
hi "I thought you didn't go outside."
show kenji happy
with charachange
ke "I wear a hat now."
"I decide to not point out that he is not wearing a hat."
"An awkward silence settles between us and then Kenji breaks it by pushing his door open slowly, releasing a creaking sound into the air that only makes the moment seem more awkward. He sets the bag down inside his room and then closes the door."
hi "I'm surprised you went out of your way to find out a test date. Trying to take advantage of an opportunity to study is pretty diligent."
show kenji tsun
with charachange
ke "I never study."
hi "Oh…"
show kenji neutral
with charachange
ke "I just wanted to know when the next test day was. I'm still going to take it, duh. I need to know so I know what day I can't afford to skip class. He usually sends out updates on that crap by phone, so I had to step out and check up on it."
hi "And why do you have to go out, when you can get it on your phone?"
show kenji tsun
with charachange
ke "I don't carry a phone."
hi "What do you mean you don't carry a phone? You mean you just leave it at home?"
show kenji neutral
with charachange
ke "Nah, I don't use phones. I don't have a phone. Phones. I have no phone."
hi "Why don't you have a phone? How can you not have a phone? No phone at all? No phone?"
show kenji tsun
with charachange
ke "I just don't like phones. Actually, I'm kind of scared of them. I don't know why. I think it's some kind of repressed trauma."
ke "But, basically, when I hear a phone, I get nervous. It's my darkest secret."
show kenji neutral
with charachange
ke "I have two theories on it: either I have some fear of receiving some undefined, ominous, life-altering doom call, or I was beaten with a phone in the past. Beaten so badly I can't remember it."
hi "Beaten in the head."
show kenji tsun
with charachange
ke "Well, where else could I get beaten with a phone that would make me unable to remember it? The ass?"
"Unexpectedly logical. I feel very depressed now. Sensing this conversation is more or less over, Kenji opens his door again and prepares to head inside."
show kenji neutral
with charachange
ke "Yeah, I'm going to sleep, dude. Have a good one."
hi "Class is going to start in like twenty minutes."
show kenji tsun
with charachange
ke "I already did something today. Too tired to go to school."
show kenji happy_close
with characlose
ke "Hey, you need some lip balm? I accidentally bought two because I thought the store had started selling individual double A batteries."
hi "Thanks but no thanks."
label en_A26b:
scene bg school_dormhallway
show kenji happy_close at center
with None
stop music fadeout 0.3
play sound sfx_doorslam
show kenji tsun_close
with vpunch
"The door down the hall opens with a crack as it swings forward from being pushed opened too strongly and crashing against the wall. The sound is followed by a peal of bubbly laughter, and I instantly know who it is."
play music music_comedy fadein 0.3
show misha perky_smile at center  behind kenji
show shizu basic_normal2 at center  behind kenji
with zoomin
show shizu basic_normal2:
    easein 1.0 tworight
show misha perky_smile:
    easein 1.0 twoleft
show kenji tsun_close:
    pause 0 0.25
    easeout 0.5 alpha 0.0 offscreenleft
with Pause(1.0)
hide kenji
with None
play sound sfx_impact2
"At the noise, Kenji disappears into his room like a ninja, slamming the door shut just as Shizune and Misha walk over, the former taking small, efficient steps towards me while the latter more or less bounces off the walls."
show misha hips_smile_close at twoleft
with characlose
"I try to do the same as Kenji, but it's too late. Misha puts her foot between my door to prevent me closing it, so I have no other choice but to let them in."
scene bg school_dormhisao
with locationskip
show shizu behind_smile at center
with charaenter
shi "…"
show shizu behind_smile at tworight
with charamove
show misha hips_grin at twoleft
with charaenter
mi "Hi, Hicchan~! Hi~ hi~!"
hi "Hi."
hi "What are you two doing here?"
"I wonder if the pause between those two sentences was politely long enough."
show shizu basic_normal
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Hicchan, that's rude~! We came to pick you up!"
show misha hips_smile
with charachange
mi "Did you think we thought you were going to escape and came to make sure you didn't? Surely not, Hicchan~!"
hi "Hey, I didn't say that that's what you were here for."
"But now I know it's exactly what they are here for."
show misha sign_smile
with charachange
mi "It's time for student council work, yes it is~!"
show misha hips_grin
with charachange
mi "Aren't you happy, Hicchan, to be able to help the whole~ school~! You are like, a hero~! The future generations will tell stories of this day!"
"Interesting. I didn't think joining the Student Council would be a heroic deed worthy of Hercules."
hi "Well… I guess I did promise so…"
show shizu adjust_happy
with charachange
stop music fadeout 7.0
"I've neglected Shizune, and only now do I notice her in the corner of my vision, peering around my room over my shoulder, her analytical eyes darting from object to object…"
"This is kinda intrusive, the feeling of being exposed crawls in my balls. Luckily I don't have dirty laundry on the floor or anything like that."
show shizu behind_smile
with charachange
shi "…"
show misha perky_confused
with charachange
mi "Hm~? What is it, Shicchan?"
show misha hips_smile
with charachange
mi "Yeah, this is Hicchan's room~! We haven't seen it before, I didn't even realize!"
show misha hips_grin
with charachange
mi "It's kinda plain, but Hicchan hasn't had time to decorate it yet, isn't that so~?"
show misha sign_smile
with charachange
mi "What are those?"
"She points at my collection of medications on the night table."
label en_choiceA26:
menu:
    with menueffect
    "I don't really want to talk about it with these two."
    "Try to dodge the subject.":
        return m1
    "Kick them out of my room.":
        return m2
label en_A26c:
hi "It's nothing."
show shizu basic_normal2
with charachange
"I quickly step in front of them, trying to hide the stuff behind my back. Shizune takes a step back, looking suspicious, but it's an expression not without concern."
"I hope if I avoid it, she'll understand that I don't want her to keep prodding me about it."
show shizu behind_blank
with charachange
shi "…"
show misha perky_confused
with charachange
mi "Really? What are you hiding, Hicchan~?"
hi "Nothing."
show shizu basic_normal
with charachange
shi "…"
show misha sign_confused
with charachange
mi "Is that so~?"
"I realize I can't really squirm my way out of this. They are nosy by nature and hiding it is just going to pique their curiosity more."
hi "Yeah okay, it is {b}something{/b}, but I don't really want to talk about it, okay? Not… yet."
hi "Can we just put this aside for now?"
show misha perky_smile
with charachange
"As Misha translates, Shizune stares at me hard with her eyes focused and analytical as ever, peering at me curiously over the rims of her glasses."
"Her fingers press against each other thoughtfully, as if she's weighing the value of pursuing this further than necessary against the insult of disrespecting my wish."
"Her expression finally melts into a slight smile and she signs something to Misha."
play music music_dreamy fadein 2.0
show shizu adjust_happy
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Okay~! Then, we'll wait, and become better and better friends, and one day when you feel like it, you can tell us about it~!"
"Both of them smile widely at me, and I feel shocked and a little stupid about being like this."
"They are not stupid, and probably can at least halfway guess what's going on with me. And…"
"Such simple, kind words. I feel relieved that they don't think any worse of me even if I'm like this. Even if I'm not like the rest here. Even if I can't be at ease about it."
"Seems that behind the obnoxious, mischievous acts, both of these girls are really kind and good people. That's what I think."
hi "Thanks."
hi "So, you want me to help you out today, right? Since I'm one of you now?"
show misha hips_grin
with charachange
mi "Yup~!"
hi "After class?"
show misha sign_smile
with charachange
mi "No no no~! Now!"
hi "Now? But what about class? You are going to skip again?"
show shizu adjust_smug
with charachange
shi "…"
show misha cross_laugh
with charachange
mi "Hahaha~! It's for the common good, so we sacrifice our math lessons, and maybe the social studies too~!"
hi "Well, I guess I'm fine with it."
show shizu behind_smile
with charachange
shi "…"
show misha sign_smile
with charachange
mi "Awesome, Hicchan~! You said it, okay? Remember: “I'm fine with helping out~,” that's what you said, right~?"
hi "Yeah."
"That tone… I suddenly regret saying it."
show shizu basic_normal2
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Okay~! Are you ready to go then? We can go to the office together~!"
hi "No. You're probably going to make me carry all your stuff for you or something."
show shizu adjust_happy
with charachange
shi "…"
show misha perky_smile
with charachange
mi "Don't be silly, Hicchan."
show misha hips_smile
with charachange
mi "We've never walked to school together, Hicchan~."
"I almost want to ask why we would, but then it dawns on me. The both of them consider me their friend, like Misha said before. And they want to become better friends with me, even."
"It's weird, I've never really thought about them that way. Or any of the people I've met so far this week. Is it really so easy?"
"Just like that…"
hi "Okay, let's go, then."
show shizu behind_smile
with charachange
"Shizune grins craftily and puts her hands behind her back."
show misha hips_grin
with charachange
mi "Hahaha~! That's great, Hicchan~! Okay, okay, but first~! You had a really great idea, Shicchan liked it a lot… So~! it's time for a game!"
hi "Oh no."
show misha hips_smile
with charachange
mi "Shicchan is holding a 1000-yen note in one hand, Hicchan~! If you guess which one, you can have it! If you don't…"
show misha hips_grin
with charachange
mi "You're carrying all our books to school~! Right, Shicchan~? Right~!"
"She and Shizune exchange nods."
show misha sign_smile
with charachange
mi "Okay, Hicchan~! Get ready~!"
stop music fadeout 7.0
scene bg school_courtyard
with shorttimeskip
"Carrying three bags instead of one, I think about the day that's ahead of me. Of us."
"I can see students walking back and forth through the courtyard, probably in preparation of their own projects."
"The festival is practically here. That means there are only two possible reasons that my help is required."
"Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."
"Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."
label en_A26d:
play music music_rain fadein 4.0
"Even so, they have really crossed the line this time. Nosy annoyances."
hi "It's nothing."
show misha perky_smile
with charachange
mi "Really~, Hicchan? It doesn't look like it's nothing to me."
show shizu adjust_smug
with charachange
shi "…"
show misha hips_smile
with charachange
mi "What a long line of bottles, right~? Right~! What are all of those, Hicchan?"
hi "Just a few things."
show shizu basic_normal2
with charachange
shi "…"
show misha perky_confused
with charachange
mi "That looks like a lot more than “just a few things”…"
"I can't fault either of them for being this way. Misha's just talking for Shizune, and Shizune is just curious by nature. Still, I wish the two of them would stop digging and take the hint. But Misha wouldn't pick up on it, and Shizune can't."
"Because of that, they keep pressing on."
hi "It's really none of your business."
hi "Shouldn't you be leaving? A man's room is private, you know."
"Shizune seems to take that as a challenge."
show shizu behind_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "What does that mean, Hicchan? When someone sees something interesting, their first instinct is to ask what it is, that's obvious. What's wrong with that?"
hi "Because, like I said, there's nothing to see."
show misha perky_confused
with charachange
mi "Hicchan, I think Shicchan is just concerned."
hi "What I have in my room isn't any of your business, that's all."
show misha sign_confused
with charachange
mi "But…"
hi "Damn it! Sometimes, I wish you two would just stop playing around so much. It's not funny all the time. You know that, right?"
"I say it way more strongly than I meant to, almost yelling straight at Misha's face. She flinches and freezes in mid-sign, and even Shizune reacts to it even though she didn't hear me."
stop music fadeout 6.0
"I guess my angry face said all that needs to be said to her."
show misha perky_sad
show shizu behind_blank
with charachange
"After Misha slowly finishes the translation, the girls look at each other regretfully."
show shizu behind_sad
with charachange
shi "…"
mi "Okay, Hicchan, we'll leave you alone."
"It's the first time I've heard Misha speak without that familiar lilting up-and-down quality in her voice. It feels so strange to hear, and I want to apologize, but they have already turned to leave."
"As the silence settles in, I regret what I said more and more."
hide shizu
hide misha
with charaexit
"The girls leave quietly, and after a while of standing in my room I dress up and follow after them."
label en_A26e:
show kenji tsun_close
with charachange
ke "Whatever, man."
stop music fadeout 2.0
hide kenji
with charaexit
"He swiftly enters his lair, finally letting me go to the class."
label en_A27:
scene bg school_hallway3
with shorttimeskip
"The halls are quiet as the courtyard was, naturally so since everyone is in class. I knock lightly at the door of 3-3 and push open the door when Mutou calls from the other side."
scene bg school_scienceroom
with locationchange
hi "Sorry I'm late."
"Fifteen pairs of eyes turn to me."
show muto irritated at center
with charaenter
mu "Good morning, Nakai."
"Mutou seems to be somewhat confounded by my coming in late, as if I interrupted his flow or something."
"Judging from the rambling lectures his classes tend to be, that might be the case."
"I pass him the note the nurse gave me. Mutou takes it with a nod and reads it quickly."
show muto normal
with charachange
"He lifts his eyebrows and gives me a kind of a stern look but doesn't say anything, just nods solemnly again."
"I shrug and he gestures at me to run along so I naturally do."
label en_A27a:
scene bg school_scienceroom
show muto normal at center
with None
hide muto
with charaexit
"Only two pairs of eyes remain keenly following me as I walk to my seat."
"I'm not surprised in the least when I feel Misha's fingernail prickle through my shirt about fifteen seconds after seating myself."
show misha perky_smile_close at offscreenleft
with None
show bg school_scienceroom at bgright
show misha perky_smile_close at Transform(xalign=-0.3) 
with charamove
play music music_another fadein 2.0
mi "Psst! Where were you?"
hi "None of your business."
"I know this is probably the worst answer I can give as it only serves to pique their curiosity, but I have no energy to come up with elaborate cover stories right now."
show misha perky_confused_close
with charachange
show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove
"However, Misha backs off. She's unexpectedly fast to give up today."
"…"
"In a minute, she's back at poking me with her finger."
show misha hips_grin_close
with None
show bg school_scienceroom at bgright
show misha hips_grin_close at Transform(xalign=-0.3) 
with charamove
mi "Come on, tell us! Shicchan is very interested too!"
"It was just my wishful thinking. She just talked about it with Shizune, probably devising ways to get me to spill the beans."
hi "No."
show misha perky_sad_close
with charachange
show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove
"She retreats to negotiate again."
show misha sign_smile_close
with None
show bg school_scienceroom at bgright
show misha sign_smile_close at Transform(xalign=-0.3) 
with charamove
label en_choiceA27:
mi "As a member of the Student Council, it's your duty to tell us why you are skipping class! Especially if it's something fun fun fun~!"
menu:
    with menueffect
    "Yeah, I sure was having fun fun fun at the nurse's office…":
        return m1
    "I don't want to talk about it, okay?":
        return m2
label en_A27b:
stop music fadeout 4.0
"God damn it. She just doesn't know when to stop."
hi "Yeah fine. Whatever. I'll tell you. I was having a great time."
hi "I had a heart attack first thing in the morning and then hung out with the head nurse for a few hours for kicks."
hi "Best morning of my life, I gotta tell you."
"I'm trying to imitate her ridiculous lilting speech while keeping my voice so low that nobody else hears me. The words come spitting out of my mouth."
show misha perky_confused_close
with charachange
mi "Hicchan, you had a what? Seriously?"
hi "Just drop it. You heard me."
show misha perky_sad_close
with charachange
mi "But Hicchan, this is important!"
hi "No, really. Leave me alone. We're in the middle of the class, too."
show misha sign_sad_close
with charachange
mi "But Hicchan!"
"Misha sounds concerned, or maybe panicky. I wonder if she realizes herself that it wasn't the best of ideas to be so damn intrusive."
"…"
"I let her simmer in her own juices for a while before replying. It won't translate to Shizune but I don't care."
hi "Piss off, Misha."
hi "And tell Shizune to do so too."
"As the words leave my mouth, I immediately regret saying them, but it's not like I can take them back any more."
show misha perky_sad_close
with charachange
show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove
hide misha
with None
"To my partial surprise, Misha actually shuts up though I don't bother checking if she passes the message to Shizune. Doesn't matter either way."
"Mutou ends his class in some generic talk about the festival two days from now."
label en_A27c:
hi "Give up. I'm not going to tell."
show misha hips_grin_close
with charachange
mi "Is that so~?"
hi "Yeah."
show misha perky_confused_close
with charachange
"She thinks about this for a moment."
show misha hips_frown_close
with charachange
mi "That's stingy, Hicchan~!"
"I can hear the pout in her voice, disappointed and downcast."
show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove
"She retreats again for a moment to negotiate with the brainy half of the dynamic duo, before returning."
show misha hips_smile_close
with None
show bg school_scienceroom at bgright
show misha hips_smile_close at Transform(xalign=-0.3) 
with charamove
mi "I think we should have lunch together and discuss more about this… Shicchan says."
show misha hips_grin_close
with charachange
mi "It's our treat."
show misha sign_smile_close
with charachange
mi "Besides, you need to make up for not being there in the morning and we need help with the work~!"
"The other students around us are starting to give us looks, probably because Misha is leaning so much over her desk that she's almost bumping heads with me. Her curly hair brushes my neck."
"It smells like shampoo and very much like whatever she puts in there to make it go like that."
"I think the girl in front of me is trying to eavesdrop. Hope nobody is getting the wrong idea about this, though I'm not really sure how it would be possible to get any other kind of idea."
"Luckily Mutou stays oblivious, or deliberately ignores Misha. So far."
"I can't really win this one, can I?"
label en_choice2A27:
menu:
    with menueffect
    "I promised to eat with Emi too, but I can't be in two places at the same time."
    "I'll go to the lunch with Emi and her friend.":
        return m1
    "I'll go with Shizune, after all I'm in the Student Council now.":
        return m2
label en_A27h:
hi "Sorry, I can't. I promised to have lunch with someone else already."
show misha perky_confused_close
with charachange
mi "Eeeh? Who? Is it a girl~?"
hi "Yeah…"
show misha hips_grin_close
with charachange
"Her giggle compels me to quickly follow with something so she doesn't get the wrong idea."
hi "It's nothing like that! It's… a bit complicated."
show misha perky_smile_close
with charachange
"Complicated… yeah, that's what my life is, despite already setting into a daily routine of school life."
"All things must be put into a new kind of perspective in this second life, reconsidered from the point of view of this new me."
"The me with a broken heart."
hi "Also, I don't know if I can come to the council after all."
hi "Or at least for now. I have something else I need to focus on first."
"That's right. I have to rethink my priorities. This is something that has swirled around in my head since the nurse gave me that speech. I really can't afford to pretend I don't have this condition."
"I'm surprised that I can think so analytically, but I'll go with the flow for now."
hi "I promise I'll explain properly later, but not now, okay? Please tell Shizune I'm sorry for letting her down."
show misha perky_confused_close
with charachange
mi "If you say so, Hicchan."
"She sounds surprised, and serious, which I don't think I've ever heard Misha to be before."
show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove
hide misha
with None
stop music fadeout 3.0
"Misha luckily understands that I'm serious, a stroke of luck that I could tell what I mean so clearly even she got it. She retreats to translate our discussion to Shizune."
"Neither of them talk to me after that."
label en_A27i:
hi "Fine, I'll come with you, but get off my back for the rest of the class, okay?"
show misha hips_grin_close
with charachange
mi "It's a deal, Hicchan~!"
stop music fadeout 2.0
show bg school_scienceroom at center
show misha hips_grin_close at offscreenleft
with charamove
scene bg school_scienceroom
with shorttimeskip
play sound sfx_normalbell
with Pause(7.0)
play ambient sfx_crowd_indoors fadein 0.3
scene bg school_hallway3
show crowd
with locationchange
"On the way to the student council room, I can see students walking back and forth through the halls, probably in preparation of their own projects."
"The festival is practically here. That means there are only two possible reasons that my help is required."
"Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."
"Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."
stop ambient fadeout 1.0
label en_A27d:
scene bg school_scienceroom
with locationskip
"For a change, I'm not among the first ones to come to morning class."
"Instead, almost everyone else seems to be here already. I recognize most of my class by their faces by now, though the names escape me still."
label en_A27e:
scene bg school_scienceroom
with shorttimeskip
play music music_normal fadein 3.0
"The class goes on lazily. I think I'm starting to get into the rhythm of the school."
"I have even stopped worrying about taking notes and being overtly attentive. The first days, I was pretty high-strung in class."
"Mutou finishes his lecture about electricity early, but continues without a pause about the festival."
show muto normal at center
with charaenter
mu "So, as you know, the festival is on the day after tomorrow. I hope everyone's projects are going to be successful this year."
show muto smile
with charachange
mu "Have a good time, but also come Sunday, please keep the meaning of this festival in your minds…"
mi "Games and fried food!"
"Everyone bursts out in laughter, and so do I."
show muto irritated
with charachange
mu "Yes, thank you Mikado."
show muto normal
with charachange
mu "But what I meant was more the—{w=.5}{nw}"
play sound sfx_normalbell
"The remainder of his sentence is buried beneath the ring of the lunch bells, and everyone starts packing their things."
"Mutou deliberates for a moment, but since almost nobody seems to pay attention any more, he gives up and sits down."
stop music fadeout 2.0
scene bg school_hallway3
show crowd
with locationchange
play ambient sfx_crowd_indoors fadein 0.3
"It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."
label en_A27f:
scene bg school_scienceroom
with shorttimeskip
stop music fadeout 2.0    
"Misha, and by proxy, Shizune, doesn't bother me for the entire morning."
play sound sfx_normalbell
"When the bell rings, I don't even look at the two of them as I walk out of the class."
scene bg school_hallway3
show crowd
with locationchange
play ambient sfx_crowd_indoors fadein 0.3
"It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."
label en_A28:
scene bg school_council
with locationchange
show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter
"Once inside the office, I look around and see that it's deserted."
hi "I guess this means there isn't a lot of work left, huh? Since there's no one here, and all."
show misha sign_smile
with charachange
mi "It's always like this, Hicchan~!"
"This confirms what I have thought before but have never actually been able to confirm definitively: Shizune and Misha are the Student Council. The whole Student Council."
hi "Damn. So it's true. The Student Council is really only you two."
play music music_ease fadein 4.0
show misha hips_grin
show shizu cross_wut
with charachange
"Shizune looks as if she's stuck wondering whether to be ashamed or explode with anger, and Misha is equally divided between laughing and trying to stop her."
show shizu behind_frustrated
with charachange
shi "…"
show misha sign_smile
with charachange
mi "Well, then, Hicchan, you'll be happy to know that since it's just us three, we have a lot to do! A lot~! A lot~ lot~ lot~…"
hi "That does not make me happy."
show shizu adjust_happy
with charachange
"But it seems to make Shizune very happy."
show misha cross_laugh
with charachange
mi "Wahaha~!"
show misha hips_grin
with charachange
mi "Just kidding!"
label en_A28a:
scene bg school_council
with shorttimeskip
"The work turns out to be sorting and double-checking the considerable amount of paperwork necessary for an event such as the school festival to get done."
"Bureaucracy is a mindboggling thing."
play sound sfx_normalbell
"But we manage to finish it just when the lunch bells ring."
show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter
mi "Okay~, now that we are done, we can relax a little! But not too much, we have lots more to do in the afternoon~!"
label en_A28b:
$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)
show shizu behind_smile
with charachange
shi "…"
show misha sign_smile
with charachange
mi "It's actually not that much work, Hicchan~. So~, we can afford to enjoy a little lunch first."
show misha cross_laugh
with charachange
mi "Hahaha~!"
"The two of them produce a small array of plastic containers seemingly out of thin air."
show misha hips_grin
with charachange
mi "Hm~ hm~… It's chicken cutlet with tomatoes and soybean sprouts~! Doesn't it sound delicious, Hicchan?"
mi "It was just made this morning, and it's still warm, so eat eat eat~!"
"I take one of the containers and open it. It looks nice, and certainly smells good. The fact that I'm really hungry adds to that even more."
hi "Wow, this looks great. Where did you get this?"
show shizu basic_normal
with charachange
shi "…"
show misha hips_smile
with charachange
mi "That isn't important, Hicchan!"
show misha sign_smile
with charachange
mi "There was supposed to be a stall selling lunchboxes, but the girl who was to run it suddenly said she couldn't do it. Shicchan said, “What a waste, it was a lot of work to trick Hicchan into making this~”—"
hi "Hey, what the hell…"
show misha hips_grin
with charachange
mi "…So~! Shicchan wanted to see if she could do it, but then decided not to, right, Shicchan~?"
show shizu basic_angry
with charachange
"Shizune sulks angrily, shooting Misha a displeased look. I don't think I was supposed to hear that story."
hi "This is your test food?"
show shizu behind_frown
with charachange
shi "…"
show misha sign_smile
with charachange
mi "I'm eating it too, Hicchan~!"
show misha hips_grin
with charachange
mi "And Shicchan is, too~!"
"That doesn't answer the question!"
"Nevertheless, I split a pair of chopsticks Shizune offers me, pick up a piece of cutlet, and pop it into my mouth."
hi "It's surprisingly good. I didn't expect Shizune to be such a good cook."
show shizu basic_frown
with charachange
"Shizune puts her chopsticks down to sign curtly towards Misha, who gulps down her cutlet with noticeable difficulty in order to speak for her."
show misha sign_smile
with charachange
mi "Hicchan~! Don't talk with food in your mouth~!"
hi "It's not like I enjoy doing it. Anyway, how motherly to show that kind of concern…"
show shizu behind_frown
with charachange
shi "…"
show misha hips_frown
with charachange
mi "You can't even eat right, Hicchan~! That's all it is~!"
show misha perky_sad
with charachange
"It's a stalemate. I can't eat in order to talk to Shizune, who can't eat in order to chastise me for eating the wrong way. Misha, caught in between, is in the same situation, and looks the most disheartened by how this is going."
show shizu behind_blank
show misha perky_smile
with charachange
"Either way, our food is getting colder by the second, and it wasn't piping hot to start with. Wherever this was going, it dies down pretty fast once we all realize that, and we eat."
play sound sfx_warningbell
"After a while the bell rings, but Misha makes no attempt to tell Shizune, so I'm sure they're planning to skip classes and spend the rest of the day in here again."
show shizu adjust_smug
with charachange
shi "…"
show misha sign_smile
with charachange
mi "Hicchan, do you have any plans for the festival?"
hi "No, not really. After all, I've only been here a week, what could I set up in that time?"
show misha cross_laugh
with charachange
mi "Wahaha~! Hicchan, you helped us out so much, don't sell yourself short!"
hi "Okay."
show shizu basic_angry
with charachange
shi "…"
show misha hips_frown
with charachange
mi "We're serious~!"
hi "Okay!"
"The two of them seem to get indignant over the strangest things."
show shizu adjust_happy
with charachange
shi "…"
show misha hips_smile
with charachange
mi "You're going though, right, Hicchan? You should at least see what we've ac—complished…? Everyone should be able to look at what they have done so they can fully understand their work, that's my belief~! You're no exception!"
show misha perky_smile
with charachange
mi "Hicchan, you should definitely go~! If you don't have anything planned, then maybe we can even go together~!"
show shizu adjust_blush
with charachange
hi "Do you need a hand? If there's anything you need help with, I'm fine with sticking around."
"I feel much more at ease than I did earlier; my previous concerns and fears long gone. I'd forgotten about this morning's trouble entirely until now, having fun with Shizune like this."
"Having fun with Shizune… It seems like an unfamiliar concept to think of, but, looking back on it, I've really enjoyed the moments I've spent with Shizune and Misha these past few days, in spite of everything else."
"If we might be going together, then maybe I can afford to stick around a little longer. And I guess it beats class."
show shizu behind_blank
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Really, Hicchan? Okay~! We can consider this you repaying us for the free lunch~!"
show misha cross_laugh
with charachange
mi "Great, this is great, really~ really~ great~! Shicchan was hoping to bring this up again later anyway! Ahahaha~! Wahahahahaha~!"
"That's not a free lunch at all. Normally I would be angry, or at least slightly unsettled, but my mood has improved from earlier on, so I'll let it slide."
"Helping them out turns out to consist mostly of stamping forms and making what seems like ten thousand copies apiece of fifty different budget reports."
"It's not hard, but very boring, and according to Misha, the simplest of the tasks they deal with."
"I feel myself getting more and more tired, and with that, less eager to return to class. This is especially bad because the more time I spend out of class, the harder it seems to just get up and go back."
"These two, they're a terrible influence. Terrible role models. Not that it bothers me all that much, and I'm sure no one looks up to them, but it's the principle of the thing…"
show shizu adjust_happy
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Done~!"
hi "Ah, that was fast. I'll be finished before this period's over, I think."
show misha sign_smile
with charachange
mi "No, no, Hicchan, everything is done. So, you're done, too~!"
hi "That doesn't make any sense, are you telling me this is all arbitrary and you've been keeping me here for the hell of it?"
show misha hips_grin
with charachange
mi "No~…"
show shizu basic_normal
with charachange
shi "…"
show misha perky_smile
with charachange
mi "But we have kept you long enough~! You should go back to class, Hicchan~! You can still make it for most of this period!"
hi "What about you?"
show shizu behind_blank
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Of course we're coming too, of course; we'll be right behind you!"
stop music fadeout 6.0
scene bg school_hallway3
with locationchange
"Reassured, I start heading back to class, but the period is almost halfway over, so I start thinking it would be pointless halfway there and pass the difference between this class and the next drinking juice in the hallway."
"I keep an eye on the door to the student council room, but it doesn't open. What's taking them so long? Are they busy wrapping up my share of the work? Well, it shouldn't take so long, unless there's more, and they just wanted me to leave."
"The more I think about it, the likelier it seems."
"Shizune is… well, not an idiot, but clearly, she's unable to just come out with things."
"Maybe it's because she can't talk, so it's harder for her. She has Misha, but all in all, as easy as they make it look, there's still a difference between casual speech and sign language."
play sound sfx_normalbell
"I contemplate going back there to check on them, but the bell rings, and I have to go to class."
scene bg school_scienceroom
with locationchange
"They join me a few minutes later, and the thoughts I had in my mind before slip away in the routine of school life."
with shorttimeskip
"By the time I remember, school is over for the day and I'm too tired to do anything but go home, do my homework, and then go to sleep."
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A29:
scene bg school_hallway3
show crowd
with None
play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3
show emi basic_happy at center
with charaenter
emi "Hisao!"
show emi excited_proud
with charachange
emi "I'm going to make you a one-time-only, super extra special lunch offer!"
show emi excited_laugh
with charachange
emi "Emi's home made lunch boxes, and the privilege of enjoying them in private with two bombshell beauties!"
"Her overly flirtatious sales pitch echoes in the hallway, a remarkable feat since it's full of people."
show emi basic_closedgrin
with charachange
"Emi strikes a very confident-looking pose as though as an attempt to one-up her own ridiculousness, puffing her very modest chest and making the V for victory sign with her hand."
hi "Sounds delicious. To what do I owe this honor of being invited?"
show emi excited_proud
with charachange
emi "You stood there looking really lost and sad so I thought you could use some company."
"That is probably the most depressing reason imaginable."
show emi basic_closedgrin
with charachange
emi "So how about it? You're probably really lonely and would eat that awful cafeteria food all alone, otherwise."
hi "Eeeh…"
show emi excited_proud
with charachange
emi "I'm kidding, I'm kidding!"
hi "Sure, I'll have your lunch offer. With pleasure."
show emi basic_happy
with charachange
emi "Let's go to the roof!"
hi "The roof?"
hi "Why the roof?"
show emi basic_closedgrin
with charachange
emi "Because that's where we eat lunch!"
emi "And if I don't get up there, then she'll probably wander off and then I just know she'll go hungry because she never packs a lunch for herself!"
hi "Who will?"
show emi basic_closedhappy
with charachange
emi "Come with me!"
"Without answering my question or waiting for a response, she grabs me by the arm and drags me through the hallways."
"I attempt to make conversation on the way."
hi "Why do you have an extra lunch?"
show emi sad_grin
with charachange
"Emi smiles guiltily."
emi "Actually, it's yesterday's lunch."
emi "I slipped in a run at lunch and forgot to eat it."
"Huh."
label en_A29x:
"Her expression is so funny that I almost laugh out loud."
"Emi giggles, to herself or to something or other, or maybe for no reason at all. I like the sound of it."
"Emi's sunny, energetic disposition alleviates the constricting feeling in the back of my head from the fight with Shizune and Misha."
"I let that issue slide out of my mind, and smile for the first time today."
label en_A29a:
scene bg school_hallway3
show crowd
with None
play ambient sfx_crowd_indoors fadein 0.3
"Normally, I'd join the flow and grab a lunch myself, but today is different."
"Today, I've been invited to lunch on the roof."
"An odd location, but that's where I was told to go."
"Fortunately, I manage to find shelter from the storm in the lee of the classroom door."
stop ambient fadeout 1.0
hide crowd
with Dissolve(2.0)
"Eventually the torrent subsides and I step tentatively out into the hallway."
"Only to be met by Emi, who comes flouncing down the hallway like a cannonball."
play music music_emi fadein 0.3
show emi basic_happy at center
with charaenter
emi "Hey! Hi Hisao! Great timing!"
show emi excited_proud
with charachange
emi "I have super extra lunch today, as promised! Let's go upstairs!"
label en_A29b:
stop music fadeout 2.0
stop ambient fadeout 1.0
scene bg school_staircase1
with locationchange
"The stairway to the roof is a little dilapidated, but it's clearly been used recently."
"At the top of the stairs is a door, complete with missing padlock."
"I wonder who the intrepid individual was that removed the lock?"
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0
scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")
"Emi shoves the door open and steps beaming into the sunlight."
show rin silhouette at offscreenright
with None
show bg school_roof
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease
show emi basic_shock
with vpunch
"Suddenly, a tall dark stranger appears out of nowhere, standing imposingly in front of us. Emi flinches back, almost falling back down the stairs."
$ doublespeak (emi, rin_, "Eeek!", "Hello.")
show emi basic_hes
with charachange
show emi basic_hes at twoleft
with charamove
emi "Yipes! You scared me, Rin!"
"Wait, isn't she…"
show rin relaxed_surprised
with charachange
play music music_rin fadein 2.0
rin "Hello."
"Noticing that Rin is speaking to me, Emi looks curiously at me."
show emi basic_confused
with charachange
emi "You two know each other?"
"I look confusedly at Emi."
hi "She's that friend of yours?"
show rin relaxed_nonchalant
with charachange
"Rin has turned her gaze towards the clouds drifting above the school."
rin "I didn't know you knew this person, Emi."
stop music fadeout 2.0
"…"
"The awkward silence lasts only for a few seconds until Emi lets out a tiny giggle, shrugging the coincidence off."
show emi basic_closedgrin
with charachange
emi "I invited Hisao for lunch. If you know him, that's just better."
show rin basic_deadpan
with charachange
rin "Oh. Does this mean I don't get food? Or did you invite him for lunch without the lunch?"
show emi basic_grin
with charachange
emi "Erm, neither, I have food for three."
show rin basic_deadpanamused
with charachange
rin "Nice thinking."
hide rin
hide emi
with charaexit
"They walk to the other end of the roof while I stay at the clock tower for a while, taking in the atmosphere."
play music music_soothing fadein 0.5
"There is nobody else but us here. I guess the roof is not as popular as it is in other schools."
"A few rundown benches and tables are scattered around the edges, perhaps in an attempt to make the rooftop look less desolate."
"The small pebbles covering the roof rattle beneath our feet."
"I peek through the chain link fence to take a look at the school grounds and beyond."
"Students are strolling in pairs and groups around the quadrangle and at the cafeteria."
"A few delivery trucks are driving past the school towards the convenience store nearby."
"Somewhere a watchdog barks at a passer-by."
"Somehow, when I look towards the town center the small town feel strikes me very strongly, almost palpably."
"The hectic lifestyle of big metropolises seems so far away and foreign here; nobody has to run to catch a bus like their life depended on it or get their senses overloaded by the neon lights and traffic jams."
"I feel surprisingly optimistic about this new life of mine, looking at my new hometown, even if it's going to be mine for only one short year."
"Finding out about my illness and having to move away from home all came so suddenly I haven't had time to think how I feel about it."
"When I step out of the shadow of the clock tower to the open I feel warmth touching my back."
"The sun shines from a perfectly clear cerulean sky."
"A cool breeze sweeping over the rooftop makes me shiver, but only briefly."
"The wind carries the scent of trees and flowers, not smog and car exhaust like it used to, just a few weeks ago."
"Emi settles on a bench with Rin in tow and produces one big and two small lunch boxes from her bag."
show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter
emi "Come on, Hisao! What are you waiting for?"
"She is beckoning me to join them, making room on the already small bench."
hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft
show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft
"I seat myself on the corner of the bench to take as little space as possible. It's pretty cramped, but somehow all three of us fit on it."
hi "Impressive view."
show emi basic_closedhappy_close
with charachange
"Emi suppresses a giggle and places a lunchbox in front of Rin, and hands another lunchbox to me."
show emi excited_proud_close
with charachange
emi "Here you go! Lunch, as promised!"
"Homemade, no less. I'm impressed."
hi "Wow. This looks really good."
show emi excited_amused_close
with charachange
emi "Thanks! I make 'em myself when I can."
"Conversation dies off as I set about the business of feeding myself."
show rin basic_awayabsent_close
with charachange
"Taking a few bites, I glance up and notice Rin deftly opening the lunch box and popping a forkful of food into her mouth using only her feet."
"Even though I've seen it before, I can't help but be impressed at her dexterity."
"It's also a reminder of the sort of place I am in right now."
"Will I ever get used to sights such as this?"
"I can't decide if getting used to such a thing would be a good thing or a bad thing either."
"Does getting used to this place mean that I'm giving up on being a normal person?"
"Or does it just mean that I'm becoming more understanding about those around me?"
"I'm distracted from my thoughts by the sight of Emi tearing into her lunch as if it had insulted her ancestors."
show rin basic_absent_close
with charachange
hi "You seem pretty hungry."
show emi basic_grin_close
with charachange
"Emi looks up, mouth half full, and swallows before nodding."
emi "My morning run always works up an appetite."
show emi basic_closedhappy_close
with charachange
emi "Which is great, because then I burn through lunch pretty quickly."
show emi excited_proud_close
with charachange
emi "Helps me keep my girlish figure."
show rin basic_deadpan_close
with charachange
rin "What would happen if you'd lose it? Would you become a man?"
"I very nearly choke on my lunch trying not to laugh."
show emi basic_annoyed_close
with charachange
emi "It's a figure of speech."
show rin basic_deadpandelight_close
with charachange
rin "Does your figure have to run in the mornings too?"
hi "Do you always talk like this?"
show rin relaxed_surprised_close
show emi basic_confused_close
with charachange
$ doublespeak(emi, rin, "Talk like what?", "Like what?")
"I think that answers my question."
hi "Er, never mind."
hi "So, uh…"
"I struggle to think of small talk and settle on the obvious question."
hi "How'd you two meet?"
show rin basic_awayabsent_close
with charachange
"Rin seems content to let Emi answer this question."
show emi basic_grin_close
with charachange
emi "Someone in the housing department thought that we'd complement each other well, so we were assigned rooms next to one another."
hi "Complement each other?"
show rin basic_deadpannormal_close
with charachange
rin "Like shoes and a suit."
hi "Huh?"
show emi basic_closedgrin_close
with charachange
"Emi giggles at my confusion."
emi "Put us together and we've got all our limbs, get it?"
hi "Ah."
show emi basic_happy_close
with charachange
emi "So I started helping Rin get ready in the mornings, and that was that!"
show emi basic_grin_close
with charachange
emi "I mean, you can't help someone get dressed every morning and not get along."
hi "I see."
"Rin chooses this moment to interject."
show rin basic_deadpan_close
with charachange
rin "I have trouble with shirts."
hi "Right, that seems… fairly obvious."
show rin basic_surprised_close
with charachange
rin "Really?"
hi "Kind of…?"
"This isn't helping, but at least Emi seems to find the whole thing funny."
"That, combined with the fact that Rin is genuinely curious, makes me feel slightly better and yet, confused."
hi "I mean, you've got no arms."
hi "So uh, putting on a shirt seems like one of those things that would be… difficult."
"You know what? I'm going to just stop talking now."
"It'll save me a lot of trouble in the long run."
"Rin nods in what I suspect is meant to be a sage manner."
show rin basic_lucid_close
with charachange
rin "I see."
show rin basic_absent_close
with charachange
"The conversation dies as I turn my attention back to my lunch."
"It's really quite good."
"Emi finishes her lunch first and makes a contented noise."
show emi excited_laugh_close
with charachange
emi "Ah, that was good."
"As she busies herself with cleaning up her lunch, Rin speaks up."
show rin basic_deadpan_close
with charachange
rin "I'm thirsty."
show emi basic_shock_close
with charachange
emi "Oh! I almost forgot about that! Sorry!"
show emi basic_closedgrin_close
with charachange
"With a flourish, she reaches into her bag and removes a trio of juiceboxes."
"She tosses me one that appears to be cranberry juice, one to Rin that appears to be some kind of strawberry milk (complete with pink color scheme), and keeps a (equally pink) box of some kind of fruit punch for herself."
show rin basic_awayabsent_close
with charachange
"Rin dexterously stabs her straw through the top of her box and begins to drink."
"I'm once again impressed by how flexible she is, but this time I keep my comment to myself."
"Somehow I don't think either Emi or Rin are the sorts of people to think twice about the way they work around their particular disabilities."
"Rin especially so."
"Indeed, she gives off the impression of being entirely unaware that she's missing any limbs at all."
"Whether or not that's a conscious decision is another matter."
"I'm honestly not sure."
show emi basic_grin_close
with charachange
emi "So Hisao, how do you like it up here?"
show rin basic_absent_close
with charachange
hi "Hmm?"
hi "It's quite nice, actually. I like high places, for the view."
hi "Thanks for inviting me up here."
hi "And for the lunch, too."
show emi excited_amused_close
with charachange
"Emi grins a thousand-watt grin, pleased by my response I suppose."
emi "No problem!"
show emi excited_proud_close
with charachange
emi "Feel free to eat with us next time too, okay?"
emi "I won't make you a lunch, but you can bring your own up here."
hi "No lunch service? I don't know…"
show emi basic_annoyed_close
with charachange
"Emi looks mock offended."
emi "Trying to take advantage of my good nature?"
emi "The nerve!"
show emi basic_closedgrin_close
with charachange
"She giggles."
show emi sad_depressed_close
with charachange
emi "Well, if that's your answer, I guess Rin and I will just keep eating lunch all alone…"
"I am suddenly assaulted by the most heart-rending puppy-dog eyes I've ever seen as Emi pouts."
hi "Kidding! I was kidding!"
hi "I'd love to eat lunch up here again."
hi "Good location, and the company's okay too."
show emi basic_grin_close
with charachange
"Emi frowns a bit at my declaration of “okay” but seems happy enough that I've accepted her invitation."
"I guess this makes us friends now."
"Or at least acquaintances."
play sound sfx_warningbell
"The lunch bell rings, signaling a return downstairs."
show emi basic_hes_close
with charachange
emi "Rin, you didn't finish your lunch again!"
show rin basic_deadpan_close
with charachange
rin "I wasn't that hungry."
show emi basic_annoyed_close
with charachange
emi "If you don't eat more, you're going to fade away!"
show rin relaxed_boredom_close
with charachange
"Rin shrugs, as if this is an acceptable risk."
stop music fadeout 4.0
hi "Come on, we'd better get going."
stop ambient fadeout 2.0
scene bg school_staircase1
with locationchange
"The three of us head down the stairs together."
scene bg school_scienceroom
with shorttimeskip
"The afternoon class passes. Once again, I find myself without a plan for something to do after school, so I head to the library to return a couple of the books I finished reading."
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
scene bg school_library
with locationskip
"Walking inside, I see that there are about as many students here as there were on Tuesday, all the more evident from the almost total silence enveloping the room."
play sound sfx_impact2
with vpunch
show yuuko panic_up at center
with easeinbottom
play music music_happiness fadein 2.0
"As I drop the books I'd borrowed into the returns slot in the counter, Yuuko suddenly pops up from behind it, quite startled from the banging they make as they hit the trolley next to her."
hi "Ah, sorry Yuuko. Didn't mean to startle you."
show yuuko worried_up
with charachange
yu "No, no. That's fine. It happens… a lot. I'm used to it by now."
show yuuko neurotic_up
with charachange
yu "Um, can I help you?"
hi "It's okay, I think I know where everything is. Thanks anyway."
hide yuuko
with charaexit
"I suppose I'll grab another book or two while I'm here. There's not much else to do, and after reading so much during my stay in the hospital, it's become a hard habit to break."
stop music fadeout 5.0
"I wander down to the fiction section towards the back of the library, scanning the bookshelves for anything that catches my eye."
"As I do, I look over to the corner where Hanako had been the last time I was here, not really expecting anything to come of it."
scene ev hana_library_read_std
with locationskip
"…surprisingly, though, she's there, absorbed completely in a fairly thick book. I decide against intruding on her like last time and get back to finding reading material."
scene bg school_library_ss
with shorttimeskip
play music music_tranquil fadein 6.0
"After an indiscernible amount of time spent perusing the aisles, I finally decide on a couple of books to get and slide them off the shelf."
"With a minimum of fuss, I quickly walk over to the counter, check out my books and pop them into my bag as I walk out."
scene bg school_courtyard_ss
with locationskip
"By the time I leave the main building, sunset isn't too far away. A small trickle of students remain, but the majority have left; presumably to their homes and dorms."
label en_A29c:
scene bg school_dormhisao_ss
with locationskip
"Feeling utterly drained, I head to my room to read the books I borrowed. There's been enough action and excitement for one day already."
"The first is “Alice's Adventures in Wonderland”. I know the story, of course, but I've never actually read the original book."
"It's just as trippy as I remember the story to be, with the wacky characters and nonsense plot."
"I start thinking of myself as some kind of an Alice too, haplessly tumbling down the rabbit hole into this Cripple Wonderland."
"…Okay, that's a rather strong expression. Still, the isolated location and the overt way the school accommodates to absolutely everything is unsettling. It is like another world."
"I wonder why I can't shake the feeling of being an outsider like Alice, despite most everyone being so hospitable and friendly with me."
"Turning another page, my mind starts drifting further away from the book. It's quiet, I can hear my heartbeat thumping against the fabric of my shirt."
"For some reason, it makes me feel really bad like it has since that time in the forest with Iwanako. Like I was locked in a cage with something nasty and scary."
stop music fadeout 5.0
scene bg school_dormhisao_ni
with Dissolve(3.0)
"I put the book down for a while and stare at the ceiling, taking my time to shake off the feeling."
"200 pages later, I fall asleep."
scene black
with shuteye
label en_A30:
scene bg school_courtyard_ss
with None
$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)
"I guess I need to buy some supplies. I can't live off cafeteria food and eating out for my entire stay here."
scene bg school_gate_ss
with locationchange
"As I leave for the gate, I make a few loud stretches to try and stave off the tiredness that's accumulated over the week."
scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange
"After passing through and rounding the corner, though, I see a solitary figure walking downhill towards the small town below. The color of her hair and tapping of her cane are unmistakable."
show lilly cane_surprised_ss
hide lillyprop
with charachange
"I quickly walk up to her, which seems to catch her attention without a word needing to be said."
hi "Hi, Lilly."
show lilly cane_weaksmile_ss
with charachange
"She takes a moment to place the voice, slightly adjusting her head to face a bit more towards the source of my voice as she does."
show lilly cane_smile_ss
with charachange
li "…Hisao?"
hi "Yep, that's me."
"She seems to have a good memory for voices. The fact that she actually remembered is a pleasant surprise."
li "Good evening. What brings you here?"
show lilly cane_weaksmile_ss
with charachange
"Once again, she gives a small polite bow. And, once again, I reply in kind before realizing that I needn't do so."
hi "Just going into town. You?"
show lilly cane_ara_ss
with charachange
li "My my, what a coincidence."
hi "Doing the same thing, eh?"
show lilly cane_smile_ss
with charachange
li "Mm. I usually go shopping on Fridays."
show lilly cane_surprised_ss
with charachange
"She pauses for a moment, suddenly looking a little lost."
li "That said, Hanako usually comes into town with me…"
"Ah. Not lost, but worried. The two do seem to keep pretty close tabs on one another. It's kind of surprising that Hanako would just forget Lilly like that."
hi "I noticed her reading in the library. She probably just got caught up in a book."
show lilly cane_weaksmile_ss
with charachange
"She lets out a small sigh of relief."
li "Thank you. She has a habit of doing that."
hi "Avid reader?"
show lilly cane_smile_ss
with charachange
li "Right. She doesn't like being around crowds of people, so reading away from everyone lets her relax a bit."
"Although she probably didn't intend it, I can't help but grimace as I recall my first meeting with her."
show lilly cane_smileclosed_ss
with charachange
"Hardly wanting to bring it up, I remain silent as we quietly continue to walk down the quiet road."
"Tack, tack. Tack, tack."
"With the road bereft of cars and the students of Yamaku increasingly far behind us, the quiet rustling of the leaves and the measured tapping of Lilly's cane against the sidewalk are all that can be heard."
"It's kind of nice, especially compared to the hustle and bustle of where I used to live."
"Before I know it, I've relaxed so much that a loud yawn escapes before I can control it."
show lilly cane_giggle_ss
with charachange
li "Tired?"
hi "Yeah, been running ragged these past few days."
"That's an understatement, to be sure. Transferring into a different school would be bad enough, but nothing like this…"
show lilly cane_smile_ss
with charachange
li "Well, hopefully everything should settle down for you. The festival's got everyone in a spin right now, and you've been plopped right in the middle of things."
"For a moment I hesitate, but given her apparent tolerance for frankness I decide to give my full thoughts."
hi "I guess. Yamaku's kind of different though. I mean, the formality surrounding everything, the isolation around it… not to mention the most obvious difference."
hi "It's kind of a whole different mindset. I suppose I'll get used to it though, in time."
show lilly cane_smileclosed_ss
with charachange
"She gives a matter-of-fact nod, apparently pleased with my answer. It feels almost as if she's included me in the flock of students she's shepherding, along with class 3-2 and Hanako."
"Well, not that I mind. It's nice to get the thoughts off my chest in any case."
show lilly cane_smile_ss
with charachange
li "Looking on the bright side, one could see it as a chance for a new beginning. You should cherish the ability to make new friends."
"That's optimistic. Nonetheless, it's good to have a positive attitude about such things, I suppose."
hi "I guess that's a good take on it."
scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip
stop music fadeout 6.0
"Walking on down the road, she seems to become somewhat unsettled. Before I can ask what's on her mind, she seems to collect herself and speaks up about something else."
show lilly cane_weaksmile_ss
with charachange
li "So, where in town were you going?"
"That's actually a pretty good question. I'd come in to buy food, but the layout of the place is still totally foreign to me."
"I had intended to just wander around and see what I could find, but with sunset already approaching and nightfall not too far away, that doesn't seem very wise."
"I'm going to have to ask her for directions. Again."
hi "I was just going to get some food… but now that you mention it, I don't really know the way."
show lilly cane_planned_ss
with charachange
li "Well now, this is quite lucky. I was just about to go to the convenience store myself."
hi "Looks like I'll be in your care again, then. Thanks."
"Together we walk to the store, my paces carefully slowed to remain beside her. Compared to my usual walking pace, hers is quite a bit slower. Not that it's without reason."
scene bg suburb_konbiniext_ss
with shorttimeskip
play music music_daily fadein 2.0
"After what couldn't be more than several minutes, I catch sight of our objective. This town really is pretty small."
scene bg suburb_konbiniint
with locationchange
"Without further ado, we make our way inside with a greeting from the counter."
show lilly cane_weaksmile at center
with charaenter
li "Mind if I tag along with you? Usually Hanako would help me, but seeing as she's not here…"
"It takes a moment before I realize what she means."
"Considering she wouldn't be able to read any of the labels, shopping without any help would be a big pain for her."
"That said, I can't shake the feeling that she'd had this idea since I said I was coming here."
hi "Sure. It'd be my pleasure."
"I grab two well-used red baskets from the small stack beside the entrance, handing one to Lilly."
show lilly cane_weaksmile at Transform(ypos=800)
with charamove
show lilly basic_smileclosed at Transform(ypos=800)
with charachange
show lilly basic_smileclosed at center
with charamove
"She lays it on the ground, putting her schoolbag in, retracting her cane and sliding it through the basket's handles before picking it back up in her right hand."
"Wait, if she doesn't use her cane…"
show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None
show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)
"Before I can complete the thought, she comes beside me and pinches the cuff of my uniform in her slender fingers."
show lilly basic_concerned_close at twoleft
with characlose
li "Is this all right?"
hi "Ah, sure."
show lilly basic_smileclosed_close
with characlose
"I have no reason not to accept. I can think of worse things than shopping with a pretty girl holding onto me, even if it is out of necessity."
"We navigate our way through the store, with not one of the occasional passing customers seeming to bat an eyelid."
"Considering how close Yamaku is, I guess seeing students from there must be entirely normal for the local residents."
"As we reach each aisle, I quickly check with Lilly and find out what she needs. I grab it along with what I'm looking for, and put our items into their respective baskets."
"I guess this is the same routine she and Hanako follow every Friday."
hi "Right, all that's left is the bread and that should be my shopping done. Do you need anything else, Lilly?"
show lilly basic_smile_close
with characlose
li "No, this should be everything."
hi "Off we go, then."
show lilly basic_smileclosed_close
with characlose
"With a quick side trip to the bakery section, we make our way to the registers."
"The line, thankfully, is almost nonexistent. It's not long before we've both paid for our food and are out the door."
scene bg misc_sky_ni at Fullpan(15.0)
with locationchange
"As Lilly retrieves her cane and extends it to full length, I waste a minute looking upwards at the night sky while holding both our bags."
"For a moment I try to make clouds with my breath, but the summer's heat doesn't seem to cooperate."
"Eventually she rights herself, taking a quick stretch before taking her bag and leaving me to my two."
scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange
hi "You tired as well?"
show lilly cane_sleepy_ni
with charachange
li "The festival preparations have been complete chaos. Shizune breathing down my neck doesn't exactly help things, either."
hi "Hey, she's only trying to get everything organized. Better now than later, right?"
show lilly cane_weaksmile_ni
with charachange
li "I suppose. I'm going to enjoy relaxing in town tomorrow, that's for certain."
"I guess the festival preparations must be taking their toll on both of them."
scene bg suburb_roadcenter_ni at bgright
with locationchange
"We walk out into the quiet street, talking between ourselves as we carry our bags of food and supplies from the store."
"…Wait, what's that?"
"I notice a very distinctive figure making its way towards us, silhouetted by the streetlamps."
"For a second I think it's another male student from my class, but as he, or should I say she, gets closer I recognize her quickly."
show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright
stop music fadeout 8.0
hi "Rin? What're you doing out here so late?"
show lilly cane_surprised_ni at center
with charaenter
li "Rin?"
"Lilly perks her head, looking like she's trying to focus on listening more keenly. It suddenly comes to me that I should probably interpret the scene for her."
hi "It's Rin… Tezuka, I think was her last name, from our school."
show lilly cane_weaksmile_ni
with charachange
"She stiffens at the name and gives a complicated-looking expression, something like a forced fusion of a composed smile and a painful cringe."
li "Ah. I understand."
"I guess Lilly knows Rin too."
show rin basic_awayabsent_ni
with charachange
show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove
"Rin turns to look at us, looking terribly out of it. I'm not entirely sure if she recognizes either of us or at least she doesn't acknowledge it if she does."
"She looks like a zombie. Or a statue. A statue of a zombie."
"But slowly, some symptoms of understanding seem to light in her dark eyes: this is something she must react to."
show rin basic_lucid_ni
with charachange
show rin basic_awayabsent_ni
with charachange
"Rin blinks once. Very thoroughly."
show rin basic_absent_ni
with charachange
rin "Hello."
"…"
"There is an awkward pause, everyone waiting for someone else to say something."
hi "What are you doing here this late?"
"…"
rin "I…"
show rin basic_deadpan_ni
with charachange
rin "I was wondering about that myself too. Just now."
play music music_rin fadein 0.5
show rin basic_deadpannormal_ni
with charachange
rin "Some people asked that just before. I assume they were wondering the same."
rin "I didn't know. They didn't know either. I asked. That's why I'm wondering."
rin "So that was pretty much it. It's a murder mystery without a murder."
"…"
show rin negative_spaciness_ni
with charachange
rin "They were going that way."
show rin basic_absent_ni
with charachange
"She turns facing to her right in order to demonstrate the direction the other people went to as if that was important, then rotates back like a mechanical puppet in one of those overly complicated clockworks."
"For a person who gives an impression of being the quiet type, Rin really does use a lot of words to say things that don't need a lot to be said."
"Unsure if she's finished, I say nothing. Neither does Lilly, who seems equally robbed of words for the time being."
"I think that both of us are in fact just scared that any response might provoke her to continue."
"Our stupefied lack of reaction doesn't faze Rin at all. She keeps looking at us expectantly, a calm hint of expression on her blank face."
"She seems to be that kind of person. Always so relaxed."
"As if bull elephant-grade sedatives were flowing in her veins in the place of blood."
show lilly cane_concerned_ni
with charachange
li "Do you have amnesia? I don't recall you having anything of the sort, though…"
hi "No, I don't think it's that."
hi "The other passersby were probably just worried, though. You do look really lost, the way you're standing in the middle of the street."
show rin basic_deadpan_ni
with charachange
rin "Oh, I see."
show rin relaxed_nonchalant_ni
with charachange
rin "Maybe I should've taken some other kind of pose in that case."
"I ponder for a while whether I should chase this angle further, or give up for the sake of my own sanity."
"I decide on the latter."
"It seems that most of the time, it's better to not read too deeply into what Rin is babbling about."
"Talking with Rin is like playing chess with a supercomputer who does seemingly completely random moves as if to mock everything you know about chess. It's like that, except with human interaction."
"And even if I win, it feels like losing."
"Damn, it's just like Kenji said. Even when I win, I lose. Is this the power of the girls of Yamaku?"
"…"
"I push the thought aside as too dangerous to consider further. It's probably just Kenji's anti-female propaganda getting to me during a moment of weakness."
hi "Yeah, maybe taking another pose might have worked."
hi "So anyway, you have no idea what you're doing here?"
show rin negative_annoyed_ni
with charachange
"She frowns, looking extremely displeased at either my question, its consequences, or the answer she's about to give."
rin "I do have. Some idea. I can't really tell what kind of an idea."
show lilly cane_smile_ni
with charachange
li "That sounds like progress, at least."
"Lilly sounds as if she's spotted an opening for some kind of discernibly normal conversation. I can't say I share her optimism."
rin "Yes, there is some. Definitely. The rest will come later."
show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange
rin "I'm sure of it. I always have… reasons."
"The ensuing silence kills Lilly's hopes all too visibly. That didn't last long."
"Rin's, as far as I can tell unbased, assurances aside… what should be done?"
"We could just leave her to her own devices, whatever those are… but it's late and I don't think we'll be getting any thanks if Rin is found standing here in the middle of the night."
"Which she probably will, unless she manages to remember what she was doing here in the first place."
"As for me trying to guess what might've been going on in her mind when she decided to embark on this adventure, the chances seem to be on par with winning the lottery."
"Several times in a row."
"Lilly is oddly quiet too. I'd appreciate some support from the sidelines here, especially if she's more familiar with Rin than I am."
"But it can't be helped. It seems her familiarity with Rin is exactly why she's staying subdued."
hi "So, I assume you were going somewhere, not coming back to the school… any idea where?"
show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange
"Her eyes widen in shock and she jolts back in a somewhat artificial way, making it seem like an act rehearsed for situations like this."
rin "Are you a mind reader? Is that your disability? How unique!"
hi "No… What? Why would you think that?"
show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange
rin "You knew what I was doing."
show lilly cane_displeased_ni
with charachange
hi "Eh, it was just an educated guess. We walked this same street in the other direction just before, to get to the store."
hi "If you were going to school, we would've met you on the way."
show rin basic_deadpanupset_ni
with charachange
rin "Oh."
"She looks a little disappointed."
"Like Kenji, Rin appears quick to jump to completely irrational conclusions."
"Maybe it's something in the water here. I make a mental note to stock up on soft drinks."
hi "You know, that is the second time this week that someone asked if I was a mind reader."
hi "Do I really give off that impression?"
show rin basic_deadpannormal_ni
with charachange
"Rin shrugs her shoulders, which is all the answer I get."
hi "You know—{w=0.3}{nw}"
show lilly cane_smile_ni
with charachange
li "Maybe you should come with us back to the school?"
"Lilly interjects just as I am about to further debunk my alleged mind-reading capabilities. She sounds rather concerned, the paper-thin smile on her face badly disguising that fact."
"Maybe she came to the same conclusion as I did. For everyone's sake, I decide to let the mind-reading topic drop, as it's entirely inane anyway."
hi "Yeah, Lilly's right. If you can't remember, there's no point staying here."
show rin basic_awayabsent_ni
with charachange
"Rin considers this rather simple deduction for a moment, then nods."
show rin basic_absent_ni
with charachange
stop music fadeout 2.0
rin "Okay."
scene bg school_road_ni
with shorttimeskip
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0
"We start towards the school again, having wasted way more time than necessary with this episode."
show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter
"Rin walks along the edge of the sidewalk in her arrhythmic way, looking like a mix of sleepwalker and rope dancer, while Lilly keeps one hand on my shoulder, tapping at the ground with her cane."
"Tap step step tap tap step step step."
"Apart from that and a few fragmented beginnings of conversation, it's quiet. A quiet quite apart from the relaxing one into town, at that."
hi "So how's the mural going?"
show rin basic_deadpan_ni
with charachange
rin "We are going to get bad luck. Never talk about works in progress."
show lilly cane_weaksmile_ni
with charachange
li "I'm sure it'll be wonderful."
show rin basic_deadpannormal_ni
with charachange
rin "Bad luck."
"Tap step tap step. She doesn't care to talk about it. Lilly's politeness feels out of place, for the first time. Step step step."
"The hill Yamaku rests on top of is surprisingly steep, going uphill. We slow the pace, but I still feel my pulse rising and breathing getting heavier."
"Almost there, I can see the gates already."
"More than that, though, I notice that Lilly's hand slightly tightens on my shoulder. Interpreting it as a gesture that she wants to ask something, I speak up."
hi "Anything wrong, Lilly?"
"I resist the urge to say “Aside from our traveling companion?” But only just."
"For a moment she seems to debate whether she should even bring it up, but goes for it anyway."
show lilly cane_concerned_ni
with charachange
li "Is everything… all right?"
hi "All right? How do you mean?"
"The fact I can't interpret her incredibly vague question puts her off, for a second."
li "It's just… you seem unusually tired, I guess."
"Now that she brings it up, I notice that my breathing is strangely heavy. The uphill walk has really done a job on me."
label en_choiceA30:
menu:
    with menueffect
    "Lilly noticed it all too quickly…"
    "Sorry, I'm not in very good condition.":
        return m1
    "I don't really want to talk about it.":
        return m2
label en_A30a:
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0
hi "I… I'm fine."
hi "There's nothing to worry about, the hill is just surprisingly steep, don't you think?"
hi "I wonder what they have the school so high up here for anyway, don't we have students in wheelchairs and everything?"
show lilly cane_sad_ni
with charachange
li "Indeed."
show lilly cane_concerned_ni
with charachange
"Lilly's forehead wrinkles in concern, and I don't really want her to have that kind of an expression over me. We barely know each other."
hi "Yeah, my thoughts exactly. Not that you can find a place like this wherever, I guess, but it makes me wonder what they were thinking."
"My voice is overly calm, it sounds weird to my own ear and I speak way too fast. I briefly wonder how much Lilly can sense from someone's voice alone."
li "Mmm…"
hi "Let's continue. We're almost there anyway."
hide lilly
hide rin
with charaexit
"For the rest of the way back to the school, we all remain silent."
stop ambient fadeout 3.0
scene black
with Dissolve(3.0)
label en_A30b:
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
hi "It's all right, I just need to catch my breath. My condition isn't the best, these days."
show lilly cane_oops_ni
with charachange
li "Oh."
li "Is it something that… is related to you being transferred here? I mean…"
show lilly cane_concerned_ni
with charachange
"She cuts herself off rather abruptly, maybe realizing she was being a bit intrusive. Her instincts are sharp though, and while I don't like the subject it's not like I should lie about it."
"If it's Lilly, I don't think I mind."
hi "I'm just a little weak for the time being."
show lilly cane_oops_ni
with charachange
li "Hanako said you look fairly… healthy, so I naturally thought…"
show lilly cane_sad_ni
with charachange
"Lilly doesn't finish her sentence again, letting it trail off with a measure of concern."
"As she furrows her brow, Lilly's uncomfortable expression spurs me to say at least something to ease her feelings."
"It's surprising she's this flustered, considering her straightforward attitude with her own blindness. She must know that not all share her own comfort about such things."
hi "No, it's okay."
hi "I have a pretty… I guess the best way to put it would be messed-up… heart. Arrhythmia."
hi "I had a bad heart attack a while ago because of it, and spent most of the spring in a hospital. Ended in Yamaku on doctor's orders."
"She silently nods her head in acknowledgment."
"My answer, though, only seems to make Lilly furrow her brow even further. She doesn't seem to quite know how to react, given we don't really know each other that well."
"I can't really fault her for it, given I have the exact same reaction."
label en_A30c:
"To my surprise, in a moment's time her face shows that she comes to some sort of realization."
show lilly cane_oops_ni
with charachange
li "Wait… so the time when Emi and you collided in the hallway…?"
"I grimace slightly. Her ability to connect the dots quite so fast is unexpected."
hi "Yeah. I guess I'm a textbook example of why those rules about running in the corridors exist."
show lilly cane_sad_ni
with charachange
"That was a lot more dry than I'd intended. Lilly visibly shies away from continuing the topic."
label en_A30d:
"While I do want to assuage her concern, I really don't want to dwell on this either."
hi "Don't worry about it."
show lilly cane_weaksmile_ni
with charachange
"I try to offer a reassuring smile but then I realize the futility. Without knowing this, Lilly smiles at me reassuringly but doesn't say anything further."
$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0
scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip
"Arriving at the dorms, Rin stops in front of her mural as if lightning struck her. She had been so quiet for almost all of the walk back that I had all but forgotten she was here."
show rin relaxed_disgust_ni
with charachange
rin "It's Friday, isn't it?"
show lilly cane_smile_ni
with charachange
li "Yes… Friday, the eighth of June."
show rin basic_upset_ni
with charachange
play music music_rin fadein 0.5
rin "This is bad."
show lilly cane_surprised_ni
with charachange
li "Bad? Why?"
show rin negative_annoyed_ni
with charachange
rin "I think I am going to go in a fetal position and throw up. Possibly in reverse order."
show lilly cane_concerned_ni
with charachange
li "Is something wrong?"
show rin negative_confused_ni
with charachange
rin "No. Nothing is wrong. It's Friday and nothing is wrong yet. This mural, it's going to need to be finished by Sunday. So everything's all right."
show rin negative_worried_ni
with charachange
rin "Do you have any drugs? Or a time machine?"
show rin negative_confused_ni
with charachange
rin "This is not good. Not good."
"So she's behind her schedule. Recalling Shizune's exasperation at Rin's carefree attitude several days ago, I don't know what to think."
"She has left herself open for a “told you so” unless she can pull off whatever she needs to pull off by Sunday morning."
"Rin keeps staring at her mural looking as mortified as she can."
show rin negative_annoyed_ni
with charachange
rin "Leave me. I'm going to need to work for a while."
"I glance at Lilly, expecting her to share an incredulous look with me as I roll my eyes, but then I realize she's not one to do that kind of thing."
show rin negative_angry_ni
with charachange
rin "Leave me."
stop music fadeout 2.0
hide rin
with charaexit
show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove
"We do, of course, not wanting to aggravate her any more than she already is."
"There is a churning bad feeling in my gut. Rin sure has a knack of making people feel worried about her."
"She seems like a person who should never be left alone."
hi "Maybe we should call someone? She sounded like she was going into shock or something."
show lilly cane_oops_ni
with charachange
li "I'm sure she will be just fine. She's just a… eeeh… how to say…"
"Lilly cocks her head a little, trying to find a polite way of calling Rin crazy without calling her crazy."
hi "Unique?"
show lilly cane_weaksmile_ni
with charachange
li "Yes, a very unique person."
hi "I guess you could say that."
show lilly cane_giggle_ni
with charachange
"She giggles at the notion melodiously, nodding in agreement."
show lilly cane_weaksmile_ni
with charachange
li "Sorry about leaving you stranded as you talked to her. I… don't really understand her, so I keep my distance."
"So my guess was right. Lilly offers a slight, apologetic smile as if she was sorry that her own shortcomings have prevented her from becoming closer to Rin."
"I'm not one to blame her. At all."
"Lilly lets slip a long breath, probably a disguised yawn. I imagine she's as exhausted by all this as I am."
show lilly cane_cheerful_ni
with charachange
li "I'd better leave now and give these to Hanako. Thank you for the company, Hisao."
"She smiles very sweetly at me. It feels different than normal, despite the fact that she seems to be smiling so often."
"I can't put my finger on what the difference is. It's just different."
"Relaxed, I'd say, but that's probably just relief over getting rid of Rin. Maybe."
hi "Yeah… good night. Say hi to Hanako for me."
show lilly cane_smile_ni
with charachange
li "I will. Good night."
hide lilly
stop ambient fadeout 2.7
scene black
label en_A31:
scene black
with None
scene bg school_scienceroom
with Dissolve(2.0)
play music music_normal fadein 3.0
"The students roll into class for the Saturday morning session, each and every one of them sporting the tired eyes of people that have worked through the night."
"With only a day left to prepare, I suppose it's not so surprising. Thankfully, we only have to suffer through classes until the lunch break, and then our time is our own."
show muto irritated at center
with charaenter
"Mutou lurches into class in a tired stagger. I suppose students aren't the only people here that enjoy their late Friday nights."
"Without saying a word, he scrawls some page and question numbers on the board and slumps down at his desk."
"It's completely atypical behavior for him, but it appears that no one in the class is going to call him out on it."
play sound sfx_paperruffling
hide muto
with charaexit
stop sound fadeout 6.0
"Wordlessly, the students shuffle their textbooks into position and get to work. Not wanting to break the trend, I do the same."
"Fatigue has made the class antisocial; not a peep is heard among the ruffling papers."
"That can partly be attributed to the two empty seats beside me. For some reason Misha and Shizune aren't present; probably doing council work for the festival."
"It's very quiet without Misha present."
"I wonder if she was born as rowdy as she is, or if she is “making up” for Shizune's lack of voice."
show muto normal at center
with charaenter
stop music fadeout 2.0
mu "Nakai, can I speak to you for a moment?"
"I'm so engrossed in thinking about Misha that I don't even notice Mutou approaching my desk."
hi "Sure… what's this about?"
mu "It's probably better if we speak outside the classroom…"
play sound sfx_dooropen
hide muto
with charaexit
"Something about this doesn't sound too good, but I stand up and follow him out into the hallway."
play sound sfx_doorclose
label en_A31b:
scene bg school_hallway3
show muto normal at center
with locationchange
"Mutou stands in the hallway, scratching his head as he works out what he is trying to say. Not knowing what's going on, I wait silently."
mu "I heard from the school's head nurse that you had an incident the other day."
"Ah. So it's about that."
hi "Well, kind of, but it's not anything to be worried about."
show muto irritated
with charachange
mu "Yes, yes it is. Anything that can endanger your health is something to be worried about."
mu "We try our best here to prepare you for life here. Part of that involves knowing your limits, and how to work around them."
mu "It would be remiss of me if I didn't speak up about this."
hi "All right, I get it. I'm sorry."
"Mutou closes his eyes in frustration, and I realize that this probably wasn't the best thing to say."
mu "Something tells me that you're not sorry. Pretend as much as you want, but this isn't a normal school."
mu "A lot of people have put in a lot of time, effort, and money to make sure that you, and every other student here, can have the same level of education as your peers."
mu "For you to abuse that by throwing out advice, especially medical advice, is plain selfish."
"I'm not quite sure if this is actually how he feels, or if it is some act that he's practiced many times to guilt-trip students into doing the “right” thing. Either way, it's working."
hi "I understand. This is all new to me, and I apologize. I know my limits now, and I'll be sticking to them."
show muto smile
with charachange
"Mutou appears to lighten up a little, satisfied that his message has been received."
label en_A31c:
scene bg school_hallway3
show muto normal at center
with locationchange
"Mutou stands in the hallway, scratching his head as he works out what he is trying to say. Not knowing what is going on, I wait silently."
mu "So, tell me, how are things?"
hi "Things?"
"I expected Mutou to be a little vague, but this is pushing the limits."
show muto irritated
with charachange
mu "You know. Things. You've had a week to settle in now, so how are things?"
hi "Er, fine I guess."
show muto normal
with charachange
mu "I see. And how is your… condition?"
"The pause before “condition” seemed a little unnecessary."
hi "Haven't had any problems so far."
show muto smile
with charachange
"A brief shimmer of relief passes across Mutou's face."
mu "Good, that's good. The school nurse was a little concerned that you might have been pushing yourself a bit too hard."
mu "He asked me to keep an eye on you when he couldn't."
hi "That makes sense…"
show muto normal
with charachange
mu "I'd ask that you don't blow us off so freely. As much as we try to give you the level of education that you would get at a normal school, you have to realize that you have limits."
mu "Our goal is to make sure that you know where those limits are, and how to maximize your potential within them. Do you follow me?"
hi "I guess. I mean, I don't plan on doing anything stupid."
show muto smile
with charachange
mu "Well, that's a start, I guess."
label en_A31d:
show muto normal
with charachange
play music music_normal fadein 3.0
mu "So then, onto my next question; how are you finding your studies? I understand you were laid up for a while. We're not too far ahead, are we?"
hi "I don't really think so. I tried to keep up when I was in the hospital, so it hasn't been too hard."
show muto irritated
with charachange
"Mutou taps his chin and raises an eyebrow as he absorbs this information."
mu "Is that so… I suppose there are still students out there that realize the importance of learning…"
"I wouldn't go that far, I was only trying to keep myself occupied in my little life-support prison."
hi "Well, yeah. You've got to keep up with these things, right?"
show muto smile
with charachange
mu "That's exactly it. One wrong move in this world and you're left behind, right?"
hi "Er, right. Wouldn't want that to happen."
show muto normal
with charachange
mu "No, no you wouldn't. Every week there's a new scientific discovery. Most of them mean nothing to the layperson, but any one of them could be the key to the Next Big Thing."
hi "I'll keep that in mind…"
"It's obvious that Mutou's Serious Talk is over, and he's gone back to his standard, slightly scatterbrained approach to life."
"I think, in hindsight, that I prefer him this way. He's slightly more predictable in his unpredictability."
show muto smile
with charachange
mu "Well then, I think that's all I really had to say. Let's get back inside, shall we?"
"My relief at that suggestion is insurmountable."
hi "Sure. You're the boss, right?"
show muto normal
with charachange
"Mutou pauses for a moment."
mu "I don't think any of my students have ever said that to me before."
"For an instant I consider replying to this, but something deep within me tells me to shut my mouth and get back into the classroom."
play sound sfx_dooropen
scene bg school_scienceroom
with locationchange
stop music fadeout 5.0
"A few of the students jump at the sound of the door, rapidly trying to pretend that they are working on the questions on the board."
play sound sfx_doorclose
"Some don't even bother, their heads slumped on the desk as they nap. Thankfully, it would appear that Mutou does not even notice them."
"He returns to his desk and retrieves a scientific journal from one of the drawers. I guess I got to him there."
"The class returns to the near-silence that Mutou and I left it in before our chat."
"Mixed feelings of tiredness and anticipation buzz around the room. Everyone here is either waiting for a chance to rest or the chance to get their last-minute preparations underway."
play sound sfx_normalbell
play music music_daily fadein 8.0
"The clock on the wall slowly ticks the remaining class time away, until finally the bells cry out, ending the torment."
show muto normal at center
with charaenter
mu "Before you all leave, I expect the answers for those problems by Monday."
hide muto
with charaexit
"The class sighs as one, instantly regretting slacking off, but still acutely aware of the more pressing issues at hand."
"The classroom empties in a blink as everyone rushes to their last-minute festival preparations."
"I stay behind and try to quickly finish the questions so I don't have to bother with it over the rest of the weekend, with the festival and all tomorrow."
show bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with charamoveinright
"Apart from me, Hanako is the only one left, obviously waiting for Lilly."
"It's weird that Lilly comes all the way to our classroom to pick her up. I expect that moving around is at least nominally harder for her than it is for Hanako."
"But it's none of my business, and I naturally don't ask about it from Hanako."
"Despite the relative proximity of our seats, neither tries to strike up a conversation about that or anything else either, so an oppressive silence falls upon the classroom."
"Time passes in silence. It's probably just fifteen minutes or so but it feels longer. I turn pages of my notebook. Hanako turns pages of the novel she's reading."
"My pencil lead splinters against the paper just when I was about to finish a paragraph."
"The sounds of my irritated sigh and subsequent fumbling around for a sharpener feel like they're breaking the mood in the classroom."
"Hanako keeps her eyes firmly away from my direction."
"Before long, Lilly's tall figure appears in the doorway."
show lilly basic_smileclosed at offscreenleft
with None
show bg school_scienceroom at center
show hanako emb_downtimid at offscreenright
show lilly basic_smileclosed at left
with charamove
li "Hanako?"
show lilly basic_smileclosed at twoleft
show bg school_scienceroom at bgright
show hanako emb_downsmile at center
with charamove
"Her name is all it takes to make Hanako jump up from her desk and run to Lilly."
hide lilly
with charaexit
show hanako emb_downsad
with charachange
show hanako emb_downsad at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_out_time_warp)
with None
hide hanako
with charaexit
"They talk quietly for a moment, but it isn't long before Lilly leaves down the hall and Hanako idles back into the classroom, taking her seat once again."
show hanako emb_downsad at offscreenright
with None
show bg school_scienceroom at bgleft
show hanako emb_downsad at right
with charamove
"I watch Hanako out of the corner of my eye out of sheer curiosity at the idea that the two would be separated."
"For a couple of minutes, she does nothing but sit with her chin in her hand, staring at the desk dejectedly."
show hanako emb_downtimid at right
with charachange
"The boredom evidently becomes too much for her though, her slender frame reaching into her bag and pulling out a small book."
"Come to think of it, that isn't the one I saw her reading at the library. She must be quite a fast reader to get through them at this rate."
label en_A31e:
hide hanako
with charaexit
stop music fadeout 4.0
"After about ten minutes of restlessly shuffling in her seat and trying to read, Hanako closes her book and leaves too."
"As should I, since the assignment is all but finished and there is nothing else to do in the classroom."
scene bg school_dormhisao
with locationskip
"Not really feeling energetic, I just go straight to my room and read for the rest of the day."
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A32:
scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None
hide hanako
with charaexit
stop music fadeout 4.0
"After about ten minutes of restlessly shuffling in her seat and trying to read, Hanako closes her book and leaves too."
"As should I, since the assignment is all but finished and there is nothing else to do in the classroom."
"Not that I have anything to do anywhere else either."
play music music_tranquil fadein 3.0
scene bg school_hallway3
show crowd
with locationchange
play ambient sfx_crowd_indoors fadein 0.3
"The school is a beehive of activity but nobody pays me any heed."
"I saunter past classrooms filled with students frantically doing this and that, buzzing around like little worker bees."
"You wouldn't guess the school day is over."
stop ambient fadeout 0.3
scene bg school_courtyard
show crowd
with locationskip
play ambient sfx_crowd_outdoors fadein 0.2
"It's a bit quieter outside, but not by much."
"People zip by, left and right, hurrying as quick as they can; busy and energetic."
"I feel the opposite. The midday sun seems to be draining all the spirit out of my body, making it feel limp all over."
"Warm, soft air flows inside my shirt, feeling like a cushion."
"I yawn lazily, thinking about what I'd do."
"I'll drop off my books at the dorms first, and then… something I haven't decided yet."
"Maybe Kenji is in his room."
stop ambient fadeout 2.0
scene bg school_dormext_half
with locationchange
"On the way to dorms, I spot Emi coming my way, running despite not having those weird running prosthetics on. I wave at her and she skids to a stop."
show emi basic_closedgrin at center
with charamoveinright
emi "Yo, Hisao!"
"Spatters of white and green paint adorn her nose and chin respectively, but her smile is wide, as it seems it always is."
show emi excited_happy_close
with characlose
"She leans closer to me, amplifying the feeling she is examining me."
emi "Whatchadoin'?"
hi "Nothing, really. I don't have anything to do for the festival and everyone else seems to be doing something important."
show emi excited_laugh_close
with characlose
emi "That's perfect! Then you can help me and Rin!"
hi "With the festival preparations? Eeeh, I'm not sure if I would be of much help."
show emi excited_proud_close
with characlose
emi "That's fine! I'm not much help either!"
"Emi grabs my wrist and starts dragging me back inside the school quite forcefully."
scene bg school_lobby
show crowd
with locationskip
play ambient sfx_crowd_indoors fadein 0.3
"Even her walking speed is more like jogging, making me stumble over myself simply trying to keep up."
scene bg school_staircase2
with locationchange
"The stairs slow Emi down a little bit. Maybe it's hard to climb with her legs, or maybe she's finally run out of breath."
stop music fadeout 7.0
scene bg school_hallway3
show crowd
with locationchange
"We go all the way back to the third floor and to the seniors' hallway, ending up where I left five minutes ago. I could just as well have stayed here waiting for Emi, had I known."
hi "So are you… is Rin working on that mural, still?"
show emi basic_closedgrin at center
with charaenter
emi "That's right! She needs all kinds of paints and brushes and stuff, so I went to get them from the art classroom."
hi "And you need me to help with that."
show emi basic_grin
with charaenter
emi "Well… Rin told me you had already helped her so I thought you wouldn't mind."
hi "I see."
stop ambient fadeout 1.0
scene bg school_classroomart at bgright
with locationchange
play music music_another fadein 0.5
"So thanks to Emi's flaky logic, here I am again, collecting stuff from the art classroom for other people. "
"The room is empty apart from ourselves and the lonely specks of dust floating in the air. Emi skips straight away to the back wall, digging out a tiny, crumpled piece of paper from her pocket."
"While she tries to make sense of the scrawled handwriting, I take a closer look at the materials lying around here."
"Dozens of paint cans and bottles are arranged on the shelves in a most unorganized fashion."
"Some look like they have been left there for several decades; relics of previous art club generations."
"Next to the heavy stacks of neatly piled drawing paper are boxes full of different-sized brushes and unsorted crayons."
"The smells of paint, turpentine and fresh paper float in the stale air, mixing in my nostrils to form that unmistakable scent of art."
show emi basic_closedgrin at offscreenright
with None
scene bg school_classroomart at bgleft
show emi basic_closedgrin at right
with charamove
"Emi studies her notes, comparing them to markings on the various paint cans, and passes them to me as she finds the correct matches."
show emi basic_grin
with charachange
"She stretches her neck to look on the topmost shelf, but it's not quite enough."
show emi basic_annoyed
with charachange
"Her eye level stays below the shelf no matter what she does. Emi gives up and just looks up to the shelf longingly, like a child at a toy store, huffing in annoyance."
show emi annoyedbounce
with None
"After a moment of building anger, she starts jumping up and down, apparently trying to speed-read the labels during the fraction of a second she can see them, and catch what she can."
show emi basic_closedsweat at center
with charachange
"It's no surprise that she fails miserably, and almost manages to bring the entire shelf crashing down."
"Now I see why me lending a hand here would be useful."
hi "Come on, let me do that. You can't jump high enough, and I don't want you to hurt yourself trying."
hi "Also, I'm like twice your height."
show emi sad_angry
with charachange
emi "You are not!"
"She turns around, flaring scorn, flushed cheeks and all."
hi "Just kidding, just kidding. Anyway, I'll look up there, okay?"
show emi basic_annoyed
with charachange
"She glares at me one more time, but can't come up with a retort. With a grudging “hmph,” turns her back to me."
hide emi
with charaexit
"So I begin scrounging around the top shelf for paint while below, Emi crouches to scavenge what she can from the cupboards."
"I shake my head a little, after double-checking to ensure she can't see me do so."
"Emi having a complex about her height was a surprise; I wouldn't have joked about it otherwise."
"She seems easygoing, but I guess everyone has their weak spots."
show emi basic_grin at center
with shorttimeskip
"Only after we have almost all the items collected and spread out on a desk like a treasure hunter's spoils do I realize that it wasn't necessarily the height jab that got her riled up."
"She might not like to be told that she can't do something. Like jump."
"But Emi herself seems to have forgotten all about it already. Quick to anger, quick to forgive… she is that type of a person?"
"At least she doesn't seem to have taken anything to heart, as she chatters away happily while we pick up the rest of the items and then make our way back to Rin."
scene bg school_courtyard
show crowd
with locationskip
play ambient sfx_crowd_outdoors fadein 0.2
"I chivalrously carry the bulk of the materials as we make our way towards the dormitories."
show emi basic_annoyed at center
with charaenter
emi "Rin is really stressed about getting her painting done. It's her own fault though; she should've started earlier."
hi "Is she going to make it?"
show emi basic_closedgrin
with charachange
emi "No idea. It looks good to me, but with Rin, you never know what's going on."
show emi basic_annoyed
with charachange
emi "I found her this morning lying in front of the dorm in fetal position. She hadn't slept all night. I can't believe that the night nurses hadn't found her."
show emi basic_grin
with charachange
emi "And now she's painting again like crazy."
hi "Yeah, I've… noticed that she comes off as kinda… unhinged. So to speak."
show emi basic_closedhappy
with charachange
"Emi giggles at that, as well as at my likely too-obvious awkwardness."
show emi basic_happy
with charachange
emi "I don't mind it. She's just a little weird sometimes."
"On that I can agree with her. Unlike me, Emi seems to be cool with Rin's… whatever it is that feels so off about her."
"Still, they don't feel close like Misha and Shizune do. With them working as a single entity sometimes, it's hard to say where one ends and the other begins."
"Even though they're so different, just like Emi and Rin are."
"And Rin is the most different of them all, different from anyone else I've met."
hi "Yeah, I guess she's a very… unique person."
"I return to that word again, as if it encompasses Rin's personality by itself, but really it's just a substitute for a lengthy description of her oddities."
show emi basic_closedhappy
with charachange
"Emi giggles as I grasp about for a properly descriptive word."
show emi basic_grin
with charachange
emi "She's just weird."
show emi excited_proud
with charachange
emi "You know, earlier, she just spent half an hour sitting on her box."
emi "And stared at her toes."
show emi basic_closedhappy
with charachange
"She giggles again in a way that makes me think she doesn't know what's funny about it, it just is."
stop music fadeout 3.0
show emi basic_grin
with charachange
emi "All that time."
stop ambient fadeout 2.0
scene bg school_dormext_half
with locationskip
play music music_happiness fadein 2.0
"The working area is a mess, but the mural itself has taken over even more of the wall since I last saw it."
"The disfigured human figures have been mostly colored in tones of red, pink, and orange; weird, imaginary… things populating the spaces between."
"It looks… nice. I can't think of any word that would describe the work concisely and comprehensively so I settle myself on a nondescript “nice.”"
"But honestly, it seems that the area around the wall becomes untidier at the same rate as the mural progresses."
"The ground is littered with dozens of paint cans, various art supplies and empty soda bottles."
show rin negative_spaciness at center
with charaenter
"Rin herself is in the center of this chaos, standing there looking very cozy as if she was a natural part of the scene."
"Her pant legs have been rolled up to her knees, exposing her thin legs which sport a drying spectrum of war paintings, similar to those on Emi's face."
show emi basic_grin at offscreenleft
with None
show rin negative_spaciness at tworight
show bg school_dormext_half at bgright
show emi basic_grin at twoleft
with charamove
"Emi sprints to Rin ahead of me and gleefully jumps in front of her."
show emi basic_closedhappy
with charachange
emi "I'm back!"
show rin basic_awayabsent
with charachange
rin "That was fast. Did you run in the corridors again?"
show emi excited_proud
with charachange
emi "Hisao helped me."
show emi basic_grin
with charachange
"Emi points victoriously at me."
show rin basic_absent
with charachange
"Rin turns around following Emi's finger with her eyes, looking at my general direction."
show rin basic_deadpannormal
with charachange
"She nods absentmindedly at me. She looks like she hasn't slept since last night: a vacant, glazed stare that's focused slightly off me, and movements like in a slow-motion movie."
rin "Hello, Hisao. Thank you for the help."
hi "Don't mention it."
show rin basic_deadpan
with charachange
rin "I just did."
hi "Never mind."
hi "Looks like you've made progress. Looking good, as far as I can tell."
show rin basic_deadpannormal
with charachange
rin "But now you get more bad luck."
hi "I know, but I'm willing to take the risk."
show rin basic_deadpandelight
with charachange
rin "That's a very nice thing to say. For me, of course. Not for you."
show rin basic_awayabsent
with charachange
rin "This is why artists are always unlucky. They have to constantly look at their unfinished paintings."
rin "So artists can't find romance, their favorite TV shows are canceled, or they die young because of an unspecified disease. It's a deep and mysterious law of the universe."
show rin basic_lucid
with charachange
rin "Unless they are blind."
"She considers this for a while, looking like she's going to fall asleep."
show rin basic_absent
with charachange
rin "There is a boy."
show rin basic_deadpannormal
with charachange
rin "At the art club, you see. Blind boy. So he doesn't. See."
label en_A32a:
hi "You already told me."
show emi basic_hes
with charachange
"I glance sideways at Emi and she glances back in a way that tells she has heard this one before too."
"Neither of us says anything to Rin, though, so she continues her monotone soliloquy like an unfunny stand-up comedian."
label en_A32b:
show rin basic_awayabsent
with charachange
rin "He should become an artist. No bad luck, guaranteed."
rin "Don't you think that would be a good idea?"
show rin basic_lucid
with charachange
hi "That only blind people should become artists? No, not as such."
"…"
show rin basic_deadpan
with charachange
rin "You might have a point."
show rin negative_spaciness
with charachange
"Abandoning this train of thought, she turns again to consider her work and starts humming a tune that I think I recognize, but can't remember the name of."
show emi basic_closedgrin
with charachange
"Emi arranges the supplies we brought and moves a few paint cans around, trying to bring some organization to the scene."
show rin basic_awayabsent
with charachange
rin "Emi, I need the Prussian blue paint."
show emi basic_confused
with charachange
emi "Which one's Prussian blue…"
"She is staring helplessly at seven or eight cans, each with a different tone of blue."
show rin basic_deadpan
with charachange
rin "It's the one with Prussian blue paint in it."
show emi basic_annoyed
with charachange
emi "Geez, Rin! You're not helping at all!"
"I look around as well, even though I don't know what Prussian blue looks like, either. I wonder what blue has to do with Prussia."
"…Or what Prussia even is. The name sounds vaguely familiar, but I can't place it."
"While none of the blues looks more Prussian than the others, the small print on the labels is legible enough to determine that none say anything about the contents being Prussian."
hi "There is no Prussian blue here."
label en_A33:
scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None
"Emi heaves a sigh."
show emi basic_closedsweat
with charachange
emi "I guess I have to go back and get some."
show emi basic_grin
with charachange
emi "I promised to help with our class project, though, so I'll be back a bit later. Can you manage without it for a few hours?"
show rin basic_deadpannormal
with charachange
"Rin nods, and so Emi leaves."
stop music fadeout 2.0
hide emi
with charaexit
show rin basic_deadpannormal at center
show bg school_dormext_half at center
with charamove
"I stay because I like watching Rin paint, and because I have nothing better to do."
"I sit on a box and pick up today's book from my bag. It's a story about three guys drinking beer for two weeks straight and doing little else."
play music music_pearly fadein 2.0
hide rin
with charaexit
"Rin moves from the spot that was in need of the blue and starts slowly working on another."
"Her foot works the brush steadily against the plastered wall. Layers of paint on top of layers of paint. The mural slowly gains more form."
"I turn the pages at a leisurely pace. In this chapter they are drinking beer at the protagonist's friend's place. In the previous ones it was the protagonist's own apartment."
"It's not a page-turner kind of book, a slice of someone's imaginary life that makes me wonder why it had to be written."
"Why indeed. The reason for doing something creative… it's something incomprehensible."
"Like why Rin does paintings. It feels like she and Emi are the same, going squarely against their fates as if it's just out of spite."
"Rin even said something like that. “Do something you can't just because you can.”"
"Is that what she meant? Is that her reason? It might be Emi's, she comes off as quite a headstrong person."
"Rin doesn't give off that kind of an air. Thinking about it, she doesn't give off any kind of air, or maybe a different kind every time I talk with her."
"Why did she say what she said? Why does she, or anyone at all paint, or draw, or sculpt, or write?"
"I've never had much of a creative impulse so I don't think I can really understand it."
"It makes me feel hollow inside."
"What a grim thought. I can't really decide whether it's true or not, either."
"Am I content being this way? I can't deny I'm feeling a little bit envious of Rin, but I can't really consider it a flaw of any kind."
"I'm myself and she is herself."
"Still, I do need to find something. Something that could… make me feel a little less lost about myself, instead of just drowning myself in these books as I did in the hospital."
"I can't help but feel disoriented; the new school, lifestyle and people around me contribute heavily to this sensation."
"I'm trying my best to fit into existing social circles, and most of the people I've met have been really nice."
"It still feels like I'm an outsider, though; like I don't belong."
stop music fadeout 2.0
"I shake the feeling off, realizing that I'm spacing out. I have neither turned a page of the book, nor done anything for Rin."
"She is trying to pour some paint from a big can using only her feet, having not bothered to ask me. Or maybe she did, and I didn't hear it."
"Either way, it looks very unstable."
scene bg mural_part
show rin basic_awayabsent_close at tworight
with locationchange
play music music_soothing fadein 0.5
"I quickly jump to help her, as it looks like she's about to spill the entire contents of the can all over the pavement."
"I take the can from her feet and pour some in the bowl."
show rin basic_absent_close
with charachange
"She doesn't say anything, and neither do I. I catch a glimpse of her eyes, looking silently at me from under her unkempt bangs."
"It's an unreadable expression, a perfect poker face, mixed with a hint of something like a mild surprise."
"I wonder what she is thinking. Maybe she is wondering about what I'm thinking. Maybe nothing."
hi "A penny for your thoughts."
show rin basic_deadpan_close
with charachange
rin "Do you have any pennies with you?"
hi "I don't think I do."
show rin basic_deadpancontemplation_close
with charachange
rin "Then I don't think I will tell. I'm not thinking anything either, so you're in luck. Except now I just did."
"She frowns, looking very unsatisfied."
rin "It's hard to not think about anything. But it's important."
"I'm about to ask why it's important when some old guy walks up to us, looking like he has some business with Rin."
scene bg school_dormext_half at bgright
show nomiya smile at center
with locationchange
no_ "Good afternoon. How's it going?"
show nomiya smile at twoleft
show bg school_dormext_half at center
with charamove
show rin basic_awayabsent at tworight
with charaenter
rin "I can make it."
"Rin doesn't take her eyes off the wall and responds so naturally that I can only assume they know each other."
"I haven't seen the man before, so I naturally wonder who he might be. Maybe a teacher?"
"His hair has faded to a silvery gray, so much so that it looks artificially dyed. I hope that's not the case."
"Small round glasses hang on the bridge of his nose, but it appears he's constantly looking over the lenses, rather than through them."
"He's studying the mural intently over said glasses."
show nomiya talk
with charachange
no_ "Good, good."
no_ "What bold composition you have here!"
"He moves to inspect the mural closer, talking to himself about it in a way that makes it obvious he wants us to hear it too."
show nomiya veryhappy
with charachange
no_ "Very good, very good indeed…"
"I don't really know what to make of it but Rin doesn't seem to care much. She's looking around her working space, the various bowls of different tones scattered all over."
show rin basic_deadpan
with charachange
rin "Hisao."
hi "Hmm?"
show rin basic_deadpannormal
with charachange
rin "A little more of this."
hi "Give me a second."
"I pour a 50-50 mix of two paints into the bowl to create more of the same pale pink tone Rin was using to fill up the shape of a man's face."
"Rin watches me doing so, which makes me feel nervous somehow. Her face is so unassuming that it feels she's just waiting for me to do something wrong."
"The man turns to reckon me as well, looking surprised as if he noticed my presence only just now."
"…Maybe he did."
show nomiya talk
with charachange
no_ "Why, hello there. Who might you be?"
hi "Ah, I'm a transfer student to class 3-3. Hisao Nakai. Nice to meet you."
show nomiya frown
with charachange
no_ "Mutou's class, eh? Well, I won't hold that against you!"
play sound sfx_birdstakeoff
show nomiya veryhappy
with vpunch
"He laughs very loudly. Obnoxiously loudly. A few small birds take flight from a nearby tree."
show nomiya talk
with charachange
no_ "I'm Shinichi Nomiya, the art teacher."
"So this is the art teacher. In retrospect, should have guessed that much. He even looks like one, as far as first impressions go."
show nomiya smile
with charachange
no "How did you come to end up assisting my protégée?"
label en_choiceA33:
menu:
    with menueffect
    "I wish I knew…"
    "I just kinda stuck with her, I think.":
        return m1
    "I'm interested in the art club.":
        return m2
label en_A33a:
hi "I guess I'm a little interested in the art club."
"I blurt it out, partially inadvertently."
show nomiya talk
with charachange
no "What do you mean?"
hi "Nothing… specific."
hi "I wonder if I could come by sometime. Even if it's just to observe or something."
hi "I've been thinking that I should join some club or something, so…"
"It's in no way a premeditated move, but a vague sense of determination has really been building inside of me for this past week."
"I want to do something. I want to belong somewhere."
"It might as well be the art club, my shortcomings notwithstanding."
"The teacher seems pleased."
show nomiya veryhappy
with charachange
no "Oh? You want to join? Well, we always welcome new people, of course."
no "Club meetings are normal enough. We study various aspects of the fine arts and try our hands at them, as well."
show nomiya frown
with charachange
no "Or feet."
"He gives an embarrassed cough, but Rin doesn't seem to mind. I take a small amount of comfort from the fact that I'm not the only one with vocabulary difficulties in this school."
"Nomiya rebounds from his faux pas by theatrically checking the time from his huge, gleaming pocket watch, and slaps his forehead even more theatrically."
show nomiya veryhappy
with charachange
no "I really must take my leave now, but if you have questions, I'm sure Tezuka can clarify."
"Somehow, mentioning “clarify” and Rin in the same sentence doesn't feel right. However, I don't say as much to the teacher, since he seems to be in a hurry."
show nomiya smile
with charachange
no "Tezuka, I'm pleased to see that this little project is going so well."
show nomiya talk
with charachange
no "I just stopped by to remind you to not run off by yourself, tomorrow. I've invited certain people to the festival for you, and I'm sure they'd like to meet you as well."
show nomiya smile
with charachange
no "I hope I'll see you on Monday, then, Nakai."
stop music fadeout 6.0
hide nomiya
with charaexit
show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove
"The teacher leaves, and we are left by ourselves again. Rin is still painting as if nothing notable happened. Since nothing in fact did, I am left wondering what on Earth is wrong with me."
"Art and I haven't worked well together in the past, at least judging from the grades I used to have in middle school."
"Maybe a club will be different than an obligatory class. Who knows?"
"I try to come up with something meaningful to ask about it, but to no avail."
"I'll just go to a club meeting and see how it goes."
hi "So he invited some people tomorrow just to check out your painting?"
show rin basic_absent
with charachange
rin "He has a lot of art-people friends. They like to talk about art."
show rin basic_awayabsent
with charachange
rin "I think he wants me to talk about art with them."
hi "Somehow, I get the feeling that you aren't too thrilled about it."
"Rin shrugs noncommittally, but it still gives an impression of her general displeasure at the idea of having to discuss her painting, or any painting, with other people."
show rin basic_deadpan
with charachange
play music music_rin fadein 5.0
rin "I don't really like talking about art. It is already a way to talk without talking, so why bother talking about it?"
hi "I can understand that."
show rin basic_deadpannormal
with charachange
rin "It's like being bored and talking about being bored, because you are bored."
hi "I'm not following you."
show rin negative_spaciness
with charachange
rin "Have you ever talked about being bored? It's pointless and not very exciting. All you can really say about it is “I'm so bored.” I once spent a week trying to think of something meaningful to say about boredness."
rin "It was the most boring week I've ever had."
hi "But that's pretty fitting, don't you think?"
show rin basic_deadpan
with charachange
"Rin gives me a look, the laconic kind that looks like it doesn't mean anything but it does."
hi "Anyway… I don't know, I guess I just rarely can come up with anything to say about art."
hi "I mean, like this one you're doing now. I have no idea what to think about it, except that it looks nice. What is this painting about?"
show rin basic_deadpannormal
with charachange
rin "It's not about anything at all."
"…"
show rin basic_deadpandelight
with charachange
rin "That's what I'd like to say. So I did. "
show rin basic_deadpannormal
with charachange
rin "But that was a small lie. I said it anyway because I would kind of like it to be true."
rin "Teacher wanted me to do this, but I didn't have any ideas. I tried to have some, but nothing happened."
show rin negative_spaciness
with charachange
rin "So now this is a painting without any ideas."
hi "But… what are you painting then?"
show rin basic_absent
with charachange
rin "No idea."
show rin basic_delight
with charachange
rin "Come to think of it, I think I'll call this “No idea.”"
show rin negative_worried
with charachange
rin "Ah, now I started thinking again. This is bad."
show rin basic_absent
with Dissolve(0.15)
show rin negative_worried
with Dissolve(0.1)
show rin negative_worried
with Dissolve(0.05)
show rin basic_absent
with Dissolve(0.05)
show rin negative_worried
with Dissolve(0.05)
show rin basic_absent
with Dissolve(0.05)
show rin negative_worried
with Dissolve(0.05)
show rin basic_absent
with Dissolve(0.05)
show rin negative_worried
with Dissolve(0.1)
show rin basic_absent
with Dissolve(0.15)
show rin negative_worried
with Dissolve(0.5)
"She shakes her head vigorously for a while, trying to shake “thinking” out of her head. That amber-red hair flies wildly around."
show rin basic_deadpannormal
with charachange
rin "This is why I had Emi help me. She makes it easy to not think about anything."
rin "You know, how she just talks talks talks about nothing for hours. It's like her head is made of bubblegum foam bath jelly."
show rin basic_deadpandelight
with charachange
rin "You are kinda the same, but not really. It's very helpful if you stay here."
stop music fadeout 5.0
"I am not sure if that's a compliment or not. It's probably neither; with Rin being the overtly neutral person she is."
hi "So is there anything specific you'd like me to do to make you not think?"
show rin basic_deadpan
with charachange
rin "Just be."
hide rin
with charaexit
"So without knowing what I should do, I just sit on an empty box to watch her continue with the painting, idly leafing the pages of the beer-drinking book."
play music music_dreamy fadein 1.0
scene bg mural_part
show rin negative_spaciness_close at tworight
with locationchange
"Rin has a serene expression on her face, her dark green eyes hiding what she might think behind them. No wait, she's supposedly not thinking anything, right?"
"She quietly hums to a tune, interrupting every now and then with polite requests for more paint or another kind of brush."
"Her concentration is admirable, even though she seems to be sleep-deprived and under pressure to finish the job."
"Inch by inch the painting gains more form, details being added on top of details, colors entwining with each other, filling the empty spaces, growing on top of each other."
"I find myself thinking about inspiration and motivation to create art again."
"Where does one get ideas? They don't come out of nowhere, and I don't think there are muses that magically inject some inspiration in your head."
"Ideas have an origin and a purpose."
"The more I think about it, the more I'm convinced that Rin is lying about her mural, or at least twisting the truth. Maybe she doesn't even realize it, herself."
"You can't do anything creative without having an idea of what you are going to create. That would go against the definition."
"Every stroke must be decided to be drawn. Even if it's made at random, then that, too, is a conscious decision."
"So her painting, even this one, must be based on having some deliberate goal or idea of what to paint."
"If Rin's idea is to have no idea, as she said, does that count as having an idea?"
"A logical paradox? That seems to be Rin's modus operandi for most normal interactions, so it wouldn't surprise me if she hadn't even noticed this herself."
"I wonder if I should bring it up, but I'm not sure if I want to engage in an argument about logic with this girl."
"One of us would probably end up short-circuiting fairly quickly, so I discard the thought."
show rin basic_awayabsent_close
with charachange
show rin negative_spaciness_close
with charachange
"Rin is squirming and shuffling restlessly."
show rin negative_annoyed_close
with charachange
show rin negative_spaciness_close
with charachange
"Even her usual blank visage breaks occasionally into pretty difficult looking expressions, the kind that one doesn't just come up with accidentally."
show rin negative_annoyed_close
with charachange
hi "Everything all right?"
rin "Yes. No."
rin "My back started hurting again."
rin "This painting is too big, after all, and it's hard to paint in this position."
hi "Want to take a break?"
show rin basic_deadpanupset_close
with charachange
rin "After I finish this part."
show rin negative_annoyed_close
with charachange
"Of course, she doesn't take a break, and I don't bring it up again because that would be completely and utterly pointless."
scene bg school_dormext_half_ss
with locationchange
"Rin continues her work and I stay with her: I like to watch her paint, and I'm going to be a member of the same club she's in, now."
stop music fadeout 4.0
$ renpy.music.set_volume(0.5,0.0, "ambient")
play ambient sfx_cicadas fadein 3.0
scene bg school_dormext_full_ni
with Dissolve(3.0)
"When she declares the mural to be finished, it's already so dark that I have no idea how she can tell."
"There is no celebration, no general sense of a job well done, just a tired and laconic “I'm done” and then we both go to sleep."
stop ambient fadeout 3.0
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A33b:
hi "I keep wondering that myself. The lack of anything better to do, probably."
show nomiya veryhappy
with charachange
"He lets out a hearty laugh, then checks his watch."
show nomiya smile
with charachange
no "I really must take my leave now. Tezuka, I'm pleased to see that this little project is going so well."
show nomiya talk
with charachange
no "I just stopped by to remind you to not run off by yourself, tomorrow. I've invited certain people to the festival for you, and I'm sure they'd like to meet you as well."
show nomiya smile
with charachange
no "Also, Monday's club meeting is off, since I'm going out of town. I guess you kids can do something among yourselves, if you want to."
hide nomiya
with charaexit
stop music fadeout 4.0
show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove
"He leaves, turning around flamboyantly, then walking off as dramatically as it's possible to walk."
"What a weird teacher."
hi "I'll be off, too. See you around, Rin."
"Holding up a hand, I turn to go up the stairs to the dorms."
"Maybe, if I can finish reading these books today, the entirety of tomorrow will be free for the festival."
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A34:
scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None
stop music fadeout 6.0
show emi basic_closedgrin
with charachange
emi "We need to go get more, then."
"I open my mouth to say that actually, we're not both needed for such a simple task like finding another pot of Prussian Blue, but Emi's already grabbed my arm and started dragging me off."
hide emi
with charaexit
"I wave to Rin, who doesn't seem to have noticed that the two of us are even leaving."
play ambient sfx_crowd_outdoors fadein 0.5
scene bg school_courtyard
show crowd
with locationskip
"Well, she'll notice when she goes for her Prussian Blue and finds out it's still not there."
scene bg school_lobby
show crowd
with locationskip
play ambient sfx_crowd_indoors fadein 0.5
"Maybe."
scene bg school_staircase2
with locationskip
"…"
scene bg school_hallway3
show crowd
with locationskip
"Probably not, actually."
stop ambient fadeout 2.0
scene bg school_classroomart
with locationskip
"While I'm busy thinking of how weird Rin is, Emi's been dragging me back to the art classroom."
"I feel myself starting to run out of breath."
hi "What's the rush?"
show emi basic_confused at center
with charaenter
emi "Huh?"
"Emi's giving me an appraising look, as if she's trying to figure something out."
hi "It's just that you seem to be in a hurry."
hi "I'm not sure I can keep up."
"Comprehension dawns on her face."
play music music_emi fadein 0.3
show emi excited_proud
with charachange
emi "You're not out of breath, are you?"
"There's almost an accusing playfulness to her tone."
"I'm tempted to deny it, but then I realize that I've been breathing heavy since we stopped."
"Guess it's kind of obvious."
hi "A little. Not everybody can be in shape, you know."
hi "Takes all kinds, right?"
show emi basic_annoyed
with charachange
"Emi frowns. It's not a particularly good frown."
hi "Er, that is…"
hi "I should… get in shape?"
"Not that I hadn't already decided to try for that."
"After that flutter on the track I figure there's a real need to get in some sort of running habit."
"I was, after all, feeling pretty good until I had my false alarm."
"Well, actually I wasn't. But it was… fun?"
"Meanwhile, my comment seems to have helped Emi come to some sort of a decision."
show emi basic_closedgrin
with charachange
emi "Well, that's it, then."
stop music fadeout 1.0
show emi basic_annoyed
with charachange
"She gives me a serious look."
emi "You're joining me."
"…"
hi "I beg your pardon?"
show emi basic_grin
with charachange
emi "In the mornings."
emi "You and I are now running partners."
show emi basic_closedhappy
with charachange
emi "I've got a routine all planned out. In fact…"
play sound sfx_paper
"She produces a crumpled sheet of paper."
show emi excited_amused
with charachange
emi "I've got it right here with me."
play music music_running
"I take the sheet of paper and give it a once-over."
"Times, dates, and laps, all laid out."
"A slow increase from just a few laps a day to…"
"My God, does she expect to have me running marathons?"
"And where did she find the time to get this all together?"
"And how long has she been planning this, anyway?"
hi "You've been planning this?"
show emi sad_shy
with charachange
emi "A little."
show emi sad_grin
with charachange
emi "But it's really the nurse's idea!"
show emi basic_closedgrin
with charachange
emi "He told me to keep an eye on you to make sure you exercised like he told you to!"
label en_A34a:
"A vast conspiracy?"
"Maybe Kenji's on to something here…"
hi "This seems a bit much for just “keeping an eye on me.”"
show emi sad_grin
with charachange
emi "Well, to be honest I've been trying to find a running partner in the mornings for a while now."
"My God, Kenji! If you could only see the scheme unfolding!"
hi "What do you need a partner for, anyway?"
show emi basic_annoyed
with charachange
emi "It's easier to keep up a workout if you're not the only one doing it."
emi "Isn't that obvious?"
emi "You're less likely to quit if someone else is counting on you to be there, right?"
hi "I see. And this won't only keep you running, but it'll make sure that I keep running as well."
hi "Meaning that I'll be obeying the nurse…"
show emi excited_proud
with charachange
emi "…and I'll be keeping an eye on you just like he asked!"
show emi basic_closedgrin
with charachange
emi "You caught on quick, Hisao."
hi "And if I refuse?"
"I have no intention of refusing, of course."
"But I've got to at least put up a token resistance to such a masterfully executed plan."
show emi basic_grin
with charachange
emi "Well, if you refused I'd have to pout."
emi "And you'd have to live with being the guy who made Emi Ibarazaki pout."
show emi basic_closedgrin
with charachange
emi "You don't want that on your conscience, do you?"
show emi sad_depressed
with charachange
"As if to demonstrate, Emi begins pouting."
"It is the most adorable, heart-wrenching thing I've ever seen."
hi "Okay! I'll do it!"
hi "Just… don't do that!"
hi "I feel like I just hit a puppy!"
show emi basic_closedgrin
with charachange
emi "So it's settled, right?"
emi "You're going to be my running partner?"
emi "Follow the workout?"
emi "And the dietary plan?"
hi "Dietary plan?"
show emi basic_grin
with charachange
emi "Yeah, the dietary plan!"
show emi excited_proud
with charachange
emi "You've got to eat healthy if you're going to get in shape, you know!"
"I examine the workout routine closely."
hi "I don't see a dietary plan on here."
show emi basic_shock
with charachange
emi "Oh right! I forgot to give that to you!"
play sound sfx_paper
show emi excited_amused
with charachange
"Another crumpled sheet of paper is produced and handed over."
"It's somewhat less detailed."
show emi excited_happy
with charachange
emi "I had the nurse help me come up with it."
"The amount of dedication that the nurse has to keeping me in good health is pretty overwhelming."
"I don't know many school nurses who would get one of their students to spy on me, much less help come up with a dietary plan."
"Then again, I guess I'm not in a normal school."
"And maybe that's not such a bad thing."
"Then again, this dietary plan seems to cut out just about everything that'll be offered at the festival tomorrow."
"Hmm."
hi "So when does our running start?"
show emi basic_grin
with charachange
emi "After the festival."
hi "Right after? What if I've had something to eat there? I could get a stomach ache, you know."
show emi basic_annoyed
with charachange
emi "I meant the day after the festival."
hi "I knew that."
"Wasn't there something we were supposed to be doing?"
hi "Oh! I guess we should get that paint for Rin, huh?"
show emi basic_shock
with charachange
emi "Oh no! It slipped my mind!"
stop music fadeout 8.0
scene bg school_dormext_half_ss
with shorttimeskip
"By the time we get the paint and get back to the mural, Rin's already wandered off."
"Oh well."
"Emi and I both decide to part ways there, leaving the paint on the ground."
"Rin'll find it. Whenever she comes back, anyway."
scene bg school_dormhisao
with locationskip
"Festival's tomorrow. I'm actually a little excited for it."
"At the same time, the week's left me feeling pretty tired, so I read a little and then go to bed."
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A34b:
stop music fadeout 1.0
"Damn, why do all these people insist on meddling with my matters? I guess the nurse is allowed, even obliged but…"
hi "You know, I don't think that would be a good idea."
hi "This is my problem, I don't really want to make anyone else involved."
hi "I gotta figure it out myself."
show emi sad_depressed
with charachange
emi "Are you angry about yesterday?"
"She's pouting, looking distantly like a hurt puppy. I couldn't be angry now, even if I wanted."
hi "No, it's not that. If anything, it was my own fault."
"I lean against the wall, looking away from Emi."
hi "I just… I don't know, it feels like a bad idea."
label en_A35:
scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None
"But why would Lilly leave her to her own devices? It seems to be quite out of the ordinary, going by Hanako's reaction."
"…"
"…Ah, that's right. I think Lilly mentioned something about going into town today before Rin bumped into us."
"The thought of that walk makes me look outside."
$ renpy.music.set_volume(0.5, 1.0, channel="music")
scene bg misc_sky at Fullpan(15.0)
with locationchange
"The bright sun and occasional people wandering around and enjoying the afternoon make me yearn to get out of school, or at least do something other than sit here."
"Giving in to one of my worst vices, procrastination, I decide that history is a subject best studied on a Sunday. Or a Monday. Or on any day other than this one."
"I give a grunt as I lever myself out of my seat, briefly debating with myself whether or not to hang out with Kenji."
"He doesn't strike me as the “enjoying the nice weather outside with others” kind of person, really. I guess I'll catch up with him later."
$ renpy.music.set_volume(1.0, 1.0, channel="music")
scene bg school_scienceroom at bgleft
with Dissolve(1.5)
"Changing tacks, I briefly entertain the idea of talking with Hanako, but by the time I look at her seat, it's vacant. She must've left for the library."
label en_choiceA35:
menu:
    with menueffect
    "There's got to be something to do that can kill the time…"
    "Go for a walk into town.":
        return m1
    "Go to the library.":
        return m2
label en_A35a:
"Following Hanako to the library seems a bit intrusive. There was a reason she left the classroom, after all."
"And that aside, I do want to catch up with Lilly. At the very least, I'd like to thank her for looking out for me despite her other, obviously taxing, duties."
"I guess I'll walk around town. With any luck, I should be able to find Lilly. The exercise'll do me some good, as well."
play music music_tranquil fadein 3.0
scene bg school_courtyard
with locationskip
"Walking through the school courtyard to the gate, I give a small nod to a couple of passing classmates, the gesture being returned in kind."
"Even from here, the shouts of the sports club members can be heard. From the sheer volume of the din, the track must be packed right now."
"I remember what Lilly said yesterday about being dropped right into the middle of a busy time for the school."
"While I'm trying to get my bearings and catch up on study that I've missed, everyone else is doing normal school activities. The feeling of being a foreigner still hasn't dissipated. At least, not yet."
"Well, I guess not everything's bad."
"This is a private school, and that much is easily noticed when walking around outside. Not only are the school grounds huge, but the buildings themselves are immaculate and quite divorced from the dime-a-dozen concrete blocks of public schools."
"There's also the fact that there's a much stronger feeling of community here, or at least a friendlier atmosphere. At my old school, it was generally accepted that people would keep to their little clique and be done with it."
scene bg school_gate
with locationchange
"Eventually I reach the gate, and begin to walk down the road and into town."
scene bg suburb_roadcenter
with shorttimeskip
"Well, that was fairly productive."
"Having seen a fair portion of town, even including the houses perched on the hills around the outskirts, I decide to take a walk around the park before heading back."
"Living in the city all my life, the total lack of smartly-dressed businessmen and fashionably-dressed girls strikes me as incredibly unusual."
"All that's to be seen are the odd elderly person shuffling along the sidewalk and assorted busily chatting pairs of middle-aged women outside of small storefronts."
stop music fadeout 8.0
"Walking along the road to the park quickly distracts me from them, though, making me realize that I perhaps pushed myself further than I should have done to see as much as I could."
"As my breath begins to wheeze and my chest tightens more and more, I give up on the prospect of soldiering on."
play ambient sfx_parkambience fadein 1.0
scene bg suburb_park
with locationskip
"After a quick glance around the park as I enter, I take a seat on a wobbly old bench that I notice near a couple of vending machines."
"For minutes on end I sit with my head bent over, forcing myself to take deep breaths. I feel more like an old man than a teenager who should be in the prime of his life."
"The stay in hospital, the surgery and the medications must be taking their toll on me. Dammit."
"Eventually, my breathing returns to normal and the muscles in my chest loosen, not without a fair measure of relief. I guess this means the end of my little sojourn though, in any case."
stop ambient fadeout 1.0
scene bg suburb_shanghaiext
with locationchange
"There's a café on the far corner, so I'll stop by to quench my thirst before heading back."
play sound sfx_storebell
scene bg suburb_shanghaiint at bgright
with locationchange
play music music_dreamy fadein 2.0
"A little bell above the door signals my arrival to an empty counter."
"For a few moments I stand there waiting, my eyes every now and again drifting from one end of the counter to the other searching for a service bell."
show yuukoshang neutral_down at center
with charaenter
"Eventually a door some ways behind the counter opens, the person emerging from it taking me by complete surprise."
hi "Yu… Yuuko?"
hi "Hi, I had no idea you worked here."
"I really have no idea how to address her either, given that she is technically school staff as well as, apparently, a waitress."
show yuukoshang neurotic_up
with charachange
yu "Ah, yes, um…"
"She quickly paces up to the counter, before flinging her upper half downwards in an overacted bow."
show yuukoshang closedhappy_down
with charachange
yu "Welcome to the Shanghai! May I take your order?"
"Straight down to business, I see."
hi "I don't know… well, some coffee, please?"
show yuukoshang neutral_down
with charachange
yu "Yes, certainly. I'll make it right away and bring it to you when it's done."
hi "Uh, thanks."
"Yuuko's formality takes me aback. She seems to take her job very seriously."
hide yuukoshang
with charaexit
"Obeying her instructions, I turn around and quickly glance around for a free table. Considering the café seems to be empty, this is a simple task to accomplish."
show bg suburb_shanghaiint at bgleft
with charamove
"As I walk towards a table adjacent to the window, I notice a flash of yellow around one of the table dividers."
show lilly basic_smileclosed at twoleft
show akira basic_lost at tworight
with charaenter
"Sure enough, no more than a glance is needed to ascertain that it's a certain Satou at the table. That said, I don't recognize the suited figure across the table from her."
"Blonde, fair-skinned and only a little shorter, he… she? I think she, must be a relative."
"Since the two are all but silent as the suited figure takes a swig from a cup of coffee, I decide to greet Lilly. Some part of my coming here was in order to meet her, after all."
hi "Hi, Lilly."
show lilly basic_smile
with charachange
li "…Hisao?"
hi "Yeah. Nice to see you again."
show akira basic_smile
with charachange
"The suited girl looks up, noting my uniform with a relaxed smile."
aki_ "Know each other?"
hi "I… guess."
"It's as good an approximation of our relationship as I can think of."
show lilly basic_smileclosed
with charachange
li "Hmm… care to take a seat?"
"She says this to the air beside me, but the message is clear enough and I take a seat beside her."
show lilly basic_weaksmile
with charachange
li "I suppose some introductions might be in order."
show lilly basic_smile
with charachange
li "Hisao, this is Akira Satou, my older sister. Akira, this is Hisao Nakai, another Yamaku student."
"Looks like my guess was correct. The newly-introduced Akira gives a nod, which I return."
"What I don't return however, is the almost analytical gaze with which she looks me over."
show lilly basic_smile at left
show akira basic_smile at right
with charamove
show yuukoshang neutral_down at center
with charaenter
"As she does so, Yuuko walks up to the table and carefully places the coffee on the table before bowing and taking her leave."
hide yuukoshang
with charaexit
show lilly basic_smile at twoleft
show akira basic_smile at tworight
with charamove
"Gently bringing my hand to the side of the cup, I realize that it's already at just the right temperature to drink. After taking a sip, the flavor turns out to be just as good as the temperature."
"Yuuko seems a lot better at this than being a librarian."
"I take a good, long drink before relaxing into the seat."
"It takes mere seconds for Akira's examination to come to an end. Apparently becoming quickly bored with the activity, she turns to her sister."
show akira basic_boo
with charachange
aki "So, how's school recently?"
"It seems Akira is entirely unconcerned with someone she doesn't know at all listening to everything they say."
"Not that I mind. Leaving them to their chatting, I sit back and continue drinking the pleasantly aromatic coffee."
show lilly basic_smileclosed
show akira basic_smile
with shorttimeskip
aki "Sounds like it's pretty busy for ya, then."
show lilly basic_smile
with charachange
li "At least I'm not cooking your meals after school any more."
"As they talk, I slowly realize that I'm entirely unable to gauge Lilly's emotions through her eyes; as I would for any other person."
"It becomes slightly unsettling as I subconsciously focus on that fact."
show akira basic_lost
with charachange
aki "Whoa, so cold. Weren't ya just cooking for yourself anyway? I only ever got leftovers."
show lilly basic_displeased
with charachange
li "That's not the point… are you managing to feed yourself, at least?"
show akira basic_resigned
with charachange
aki "I can cook without blowing myself up, you know."
show akira basic_annoyed
with charachange
aki "Mostly."
show lilly basic_listen
with charachange
li "That's…"
show akira basic_laugh
with charachange
aki "Hahaha! It's fine, it's fine. I needed to learn sometime anyway."
show lilly basic_listen at left
show akira basic_laugh at right
with charamove
show yuukoshang neurotic_up at center
with charaenter
yu "Ah, Lilly?"
show lilly basic_smile
show akira basic_boo
with charachange
"Everyone present is momentarily distracted by Yuuko, who places a cup of tea on the table for Lilly."
hide yuukoshang
with charaexit
show lilly basic_smile at twoleft
show akira basic_boo at tworight
with charamove
"Taking the moment to glance at her watch, Akira levers herself off her seat and gives me a quick nod."
show akira basic_smile
with charachange
aki "Well, I'd better be off. It was nice talking to ya, Lilly."
show lilly basic_oops
with charachange
li "Akira, do you have to…"
"Lilly looks genuinely mournful at her sister suddenly leaving. It does seem like she might have the wrong idea."
show akira basic_resigned
with charachange
aki "Sorry, I need to get back to work. They'll be on my neck again if I don't make it back quickly."
"So informal… Akira's trim and tidy appearance would give anyone the wrong impression of her."
show lilly basic_concerned
with charachange
li "Bye, Akira…"
show akira basic_smile
with charachange
aki "C'mon, don't look so down. I'll be around again soon. Seeyas."
hide akira
with charaexit
"With that, she waltzes out of the Shanghai with her hand held high."
"Lilly still looks pretty depressed, so I try to make some small talk in an effort to take her mind off it."
show lilly basic_concerned at center
show bg suburb_shanghaiint at center
with charamove
hi "She seems nice."
show lilly basic_displeased
with charachange
li "We used to live together, but now that I live at school we hardly ever see each other."
"Despite Lilly having been quite affable, I still don't really know much about her. In hindsight, it's surprising just how much she's extracted from me, really."
hi "You used to live together? Was it somewhere around here?"
li "It was pretty far south, so the trip into Yamaku was fairly long."
show lilly basic_reminisce
with charachange
li "With her working hours getting longer and Yamaku being so far away, there was little choice in the end but to move into the dormitories."
"Well, that explains the chatter about cooking. Evidently regaining her composure, she livens back up… at least, in part."
show lilly basic_weaksmile
with charachange
li "I take it you're better rested, now?"
hi "Sorry?"
show lilly basic_smileclosed
with charachange
li "You sound less exhausted than you did when you first came in."
"To be able to pick out my breathing like that… she must have pretty good ears."
hi "Yeah. Ended up walking all over town, despite only planning on taking a short walk down here."
"Reminded of my thirst from the walk, I lean forward to take a sip."
play sound sfx_teacup
"Without further ado, Lilly starts on her cup of strong-smelling tea."
"I guess I'd better get going back to Yamaku. There's only so long I can stall studying for, and I want to get a good night's sleep before the festival."
stop music fadeout 4.0
"Standing from my seat, I take the coffee-stained cup from the table."
show lilly basic_surprised
with charachange
li "You're leaving?"
hi "Yeah. You going to head back as well? It's getting kind of late."
"For a moment she pauses, before lifting her face over her teacup as if she was looking at me."
play music music_lilly fadein 3.0
show lilly basic_smile
with charachange
li "Yuuko, could we have one more coffee please?"
yu "Okay, I'll bring it right away!"
hi "That's… not subtle."
show lilly basic_giggle
with charachange
"She gives a short giggle at my frank assessment of her maneuver. It's surprisingly childish and carefree, given her otherwise collected appearance."
"In the end, though, I have little reason to refuse. To be honest I can hardly say no, all things considered."
"Giving a manufactured sigh, I take a seat opposite her."
hi "Wanting company, then?"
show lilly basic_cheerful
with charachange
li "Hmm… I'd say that it's more that I was wondering…"
"I see she's in questioning mode, again. She does seem to be unusually interested in me, or at least curious."
show lilly basic_smile
with charachange
li "Do you have any siblings?"
"Not exactly an unexpected tangent."
hi "No, only child. To be honest, the idea of having someone that close makes me a bit envious."
show lilly basic_smileclosed
with charachange
li "Interesting…"
"I raise an eyebrow, which of course goes unseen. The short silence communicates the question well enough."
show lilly basic_smile
with charachange
li "It's just that others have said the same thing before."
li "It's a difficult subject to try and think about objectively, given that I've always had someone like that."
"I can mostly understand what Lilly means, given that it would be hard to place oneself outside of a situation they've been in all their life."
"She and her sister must have a pretty close relationship."
"Taking pains to interrupt us as little as possible, Yuuko dutifully comes over and places a cup on the table."
"Lilly thanks her as I sit back, taking in this vexing girl in front of me."
"Despite always seeming to be on her guard and in control of herself when talking to others, she has an almost childlike curiosity about other people."
"That said, those rare moments she seems to slightly lower her guard are the most insightful into how she thinks."
"Reaching forward for my drink, I realize something I probably should've noticed earlier."
"…I think I'm starting to become kind of curious about her."
stop music fadeout 2.0
scene bg school_gate_ni
with shorttimeskip
play ambient sfx_cicadas fadein 0.5
"Despite making a good pace, it's already nightfall by the time I reach the large iron gates in front of the school."
"While it's nice to have plenty of time to wander around by virtue of living right next to the school, I can't help but get the feeling that very few students actually take the opportunity."
scene bg school_courtyard_ni
with locationchange
"Compared to the number of students I see milling around on-campus during free time, it's startlingly rare to see anyone around town."
"Given the large number of accommodations and facilities that the school offers, many of them might simply not see any point in venturing outside, let alone people such as Hanako and Kenji."
"It makes me wonder if students like Shizune, Misha, and Lilly are the exception for this school, rather than the norm."
stop ambient fadeout 1.0
scene bg school_dormhallway
with locationskip
"As I wander back to my dorm room, I continue to compare my old school with Yamaku. As I do so, I begin to be surprised that I managed to get even this used to everything that's happened to me."
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
label en_A36:
window hide None
scene black
with dissolve
play sound sfx_doorknock
scene bg school_dormhisao
with openeye
window show
"At five minutes past eight, an unbelievably loud banging jolts me awake. It's coming from outside my door."
scene bg school_dormhallway
show shizu behind_blank at tworight
show misha hips_smile at twoleft
with locationchange
play music music_comedy fadein 0.3
"Quickly, I open the door to see Shizune and Misha standing side-by-side before me. Both of them look a little worn out, although it's more noticeable on Misha."
hi "Which one of you knocked?"
"I ask, echoing the question that must be on the mind of everyone in the entire building."
show misha hips_grin
with charachange
mi "Ahahaha, that's not important, Hicchan!"
"She quickly dismisses it without even batting an eye."
show misha hips_smile
with charachange
mi "Oh? You're still in your pajamas, Hicchan? So you don't wake up at eight?"
"I notice her hair is wet. Her curls are barely holding their shape."
hi "No, I thought I'd sleep a bit later since it's the weekend and all, and I've been seriously sleep-deprived this week."
"I wonder if she missed the poison in my words."
show shizu basic_normal2
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Then it's a good thing we came to wake you up!"
show shizu adjust_happy
with charachange
shi "…"
show misha sign_smile
with charachange
mi "Anyway, Hicchan, I guess you would like to know why we're here, wouldn't you?"
"It's not hard to guess, but I wish she wouldn't say the words she is going to say next."
show misha perky_smile
with charachange
mi "Would you like to skip class and go somewhere nice with us?"
hi "Come again?"
show misha hips_smile
with charachange
mi "Would you like to skip class to do something fun?"
"I was certain they'd force me to help them again with some slave work."
hi "Seriously?"
show misha hips_grin
with charachange
"Misha grins and nods enthusiastically."
"I like this new approach they're taking although I'm somewhat surprised that they would suggest skipping class, even if we have only half a day since it's Saturday."
hi "Aren't you two worried about constantly missing class?"
show shizu behind_smile
with charachange
shi "…"
show misha perky_smile
with charachange
mi "Well, it doesn't seem to be a problem! Hicchan, this school is pretty much at a standstill whenever this time rolls around."
show misha hips_smile
with charachange
mi "It's a Saturday, too~. Don't you want to do something fun?"
"I'm amazed by how little they seem to care."
show shizu adjust_smug
with charachange
shi "…"
show misha perky_smile
with charachange
mi "Not that we're pressuring you to give us your company, but we thought you might like to hang out!"
show shizu behind_blank
with charachange
shi "…"
show misha hips_smile
with charachange
mi "So… would you like to join us? Come on, you'll have a lot more fun than just sitting here with your head on your desk~!"
"I guess I won't be missing anything important; nor will I be missed."
hi "All right, then, I don't think I'd be missing much. What do you have in mind?"
"My eyes narrow with suspicion as a thought crosses into my mind."
hi "Wait… this isn't just some trick to get me to do some more student council stuff, right?"
show shizu basic_angry
with charachange
shi "…"
show misha perky_confused
with charachange
mi "No, of course not!"
show misha hips_frown
with charachange
mi "And that's a really mean thing to just assume like that, Hicchan."
show shizu behind_frown
with charachange
shi "…"
show misha hips_smile
with charachange
mi "…And besides, you're in the Student Council now, remember?"
show misha hips_grin
with charachange
mi "If we wanted you to do something for us, we wouldn't have to trick you~!"
show misha hips_laugh
with charachange
mi "Hahaha!"
show misha hips_smile
with charachange
"This is a kind of coercion that is new to me. Only two pretty girls could pull it off."
stop music fadeout 3.0
"I allow myself to relax a bit. Maybe I'm being too paranoid; it seems like they may really just want to hang out."
"Nevertheless…"
hi "No tricks?"
play music music_shizune fadein 4.0
show shizu basic_angry
with charachange
shi "…"
show misha hips_grin
with charachange
mi "No tricks! Stop being so paranoid!"
hi "Well, if you say so."
"Suddenly, I realize I still am wearing pajamas."
hi "I wonder if you'd let me dress up first?"
show shizu adjust_smug
with charachange
shi "…"
show misha hips_smile
with charachange
mi "Eh? Why, Hicchan? You look just fine!"
hi "I'd still prefer wearing something else."
play sound sfx_doorclose
scene bg school_dormhisao
with locationchange
"I close the door before she gets a chance to reply and quickly pull on my uniform."
play sound sfx_dooropen
scene bg school_dormhallway
show misha perky_smile at twoleft
show shizu basic_normal at tworight
with locationchange
"Stepping back into the hallway, I see Shizune and Misha are engaged in an animated discussion."
"I wonder if people discussing in sign ever accidentally poke each other in the eyes."
show shizu behind_frown_close
with characlose
"While I'm contemplating this, Shizune taps me on the shoulder impatiently."
shi "…"
show misha hips_smile
with charachange
mi "So, we're planning on slipping into town! Remember that tea shop we were at on Wednesday?"
hi "Tea shop?"
show shizu behind_frustrated_close
with characlose
shi "…"
show misha perky_confused
with charachange
mi "You don't remember?"
hi "Oh, you mean that café."
show misha hips_smile
with charachange
mi "Tea shop! It's called the Shanghai. China is the birthplace of tea, you know. Come on, Hicchan! I'll even treat you today!"
show misha hips_grin
with charachange
mi "Ah… not me, not me, I mean Shicchan! Ahaha~!"
hi "I don't know…"
show misha sign_smile
with charachange
mi "It's nice, it's really relaxing! It's like… half café, half restaurant, half sophisticated, half… library…"
"What?"
hi "That's a lot of halves."
"But Misha doesn't seem to notice that."
show misha hips_smile
with charachange
mi "So~! Come on, it's not often that we have this much free time!"
show shizu adjust_smug_close
with charachange
shi "…"
show misha hips_grin
with charachange
mi "If you're busy, though, you don't have to! It's not like your presence is absolutely, absolutely required!"
show misha cross_laugh
with charachange
mi "Hahahaha!"
show misha cross_grin
with charachange
"I've never seen more weakly disguised reverse psychology in my life. I feel kind of tired today, and my teachers in my classes might want to know where I am. Maybe."
"On the other hand, I haven't really been into town at all since I've gotten here, so this is a good reason to head there."
"Also, I could use something to eat. If it's Shizune's treat, even better; I'm totally broke."
hi "All right, let's go. Lead the way."
show misha hips_smile
show shizu behind_smile_close
with charachange
mi "Great~!"
stop music fadeout 2.0
scene bg suburb_shanghaiint
with shorttimeskip
"We make it to the tea shop with a fifteen-minute walk. It seems that we are the only customers around."
play music music_another fadein 2.0
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter
hi "Is it always this quiet in the morning?"
"By that, I mean is it always this empty."
show shizu basic_normal
with charachange
shi "…"
show misha perky_confused
with charachange
mi "No, this is kind of weird. Hey, this isn't a bad thing though, right?"
hi "You're right."
scene ev shizu_shanghai
with locationchange
"We take our seats at a large, square wooden table, and it hits me that I don't know what this place serves. I just went with what Yuuko recommended the last time."
hi "Hey, is there a menu or something?"
scene ev shizu_shanghai_normallaugh
with charachange
mi "Nope!"
"That was a strange amount of zest."
scene ev shizu_shanghai_smirklaugh
with charachange
shi "…"
scene ev shizu_shanghai_smirknormal
with charachange
mi "So, Hicchan, have you decided what you're going to order?"
scene bg suburb_shanghaiint at Fullpan(8.0)
with locationchange
"I look around the store and can't see anything resembling a menu."
"I don't understand, what's up with this place? What gives?"
"Is this some kind of secret shop? Can you normally only enter here with a secret handshake? Some kind of wink and a nod?"
"Do you need someone to vouch for you? A blood oath? Dammit, it was nothing like this last time."
scene ev shizu_shanghai
with locationchange
hi "I don't know, the last time I think I just got coffee? What do they serve here?"
scene ev shizu_shanghai_smirknormal
with charachange
shi "…"
scene ev shizu_shanghai_smirklaugh
with charachange
mi "Tea!"
hi "Ah, well, that's…"
hi "Not just tea, right? Not only tea? There's other stuff too, right?"
scene ev shizu_shanghai_normallaugh
with charachange
shi "…"
scene ev shizu_shanghai
with locationchange
mi "Clearly~!"
hi "Clearly? Like what? There are no menus here. Where are the menus?"
"They're playing another joke on me. There is no way out of this; all I can do is brace myself for the inevitable, oncoming burn."
"I almost want to walk out of the store, but I'm already sitting down."
"It would be improper to leave now; the unspoken rules of polite social conduct block my exit like a wall of fire."
"I decide to play it safe. I'll order what they order, if it's acceptably manly enough."
hi "Why don't you two order before me? Ladies first."
scene ev shizu_shanghai_smirknormal
with charachange
shi "…"
mi "Well played, Hicchan, but~ we already ordered!"
hi "How is that possible? When? How? From who?"
mi "We're regulars, we come here so often that we don't have to do that any more!"
scene ev shizu_shanghai
with charachange
shi "…"
mi "Well, I guess you've had enough. We're sitting on the menus, of course~!"
scene ev shizu_shanghai_normallaugh
with charachange
mi "Hahaha!"
"I look around at the other tables. There are no menus on any of them. That means they must just keep them in a big stack near the door or something. What a thing to sit on, and what speed to grab them so quickly."
hi "Well, whatever. Can I have one, then?"
scene ev shizu_shanghai_smirklaugh
with charachange
shi "…"
scene ev shizu_shanghai_smirknormal
with charachange
mi "You can take one if you want, but you're not the kind of person who would do something that la—sci—vious?, isn't that right?"
"I tell them that I'd just like some coffee and put my head down on the cool tabletop."
scene ev shizu_shanghai_borednormal
with charachange
shi "…"
scene ev shizu_shanghai_boredlaugh
with charachange
mi "Coffee? This is a very high class establishment, and you're going to order coffee?"
"I can tell they're messing with me again."
hi "In that case, I'll have whatever you're having."
scene ev shizu_shanghai_smirklaugh
with charachange
shi "…"
scene ev shizu_shanghai_smirknormal
with charachange
mi "Hicchan, Shicchan is drinking a special tea that is only grown in remote areas of India."
mi "The tea is still handmade by a tribe of tea makers who have passed the methods down in their families for generations."
mi "They must wade through alligator-infested waters to obtain the leaves once a year. On each trip, some do not make it back alive."
"I can't drink that, I would feel too guilty."
hi "Then I'll have what you're having."
scene ev shizu_shanghai_smirklaugh
with charachange
mi "I don't know what I'm drinking."
"How?"
hi "Fine, then I want the tea that people died for."
hi "No, never mind. I'll have coffee."
hi "If this is a very high class establishment, then they should have very high class coffee, right? … No one died for it, right?"
scene ev shizu_shanghai
with charachange
"The perfect answer, there is no way they can stand against it. Shizune shrugs, as if to say “well played.”"
"They still didn't answer my second question."
scene bg suburb_shanghaiint
with locationchange
show yuukoshang neutral_down at center
with charaenter
"Misha calls for Yuuko, who brings over our drinks and a single incredibly tiny yellow cake with a little black plastic fork stuck in it for each of us."
hide yuukoshang
with charaexit
"I eat my cake in one bite, amazed at how it's probably the least filling thing I've ever eaten."
show shizu behind_blank at Slide(0.2,0.5,0.3,0.5,1.0)
show misha perky_smile_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)
stop music fadeout 3.0
mi "Hicchan, do you have any plans for tomorrow?"
"Misha takes a gulp of her tea, something sounding suspiciously high class even though it looks like ordinary tea."
"She drinks with incredible recklessness considering how hot it is. The exact opposite of Shizune or Lilly."
"Plans? That sounds ominous."
play music music_running fadein 8.0
hi "Plans? Yes."
hi "Yes, I am incredibly busy tomorrow. In fact, I have so much to do that I will not have any free time at all."
hi "That's right… none whatsoever. And everything I have to do is extremely important. Very, very important."
show misha hips_grin_close at tworight
with charachange
"Misha giggles, clearly not buying it, and then signs it all back to Shizune, who nods slowly and deliberately while looking very unamused."
show shizu basic_normal_close at twoleft
with characlose
"Suddenly, she leans forward, staring analytically at my face like a human lie detector, waiting for the smallest tell to give me away."
"After at least a minute of this, she sits back down in her seat and takes a sip of tea."
show shizu behind_blank
with charadistant
shi "…"
show misha perky_smile_close
with charachange
mi "Okay, Hicchan, if you're that busy. We don't have anything to do tomorrow, so we thought maybe you would want to hang out with us at the festival!"
show misha sign_smile_close
with charachange
mi "You're new here, anyway, right? Right? So~ we thought we would show you around and have some fun together, but if you're that busy, we understand!"
show shizu adjust_happy
with charachange
shi "…"
mi "Oh well, oh well!"
show misha cross_grin_close
show shizu basic_normal2
with charachange
"The both of them shrug together in perfect sync, as if they've rehearsed it."
show misha cross_laugh_close
with charachange
mi "Ahahahahaha~!"
show misha cross_grin_close
with charachange
mi "Hicchan, you're so paranoid."
show shizu adjust_smug
with charachange
shi "…"
show misha cross_smile_close
with charachange
mi "…And you'll never beat me anyway, so why bother getting so worked up about it?"
show misha cross_laugh_close
with charachange
mi "Haha! Wow, Shicchan~!"
hi "Beat you? What are you talking about?"
"Is she talking about the coercion? I never realized that was just a game to her. I thought I was the only one who saw it as competition."
show shizu basic_happy
with charachange
shi "…"
show misha hips_grin_close
with charachange
mi "You know~! …Eh? Do you, Hicchan? Because I don't."
show shizu adjust_smug
with charachange
shi "…"
show misha hips_smile_close
with charachange
mi "You can't outwit me! —Ah, well, Hicchan, not me…"
show shizu basic_sparkle
with charachange
shi "…"
show misha perky_confused_close
with charachange
mi "What? What are you talking about, Shicchan…"
"I can see Shizune smiling craftily, daring me to enter this battle of wills and wits with her."
"When he is pushed to the edges of despair, a man has no choice but to sink, or grasp at the fleeting wisps of hope, fight with all his power against the inevitabilities of his fate and struggle against the impossible."
"For even if he fails, at least fail knowing that he dared greatly…"
"…Or something like that."
hi "Well, we'll see about that. Don't underestimate me."
show shizu behind_blank
with charachange
shi "…"
show misha perky_smile_close
with charachange
mi "Don't you have to follow through to make good on that, Hicchan?"
hi "Ah, well, I could get lucky. Don't count out that possibility."
show shizu adjust_smug
with charachange
shi "…"
show misha cross_grin_close
with charachange
mi "You won't~."
hi "I will! Wait—"
show shizu basic_happy
with charachange
shi "…"
show misha cross_smile_close
with charachange
mi "Let's make a wager on it, then!"
hi "I don't care about competition."
"That's a blatant lie."
hi "Wait, what exactly do you mean?"
show misha cross_laugh_close
with charachange
mi "That's okay if you don't know, neither do I! Wahahaha!"
show shizu basic_normal2
with charachange
shi "…"
show misha perky_smile_close
with charachange
mi "So it's settled, then! All right, all right!"
hi "What? Didn't you hear what I just said?"
show shizu adjust_happy
with charachange
shi "…"
show misha sign_smile_close
with charachange
mi "Now all that's left is the stakes! What the winner wins, or, more interestingly, what the loser loses!"
hi "Hey!"
"This is a very dangerous game I'm playing. Shizune herself is a very dangerous girl, if she can only think in terms of winning and losing."
"If she views every time that I talk with her as some kind of battle of wills, I don't think I could take it."
"That kind of thing drives people insane. She's too Machiavellian; before this I'd assumed she was just kind of stoic."
"But nevertheless, I'm interested. In hindsight, I realize that I just challenged her to what is essentially a duel without any rules that won't end until one of us… what?"
"I guess that's it. That's so vague. What are the conditions for winning or losing? The first person to feel stupid loses?"
hi "I don't know, I've never had to think of anything like this before."
show misha hips_smile_close
with charachange
mi "Never?"
hi "Never."
show misha perky_confused_close
with charachange
mi "So you have never gambled, Hicchan?"
hi "I'm surprised you two have."
show shizu behind_blank
with charachange
shi "…"
show misha hips_grin_close
with charachange
mi "Oh, come on… It's just for fun, anyway! Between friends~!"
show misha sign_smile_close
with charachange
mi "It's about causing humiliation, suffering, and absolute despair! Isn't that the point?"
"Shizune puts a finger to her temple thoughtfully."
show shizu adjust_happy
with charachange
shi "…!"
show misha hips_smile_close
with charachange
mi "Hm… Ah, how about this, Hicchan: If you lose, you have to go to school one day without any pants on."
hi "Are you insane?"
"Although in comparison to what I was afraid she would say, it's pretty mild."
hi "Can't we just bet money, like normal people?"
show shizu basic_sparkle
with charachange
shi "…"
show misha hips_grin_close
with charachange
mi "It's not like you could match my wager if we did~! Now, it's your turn! …But nothing perverted! Understand?"
show misha hips_laugh_close
with charachange
mi "Hahaha!"
hi "I think I need more time."
"This is going to have me constantly on edge for weeks."
show misha hips_grin_close
with charachange
mi "Okay~! Come on, you should both hurry up, your drinks are getting cold!"
show shizu basic_happy
with charachange
"I quickly down the rest of my coffee as Shizune does the same, staring at me with a fierce look of competition in her eyes."
"It seems like a waste for her to be gulping down something that someone may have died for her to enjoy."
show misha sign_smile_close
with charachange
mi "Hicchan, are you sure you don't want to hang out tomorrow? A lot of people are looking forward to it; you don't want to miss out."
"I mumble unintelligibly at her."
show misha perky_confused_close
with charachange
mi "I don't really understand…"
"It's time to think. Shizune's drink is smaller, but I can consume mine faster."
"If Shizune finishes her drink first, she might skip out on paying, leaving me to pick up the tab, even though she said the drinks were on her."
"Because I have no money on me, I would be humiliated, and therefore this could be considered a loss."
"If I finish first, the laws of chivalry would make me look like a jerk, as I would need to run out of this teahouse, leaving her to pay for everything. That could also be considered a loss. She would use that."
"In the event of a draw, she may attempt to run out the door, and I'll probably do the same. This might lead to a collision at the door, which would be humiliating, but not overly so. …And Misha would be left to pick up the tab."
"This is really childish. I'm a little disappointed in Shizune, and myself."
show misha perky_smile_close
with charachange
mi "Well, Hicchan, it'd be really nice if we could all celebrate how well we put everything together for the festival by taking a look at our handiwork…"
"Misha seems oblivious to the fact that an epic battle of wills is raging in front of her. I nod slowly and down the last of my coffee."
hi "Well, I am finished enjoying my drink. I guess it's time for me to leave. And I am going to leave now. Calmly."
show shizu adjust_happy
with charachange
shi "…"
show misha perky_confused_close
with charachange
mi "You too, Shicchan?"
mi "Why are you two acting so weird?"
scene bg suburb_shanghaiext
with locationchange
"I quickly walk out the door and Shizune follows. Misha is going to have to foot the bill."
scene bg suburb_roadcenter
with locationchange
"Sorry, Misha."
show shizu behind_smile at center
with charaenter
"Catching up to me, Shizune quickly pushes her glasses up and presses a note into my hand."
window hide
$ written_note("If you lose, you have to come hang out with us tomorrow.")
window show
hi "So you think you can win today? That's kind of cocky, Shizune."
"I forgot for a second that she can't hear me. I nod."
"Right now, she seems much cuter than she usually is, smiling softly with a hint of confidence coming through."
"Shizune looks energetic and carefree, although it could just be the caffeine."
show shizu adjust_happy
with charachange
"She winks, and extends her hand for a handshake. I wonder if there's a buzzer in there and she plans to shock me, but that doesn't seem like something she would do, so I accept."
"With a squeeze, she pushes another note into my hand. I momentarily think that it's a buzzer and wonder if the shock could kill me."
hide shizu
with charaexit
"Shizune smirks and then runs off."
window hide
$ written_note("You probably don't know how to get back to school from here.\n\nThere will be work waiting for you when you do. See you then~")
window show
"I crush the note in my fist dramatically, but no one is there to see it, and that makes me sad."
"I wonder if it's too late to go back to the shop and ask Misha for directions."
"But then again, I gave her a hard time for not knowing the way here, so I can't allow her to score off me for not knowing the way back."
"And if I ask her, Shizune could see it as a victory. No, it's not necessary."
stop music fadeout 3.0
"The school is on top of a damn hill, how hard could it be to find?"
"I may be slightly directionally challenged, but I'm sure that even I can do this."
scene bg school_courtyard
with shorttimeskip
play music music_happiness
"About an hour and a half later, I walk the long paved path leading from the gates to the main building."
scene bg school_lobby
show shizu behind_blank at tworight
show misha hips_grin at twoleft
with locationchange
mi "Hahaa! Just the person we were waiting for. So you made it here eventually, Hicchan, good! Now it's time for work work work~!"
"Misha and Shizune had laid an ambush for me in the main lobby of the ground floor and I walked straight into it. I should have just circled around the school like I had originally planned, but I thought that I was overreacting and being silly."
"Misha is waving a thick stack of printouts in my general direction, taunting me."
show misha perky_smile
with charachange
mi "We sort of need your help~!"
hi "Sort of?"
show misha hips_grin
with charachange
mi "We need your help~!"
show shizu cross_angry
with charachange
shi "…"
show misha sign_smile
with charachange
mi "You will help us!"
"Misha speaks with her usual playful, carefree manner, but even so I can hear Shizune's unnervingly hard severity behind it."
hi "That sounds like an order."
mi "Really? Is it?"
show shizu behind_frown
with charachange
shi "…"
show misha perky_confused
with charachange
mi "Eh? It is?"
show misha hips_laugh
with charachange
mi "Ah, sorry, Hicchan, I guess it is! Hahahaha!"
"She doesn't sound very sorry at all."
show misha hips_grin
with charachange
mi "I thought we had almost everything done by now, but it turns out we have all these signs to attach to backing boards."
show shizu adjust_angry
with charachange
shi "…"
show misha sign_smile
with charachange
mi "More hands make light work!"
show misha hips_laugh
with charachange
mi "And everybody wins! Hahahahaha!"
show shizu basic_angry
with charachange
shi "…"
show misha hips_smile
with charachange
mi "This is your duty, after all, as a member of the Student Council. Which you are a part of."
mi "As a member."
mi "Of the Student Council."
show misha hips_laugh
with charachange
mi "Ahahaha~!"
show shizu behind_blank
with charachange
shi "…"
show misha perky_smile
with charachange
mi "It's a simple task, so getting it out of the way now would be good. It's not that much work. A small thing, really!"
show shizu basic_normal2
with charachange
shi "…"
mi "And we'd really appreciate your help!"
mi "Really, really appreciate it!"
show misha hips_grin
with charachange
mi "Besides, it's time to pay back for us treating you so nicely!"
hi "So the tea shop was a trap after all! You two-timing scoundrels!"
show shizu behind_blank
with charachange
shi "…"
show misha cross_smile
with charachange
mi "Don't say that, it was completely unrelated. We wanted to celebrate you joining the council!"
"But why did she bring that up, then?"
hi "But—{w=0.3}{nw}"
show shizu cross_rage
with charachange
shi "…!"
show misha hips_grin
with characlose
mi "No buts! You're coming with us!"
show misha hips_grin at offscreenleft
show shizu cross_rage at offscreenright
with ease
show misha cross_smile_close at closeleft
show shizu cross_angry_close at closeright
with ease
"I don't even get to finish my sentence as they grab me by the arms and try to pull me towards their office."
show misha cross_laugh_close
with charachange
"Misha laughs giddily as she and Shizune exchange sly looks behind my back."
show shizu basic_angry_close
with charachange
shi "…!"
mi "Ah, I don't think you have a choice in this, Hicchan! Hahahaha!"
show misha hips_grin at twoleft
show shizu basic_angry at tworight
with charadistant
mi "There are two of us, so don't even try to get away, now! Don't take us lightly!"
show shizu behind_frown
with charachange
shi "…!"
mi "Hicchan, it's your duty to help us, anyway! As a member of the Student Council!"
hi "All right, all right! How could I forget?"
hi "But, seriously, aren't there other people who can help you?"
show misha perky_confused
with charachange
mi "Like who, Hicchan?"
mi "You were fine with helping us yesterday…"
hi "Yesterday is not today!"
hi "And anyone who isn't me!"
hi "Why don't you have anyone else in the council?"
show shizu cross_wut
with charachange
shi "…!"
show misha cross_laugh
with charachange
mi "That's what we'd like to know! …Aha… Ahahahahaha!"
"Misha's laughter explodes through the hall. She doesn't notice the grimace on my face at all. That's right, it's just the two of them, isn't it?"
hi "Oh, right. Okay, I'll help you."
show misha hips_grin
with charachange
"Misha runs her tongue over her teeth, looking quite pleased."
mi "That's my Hicchan! I knew we could trust you~!"
show shizu behind_smile
with charachange
shi "…!"
mi "So predictable~."
stop music fadeout 2.0
scene bg school_council
with locationskip
"When we get to the student council room, my jaw drops. The number of signs, backing boards, and signposts is insane."
"They're stacked all over the place like building materials at a construction site, something I let Shizune and Misha know right off the bat."
hi "There are so many signposts here you could probably build a second wall around the school with them!"
play music music_ease fadein 4.0
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter
mi "Hahaha~! Really? Well, there are a lot of them, so maybe…"
show shizu basic_angry
with charachange
shi "…!"
show misha perky_confused
with charachange
mi "Eh? No?"
mi "How do you know that, Shicchan?"
show shizu behind_frown
with charachange
shi "…!"
mi "Really?"
hi "Don't tell me she's actually considered it?!"
show misha hips_grin
show shizu adjust_smug
with charachange
"Shizune hesitates, then pushes her glasses up a bit as Misha lets out a very uneasy sounding laugh."
"So she has considered it."
show shizu basic_normal2
with charachange
shi "…!"
mi "Ahaha! That's… irrelevant, Hicchan! Can you get on with making the signs, please?"
hi "All right, all right."
hi "I feel sort of lied to, though. I thought you said it wouldn't be that much work?"
show shizu behind_blank
with charachange
shi "…!"
show misha hips_smile
with charachange
mi "Ah, well, Shicchan meant it wouldn't be that much work for us."
show shizu basic_normal
with charachange
shi "…!"
mi "Someone has to supervise you while you do this, you know, to make sure you're doing it right. And those people will be us."
hi "So what are you two going to do?"
show misha cross_laugh
show shizu basic_happy
with charachange
mi "Watch you! Hahahaha~!"
show shizu adjust_happy
with charachange
shi "…!"
show misha perky_smile
with charachange
mi "No, that was just a joke, Hicchan. We'll help out too, of course. The Student Council is really supposed to have a lot more people."
show misha perky_sad
with charachange
mi "This is just a bad year. Fewer people than usual, even though we already didn't have many the year before."
mi "And then there's just a lot more work than before, too."
show shizu behind_smile
with charachange
shi "…!"
show misha perky_smile
with charachange
mi "Besides, Shicchan likes working with you. And so do I!"
mi "We've accomplished a lot more than we normally could, you know."
stop music fadeout 7.0
"I can accept that. Lately, they've been looking a little fatigued every time I see them."
"Student council work is apparently a 24-hour-a-day thing, and from what I've seen and heard, there are just the two of them. Well, I guess I make it three."
"They must work almost nonstop. I wonder how much time they spend working in this room, when I don't see them."
"And I've even glimpsed Misha taking naps sometimes without Shizune at her side. By herself, Shizune has to be working 60-hour weeks doing her student council duties, on top of regular classes."
scene bg school_council_ss
with shorttimeskip
play music music_tranquil fadein 3.0
"Two hours pass, and I reach for a tack only to find the box is empty. Shizune grabs it before I can even say anything."
show shizu adjust_happy_ss at tworight
show misha perky_smile_ss at twoleft
with charaenter
"She smiles, tossing it expertly into a trash can along with another empty box of tacks."
show shizu behind_smile_ss
with charachange
shi "…!"
show misha hips_grin_ss
with charachange
mi "So you're out too, Hicchan? Don't worry, Shicchan says she'll get some more."
show misha hips_laugh_ss
with charachange
mi "Hahahaha!"
show misha hips_grin_ss
with charachange
mi "We went through a box too, but me and Shicchan decided to wait until you needed a new box as well before getting a new one."
"Something about that strikes me as odd."
hi "Wait, we both ran out of tacks just now? Wow, what a weird coincidence, huh?"
show misha perky_smile_ss
with charachange
mi "Ah, well, actually, Hicchan, we ran out twenty minutes ago, and there was only one spare box of tacks, the ones we gave to you."
mi "And you were flying through those pretty quickly, so~! we thought that we should wait until we both had no more tacks before getting more!"
show misha sign_smile_ss
with charachange
mi "Then, Shicchan could go get fresh boxes of tacks for all of us at the same time. You know, for efficiency~!"
show shizu basic_normal2_ss
with charachange
"Shizune nods, preparing to step out the door."
hi "Wait a second, so what did you two do for the past 20 minutes?"
show shizu adjust_happy_ss
with charachange
shi "…!"
show misha hips_grin_ss
with charachange
mi "Ahaha~! Nothing, of course! What could we do? We had no tacks, Hicchan!"
show shizu behind_smile_ss
show misha cross_grin_ss
with charachange
"Shizune and Misha exchange knowing glances before they give me a perfectly synchronized and incredibly exaggerated simultaneous shrug."
hi "I see. So you decided to take a break. Clever."
show shizu adjust_smug_ss
with charachange
shi "…!"
show misha hips_grin_ss
with charachange
mi "Oh, we know it was clever."
hi "Whose idea was it?"
show misha hips_smile_ss
show shizu adjust_happy_ss
with charachange
mi "The both of us, of course, of course!"
show misha cross_laugh_ss
with charachange
mi "Ahahaha~! Well, Hicchan, it was all Shicchan's idea."
show shizu behind_smile_ss
with charachange
hide shizu
with charaexit
stop music fadeout 3.0
"I turn immediately to Shizune, who gives me a curt wave and a surprisingly cheery smile before quickly vanishing out the door."
show misha cross_grin_ss at twoleft
with charachange
show misha cross_grin_ss at center
show bg school_council_ss at bgright
with charamove
"Well then why didn't you just say you wanted to take a break!?"
"I used to think that Shizune and Misha were polar opposites. Misha always seems so energetic and playful, like any other girl. Shizune, on the other hand, always seemed distant. Aggressively manipulative and vaguely scary, but distant."
"There were times when I thought that she had no sense of humor. As cute as she was, I'd almost never seen her smile. Not to mention all the other things."
"The analytical stare, the permanently stoic expression, and even her penmanship; so mechanically precise that everything she writes looks typed."
"But Shizune and Misha really aren't as different as I'd thought."
hi "I'm a little surprised."
play music music_shizune fadein 5.0
show misha perky_confused_ss
with charachange
mi "Why?"
hi "Shizune. I didn't know that she liked to joke around like that."
"What I mean to say is, I didn't know that she could act so girlish. It was actually pretty cute."
show misha perky_smile_ss
with charachange
mi "You would be surprised, Hicchan."
hi "Well, I didn't know you and her were so close, either, the first time I saw you."
"I've always been curious as to how these two met."
hi "Do you two go far back or something?"
hi "Childhood friends?"
hi "Next-door neighbors?"
show misha perky_sad_ss
with charachange
mi "Haha… Sorry, Hicchan, it's not anything like that, even if it would be cuter that way."
show misha perky_smile_ss
with charachange
mi "When I came to this school, they just placed me next to Shicchan, and she looked like a very serious person."
show misha sign_smile_ss
with charachange
mi "And I thought, “I'm going to be spending the rest of the year next to this person, maybe!”"
mi "“So it would be nice if we could be friends! But~, I wonder if she'll like me.”"
show misha hips_grin_ss
with charachange
mi "And I learned that she was deaf. You know, Hicchan, the first time I just thought she was ignoring me~!"
show misha hips_smile_ss
with charachange
mi "But, luckily, I knew a little sign language, and we became friends."
"I want to know where Misha learned how to sign, but I guess that's something for another time."
show misha perky_smile_ss
with charachange
mi "Now, I guess we're always together. It's nice, I've always wanted someone to listen to me, and I think Shicchan likes having someone to talk to! So, everybody wins."
hi "Heh. That's nice."
show misha hips_grin_ss
with charachange
mi "That's it? You look disappointed, Hicchan, what were you expecting?"
show misha hips_laugh_ss
with charachange
mi "Ahahahahaha!"
show misha hips_grin_ss
with charachange
mi "You know, Hicchan, I don't think that me and Shicchan thanked you properly."
hi "For what?"
show misha perky_smile_ss
with charachange
mi "Joining the Student Council. You've been a real help to us, Hicchan! I think I will get a lot more sleep now~!"
hi "Well, I'm glad I could help, if it helps a young woman sleep at night."
show misha hips_smile_ss
with charachange
mi "That's an interesting thing to say, Hicchan."
mi "Shicchan really appreciates you helping us out too."
show misha hips_smile_ss at twoleft
show bg school_council_ss at center
with charamove
show shizu behind_frustrated_ss at tworight
with charaenter
"At that moment, Shizune steps back into the room, looking slightly annoyed and sipping offhandedly from a juicebox."
show shizu adjust_happy_ss
with charachange
shi "…"
play sound sfx_dropstuff
"She throws two boxes of tacks on the floor with a wry smile."
show shizu basic_normal2_ss
with charachange
shi "…!"
show misha sign_smile_ss
with charachange
mi "Ah, Shicchan."
play sound sfx_crunchydeath
show shizu behind_frown_ss
show misha sign_confused_ss
with charachange
"Misha opens her mouth to speak, but then quickly closes it as Shizune suddenly crumples her juicebox with a crunch like the sound of breaking bones."
show shizu basic_angry_ss
with charachange
shi "…!"
show shizu adjust_angry_ss
with charachange
shi "…"
show shizu behind_frown_ss
with charachange
shi "…!"
"I can tell that each harsh, quaking hand gesture is most likely an epithet."
hi "What's she saying?"
show misha perky_confused_ss
with charachange
mi "It was just very hard to get these…"
show shizu basic_angry_ss
with charachange
shi "…!"
show misha sign_confused_ss
with charachange
mi "I guess that is an understatement, Shicchan…"
"Shizune calms down a bit, straightening her glasses and lightly brushing her bangs back with one finger."
show shizu adjust_happy_ss
with charachange
shi "…"
show misha perky_smile_ss
with charachange
mi "It really wasn't a big deal in retrospect? That's forward thinking of you!"
show misha hips_smile_ss
with charachange
mi "All right then, I guess the two of us should get back to work, Hicchan!"
stop music fadeout 4.0
hi "Sure, why not."
scene bg school_council_ni
with shorttimeskip
"By the time we're done with the signs, it's already getting dark out."
"I hadn't expected something like this to take so long. But then again, if it were that easy, I doubt Shizune and Misha would have asked for my help."
play music music_dreamy fadein 2.0
show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter
"Shizune falls into a nearby chair, cracking her knuckles systematically and letting out a muted yawn."
show shizu behind_blank
with charachange
shi "…"
show misha sign_smile
with charachange
mi "That's all for today, I guess! That's a good thing, Shicchan, I'm very tired, too."
hi "That took longer than expected."
show shizu behind_frustrated
with charachange
shi "…"
show misha hips_grin
with charachange
mi "You agree? Hahaha, we didn't expect it to take so long either! Not as planned!"
show misha perky_sad
with charachange
mi "Aww, I'm so hungry. I just realized I haven't eaten all day."
"Now that I think about it, I have eaten nothing since I woke up this morning, but right now I'm almost too tired to think about food."
hi "I think they already stopped serving dinner."
show misha perky_confused
with charachange
mi "This can't be happening! Hicchan, can you think of any way we could… obtain food?"
hi "Obtain food?"
"I don't like her tone of voice."
show shizu adjust_happy
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Why not order out? Oh, that's right, I guess I could do that."
hi "Order out? From where?"
mi "From town, of course!"
hi "I didn't know they deliver to the school. Well, what are you going to get?"
show misha hips_smile
with charachange
mi "Maybe some Chinese food!"
hi "As long as you're going to, can I get in on it too? I'm also pretty hungry."
show misha hips_laugh
with charachange
mi "Ahahaha~! Hicchan, you should have just said so in the first place!"
show shizu basic_normal2
with charachange
shi "…"
show misha hips_grin
with charachange
mi "What's that? It's your treat? That's great! That's great!"
show shizu behind_blank
with charachange
shi "…"
show misha cross_laugh
with charachange
mi "Wahaha, that's true, if it wasn't for you, we wouldn't be here so late, Shicchan!"
show misha cross_grin
with charachange
"Misha quickly grabs a menu from a drawer behind her and begins to enter the number slowly and carefully, as if she's used to messing it up."
mi "What do you want, Hicchan?"
hi "Well, I guess I'll just have some dumplings."
show shizu behind_smile
with charachange
"I raise my hand in a gesture of thanks to Shizune, who responds with a very faint, split-second smile."
show misha cross_laugh
with charachange
mi "Ahahahahaha~!! Hicchan, Shicchan is paying for everything tonight, it's all on her, so you can afford to splurge a little!"
hi "Some shrimp fried rice too, then."
show misha cross_grin
with charachange
mi "All right, all right! And you, Shicchan?"
show shizu basic_normal2
with charachange
shi "…"
show misha hips_smile
with charachange
mi "A Chinese omelette? Okay, then."
hi "Hey, Misha, does that really mean “omelette”? Can I see that again?"
show misha hips_grin
with charachange
mi "Sure! Haha! Like this, like this…"
show misha sign_smile
with charachange
show misha perky_smile
with charachange
show misha hips_grin
with charachange
mi "And this is for what you ordered: Dumplings!"
show misha perky_smile
with charachange
show misha sign_smile
with charachange
show misha hips_smile
with charachange
mi "Shrimp fried rice!"
show misha hips_grin
with charachange
mi "I'm going to get soup and a stir-fry, you say that like this…"
show misha sign_smile
with charachange
show misha perky_smile
with charachange
mi "And here's how much it all costs: 3685 yen!"
show misha perky_smile:
    pause 0 "misha cross_laugh" with Dissolve(0.5, alpha=True)
with None
extend " Wahahahaha~!"
hi "Well, I don't know in how many situations I'll need to remember such an exact number…"
mi "Ahahahaha! Okay~! I'm going to order now, unless anyone wants something else. No objections? All right all right, then!"
scene bg school_council_ni
show shizu behind_frustrated at tworight
show misha hips_smile at twoleft
with shorttimeskip
"Shizune impatiently twirls a pair of chopsticks between her fingers as we wait for the food to arrive."
hi "Hey, where did you get those?"
show misha hips_grin
with charachange
mi "This isn't the first time we've ordered out, Hicchan, and they always give us a ton of chopsticks, for some reason, even when we tell them we're only two people."
hi "And you two have accumulated a lot of them from a lot of long nights eating takeout in the office?"
show misha cross_laugh
with charachange
mi "That's exactly it! Hahahahahaha!"
show shizu basic_angry
with charachange
shi "…"
show misha perky_confused
with charachange
mi "I'm overstating it?"
show shizu behind_blank
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Haha! That's right, Shicchan! Hey, Hicchan, did you know that once we've collected a hundred pairs of chopsticks from ordering out, we'll be able to take over the universe?"
hi "I used to think that too, when I was little."
show misha perky_smile
with charachange
mi "Hicchan, are you good at breaking them down the middle? I can never do it right, so I found the little pile of chopsticks Shicchan had saved up and practiced on at least twenty of them."
show misha hips_grin
with charachange
mi "She was really mad about that!"
show shizu adjust_blush
with charachange
shi "…!"
"I let out a laugh as Shizune turns bright red with indignation. I didn't know she had such a childish side."
stop music fadeout 5.0
scene bg school_council_ni
with shorttimeskip
"When the food arrives, I dig in heartily, drinking one of the tiny cans of soda Shizune bought for us from one of the vending machines in the hall."
"Thanking them both for the food, I head back to the dorms, ready to turn in for the night."
scene bg school_dormhallway
with locationskip
"The dorms are eerily quiet except for the sounds of portable TVs and radios murmuring unintelligibly behind thin walls."
$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 4.0
scene bg school_dormhisao_ni
with locationchange
"It's quiet here at night, and very peaceful. I can hear the crickets chirping outside my window, and see actual stars when I look up."
"Tired, I try to fall asleep as quickly as I can, only feeling slightly robbed of my Saturday."
stop ambient fadeout 2.0
$ suppress_window_after_timeskip = True
scene black
with shuteye
label en_A37:
scene bg school_scienceroom at bgleft
with None
"The library seems as good a place as any to go. Hanako looked as if she was taken pretty off-guard by Lilly leaving, so she might want someone to talk to."
"Slinging my bag over my shoulder, I make my way out of the classroom."
stop music fadeout 4.0
scene bg school_hallway2
with locationchange
"I walk down the hallway to the library, past a multitude of closed doors."
"Through each one the sound of furious rehearsal can be heard. Rock music blares out of one door, almost as loud as a concert."
"I guess that's one of the advantages of a private school; there are actually enough rooms to go around at a time like this."
"And, when I think about it, the grounds and buildings of the school are kept in pretty good condition. That can't be too cheap."
"I've heard that this place has some pretty serious benefactors."
scene bg school_library
with locationchange
play music music_happiness fadein 1.0
"The walls of the library only partially insulate the noise of the festival preparations, but they're the only sounds to be heard."
"Not a soul stirs here, with everyone apparently enjoying the weather outside or working on festival events."
"Yuuko isn't here either. Maybe she doesn't work on Saturdays."
"I quietly walk through the library, now fairly familiar with its layout. I head to the back, where Hanako's private little corner is."
"I run my hand along the spines of the books on the way through, feeling the individual texture of each as I glance across the titles."
"I used to do this all the time at the library at the hospital. Some things never change, I guess."
"Like the smell of a library. No matter how much care you take, the paper in books is always going to degrade with time."
"Probably, no matter which library you go into, anywhere in the world, it must have that same, musty smell."
"I find something that looks light enough to read without any major thought involved then look for Hanako in the reading area."
scene ev hana_library_read_std
with locationchange
"Once again, she is sitting on a beanbag with her back to a bookshelf. Reading the same book she'd had in the classroom, she's slowly making her way through the pages."
play sound sfx_pillow
show ev hana_library_std
with locationchange
"Unlike last time I saw her here, I quietly take a seat in a beanbag. The noise is enough to catch her attention, but not startle her."
"This delicate routine that must be followed each and every time I try to talk to her almost feels like hunting game."
hi "Is that the same book as before?"
ha "Y-yes… I'm almost finished…"
hi "Cool."
"I wonder if I should…"
hi "Do you mind if I borrow it when you're finished?"
"My mouth is faster than my mind, it seems."
ha "S-sure… you m-may not like it but…"
hi "I'm sure it can't be that bad. After all, you've stuck with it, haven't you?"
ha "I-I guess."
scene bg school_library
with locationchange
"I settle into my beanbag and set about reading my own book that had been buried in my bag."
"It's a light novel about pirates. To be honest I'm barely skimming over the words, having chosen the book merely because it belongs to a different genre than I usually read."
"Finding it hard to muster enough enthusiasm to finish the book, and noting that I've inadvertently distracted Hanako quite a bit, I decide to try and make conversation."
hi "So, I see Lilly left without you?"
show hanako emb_downtimid at center
with charaenter
show hanako basic_worry
with charachange
"She nods before taking her eyes off her book. She must have been really into it after all."
ha "Lilly said she had to go and… meet someone…"
hi "Oh?"
show hanako basic_normal
with charachange
ha "A-Akira. Her sister…"
hi "Sister? I haven't heard her talk about her family…"
show hanako cover_distant
with charachange
ha "She… she and Akira used to live together."
hi "I thought all the students lived in the dorms?"
show hanako cover_worry
with charachange
ha "T-they… I mean we… don't have to."
hi "But it's easier, right? I mean, there's food here and you're close to school… I don't think I've ever been to class on time so often in my life."
show hanako cover_smile
with charachange
"Her badly hidden smile proves quite rewarding."
"In the back of my mind I know I have a bit of homework to catch up on, but it's quite comfortable in here. No one can find me and force me into working for their pet project, either."
"Though now that I'm thinking about the festival, another question comes up…"
hi "Hey, Hanako, what are you doing for the festival?"
stop music fadeout 0.2
show hanako def_shock
with charachange
"For a split second I think that Hanako is about to throw her book in the air from shock."
ha "S-sorry…?"
hi "I was just asking what you're doing for the festival tomorrow. Anything planned?"
show hanako def_worry
with charachange
ha "I… I don't know."
"Hanako answers in the way that people do when they don't want you to ask any more questions. I take it large crowds and loud music aren't really her “thing.”"
hi "Oh, okay."
"Change the subject, change the subject…"
play music music_happiness fadein 4.0
hi "So, what's Lilly's sister like?"
show hanako basic_normal
with charachange
ha "She… she's nice. She's pretty like Lilly, but she dresses… business-like…"
hi "Business-like?"
show hanako basic_distant
with charachange
ha "She… she's always wearing a suit…"
hi "Ah, I see. And that makes her less pretty somehow?"
show hanako emb_emb
with charachange
"Hanako gives an embarrassed shake of her head."
ha "N-no… just… different."
"I'll admit it, this has got me intrigued. To hear Hanako talk about someone other than Lilly is a first, and to be complimentary about it too…"
"But as I try to picture this mystery sister, all I can think of is Lilly in a suit. And I can't imagine that not being attractive. Not at all."
hi "Well, one day you'll have to introduce me to her."
show hanako basic_bashful
with charachange
ha "O-okay."
"Our brief conversation ends as abruptly as it started, and we both return to our novels."
stop music fadeout 4.0
scene bg school_library_ss
with shorttimeskip
"The passage of time is marked only by the gradual movement of the patch of light cast through the window."
"Slowly, the noises from the various rehearsals in the building fade out and die as students start to get hungry and tired."
"Just thinking about that makes my stomach start to turn knots around itself. I think it's time to head back."
hi "Do you think Lilly would be back by now? I think I might head back to my dorm. I'm pretty tired from this week."
"And not a word of that is a lie. Moving to a new school as it ramps up for a major event has been taxing, to say the least."
"I can feel myself nodding off as I read my book."
show hanako basic_smile_ss at center
with charaenter
ha "O-okay. I… I might stay here a little longer."
"Looking at Hanako's book, I can see that she is only a few pages away from completing it."
"For a moment I consider hanging around until she finishes, but once again my stomach turns, emitting a gurgling sound."
hi "Sure thing. Well I'm going to head off before it gets dark. I'll see you around, okay?"
show hanako basic_bashful_ss
with charachange
ha "O-okay. See you, Hisao."
hi "Later."
show hanako defarms_worry_ss
with charachange
ha "H-Hisao?"
hi "Hmm?"
show hanako emb_smile_ss
with charachange
ha "T-thank you. F-for hanging out with me."
play music music_dreamy fadein 2.0
"I can see how hard it was for her to get that simple sentence out of her mouth. It leaves me hanging for a moment."
"So. There is someone in this school who is even lonelier than me. Maybe lonely is a wrong word, I haven't been lacking company for this first week, but I've still managed to feel somewhat alone and detached."
"Maybe lonely is a wrong word for Hanako too, she has Lilly after all, doesn't she?"
"I realize I've been standing there far too long without answering, and pull off a flawless, not too exaggerated smile."
hi "You're welcome."
hi "Good night, Hanako."
show hanako emb_downsmile_ss
with charachange
ha "N-night."
scene bg school_hallway2
with locationchange
"I leave her to finish her book and head back to the dorms and the promise of food…"
stop music fadeout 3.0
$ suppress_window_after_timeskip = True
scene black
with Dissolve(3.0)
return
label en_A38:
window hide None
scene black
with dissolve
scene bg school_dormhisao
with openeye
play music music_daily fadein 4.0
window show
"The next day, I wake up feeling a little lightheaded. It's almost noon already."
$ renpy.music.set_volume(1.0,0.0, "ambient")
"Sleeping late is fine, since it's a Sunday and there are no classes."
"Not just a Sunday, though, but the festival as well."
"From my window I can already see some people at the soba booth slinging noodles onto plates for people with a craving for low-quality food."
"I throw back a handful of my morning meds and ponder how to spend the day."
"There will be a few exams in the coming week, but I don't consider those as ominous as others, so I'm not as worried about them as I probably should be."
"With no urgent obligations regarding education, I should be free to spend the day at the festival as I like."
scene bg school_dormhallway
with locationchange
"Finishing my morning routine, I exit into the hallway, intending to go out and find something to eat."
"Passing by his door, I decide to see what Kenji's up to today out of impulse."
"I'm curious if he has any plans, since everyone is doing something."
"Then again, I can picture him having built a soundproof shelter in his room."
"Or possibly something like a fort, complete with “No Girls Allowed” sign."
"… and with the “Girls” crossed out and “body” crudely scrawled underneath it."
stop music fadeout 2.0
play sound sfx_doorknock2
"Knocking on his door which is luckily devoid of any kind of sign, I hear again the unsettling clicking of at least ten locks being pulled back. The door opens up a crack."
show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)
ke "Who is it?"
hi "You're supposed to ask that before you open the door."
show kenji neutral at center
show bg school_dormhallway at bgright
with charamove
play music music_kenji fadein 1.0
ke "Oh, it's you. Damn, it's early."
hi "It's not really that early."
show kenji happy
with charachange
ke "What is it, man?"
hi "Nothing, was just gonna ask what you're gonna do today."
hi "Half the school is out there already."
show kenji rage
with charachange
ke "Out where? Why?"
hi "What?"
ke "What what? Is today special? Why are they there? Who are?"
show kenji tsun
with charachange
ke "I can hear them. It's loud… don't tell me… Has the invasion begun?"
"He suddenly looks more alarmed."
show kenji neutral
with charachange
ke "What day is it, man?"
hi "Yeah I guess you can't see the big wooden booths outside, and people selling stuff…"
ke "What the hell are you talking about? I have my curtains closed at all times to thwart the snipers."
hi "Uhh, it's the festival. You know that… right?"
show kenji tsun
with charachange
ke "Oh shit, that's today? Ah, damn. Ah… damn. Dammit."
ke "I can't believe I forgot, I don't have my fort finished yet. This is bad."
ke "This is going to be a very bad day… It's good you told me this, man. This is going to be a bad day."
hi "Why?"
show kenji neutral
with charachange
ke "Oh man, they're going to be everywhere. The people. Outside my window. Socializing!"
"Kenji rubs his temples nervously, suddenly looking very ill."
show kenji tsun
with charachange
ke "It's going to be loud as hell. Damn, and I was going to go out today, but now it's ruined, everything is ruined."
ke "This is awful. This sucks. This sucks!"
ke "What the hell, this really sucks. I can't go anywhere now. There's nowhere to run."
"Kenji seems nervous. You could even say he's majorly freaking out."
show kenji neutral
with charachange
ke "I can't believe this. So that's what today was."
ke "Damn, and I couldn't even prepare for it."
show kenji tsun
with charachange
ke "I couldn't even brace myself and now it's here and I can't do anything. You should have told me this earlier, dude. I mean, at least, I know, but… I could have known earlier! Imagine what I could have accomplished…"
hi "Sorry. I thought you knew."
hi "So I guess you're not going to do anything today?"
hi "The weather is even good. Yesterday was really windy, so I thought today would be cold. It's not, though, so there's no reason to just stay inside. Yeah, you should check the festival out."
"Kenji groans and covers his face with his hands."
ke "Agh, no, no! I can't do it. They'll eat me alive out there, I know it."
"That has to be a joke, but he said it with such a straight face. Relatively straight."
show kenji happy
with charachange
ke "What are you going to do? We should hang out in here, you can help me build my fort. We might still make it if we work together."
label en_A38a:
hi "I'm going to have to hang out with the Student Council, since I lost a bet."
"I realize that we didn't agree on when and where. I'll just wait for them rather than risk us missing each other in the chaos outside. They must be busy running around and organizing things, anyway."
"It's funny. I would've assumed the price for losing to Shizune in her stupid game to be a lot more severe. This is just a pretense for spending time with her. In that case, I guess she just wants me to have fun."
"Even though she can't just come out and make her intentions clear, they may be good intentions after all, and I think I'm starting to like her more."
hi "I could skip going, but it'd be a waste. And I want to go, too. I mean, you know, today does seem pretty exciting. If anything, it'll be interesting."
show kenji tsun
with charachange
stop music fadeout 1.0
ke "The Student Council? What? That's still around?"
ke "Isn't it like, two dudes?"
hi "They're both girls."
play music music_tension
show kenji rage
with charachange
ke "Really? Are they cute? Damn, no, wait… are they cute?"
ke "No! It doesn't matter! I heard the Student Council president is insane… that whoever it is never talks and only gives orders through flunkies."
show kenji tsun
with charachange
ke "Shit, they're the same in every school… Sounds like a cold-hearted bitch. Bitches everywhere."
ke "If it's two girls, they outnumber you two-against-one. That is a dangerous situation, dude. Who knows what can happen."
ke "Damn, the Student Council is just two women, but they hold so much power."
ke "They must be stopped."
ke "I can see them, plotting ways to push their feminist agenda. I can't trust an administration like that."
ke "This is not cool. Not cool!"
show kenji rage
with charachange
ke "Damn. Shit! Damn!"
label en_A38b:
hi "I don't know. I'm pretty hungry so I thought I'd get some food first and then check out the attractions."
hi "Your class project seemed pretty cool, and I gave a hand with it so I want to see at least that one and chat with Lilly I guess."
hi "Speaking of that, don't you have any obligation for the project?"
show kenji rage
with charachange
ke "Are you out of your mind?"
ke "That blind broad is up to no good; I can feel it in my spleen, man. Her presence is like a dark shadow that's in the way of my great vision."
ke "As expected of blind people."
hi "What."
hi "Besides, I thought that you were also…"
show kenji neutral
with charachange
"He holds up his hand to interrupt me."
ke "Only legally."
ke "Metaphorically, I can see farther than any man before me has seen."
"Kenji looks stoically into the metaphorical distance to emphasize his statement, thrusting his chin forward to look manlier. Actually it's just the corridor wall two meters away but it's all the same."
show kenji tsun
with charachange
ke "I can see the future of mankind, and it's a dark one unless the threat of women is stifled."
ke "They are everywhere."
label en_A38c:
hi "Well, I joined the art club so I guess I'll go with them."
show kenji rage
with charachange
ke "You did what?"
hi "I joined the art club."
show kenji tsun
with charachange
ke "Man, that was a bad move. Really bad. You don't know what kind of girls there are in the art club. Troubled, angsty cuties who tear your heart out and eat it raw."
"Well, I know one art club member, and I don't really see Rin suddenly becoming a psychotic murderer."
hi "That seems unlikely."
ke "Don't say that. Don't fool yourself. You have no idea what you are dealing with here, man. They are the worst kind."
show kenji neutral
with charachange
ke "They drag you in with all this fancy-pantsy shit and when you least expect it, BAM!"
hi "Bam what?"
"Kenji seems slightly fazed at my skepticism, but not any less loony."
show kenji tsun
with charachange
ke "It doesn't matter."
ke "Tread carefully man, tread carefully."
label en_A38d:
hi "I wonder… I'm kinda hungry, but I made this deal that I try to take better care of myself. Be healthier, you know."
hi "Dunno if I should steer clear of the takoyaki, or head straight in."
show kenji tsun
with charachange
ke "Deal? Sounds ominous. So what are you getting in return?"
hi "Nothing, I guess? It's not that kind of a deal."
hi "You know Emi, from our year? We kinda agreed to watch each other's backs and…"
show kenji rage
with charachange
ke "Aieeeeeeee!"
"The shrill scream and the expression of abject terror in Kenji's face chill my blood. It's as if I told a Catholic priest I sold my soul to the devil."
ke "Her! You sold your soul to the devil, and didn't get anything in return?"
ke "What the hell is wrong with you, man?"
ke "Do you know who you are dealing with?"
ke "She's a public health danger. Do you know how many people she sends to the hospital monthly with her carefully placed flying tackles?"
show kenji tsun
with charachange
ke "She's one of them! A key player in the vast conspiracy that aims for the complete submission of everything that is manly."
ke "I can't believe what I'm hearing. I trusted in your judgment, man. I thought we were brothers."
ke "You have to call it off before it's too late."
ke "This festival too; it's just one of their ploys."
label en_A38e:
"He fingers his scarf nervously, faster and faster like he is trying to start a fire, then slowly begins to calm down once the panic attack finishes running its course."
show kenji neutral
with charachange
ke "I'm going to have to find some place to hide in, a safe haven. And then knock the lights out of myself so that I don't have to experience this horrible day."
ke "I have the perfect thing for that. I must prepare now."
show kenji tsun
with charachange
ke "Don't go to the festival."
hi "Okay."
show kenji neutral
with charachange
ke "Later, dude."
stop music fadeout 2.0
hide kenji
with charaexit
"The door slowly closes with a low creak and I don't know how to feel about what Kenji just said."
label en_A44:
show bg school_dormhallway at bgright
with None
"I ponder what I'd like to do with Shizune and Misha. Deciding it's best to be extra prepared, I duck back into my room to stock my wallet with money."
scene bg school_dormhisao
with locationchange
"I wonder if they have that game where you try to catch goldfish on a paper net."
"It seems way easier than they make it look. Then again, if I were to catch a goldfish, I'd have no real reason to keep it."
"What am I going to do with a fish in my tiny room? Cook it?"
"I could give it to Shizune, or Misha, but that might be overstepping my bounds."
"It's a real problem. Both of them are cute, but I don't think I have any chance with either of them. Regardless, I mull over the thought of doing it. I imagine how they might react if I were to give them a gift tonight, like a fish or a doll."
"Misha would probably laugh like she always does. Shizune might slap it out of my hand."
"Maybe it isn't such a good idea after all."
"Okay, I think I'm set."
with shorttimeskip
"A good while later, I decide that this could be another psych out test devised by Shizune. Even if it isn't, it's starting to get kind of late."
"I resolve to just go out and search for them, even though I don't know where I could look. They might be really hard to find today."
scene bg school_dormhallway
show shizu behind_blank_close at center
with locationchange
"As soon as I step outside, I almost bump into Shizune."
hi "Hi, Shizune. Where's Misha?"
show shizu behind_frustrated_close
with locationchange
"I try to sign it as best as I can, but really I'm just making stuff up. I've got to ask Misha to teach me some of this."
mi "Here!"
play music music_comedy
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None
show misha hips_grin at Slide(0.5,0.5,0.3,0.5,1.0) behind shizu
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)
"Misha pops up from behind Shizune, grinning widely."
mi "We just came to make sure you're coming along with us to the festival."
show shizu basic_angry_close at tworight
with charachange
shi "…"
show misha sign_smile at twoleft
with charachange
mi "Don't renege on your promise~!"
hi "Promise? I don't think I promised anything."
show shizu cross_angry_close
with charachange
shi "…"
show misha hips_frown
with charachange
mi "Stop trying to get out of it!"
show misha perky_sad
with charachange
mi "C'mon, Hicchan, it'll be fun! You need this, anyway, or you'll become a no-good person!"
show misha perky_smile
with charachange
mi "You don't want to become one of those people who just stays in their dorm room all day, being paranoid, do you?"
"I find myself staring over her shoulder at the door to Kenji's room right across from mine."
"I hope he didn't hear that, but I think Misha wants the opposite."
hi "No, of course not. I was just playing around a little, and was right about to leave anyway. You two didn't have to come here."
show misha cross_laugh
with charachange
mi "Really? Ahahaha! Shicchan was worried you would try to get out of it somehow!"
show misha hips_grin
with charachange
mi "We need you, Hicchan~!"
hi "Huh?"
"I think my heart just skipped a beat."
show misha perky_smile
with charachange
mi "I don't have the aim to knock the dolls off their pedestals in that one game… and Shicchan refuses to throw things."
hi "Oh."
"Shizune stares at me, immediately noticing my disappointment. She uncrosses her arms and adjusts her glasses."
show shizu adjust_happy_close
with charachange
shi "…"
mi "What did you think we meant? I refuse to throw anything."
show misha perky_confused
with charachange
mi "Why, Shicchan? That is weird…"
show misha perky_smile
with charachange
mi "Well, anyway, Hicchan, you've thrown a ball before, right~, right~? So! You have to come with us!"
"I'm amazed by their logic. I don't know if they're joking or if they're not."
hi "Heh, I'd feel offended if I didn't know you guys were joking."
hi "You're joking, right?"
show shizu behind_frown_close
with charachange
shi "…"
mi "It is what it is, Hicchan~! It is what it is what it is what it is what it is!"
hi "Well that's reassuring."
show shizu basic_normal2_close
with charachange
shi "…"
show misha hips_smile_close at closeleft
with characlose
mi "Come on, let's go! The deaf band is setting up outside your window."
"Misha grabs me by the hand and tries to pull me out the door, but it's clear that she isn't trying at all."
hide shizu
with None
show shizu basic_normal2_close at tworight behind misha
with None
show shizu adjust_blush_close
with charachange
stop music fadeout 3.0
"Shizune looks at the both of us, blushing slightly and fiddling with her glasses impatiently."
"I'm not used to this kind of casual contact, but I have nothing against it. How could I object?"
play ambient sfx_crowd_outdoors fadein 1.0
scene bg school_courtyard
show crowd
with locationskip
play music music_running
"It's still light outside, but the sun is getting ready to set behind the trees."
"It looks like half the school is out here, and I can even see some faculty members standing off to the side, helping themselves to some punch."
"They are about to empty the entire bowl, to the dismay of the girl working the stall."
"There are some fortunetellers chatting idly with their friends, while others have already gotten started slinging horoscopes at anyone who walks in range."
"I think that kind of tactic is a little too aggressive, but it shows that they're into it. It's refreshing to see, but I don't know if I'll be able to get used to it."
show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter
shi "…"
show misha sign_smile
with charachange
mi "Well, we should get something to eat. Hungry, Hicchan?"
"Come to think of it, I haven't eaten all day."
hi "I don't really want to eat fried noodles."
show misha hips_grin
with charachange
mi "That's okay, there are other fried foods!"
hi "Are there any foods that aren't fried?"
show shizu adjust_smug
with charachange
shi "…"
mi "Candy. Junk food is the essence of celebrations!"
show misha cross_laugh
with charachange
mi "Wahahahaha!"
show shizu behind_smile
with charachange
shi "…"
show misha hips_grin
with charachange
mi "Come on, I - I mean, Shicchan - will treat you to one thing~!"
mi "One?"
show shizu adjust_smug
with charachange
shi "…!"
show misha sign_smile
with charachange
mi "Just one~! Only so you can build up energy for your throwing arm!"
show misha perky_smile
with charachange
mi "Ah, but it doesn't look like all the booths are done setting up yet, so you might not be able to get what you want."
"I take a look around, surprised by the number of stalls. It's unbelievable, this festival seems larger than the ones you might see in actual towns."
"Despite what Misha said, it seems like half the school is already celebrating."
"The air is humming with the excited chattering of at least half the student body."
"I can smell food cooking, and it's only making me hungrier by the second."
show shizu behind_frustrated
with charachange
shi "…"
show misha perky_confused
with charachange
mi "Come on, Hicchan, the food is already disappearing fast! If you want takoyaki, we need to move now!"
show misha hips_grin
with charachange
mi "I could go for some takoyaki~! Come on, let's eat that!"
hi "All right, I haven't had takoyaki in forever. I'm game."
hide shizu
with charaexit
hide misha
with charaexit
"Shizune takes off before Misha can even sign it back to her, briskly walking towards the takoyaki stand as Misha and I try to catch up."
scene bg school_stalls1
with locationchange
"Misha laughs as she skips towards Shizune, who asks for three orders of takoyaki by holding up three fingers."
"I never noticed it before, but for someone who is so obsessed with high class tea, it's a little weird that Shizune is also so into fast food."
"I take the plate of takoyaki she hands me and wonder if I should dig in. It looks extremely hot."
"I can see the smoke coming off of it and the oil bubbling on the surface."
show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)
"Shizune and Misha both look at me, as if waiting for me to eat before they can begin."
"I can't back down, so I spear one on the tiny plastic fork jauntily sticking up from the corner of the plate."
show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange
stop music fadeout 12.0
"However, before I can even put it in my mouth, Shizune and Misha begin eating eagerly, Shizune taking quick but delicate bites out of the takoyaki while Misha eats with relish like a small child."
"I guess at the end of the day, both of them are just kids like any other student here."
"This is kind of nice. I don't think I've had a chance like this in a long time to just hang out with other people and enjoy their company."
"Even before coming here, I'd been going through a very busy year. So busy that I hadn't realized what I have been missing until now."
"Here, I feel at peace."
"This is a soothing atmosphere. I didn't know these kinds of festivals still existed."
show misha perky_confused
with charachange
mi "Eh? Hicchan, you aren't going to eat your food?"
hi "No, I'm going to eat it."
show shizu adjust_smug
with charachange
shi "…"
show misha sign_smile
with charachange
mi "I hope you aren't chickening out because it's too hot."
hi "That's not it."
"Even their teasing is beginning to become endearing."
$ renpy.music.set_volume(0.6, 2.0, "ambient")
scene bg school_stalls1_ss
with shorttimeskip
play music music_tranquil fadein 1.0
"I eat quickly before my food can get cold, thinking that the dimly lit paper lanterns glowing warmly against the sunset make for a beautiful sight."
show shizu behind_smile_close_ss at center
with charaenter
"Before I can finish my last bite of takoyaki, Shizune steps in front of me, standing perfectly straight with her arms rigidly behind her back."
"I can see she's trying her best to look as serious as possible, but even she can't hide her good mood, as there is a slight smile on her face."
show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove
show misha cross_laugh_ss at twoleft
with charaenter
mi "Ahahaha~! Come on, Hicchan, let's go play some games!"
hi "Are they even done setting up?"
show shizu adjust_happy_close_ss
with charachange
shi "…"
show misha cross_grin_ss
with charachange
mi "No, but it doesn't matter, it doesn't matter~! Come on, Hicchan, before it gets too crowded!"
show misha hips_grin_close_ss at closeleft
with characlose
"Misha puts her hand on my shoulder and laughs very loudly."
show misha perky_smile_close_ss
with characlose
mi "Come on! Come on! The prizes look really great this year, really really~! Wouldn't you like to win some prizes for two cute girls like us?"
"Misha flashes her best “cute” look, which is admittedly pretty cute. I look at Shizune, expecting her to do the same, but she just looks at me like I'm insane."
show shizu cross_wut_close_ss
with charachange
shi "…"
show misha hips_grin_close_ss
with characlose
mi "Misha, stop doing that!"
show misha perky_confused_close_ss
with charachange
mi "Wait… I'm Misha…"
show shizu basic_normal2_close_ss
with charachange
shi "…"
show misha sign_smile_close_ss
with charachange
mi "Hicchan, hurry up, you've been holding that piece of takoyaki for like a thousand years!"
show misha cross_laugh_close_ss
with charachange
mi "Hahahahaha!"
show misha cross_smile_close_ss
with charachange
hi "I like to savor everything that I eat. Even this."
show shizu basic_sparkle_close_ss
with charachange
show shizu adjust_smug_close_ss
with charachange
"Without warning, Shizune picks the takoyaki from my hand and plops it into her mouth with a smile."
"It happens so fast that there was no way I could have stopped her."
show misha cross_laugh_close_ss
show shizu behind_smile_close_ss
with charachange
"Before I can even fully process what just happened, Misha bursts into laughter, and Shizune smiles at me, probably the closest I've ever seen her come to laughing."
show shizu adjust_happy_close_ss
with charachange
shi "…!"
mi "Well, that takes care of that~! Wahaha! Hahahaha!"
stop music fadeout 6.0
"Shizune grabs my right hand, and Misha grabs my left."
show shizu behind_smile_close_ss
with charachange
shi "…"
show misha hips_grin_close_ss
with charachange
mi "You're coming with us! There's a lot to do tonight, you should try harder to enjoy it!"
show misha cross_laugh_close_ss
with charachange
mi "Hahahaha~!"
$ renpy.music.set_volume(1.0,2.0, "ambient")
scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip
play music music_ease fadein 6.0
"Running through an already sizable crowd of people, we play game after game, from ring toss, to whack-a-mole, to games I've never even heard of."
"We rarely win, but it's fun nonetheless."
hi "Hey, do they have that goldfish scooping game here?"
show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter
shi "…"
mi "Of course! I didn't know you liked that game, Hicchan!"
hi "Well, I've always wanted to try it. It doesn't seem too hard."
show misha hips_grin_ss
with charachange
mi "Are you sure about that, Hicchan~?"
show misha cross_laugh_ss
with charachange
mi "Wahahaha~! Okay, okay! We'll see! It should be around here somewhere!"
show shizu basic_normal_ss
with charachange
shi "…"
show misha perky_smile_ss
with charachange
mi "But, where are you going to keep your fish? Do you have a bowl for it?"
hi "Well, no…"
show misha hips_grin_ss
with charachange
mi "Maybe he'll eat it!"
show shizu adjust_smug_ss
with charachange
shi "…"
show misha cross_laugh_ss
with charachange
mi "Hahahahahaha! Ahahahahahaha!!"
show misha cross_grin_ss
with charachange
mi "All right, Hicchan, if we win any fish, we'll give them to you!"
hi "Oh, really? Another game? Fine, then."
show shizu basic_happy_ss
with charachange
"Shizune pushes me excitedly towards the booth, trying to hide the enthusiasm in her eyes."
scene bg school_stalls2_ss at bgright
with locationchange
"Fortunately, the two of them fail to catch a single fish, but I don't do any better."
show bg school_stalls2_ss at bgleft
with charamove
$ renpy.music.set_volume(0.6,2.0, "ambient")
"I can't help but laugh as immediately afterwards, they start tugging me towards a particularly large, colorful stall that I helped build."
"I remember this one; it had been a real pain in the ass to make."
"The booth runner, an average-looking guy with dyed brown hair, snaps to attention when he sees us walking over. I notice two things:"
"First, it's one of those games where you throw a ball at a pyramid of opaque bottles and try to knock over as many as possible."
"Four balls for 50 yen, that's pretty good."
"Second, there are instructions on how to play in braille. I almost want to say something, and look to see if Shizune and Misha see it as well."
"Either they don't, or they don't find it strange at all."
"Booth Operator" "Hey! It's good to see you, Hakamichi! Thank you so much for your help with this booth. Having fun?"
"Shizune glances towards Misha, who signs everything to her in a flash, then beams at the operator."
show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)
shi "…"
show misha hips_grin_ss at twoleft
with charachange
mi "Haha~! It was nothing, nothing at all, really~! Yeah, this is great, I think the best festival we've put together yet!"
show misha perky_smile_ss
with charachange
mi "Shiraki, we'd like to play this, that's okay, right?"
show misha hips_grin_ss
with charachange
mi "Of course~, it would be really great if you would just give your cute, hard working Student Council representatives a prize, for all the hours we put in to make all of this possible!"
"Shiraki" "Hahaha, haha… No."
"If anything, Shiraki has balls."
hi "Hey, I built this stall, it was a backbreaking job, too. I wasted two hours of my life, I think I deserve at least a free round."
show misha hips_frown_ss
with charachange
mi "And me!"
show shizu basic_angry_ss at tworight
with charachange
shi "…"
mi "Me too!"
show misha perky_confused_ss
with charachange
mi "Ah…"
"After some hesitation, he eventually gives in, and hands us each four balls with a shrug."
show misha hips_grin_ss
show shizu behind_blank_ss
with charachange
"Barely a second later, Shizune and Misha dump theirs in front of me."
hi "What gives?"
hi "Don't tell me that after making such a big deal out of it, you two aren't going to even play?"
hi "Not after the way we ganged up on Shiraki."
"Shiraki" "Yeah…"
show shizu basic_frown_ss
with charachange
shi "…"
show misha sign_smile_ss
with charachange
mi "You stay out of this, please~!"
show shizu adjust_happy_ss
with charachange
"Shizune turns to me and begins waving her hand dismissively. Misha appears torn between translating for her and consoling the booth operator."
show shizu adjust_smug_ss
with charachange
shi "…!"
show misha hips_grin_ss
with charachange
mi "Ahahaha! Hicchan, where's your sense of chivalry? Besides, I - Shicchan, have a policy against throwing balls!"
show misha hips_smile_ss
with charachange
mi "Ah, sorry, Hicchan. I don't know if my aim is that good, either. You must be pretty good at these things, though, right, right? It shouldn't be a problem for you!"
stop music fadeout 3.0
"This looks simple enough. The bottles aren't even that far away, the only challenge is that these are wiffle balls."
play sound sfx_impact
"I throw one at the bottles hard, and it bounces off unceremoniously."
show shizu behind_blank_ss
show misha perky_confused_ss
with charachange
hi "What the hell?"
"Shiraki" "Ah, yeah, it's not as easy as it looks. There's water inside the bottles. Trade secret."
show misha hips_frown_ss
with charachange
mi "That's not very fair!"
hi "This must be why it's four balls for 50 yen. How devious."
show shizu basic_angry_ss
with charachange
shi "…"
show misha hips_smile_ss
with charachange
mi "Come on, Hicchan, you can knock them down! You have eleven more chances! Go!"
hi "Maybe you should do it."
hi "Shizune? Do you want to try?"
show shizu behind_blank_ss
with charachange
"Shizune emphatically shakes her head from side to side."
"I laugh, this is actually pretty fun."
play sound sfx_impact
play music music_soothing fadein 3.0
"Winding up, I throw another ball at the pyramid of bottles and manage to get them to budge just slightly."
show shizu basic_normal_ss
show misha perky_smile_ss
with charachange
"Both Shizune and Misha are casting longing glances towards a doll shaped like a cat."
"All-in-all, they really aren't that different."
"Sometimes I wonder if Shizune would sound like Misha if she could talk."
"No, they're not that alike."
play sound sfx_impact
"I throw another ball, realizing that it's actually quite simple. If I can hit two bottles in the bottom row at the same time, it's an easy win."
"Already, a small crowd is beginning to gather, so the pressure is really on me. Nine more shots."
play sound sfx_dropstuff
"Winding up like a baseball pitcher, I throw as hard as I can and the bottles come tumbling down."
show shizu behind_blank_ss
show misha cross_laugh_ss
with charachange
show stuffedcat:
    pause 0 alpha 0.0 yalign 0.5 xanchor 0.5 xpos 0.6 subpixel True
    easein 1.0 xpos 0.5 alpha 1.0
with Pause (1.0)
"Triumphantly, I claim my girlish cat doll prize and Misha laughs uproariously as if it was her who won it."
"Shizune stares at me with her usual blank expression. It's clear she wants the doll too."
show stuffedcat:
    easeout 1.0 xpos 0.4 alpha 0.0
with Pause (1.0)
hide stuffedcat
with None
show shizu basic_normal2_ss
with charachange
shi "…"
show misha hips_grin_ss
with charachange
mi "Hicchan, congratulations~! What are you going to do with that doll?"
"There is no right answer. I have to tread carefully."
hi "I… do not know."
mi "Wellllll~ I'll take it, if you don't want it…"
show shizu adjust_smug_ss
with charachange
shi "…"
show misha cross_grin_ss
with charachange
mi "Unless you want to keep it for yourself, Hicchan. I didn't know you liked dolls. How delicate."
hi "I don't. I have no use for this."
show misha cross_smile_ss
with charachange
mi "Can I have it, then?"
show shizu behind_blank_ss
with charachange
shi "…"
"Their eyes are drilling into my soul."
"This is a decision I don't want to make. I turn back to the booth."
hi "Hey, you have more than one of this doll?"
"Shiraki" "Actually, yeah, just one more."
hi "Okay, set everything up again, I want to try for that one as well."
"I still have eight tries."
play sound sfx_pillow
"As soon as the game is set up again, I throw as hard as I can again, but miss."
show misha hips_grin_ss
with charachange
mi "Hahaha! Trying to win another one? Taking the easy way out, Hicchan?"
hi "If it's that easy, you could try it."
mi "No thanks~!"
show misha perky_smile_ss
with charachange
mi "Say, Hicchan, can you at least put the doll down while you throw the balls?"
hi "No."
show shizu adjust_smug_ss
with charachange
shi "…"
mi "There's only one more left, you had better get it! If you fail, I'll kill you~!"
show shizu behind_smile_ss
with charachange
shi "…"
mi "What a clever way to duck out of giving me the doll, though! And by me, I mean me~!"
show shizu adjust_happy_ss
with charachange
shi "!"
show misha cross_laugh_ss
with charachange
mi "Ahahahaha~! Just kidding!"
"I can see Misha didn't mean any harm from it, and Shizune seems to enjoy her joke, smiling at it, but she looks a little depressed afterwards."
"I decide to hand her the doll, at least while I'm trying to win the other one. It's kind of hard to aim holding a giant cat."
show shizu behind_smile_ss
show misha perky_smile_ss
with charachange
shi "…"
mi "Thank you, Hicchan. Shicchan seems happy, Hicchan~! But, you're going to win one for me, too, right?"
hi "That is what I'm trying to do, isn't it?"
stop music fadeout 5.0
show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None
hide shizu
hide misha
with Dissolve(1.0)
play sound sfx_pillow
"I throw again, but my aim is way off this time."
"My arm feels kind of heavy as well, as if blood isn't flowing to it properly."
"I scold myself mentally, thinking that it's pathetic I could get tired from something like that."
"Then I realize maybe it's because of my heart. If it is, then I don't know what to think."
play sound sfx_impact
"It's depressing that even something as small as this is enough to make me realize my own mortality."
"I guess there won't ever be a time when I'll be able to forget about it."
"Even today, when I thought I would be able to just enjoy myself, on this beautiful night and in this beautiful place, I can't escape the reason why I'm here."
"I've never felt so at peace in my life, in this place which is like nowhere else I've ever been."
play sound sfx_pillow
play music music_sadness fadein 2.0
"It's hard now to keep from thinking the unthinkable:"
"That I may just have been sent here to die."
"These past few days have been some of the best of my life. The first time in a long time that I've ever felt truly alive."
"But in the end, I'm someone who finds himself reminded every time he climbs too many stairs or throws a ball too hard that he could die at any second."
play sound sfx_pillow
"I'll always be limited by this."
"I feel depressed by that, and angry as well. In the end, I care about my life, and I enjoy it, and now it's more transient than ever before."
"I wonder what it is that will finally do me in. It could be anything, if I'm this weak and pathetic: a bad fall, a punch to the chest, a stray baseball."
"I've now lost my will to keep playing this game, but I keep playing anyway."
stop music
$ renpy.music.set_volume(0.0,0.0, "ambient")
play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)
hide heartattack alpha
with Dissolve (0.7)
"Suddenly, I feel a split-second sensation of pain in my chest. It comes and goes instantaneously, but it's enough to make me stumble just a bit."
$ renpy.music.set_volume(0.4,10.0, "ambient")
show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)
"Shizune jumps back, startled. She comes closer, staring at me with concern. Misha puts her hand on my shoulder."
play music music_pearly
mi "Hey, Hicchan, are you okay?"
hi "Yeah, I'm fine. I don't really feel too good right now. I think I'm sick. I don't think I can go on."
show misha hips_frown_close_ss at twoleft
with charachange
"Misha frowns."
mi "Don't strain yourself. If you're that sick, you'll just make yourself sicker."
show shizu basic_normal2_close_ss at tworight
with charachange
shi "…"
show misha hips_smile_close_ss
with charachange
mi "Look, the festival is just getting started, and we've been playing games for a while. We can take a little break if you're tired."
show misha sign_smile_close_ss
with charachange
mi "Good idea, Shicchan, I'm feeling a little tired too! I think we're all a little worn out, running all over the school, Hicchan!"
"I nod. They don't seem to notice anything unusual. That's good."
scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip
$ renpy.music.set_volume(1.0,2.0, "ambient")
"We walk through the sea of people, with Misha cheerfully pointing out the faces of everyone she knows. Shizune holds the stuffed cat in her arms, cradling it absentmindedly. It seems like they're having fun."
"Suddenly, I feel a pang of guilt."
"Because of my poor health, we all had to stop."
show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter
shi "…"
mi "Hicchan, we're both feeling kinda hungry. How about you?"
hi "I'm not as hungry as I could be, but I do want something to eat."
show misha hips_smile_ni
with charachange
mi "That's good enough, Hicchan~! So, what should we get to eat?"
hi "It doesn't really matter to me."
show shizu adjust_happy_ni
with charachange
shi "…"
show misha hips_grin_ni
with charachange
mi "Ah! How about sandwiches, then? And we'll need something to drink, too! Misha'll get everything!"
show misha perky_confused_ni
with charachange
mi "What?"
show shizu behind_smile_ni
with charachange
"Shizune looks at me and smiles, and I realize she might be trying to cheer me up with a joke. I laugh."
show shizu adjust_happy_ni
with charachange
shi "…"
show misha perky_smile_ni
with charachange
mi "Hicchan, it's getting kind of crowded, so we might not be able to eat here. It's getting kind of loud, too."
show misha sign_smile_ni
with charachange
mi "Maybe we should go eat up on the roof."
hi "That's fine with me. It might be a nice view, and there could be a little breeze."
show misha hips_grin_ni
with charachange
mi "Okay then! I guess I should get the food and drinks now… So I'll see you two then~!"
hide misha
with charaexit
stop music fadeout 6.0
"Misha gives a clumsy wave and then runs off."
"Before, I didn't notice how the paper lanterns look illuminating the dark night, but now that I'm able to see it, it's really an amazing sight."
"Fireflies float overhead, their soft glow making it look as if it's snowing lights in the night sky."
"This type of thing would be impossible to see in the city."
show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None
show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)
"Shizune tugs at my sleeve impatiently and crosses her arms, frowning as if to show displeasure at me for getting distracted."
show shizu basic_angry_close_ni at center
with charachange
shi "…"
hi "You know I don't know how to read sign language."
show shizu behind_frown_close_ni
with charachange
shi "…"
"Come to think of it, isn't it kind of stupid of me to have said that to a deaf person? She wouldn't have heard it."
show shizu behind_blank_close_ni
with charachange
"I shrug, hoping to show her that I don't understand. Shizune shakes her head and dismisses it with a wave of her hand."
"Maybe I should get around to asking Misha for some lessons on sign language."
$ renpy.music.set_volume(0.3, 1.0, "ambient")
scene bg school_roof_ni
with locationskip
"Climbing up onto the roof, I find myself in awe again at the sheer size of this school. The grounds are so expansive I can't believe I hadn't realized it before."
"As I walk across the roof, trailing behind Shizune, I can't help but be taken in by the stars shining in the sky."
show shizu behind_smile_close_ni at center
with charaenter
"Shizune and I sit down on a bench. She seems like she's in a good mood as she smiles softly while the breeze blows through her hair."
"We look down at the festival, which looks like a sea of glowing amber lanterns and waving paper fans teeming with people, some of them festively dressed in yukata."
"In fact, most of the girls seem to be wearing yukata. I wonder why Shizune and Misha didn't dress up today."
"The two of them would look nice in yukata. I briefly think about what types they would wear."
"Shizune would likely go with something traditional. However, Misha is a bit harder to place."
"Misha arrives, panting as she runs to us, trying to keep the food in her arms from falling."
"Setting everything on the ground, she lets herself drop backwards."
show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove
show misha hips_grin_ni at twoleft behind shizu
with charaenter
mi "Ahahahahahahahahaha~! That took awhile! Come on, you two didn't tell me what you wanted, so I got some rice punch, some sandwiches, and some candy, too! A little bit of everything!"
hi "That's great. Let's dig in."
"Misha takes a bite out of a small, triangular sandwich."
show misha hips_smile_ni
with charachange
mi "So, Hicchan, what do you think of the festival? It's nice, isn't it?"
hi "Yeah."
show shizu adjust_happy_close_ni
with charachange
shi "…"
mi "The stars are nice tonight. This couldn't have been a more perfect day."
play music music_serene fadein 5.0
$ renpy.music.set_volume(0.1, 2.0, "ambient")
scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange
"The sound of people talking below us is like faint music alongside the chirping of crickets in the distance."
"I take a sip from the can of punch and look over at Misha, who looks as if she's sleeping comfortably with her back stretched out and a half-full can of apple juice balanced on her stomach."
"Shizune sits with her legs drawn close to her, rocking back and forth slowly like an impatient child as she stares up at the sky."
"The two of them are so cute. I look around and can see many students holding hands with their girlfriends or their boyfriends."
"Not too far from us on this roof, there are couples gazing up at the stars or down at the lights of the festival, holding each other's hand."
"A part of me wants that."
"Looking at Shizune and Misha, I wonder if maybe I should ask one of them out some day. I wonder if it would be worth the risk."
"The golden hands moving across the face of the delicate watch on Shizune's wrist catch my eye, and I see that it's getting kind of late. But the festivities are still going strong."
"Shizune is still holding the stuffed cat I won by the paw. She notices me looking at it."
shi "…?"
"Offhandedly, she offers it to me. I smile, wanting to ask her what I would do with it, but she wouldn't be able to understand me."
"I shake my head and try my best to tell her to keep it, hoping she'll understand."
"As I look out towards the school, I can see before me so many people, all of which are happy and cheerful."
"Watching them makes me feel content."
"This really was something. Today was worth it."
"But I still can't shake the feelings of guilt and melancholy from earlier, they keep hanging onto me, and I can't let them go."
"Shizune signs something to me, and I can't understand her. No matter what I say, she won't be able to hear me."
hi "I can't understand you, Shizune."
hi "Well, whatever. I wonder if we both consider ourselves at fault for this. Anyway, I'm sorry for not being able to understand."
hi "You know, I'm almost, almost glad that you tried to coerce me into coming here. If I attempt to date you, though, I might have to think more about that side of you."
hi "No, actually… I'm glad. Today was nice."
hi "You would be cuter if you smiled more, you have a nice smile."
stop music fadeout 5.0
show shizu behind_frustrated_close_ni at center
show bg misc_sky_ni at right
with charaenter
"Frustrated, she stands up, arms behind her back, looking authoritative and confident against the backdrop of stars."
stop ambient fadeout 2.0
show shizu out_serious_close_ni
with charachange
"Suddenly, Shizune throws her arms out towards the open sky, seeming to hold it between her hands."
"It's as if she's telling me to look at everything in front of me:"
show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu
"The school, bathed with the festival's glow and lit up with the colorful yukata, the roof illuminated by fireflies, the sky so vast that it imposes the feeling of awe onto you."
"What does she want? It slowly dawns on me with time. This beautiful scene before me is proof that there are things wonderful enough that spoiling them with a bad mood would be unforgivable."
"And I can feel the weight of Shizune's personality pressing the point further."
hi "Thanks, I guess."
hide shizu
show hill pairtouch at center
with charachange
"I look away, but then Shizune grabs me by the shoulder, her watch brushing against my cheek."
"With her left hand, she points up at the sky."
play ambient sfx_fireworks fadein 1.0
show fireworks behind hill
with None
show fw_screen behind fireworks
with Dissolve(5.0)
"With faint pops, fireworks begin to go off in the sky, each one spreading a shower of bright colors that slowly fade into the dark."
"I can't even recall the last time I saw fireworks at all, much less a display this large. Not to mention it seems that they're being launched from the school; it's almost impossible to believe."
"The lights in the sky mingle with a second salvo from the town below, and they seem timed to complement each other like two parts of a duet."
"They continue for maybe fifteen more minutes, and then stop."
"Shizune realizes her hand is still on my shoulder and withdraws it carefully, looking a little uncomfortable."
stop ambient fadeout 5.0
hide fireworks
hide fw_screen
show hill pairnotouch
with Dissolve(5.0)
"Regaining her composure, she grins, with her hands on her hips and her chest thrust out in front of her."
"It's in these moments that she seems most like a regular teenage girl. Energetic, happy, and carefree."
"I eat thoughtfully with Shizune, the two of us looking out at the gradually thinning crowds below in silence."
"She sits leaning forward slightly, her chin resting softly on her hands and a contented look on her face with just a hint of wistfulness."
"All the while still gently holding on to the stuffed cat's paw."
"I start feeling tired and I tell her that I'll see her and Misha tomorrow, without even realizing that she can't hear me, and then start walking back to the dorms."
"I feel warm and alive, even in this chilly night air."
stop music fadeout 4.0
"The image of Shizune standing forcefully before the stars themselves, denying my self-pity, does not leave my mind easily."
"If… if it only takes a moment for there to be love, I think I may be falling in love with her."
"Just a little bit."
window hide
label en_A39:
show bg school_dormhallway at bgright
with None
"It's kinda unsettling, and now I start to feel doubtful, myself."
"Should I bother going?"
"I've got a book I've been meaning to read."
"Something about an underground postal system that may or may not exist."
"It's short, too. I could have it finished in a day."
"But would that be a good way to spend my time?"
"Well, yeah. It definitely would be."
"But I suppose that it would probably be a better idea to head outside."
"See the festival."
"Try to integrate with all the other sideshow acts."
"Honestly, I should at least make an attempt to keep up the somewhat friendly personality I've had the past week."
"Maybe get something to eat, my stomach suggests."
"It's almost lunchtime… I could at least grab something from one of the stalls outside."
play music music_soothing fadein 1.0
play ambient sfx_crowd_outdoors fadein 1.0
scene bg school_courtyard
show crowd
with locationskip
"I'm soon outside, surrounded by various students and people who may or may not be their parents."
"Every so often I catch a glimpse of someone who clearly just came up from town for the promise of a festival."
"They're easy to spot."
"The ones who can't stop staring, and behind their eyes you can tell they're thinking “Now, what's wrong with {b}this{/b} one?”"
"I almost want to yell at them."
"But at the same time, can I deny that I've been doing the same thing all week?"
"A wave of something like disgust sweeps over me; guilt for my own narrow-mindedness."
"…"
$ renpy.music.set_volume(0.6,2.0, "ambient")
scene bg school_stalls1
with locationchange
"I push the thoughts aside, concentrating on the pangs of hunger that burn my guts like a wildfire."
"The scent of something fried leads me to the promised land, where I can get some lunch."
stop music fadeout 0.6
"I'm just getting my order when a loud voice interrupts me."
show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter
emi "Hey, what the hell are you doing?"
play music music_comedy fadein 0.5
hi "Having break— er, lunch."
show emi sad_annoyed at center
with charachange
emi "Breakfast?"
show emi sad_angry
with charachange
emi "You mean you just got up?"
hi "Er…"
"Suddenly sleeping all morning feels like a crime."
hi "No, I meant lunch… honest."
"She's not buying it."
hi "Brunch?"
show emi basic_annoyed_close
with characlose
emi "That's not a healthy breakfast at all!"
"She snatches my food out of my hand and glares at me."
"What the hell is this girl doing?"
hi "Hey, that's my breakfast!"
show emi sad_annoyed_close
with charachange
emi "What happened to it being your lunch?"
hi "That's my… whatever, it's my food!"
"Emi places her hands on her hips and begins lecturing me."
show emi basic_annoyed_close
with charachange
emi "Did you really forget your dietary plan already?"
emi "You need to be more conscious of your health, Hisao!"
show emi sad_angry_close
with charachange
emi "What about your heart?"
hi "My heart's fine the way it is! Mostly."
"All I get in response is a roll of the eyes."
show emi basic_annoyed_close
with charachange
emi "I doubt that."
show emi basic_closedgrin_close
with charachange
emi "You wouldn't be here if that was the case, would you?"
"The girl's got a point, of course."
"But I'm not about to concede it."
hi "It's not that bad of a heart!"
hi "Certainly it can handle a little grease now and again!"
"Yeah, sure. And it handled a little running just fine, too."
show emi basic_annoyed_close
with charachange
"Emi seems unconvinced."
"Not surprising, as I haven't even managed to convince myself."
emi "Maybe, but not if you're sleeping the day away all the time!"
"A devious look suddenly crosses her face."
show emi basic_grin_close
with charachange
emi "Of course, if you'd been following a routine from the beginning you wouldn't be in this situation…"
stop music fadeout 6.0
hi "Hey, I've had a pretty eventful week, you know!"
hi "For example, I almost died! And there was a lot of meeting people, and then I was on a roof for a while…"
show emi sad_annoyed_close
with charachange
emi "Which is no excuse for slacking off, you know."
emi "A little near death experience is no excuse for skipping basic exercise."
show emi basic_closedgrin_close
with charachange
emi "Like running in the mornings."
"She nods, as if something important has just been decided."
show emi basic_happy_close
with charachange
play music music_emi fadein 0.5
emi "So it's settled, then!"
show emi excited_proud_close
with charachange
emi "You've seen the error of your ways and are willing to adhere to my routine, right?"
emi "I'll see you bright and early in the morning?"
show emi excited_happy_close
with charachange
emi "We'll be running buddies?"
hi "You know, you'd already convinced me yesterday that this was a good idea."
hi "You don't need to convince me again."
"Not that I did a good job of being convinced."
"She's right about eating healthy, after all. And here I am ordering up something grossly unhealthy."
"But delicious!"
"There are more important things than deliciousness, aren't there?"
"Like staying alive?"
"If Emi weren't here browbeating me for my poor decisions, I'd probably…"
"Hey, wait a second."
"A sudden question springs to mind."
hi "Hey, why the hell have you taken such an interest in my well-being?"
show emi basic_closedgrin_close
with charachange
"Emi shrugs and grins at me."
show emi basic_grin_close
with charachange
emi "You're the new guy."
emi "I figure you don't have any friends yet, right?"
show emi sad_grin_close
with charachange
emi "Besides, I've caused you trouble all week, right?"
emi "I owe you for not getting angry."
show emi basic_happy_close
with charachange
emi "And I told the nurse I would, anyway."
"Uh… huh. Crazy little running girl wants to make me healthy."
"Well, I suppose there are worse fates."
hi "Okay, that sounds… fine."
hi "Thanks for your concern."
hi "Tomorrow morning, then?"
stop music fadeout 1.0
hide emi
with charaexit
"I figure that ends the conversation, so I turn to leave."
emi "Not so fast!"
play music music_running
with vpunch
"I feel a hand on my collar and in a second I've been yanked backwards."
hi "Hey, no need to be so rough!"
hi "What do you want now?"
show emi sad_shy_close at center
with charaenter
"Emi looks almost wounded by my annoyed question."
emi "Thought you could use the company."
show emi basic_annoyed_close
with charachange
"Her eyes narrow."
emi "Besides, you were just going to try sneaking some more of that fried crap, weren't you?"
"Well, I wasn't going to, but now that she mentions it that would have been a really good idea."
hi "I was not!"
show emi sad_annoyed_close
with charachange
"Another glare."
hi "Okay, maybe I was going to get a little…"
"The glare continues."
hi "Okay, a lot."
"Jesus, I'm a danger to myself and others, aren't I?"
"I get done agreeing that I need to be healthier, and then immediately start considering the next unhealthy habit that comes my way."
show emi basic_closedgrin_close
with charachange
emi "I knew it! You can't be trusted."
show emi basic_grin_close
with charachange
emi "Now I definitely have to stick with you."
"This whole situation feels silly."
"I can only imagine what passersby think of the sight of me being lectured by a tiny girl half my size."
"Maybe I should just give up for now."
hi "Fine, do what you like."
"I sigh."
"Might as well make the best of this."
hi "What do you want to do?"
show emi basic_confused_close
with charachange
"Emi thinks for a minute."
emi "Well, I promised Rin I'd stop by her mural…"
show emi basic_grin_close
with charachange
emi "So let's do that!"
"I confess I'm slightly curious as to how her mural turned out myself, so again I consider there are worse fates."
$ renpy.music.set_volume(1.0,2.0, "ambient")
scene bg school_courtyard
show crowd
with locationchange
"I give a nod of assent and find myself almost dragged bodily through the crowd as Emi races to our destination."
stop music fadeout 6.0
stop ambient fadeout 2.0
scene bg school_dormext_full at bgright
with locationchange
"By the time we reach the dorms, I can feel my heart pounding."
"My heart shouldn't be pounding after just that."
"I take a few deep breaths, willing myself to calm down."
"I'm one of the most normal looking people in the school, but I still have to be here."
"Sometimes I almost wish I'd lost a hand or something."
"At least then it'd be obvious that I belong."
"But instead I don't even look sick."
"Even now, trying to catch my breath, I just look out of shape."
"Emi looks back and notices my state of distress."
show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter
emi "You're not going to die on me, are you?"
show emi basic_shock at center
with charachange
emi "Please don't!"
show emi sad_depressed
with charachange
emi "It'll be all my fault, and I don't want to deal with that kind of guilt."
emi "Besides, after the last time I really don't think I need to see that again, especially because the nurse will totally say it's all my fault."
play music music_soothing fadein 8.0
hi "N… nah, I'm fine."
hi "Guess I need to start running after all."
show emi basic_closedgrin
with charachange
emi "And you wanted to keep eating your greasy… whatever it was."
show emi excited_proud
with charachange
emi "See? It's a good thing I found you, right?"
"Yes it was."
hi "Maybe."
show emi basic_grin
with charachange
"Of course I don't add that I wouldn't be in this state if she hadn't dragged me across the festival grounds."
"Further conversation is interrupted by the sudden appearance of Rin."
show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)
rin "Oh, it's you."
show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove
show rin basic_awayabsent
with charachange
rin "Hello Emi."
show emi basic_closedhappy
with charachange
emi "Hey Rin! I brought Hisao along because he was going to give himself a heart attack!"
show rin basic_absent
with charachange
hi "I was not!"
"My objection goes unnoticed."
show emi basic_grin
with charachange
emi "We stopped by to see how the mural turned out!"
"Rin nods slowly."
show rin basic_awayabsent
with charachange
rin "Well, it's right there."
show rin basic_deadpan
with charachange
rin "You can see it pretty clearly."
"I find myself wondering how long Rin's been standing here in front of the mural."
"Has anyone even stopped by to look at it?"
"Are we the first ones?"
"Obviously we're not the first to see it, of course."
"I mean, it's pretty big."
"You'd be hard-pressed not to see it."
"At the same time, I don't think anyone's actually talked to Rin about it."
"Anyone but us, that is."
"I feel compelled to say something."
hi "It looks pretty good."
show rin negative_spaciness
with charachange
rin "I'm still not happy with how it turned out."
rin "But I guess it'll do."
"She seems almost resigned to it."
"I'm not sure what she expected as a result, but I guess she didn't quite get there."
scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)
"We stand in front of the mural, taking it all in."
"I try my best to concentrate on the composition of the thing."
"It's actually fairly interesting."
"The colors swoop and blend together, dragging me along with them."
"There's a dreamlike quality to the whole thing that makes me almost feel sleepy."
"I try hunting out some of the colors Emi and I grabbed for her."
"Try as I might, I can't see any Prussian Blue."
"Oh well."
"I'm sure it's in there somewhere."
scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)
"My feet start to hurt, but Rin doesn't seem inclined to move on."
"Emi speaks up."
show emi basic_confused
with charachange
emi "Hey Rin, have you eaten?"
show rin basic_deadpan
with charachange
rin "Of course. You can't survive otherwise."
show emi basic_hes
with charachange
emi "What about in the past five hours?"
show rin relaxed_nonchalant
with charachange
rin "Maybe. But I'm hungry again, so maybe that means I'm wrong."
show emi basic_closedgrin
with charachange
"Emi grins and claps her hands together."
show emi basic_grin
with charachange
emi "Good! Come get some food with us!"
"Rin nods in assent."
show rin basic_deadpannormal
with charachange
rin "Okay, but we should hurry before they notice I'm gone."
"Somehow I don't think they'd care."
"Whoever they are."
stop music fadeout 3.0
$ renpy.music.set_volume(0.6,0.0, "ambient")
play ambient sfx_crowd_outdoors fadein 1.0
scene bg school_stalls1 at Fullpan(8.0)
with locationskip
"As we head back to the food stalls, I cast a longing eye over the fried food."
"No, I'd better not."
"I'm pretty sure Emi wouldn't let me, anyway."
stop ambient fadeout 1.0
scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange
play music music_ease fadein 9.0
"We find a nice spot on the grass and sit down to eat our purchases."
"Well, my purchases, anyway. Somehow I've wound up paying for all the food."
"Surprisingly, my (unfried) food is pretty good."
"Silence falls as Emi and I eat and Rin stares at… something or other, occasionally eating a bite or two of her food."
"I finish my meal first, and lay back on the grass."
"Emi glances up from her food."
show emi basic_confused
with charachange
emi "Tired, Hisao?"
hi "A little, I guess."
show emi basic_annoyed
with charachange
emi "Well, don't oversleep or anything tomorrow morning."
show emi excited_proud
with charachange
emi "We start our morning runs, remember?"
"Actually, they'd slipped my mind."
"I was actually just enjoying myself."
"Wandering around the festival with these two has actually been fun."
hi "Yeah, I'll set an alarm."
show emi basic_annoyed
with charachange
emi "You'd better be there!"
show emi basic_closedgrin
with charachange
emi "I'll get angry if you aren't!"
hi "God forbid."
show rin basic_lucid
with charachange
rin "I don't think God comes into it."
show rin basic_deadpan
with charachange
rin "Unless there's some kind of freak accident and your alarm clock shorts out."
show rin basic_deadpannormal
with charachange
rin "That might be a random act of God."
show emi basic_grin
with charachange
emi "Well don't cause any random acts of God, then."
"A plan forms itself in my mind."
"It's a plan that makes me feel kind of guilty, but I throw it into execution anyway."
"Dammit, I've earned a little fried food."
"And anyway, I'm going to start running tomorrow, right?"
"So the actual routine all starts then, not now."
"Ergo, the dietary portion starts tomorrow too, ergo I can have something unhealthy today."
"A sort of final farewell to all the stuff I used to eat with wild abandon before the hospital."
hi "Actually, I suppose I should head back to my room."
hi "I had some homework to do, and if I'm going to run in the morning I should make it an early night…"
show emi basic_annoyed
with charachange
"Those narrowed eyes again."
show emi sad_annoyed
with charachange
emi "You sure you're not just going to sneak off and buy some of that fried stuff over there?"
hi "Nah, I'm too full to bother now."
"I pat my stomach for emphasis."
hi "Besides, you two have cleaned me out anyway."
show emi basic_closedhappy
with charachange
"Emi giggles. It's a surprisingly pleasant sound."
"Another pang of guilt."
"She's got to know that I'm lying to her, doesn't she?"
"Or is she just that trusting?"
"I feel kind of like a monster."
show emi excited_proud
with charachange
emi "All part of my master plan, Hisao."
show emi basic_closedgrin
with charachange
emi "Well, I guess I'll see you tomorrow morning then."
show emi basic_grin
with charachange
emi "Thanks for the food! And for keeping us company!"
"And here I thought she was doing me a favor."
show rin relaxed_surprised
with charachange
"Rin nods in agreement."
rin "I won't say “See you tomorrow” because that would be like predicting the future, and I'm pretty sure I can't do that."
hi "…"
hi "Okay."
hi "Bye, you two."
"I feel oddly glad that I decided to leave my room today."
"Not a bad way to start my second week here, I suppose."
stop music fadeout 9.0
play ambient sfx_crowd_outdoors fadein 1.0
scene bg school_stalls1
with locationchange
"Once I'm sure I'm out of Emi's line of sight, I make a beeline for the food stands and buy some cake."
"At least it's not fried, right?"
"That's slightly better than what I was planning to do."
"I still feel a little bad about lying to Emi, though."
"She really does seem concerned about my health."
"I'll make it up to her somehow."
"Better head back to my room."
"Hey, I {b}do{/b} have work to do."
stop ambient fadeout 1.0
scene bg school_dormhisao
with locationskip
"My book waits for me, and I flop on to my bed and read through the fireworks display."
$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 2.0
scene bg school_dormhisao_ni
with Dissolve(2.0)
"Eventually all the walking around (or more accurately, running around) catches up with me."
"I really am out of shape."
"Emi dragging me out in the morning to run might just be a good thing after all."
"It's something to look forward to."
stop ambient fadeout 2.0
window hide
label en_A40:
play ambient sfx_crowd_outdoors fadein 0.3
play music music_soothing fadein 0.5
scene bg school_dormext_full
show crowd
with locationskip
"The happy hubbub of the crowd greets me as I push myself through the main door and step outside."
"The school grounds were transformed into festival grounds over yesterday and this morning."
"Colorful stands line at the main walkways from the main entrance to the school building."
"Some people are still carrying stuff to and fro, but behind most counters are relaxed students who look like they are good to go."
"Most of the other students have been up early to finish the preparations."
"A feeling of guilt passes through me, but it soon goes away."
"I'm just a lowly transfer student, after all."
"Some visitors are already strolling around the grounds."
"There are some young families with the perturbed parents trying to keep up with their overenthusiastic offspring…"
"…a few students of our own accompanied by their parents…"
"…and a lot of old and young people who are here for no reason I can imagine."
play sound sfx_warningbell
"The carillon bursts into life and the principal's squeaky voice announces the opening of the festival over the PA system."
"Everyone applauds politely if a bit unenthusiastically."
"A school festival… we didn't really have festivals at my old high school. It feels kind of old-fashioned, especially considering the school I came from, but it's still somewhat exciting."
"A day off feels sweet after the first week of hard work, despite me lying on the hospital bed for four months prior to this."
"I recall even wishing that I could go to math lessons during my stint at the hospital."
"I can't remember the program for the festival, even though Mutou went through it during class just the other day."
"I step off the dorm steps, intending to take a tour around the grounds to see all the stuff the others have set up, but I only make it down to the bottom of the stairs."
stop ambient fadeout 1.0
hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)
"A few people are studying Rin's mural on the wall, while the artist herself is lounging on the sidelines, leaning against the wall and looking extremely bored and mildly under the weather."
hi "Good morning."
show rin relaxed_surprised
with charachange
rin "Hello."
hi "How's it going?"
show rin relaxed_nonchalant
with charachange
rin "Nowhere."
rin "I'm stuck."
hi "What do you mean stuck?"
rin "I mean I can't walk stuck. I think my legs are out of order because of yesterday."
hi "Does it hurt?"
show rin relaxed_sleepy
with charachange
rin "It's hard to say. Maybe."
"The strain of working on the mural was greater than she let me know. I thought it was just a bit of tired muscles or something. I mean to ask something further, but Rin swiftly moves on to another topic."
show rin basic_awayabsent
with charachange
rin "Teacher's friends came by."
show rin basic_absent
with charachange
rin "Then they headed into town for lunch and asked me to go. It was a good thing my legs hurt so much."
hi "But you're stuck sitting there? That's not good."
show rin basic_lucid
with charachange
rin "I'll just wait till I can walk again. It should be either sooner or later, if you think about it for a while."
rin "Teacher was happy that I finished the mural."
hi "He should be."
show rin basic_awayabsent
with charachange
stop music fadeout 5.0
rin "But I wonder if it's finished after all."
hi "Oh?"
show rin basic_deadpanupset
with charachange
rin "I thought yesterday that I had done everything, but now I'm not sure any more. I should paint more details. Maybe. Probably. It's very hard to decide."
"Finished or not, the mural looks great in broad daylight."
play music music_another fadein 2.0
scene bg mural at Transform(xalign=0.05)
with Dissolve(2.0)
"Various human body parts, repeated over and over in a wildly mutating, mostly disfigured variety are the main element."
"They are rough-looking, as if thoughtlessly placed and rudimentarily painted, but a great deal of thought and care has gone into each and every one of them."
show bg mural at Transform(xalign=0.25)
with charamove
hi "Does this one have a frog growing out of his head?"
rin "It's a goldfish."
show bg mural at Transform(xalign=0.45)
with charamove
hi "What's that?"
rin "It's nothing."
show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None
"Anyway…"
"The wall is so wide I have to turn my neck from side to side to see the entire painting."
"It's hard to consider it as a single piece. The elements don't seem to fit together, but I guess they do create some kind of a whole."
"Abstract as it is, I have no idea what it's supposed to be portraying, but it looks nice. That's enough for me."
"I settle myself next to Rin, leaning against the wall like she does."
"The happy noises of the festival are becoming louder as more and more folks enter the grounds."
"The dorms are far from the main attractions in the main building and the stands around the courtyard so most visitors have not found their way here yet."
show rin negative_spaciness_close at offscreenright
with None
show rin negative_spaciness_close at tworight
show bg mural at Transform(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))
"A somewhat bored expression settles on Rin's face, making her look detached from everything that's going around her."
"She is being awfully quiet. I wonder if she's in pain."
hi "So what did the art people say about your mural?"
show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)
"My question wakes Rin from her daydreaming. She lazily turns her face towards me."
show rin basic_deadpan_close
with charachange
rin "I'm not sure."
show rin basic_awayabsent_close
with charachange
rin "I think they liked it? Maybe they did."
hi "What about you? Are you happy with the mural? 'Cause I kind of participated, it'd be terrible if you were unhappy."
"Rin tilts her head, biting her lower lip."
show rin negative_sad_close
with charachange
rin "I think it came out decently. It's not bad but it's not good either. It just… is. I guess I'm all right at being empty-minded."
hi "Can I ask something else? What does the painting really portray? I thought about it yesterday, when you said that it doesn't portray anything."
hi "But that's a logical fallacy, isn't it? You can't make something out of nothing, not even art."
show rin negative_annoyed_close
with charachange
"Rin frowns and turns her head back towards the clouds."
rin "I don't know. I am not really good at explaining things. It's just a mural; there is nothing special to it. I said it already."
"She sounds annoyed at my inquiries."
rin "I didn't know what I'd paint, so I decided to paint just a mural."
rin "It's a mural that portrays a mural."
show rin basic_deadpancontemplation_close
with charachange
rin "No, wait. I just thought up a better way to say it: It portrays itself."
show rin basic_deadpannormal_close
with charachange
rin "So… its muralness is at the maximum, at least as far as I can do, so if you think it has some meaning, I think that's the same as this one has."
"That makes no sense."
"Meaning… I feel the corners of my mouth turning upwards into a smile that's just a tiny bit bothered."
stop music fadeout 5.0
scene mural all
with flash
"I have never understood art in the deepest meaning of the word."
"I get the basics, how art is supposed to be only a means for exchanging ideas and thoughts."
scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash
"However, I never learned how I should interpret a piece of art, to somehow divine what the artist intends to say through it."
"I know it's not any special skill, but somehow, my brain never can connect art with anything else than what I see. All I see is a mural."
"I can admire the technical skill, after all even I know the difference between bad art and mediocre art; mediocre art and good art."
"But that's as far as I can go, so don't ask me about meanings, Rin."
"Her reply sure made me reluctant to ask her about it any further either."
hi "So what are you doing when you get on your feet?"
play music music_happiness fadein 4.0
scene bg mural at Transform(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash
rin "Nothing."
hi "Nothing? But there's the festival, don't you want to go have some fun?"
show rin basic_absent_close
with charachange
rin "I'm fine like this."
hi "You don't like socializing much, do you?"
"I think I'm arguing more for her than for myself at this point. It's not that I'm particularly thrilled about the festival, either; just a bit curious to see what it's like, and that's about it."
"Her answer is unsurprising."
show rin basic_awayabsent_close
with charachange
rin "No, I don't."
hi "I guess… me neither, in the end."
show rin basic_deadpan_close
with charachange
rin "You should go if you want to."
hi "I know, but I can keep you company. I'm not used to all this just yet, so it's okay to take it easy."
hi "I can leave though, if you want to be alone."
show rin basic_deadpannormal_close
with charachange
rin "I like it if you are here."
"We circle around each other with words, but eventually end up somewhere. Her saying that makes me feel oddly happy, so I stay."
"Her presence is something I like too. The odd, warm aura of serenity that she seems to emanate makes it comfortable to be silent. I really like that."
"We watch people walk by, the two of us silent, everyone else chattering happily among themselves."
"Students are leading their families to the dorms to show their rooms. They pass us and the mural, maybe glance at it once or twice."
"I pay less attention to them, and more to my companion, trying to figure my way past her cryptic, unreadable wall of a face."
show rin basic_awayabsent_close
with charachange
show rin basic_absent_close
with charachange
show rin basic_awayabsent_close
with charachange
"Rin's eyes flicker restlessly from one person to another as they walk by."
"Is she waiting for people to stop at the mural, maybe secretly hoping someone would comment on it?"
"I don't think anyone would assume she was the artist. We're just sitting here like a pair of hobos, after all, and she doesn't even have hands."
"I wonder if it's even in Rin's style to fish for compliments. She seems so aloof."
"More people walk by, some of them pointing their fingers at the mural, exchanging words that I can't make out. Someone drops a snow cone on his shoe. Too bad for him."
hi "Everyone seems to like it."
"I suggest it tentatively, throwing a topic in the stale summer air separating us."
"Rin doesn't answer right away, but by now I am mostly used to her occasional slowness when she must talk. It's like she takes great care picking her words, which is really unbelievable when you consider the jumble that comes out of her mouth."
show rin basic_lucid_close
with charachange
rin "I wanted to make it so that you can just look at it without thinking. Then I realized that it doesn't make any sense. So it became something like a mix of this and that."
show rin negative_spaciness_close
with charachange
rin "From far away, it looks like someone vomited a herd of butterflies on the wall. Which is exactly what that obnoxious president person didn't want. Is that word that?"
hi "What word?"
show rin basic_deadpannormal_close
with charachange
rin "That. What is the word for more than one butterfly?"
hi "Butterflies?"
show rin basic_deadpanupset_close
with charachange
rin "No, like a herd, or a school, or a heap."
hi "Oh. I don't know. A flock maybe?"
rin "Maybe people like butterfly vomit."
show rin negative_confused_close
with charachange
"Rin looks at the mural, looking surprisingly unhappy."
rin "The middle could be better."
show rin negative_annoyed_close
with charachange
rin "Usually I like in-betweens, but this was a pain in my butt. Not literally of course… then again I did get that too. I guess it was literally after all."
hi "Don't be so critical of yourself."
show rin basic_deadpannormal_close
with charachange
"She looks at me funnily, but shuts up."
scene bg school_dormext_full at bgright
with locationchange
"At about this point I start thinking if I should really leave and do something more constructive with my Sunday."
"This is the pinnacle of social failure. A whole free day, a festival right outside my doorstep, and what do I do?"
"Sit here with Rin; two bystanders with nothing to do except to think what a pity it is to be just a bystander."
"Even realizing how pitiful it is, I don't do anything. I don't stand up and take off for a day of fun."
stop music fadeout 5.0
play sound sfx_rustling
centered "*shuffle shuffle*"
"…"
centered "*fidget*"
play sound sfx_rustling
centered "*shuffle*"
"…"
scene bg mural at Transform(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange
"Rin is shuffling about restlessly, constantly swinging one leg over the other knee and then back again."
"She has a very irritated look on her face."
hi "Is something wrong?"
show rin basic_deadpanupset_close
with charachange
rin "Yes. No. Yes."
scene bg school_dormext_full at bgright
show rin basic_deadpanupset:
    pause 0 xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 0.5 yanchor 1.0
with locationchange
"She suddenly hops up on her feet. It's surprising, I thought she was still rendered immobile but apparently that's not the case."
show rin negative_confused at tworight
with charachange
rin "I have to go find Emi or someone, I need some help with something."
hi "I can help you."
show rin relaxed_nonchalant
with charachange
rin "No, it's okay. One of us has to stay here in case something happens."
hi "Don't be ridiculous. Nothing even remotely interesting has happened since I came here except that one guy who dropped a snow cone on his foot. Let me help you, since I'm bored."
hi "So what is it?"
show rin negative_annoyed
with charachange
"Rin's lips flatten tightly against each other into an almost perfectly horizontal line."
show rin basic_lucid
with charachange
"She closes her eyes and draws in a deep breath."
"When she opens her eyelids the frighteningly stern look in her dark eyes takes me aback."
play music music_rin fadein 0.5
show rin negative_angry
with charachange
rin "Hisao, you might not want to hear this or maybe you do, I don't know, but it doesn't matter and even if it would you are not leaving me any choice."
rin "I'm having my period and I need some help regarding that. However, I don't feel that our relationship is yet on the level where I could allow you to pull my underwear down in the girls' toilet even if you offer to."
rin "That's why you should stay here while I go and look for Emi."
"As blood rushes to my cheeks like the rising tide my brains try to desperately search for an answer, but the only thing I can think of is how that was the most coherent thing I have heard coming out of Rin's mouth during these four days I've known her."
hi "Yes."
hide rin
with charaexit
stop music fadeout 4.0
"Not wanting to meet Rin's eyes, I turn my face aside, pretending I'm looking at someone's parents."
"From the corner of my eye I see Rin turning on her heel and walking off without further ado."
"I feel like going to hide under some rock."
"I wonder how long Rin will be gone… or if she will return at all."
scene bg mural at Transform(xalign=0.6)
with shorttimeskip
play music music_dreamy fadein 3.0
"She does return eventually, appearing seemingly out of nowhere and sitting back to where she was, next to my place."
show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)
rin "I'm back."
"She says it flatly, like my blunder never happened. I'd prefer to forget the whole matter as well, so I keep quiet."
scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin:
    pause 0 xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.85
    easein 3.0 xpos 0.8 yanchor 0.9
with Dissolve(3.0)
"Time passes in standstill, the sun gleams from high above the main building. It hits me directly in the eyes, but I just squint instead of moving."
"In a bit it becomes painful to keep my eyes open just a little, and my temples start aching."
hi "My head hurts. I think this day gave me a headache, can you believe it?"
show rin basic_deadpan_close_ss
with charachange
rin "Are you hungry?"
hi "How is that related to headache?"
show rin basic_deadpansurprised_close_ss
with charachange
rin "It's not. I ask because I am."
"…"
"Her oblivious seriousness melts my irritation with its ridiculousness, and I find the corners of my mouth turning slightly upwards again."
hi "You know what? So am I."
hi "I'll go get some food for us. What do you want? My treat."
show rin basic_lucid_close_ss
with charachange
rin "Doesn't matter."
show rin basic_deadpannormal_close_ss
with shorttimeskip
"Returning with the food, I give one portion to Rin, taking the other for myself and we dig in without a word."
show rin negative_spaciness_close_ss
show rin_shadow negative at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange
"Rin looks upwards, fork hanging out the corner of her mouth."
rin "What are clouds? I always thought they were thoughts of the sky or something like that. Because you can't touch them."
hi "You thought like that when you were a kid?"
rin "No, last week."
rin "Maybe because sometimes my thoughts feel like clouds. Fluffy and white and slow."
rin "Like the sky was in my mind. Like my mind was the sky."
hi "The sky of your mind?"
rin "Close your eyes and think of sky. You won't be able to think of anything else until you stop."
scene black
with shuteye
"I try it. It works. Magic?"
scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9) behind rin
with openeye
"Opening my eyes, I see Rin studying me with her eyes. It feels uncomfortable because she doesn't say anything. I turn away."
scene bg misc_sky_ss at Fullpan(20.0)
with locationchange
hi "Clouds are water. Evaporated water."
hi "You know they say that almost all of the water in the world will at some point of its existence be a part of a cloud."
hi "Every drop of tears and blood and sweat that comes out of you, it'll be a cloud. All the water inside your body too, it goes up there some time after you die. It might take a while though."
rin "Your explanation is better than any of mine."
hi "Because it's true."
rin "That must be it."
"I carry on eating the food before it gets cold."
"The wall offers a bit of blessed shade as the sun revolves around the dome of the sky."
"But the afternoon is already slowly making way for the evening so our lunch becomes more of a dinner. Or whatever the word is for an irregular meal like this."
"Despite what I decide to call it, it certainly hits the spot. I haven't eaten a bit since forever."
"…"
"My appetite filled, I let out a satisfied sigh. Rin hasn't eaten all of hers but seems to be done with her food as well."
"I lean back, taking in the atmosphere. The crowd has thinned already, but the activities are still going. Everyone seems to be enjoying themselves."
"And why not? It's warm, the kind of perfect summer day when it's hot but not too hot for comfort."
"The sun will set soon. Time really has flown by."
scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9) behind rin
with locationchange
hi "We've been sitting here for six hours."
show rin basic_deadpansurprised_close_ss
with charachange
rin "Yes we have."
show rin basic_deadpancontemplation_close_ss
with charachange
rin "Do you want to do something else now?"
hi "No, not really."
show rin basic_deadpannormal_close_ss
with charachange
rin "Me neither."
show rin basic_lucid_close_ss
with charachange
"She adjusts her position and leans against the wall, and I follow her lead, relaxing my own body."
"For minutes on end, we sit there without saying a word."
"I'm trying to feel Rin's mood from her demeanor, the tension of her muscles, the tiny expressions fleeting on her face. It's no use. She's unreadable as always."
$ renpy.music.set_volume(0.5, 0.0, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 1.0
scene bg school_dormext_full_ss
show crowd_ss
with locationchange
"The crowd swells to and fro, people happily chattering with each other. Very few people pay real attention to the mural, and even less to us."
"I fiddle with a few odd pebbles absentmindedly."
"The act of doing something just for the sake of doing something, the pinnacle of idleness."
"Inch by inch, the sun creeps lower and lower towards the treeline, changing the color of the sky close to the horizon from golden yellow to orange and red as the moment of sunset draws near."
"I feel like my stomach is filled with lead after eating so heavily, but the brick wall feels surprisingly comfortable against my back."
"I try to fight against the drowsy feeling that is overwhelming me, to no avail."
scene black
with shuteye
stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)
with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0
scene bg misc_sky_ni
with openeye
"I wake up with a start."
"A low boom reverberates through the school grounds. Afterimages of bright sparks flash through my vision like stars."
"Something rises towards the skies from the direction of the sports field."
"A tail of fire trails behind it until a burst of red and yellow flame lights the sky high above the school with another loud boom."
show fireworks
with dissolve
"Fireworks."
"The sudden flash of light against the canvas of the night sky awakens me to realize that it's actually dark already."
"How long did I sleep? I feel groggy and can't feel my right arm."
"As I attempt to flex it, I realize why."
play music music_twinkle fadein 1.0
show rin basic_lucid_close_ni:
    pause 0 xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
    easein 1.0 xpos 0.9
with Dissolve(1.0)
"Rin is leaning heavily against my shoulder, almost falling on my lap."
"She is fast asleep, not even fazed by the fireworks."
"Her mouth is slightly open and her eyes are peacefully closed. A sleeping child-like face of the innocent."
"I shake Rin gently with my free arm, trying to wake her up or failing that, move her so that my other arm is liberated from its pinch."
"Rin's face twitches and her eyelids shut tighter, as if to resist against waking up."
show rin basic_deadpanupset_close_ni at Transform(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange
"She gradually opens her eyes but keeps them half-closed, letting the light from the fireworks sneak just past her eyelashes so that her green irises mirror the bright flashes of the explosions, then looks up at me and frowns."
show rin basic_deadpan_close_ni
with charachange
rin "Just a while longer, okay?"
"Rin's voice is drowsy and slow, leaving her almost unintelligibly muttered words hanging lazily in the air."
"It seems she is not entirely aware of the situation."
show rin basic_lucid_close_ni
with charachange
"Rin's head drops back on my shoulder as she leans against me with all her weight."
"She snuggles against my side, trying to make herself comfortable but making me feel very uncomfortable at the same time."
"I become intensely, almost painfully aware of Rin's warm body and the deep, peaceful movement of her chest against my arm, her breathing soon returning to the even rhythm."
"I can't help admiring her gift for sleeping, or the ease of mind of hers to use someone she has known for less than a week as a pillow."
"The rockets rise up to the sky one at a time, breaking into flowers of red, green and gold, accompanied by the oohs and aahs of the audience."
"I try to push Rin's disconcerting proximity out of my mind, for what can I do about it? I just hope her short while really is that."
"One by one, the glittery bursts are born and die in a blink of an eye, coloring the dark night sky into a constantly changing abstract painting."
"I listen to the low booms of the explosions and Rin's quiet breathing, trying to clear my own head of the post-awakening disorientation."
"Thankfully, just a while longer really proves to be just a while, as Rin stirs from her slumber and wakes up again before the fireworks are over."
show rin relaxed_sleepy_close_ni
with charachange
rin "I fell asleep."
show rin basic_awayabsent_close_ni
with charachange
show rin basic_lucid_close_ni
with charachange
show rin basic_awayabsent_close_ni
with charachange
"She finally opens her eyes completely and blinks a few times."
hi "You fell asleep on top of me. Twice."
show rin basic_absent_close_ni
with charachange
rin "You didn't like it?"
hi "Err…, well…"
show rin basic_absent_close_ni:
    ease 1.0 ypos 1.0
"Despite the inconclusive stammering, Rin sits upright, drawing herself away from me."
hi "Well, you are heavy."
"It's a lie, she weighs next to nothing, but I have to get a jab back at her, even if it's under the belt. My mock protest fails to draw any reaction as Rin's attention draws upwards, to the flashes of the fireworks."
show rin negative_spaciness_close_ni at Transform(xpos=0.9, xanchor=0.5)
with charachange
"She seems hypnotized by the colorful play of the explosions."
"A slight tingling sensation goes up and down in my arm as blood starts to circulate again. It's unpleasant but it helps me to get rid of this dizzy feeling."
"More and more rockets rise up to the sky, the bright colors of their explosions reflecting from the clouds."
"Both of us stare at the fireworks fixedly through the canopy of the trees, enthralled by the show."
"We would get a vastly better view of the sky if we moved even a couple of yards, but neither of us bothers to even suggest it."
show rin negative_worried_close_ni
with charachange
rin "I really do like fireworks, even though looking at them makes me feel kinda sad, I think. It's like they want you to look at them so bad so they are loud and bright, but when someone looks, they are already gone."
show rin negative_sad_close_ni
with charachange
rin "It's like they were not even real."
"…"
hi "They are real, I can tell you that."
hi "All of this is… real, you know?"
hi "If you think about it, nothing really lasts for long. Even something like my life or yours is just a blink of an eye in the history of everything, like one of those rockets. Poof, and we're gone."
hi "But we're here, aren't we?"
"Yeah, this is reality. Rin, sitting next to me, the loud bangs of the fireworks, the vast, unlimited sky. These things are definitely real, even though they won't stay here forever."
"I feel warm inside, and I wonder if it's because Rin is so close to me or just the feeling of being alive."
show rin negative_spaciness_close_ni
with charachange
rin "I don't really know what I should say next."
hi "It's all right… maybe I'm just talking to myself."
hi "But you know, fireworks are pretty… but in the end isn't it somehow silly to spend so much money on a fraction of a second worth of pretty sparkles?"
show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None
show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)
"Rin rips her gaze off the still ongoing spectacle and leans backwards, looking at me with a repulsed face."
rin "Wow, I never expected you to be such a cynic."
hi "Cynic is a pretty harsh word. Rather than that, I think of myself as a realist."
show rin relaxed_surprised_close_ni at tworight
with charachange
rin "Isn't a realist just the word for what a cynic calls himself?"
stop ambient fadeout 1.0
hide fireworks
with dissolve
"The final rocket goes out with a bang of silver and blue, leaving the grounds eerily silent for a moment until the crowd starts moving towards the main gate like a cattle herd."
"Wisps of gray smoke drift towards the dorms from the sports field. The pungent, sulfurous smell of gunpowder it carries along feels like it sticks to my hair and clothes."
hi "Was that it?"
show rin negative_spaciness_close_ni
with charachange
rin "I think so."
scene bg school_dormext_full_ni
with locationchange
"I stand up and stretch my sore back. Sleeping against a brick wall wasn't such a good idea after all."
show rin negative_spaciness_ni:
    pause 0 xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 1.0 yanchor 1.0
with Dissolve(1.0)
show rin basic_absent_ni at tworight
with charachange
"Rin stands up as well and turns to face me, with an expectant gaze on her tired features."
"Although she seems to have trouble focusing her eyes, she is looking straight at me, something I feel has not occurred too often in the past week."
hi "Umm…so…"
"I suddenly realize we have been almost on a date here, as if by accident. Even if we did nothing."
"But it wasn't… so why blood is rushing to my cheeks and my speech stammering?"
"I don't know what I should say, especially since it seems Rin is waiting for me to say something, but luckily she solves my problem for me."
show rin basic_deadpannormal_ni
with charachange
rin "Good night, Hisao."
hide rin
with charaexit
"She gives me one more lingering look, measuring me from tip to toe, turns around on her heel and skips off, disappearing into the crowd."
stop music fadeout 7.0
"…"
hi "Okay… Good night."
"I'm left standing there, giving my response to the cooling night air."
"Sigh."
"The festival turned out to be nothing like I expected."
"I ended up spending all day in one spot with Rin, even though neither of us agreed on nor suggested that we do anything."
"I just didn't have anything better to do and evidently, neither did she."
"Rin's warmth lingers for a while longer in my body before disappearing into the falling night."
window hide
label en_A41b:
scene bg school_gardens
with shorttimeskip
$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 0.5
play music music_soothing fadein 0.5
"After buying a plastic plate of takoyaki from a stall belonging to the class next to ours, I take a seat in the school gardens and watch people pass as I tentatively nibble away at the rather bland-tasting item."
"I guess I shouldn't complain. It's better than nothing and didn't cost much."
"As I look out towards the school, watching the people coming and going proves a surprisingly entertaining way of passing the time as I eat."
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
show bg school_courtyard
show crowd
with locationchange
"Little children accompanied by parents or grandparents scamper about in the din from event to event; one hand dragging their company and the other bearing an oversized, colorful snack."
"I can't help but notice the age range among the people here is skewed towards the elderly, something that I'd also noticed when I was walking around town."
"This must be one of those towns where the only people left are those that lived here their whole lives and ardently refuse to leave, and those wanting to live out the rest of their days in one of the increasingly few tranquil places."
"I guess that also goes a way to explaining how conservative Yamaku's school culture seems to be."
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
scene bg school_gardens at Fullpan(8.0)
with locationchange
"Not that I mind one bit. I kind of like how calm Yamaku and its surroundings are."
"The heat, though, is another matter entirely. Sitting in one place for so long has focused my mind on how annoyingly humid it's getting, now that the hottest part of the day is here."
"I'd better get moving if I—{w=.5}{nw}"
play sound sfx_warningbell
"Gah!"
"The sound of the carillon bells takes me completely by surprise as I stand up, a reaction shared by a few of the people strolling around as well."
"The PA system crackles to life after the tolling bells end. Its age shows as the principal makes a barely intelligible announcement over it, officially opening the festival that's very much in full swing."
"It's quite amusing to contrast the pleasant smiles of the older folk against the alternatively pained and bored grimaces of their younger charges. The students, on the other hand, seem to pay it little heed."
"Nevertheless, as the address finally ends, all are united in polite - if not overly enthusiastic - applause, and then get back to business."
"Slipping a hand in my pocket to look as relaxed as possible, I casually glance around for something to do."
"…It's somewhat difficult to see very far with all the people around."
"I decide to fall back on a tried and trusted rule: go where everyone else seems to be gathering. Right now, that's the school courtyard and surroundings."
play sound sfx_can_clatter
"Throwing the used plate into a trash can, I make my way towards the school building."
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
scene bg school_courtyard
show crowd
with locationchange
"Seeing the number of stalls around the perimeter of the school building surprises me. Quite a few of the classes must have opted to have multiple stalls."
"In deciding which to visit first, I catch sight of a familiar banner with a blue patterned border and red text."
"Lilly's stall is as good a place to start as any. I'm curious as to how it's going, after all of the work she and her class have been doing for it."
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")
scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange
"Stepping up to it, I begin to see why the class took so long to organize everything."
"Easily twice as wide as many of the other stalls and with equipment for cooking strewn everywhere, it's closer to an outdoor restaurant than a festival event."
"As a student in front of me takes a bowl of noodles and leaves, I walk up to the counter."
"The girl behind it seems quite exasperated, and asks me to wait a moment before she disappears underneath the counter."
"Seizing the moment, I take a quick glance around."
"Steam seems to be rising from everywhere, as pots and pans simmer away. The most blind of the students are unpacking ingredients while being helped by someone who is probably the teacher of 3-2."
"It doesn't take long to notice Lilly among them, talking with the teacher as she quickly counts out the boxes and packets with her fingers."
"From her expression and the fact that both she and the teacher seem to be in a state of mild confusion, it appears that there's been some problem in coordination."
"Before I can stare any longer, the girl behind the counter pops up again, only to look back and ask where the spare change box is."
"Lilly pauses for a moment, before she and the girl switch places at the counter and the teacher quickly walks off somewhere."
stop music fadeout 2.0
show bg school_stalls2 at left
show lilly basic_smileclosed at center
with charaenter
li "Sorry about that, we're having a few problems. What would you like?"
"It takes me a second to remember what I'd come here for. My eyes quickly dart to the side to read the menu sitting on the counter."
hi "Oh, uh, I guess some… miso soup?"
show lilly basic_surprised
with charachange
li "Ah, is that Hisao?"
hi "Yep. Looks like you're pretty busy."
play music music_ease fadein 6.0
show lilly basic_weaksmile
with charachange
"Her face all but confirms it as she drops her waitress facade."
li "Somewhere along the line, our order got mixed up. We're trying to fix it now, but it looks like we only have half of what we needed."
hi "Wouldn't serving smaller portions cover over the problem?"
show lilly basic_sad
with charachange
li "It seems like that's what we'll have to do, though I wish we didn't. The fact that a good half of our class is gone doesn't help, either."
"I glance behind her to see how many people are actually operating the stall."
"It couldn't be over about eight."
hi "I take it that's why your teacher left?"
show lilly basic_weaksmile
with charachange
li "That's right. She's going to try and round up a few more of our classmates to help."
"Hearing the sound of footsteps behind me, I stealthily glance backwards to see an elderly couple taking a place in the line. I guess I'd better stop loitering around and chatting."
hi "Here's the money for the soup."
show lilly basic_smile
with charachange
li "Soup… oh, right, coming right up."
"Lilly turns and calls for a bowl of miso soup as I hand over the money for it."
show lilly basic_reminisce
with charachange
"Taking the coins in her palm, I can't help but notice how efficiently she counts them out with her long, pale fingers. Eventually satisfied that I've handed over correct change, she puts it into a small metal tray."
show lilly basic_smileclosed
with charachange
"It isn't long before the soup is made and carefully handed to her, after which she turns and subsequently passes it to me."
hi "Thanks. I'll come back to drop off the bowl."
show lilly basic_smile
with charachange
li "Thank you, Hisao. Oh, there is one other thing. Have you seen Hanako?"
hi "Hanako… no, not today. Why?"
show lilly basic_sad
with charachange
"She gives a small sigh of abject disappointment."
li "It's okay. I was just wondering what she was doing for the festival."
show lilly basic_weaksmile
with charachange
li "You'll come back when you're done, then?"
hi "Sure. I'll keep an eye out for Hanako, too."
li "Thank you, Hisao."
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
scene bg school_courtyard
show crowd
with locationchange
"I walk off from the stall and find a seat, carefully cradling the steaming wooden bowl in both hands."
"Compared to the dumplings from before, this is quite nice. A little cool compared to what it probably should be, perhaps, but the flavor is enough to cover for that reasonably well."
"As I drink, I can't help but feel somewhat guilty for not being as involved in the festival as the others."
"It can't really be helped, considering I was dropped into the school only a week ago, but it still weighs heavily on my mind."
"That, and the fact that a few students don't really seem to be enjoying the festival as much as the visitors."
"Eventually I finish my bowl and leave for the stall, to drop it off."
"Considering that there seems to be no line at all, I take my time walking up."
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
scene bg school_stalls2
with locationchange
"It seems the teacher's mission paid off: there are now over a dozen students helping, and much of the unpacking has been done."
"Despite most of them seeming quite relaxed as they work, Lilly still appears to be somewhat stressed."
label en_A41a:
stop music fadeout 4.0
"…Right. I know what I'll do. Even if it's just one person, I'll make the festival more enjoyable for her."
"As I place the bowl on the counter, I call out to Lilly."
show lilly basic_smile at center
with charaenter
li "Ah, Hisao. You brought it back?"
hi "Yeah, here."
hide lilly
with charaexit
"I slide it into her hands, and she takes it over to someone who is apparently on cleaning duty. Considering that I didn't see them here before, it's probably a penalty for their tardiness."
hi "Hey, Lilly?"
show lilly basic_smileclosed at center
with charaenter
"She perks up and returns to the counter as she hears my voice again, realizing that I'm still here."
hi "Want to go see some more of the festival?"
play music music_another fadein 0.5
show lilly basic_pout
with charachange
"She puffs her cheeks disapprovingly. It looks kind of cute, and in complete contradiction to her usually reserved nature."
"It takes a few seconds for me to get what she's taking issue with. Whoops."
hi "Ah… um, I didn't mean to…"
show lilly basic_giggle
with charachange
"Lilly giggles at me, exposing her teasing for what it is."
li "You're still not used to the school, are you?"
"She got me."
show lilly basic_reminisce
with charachange
li "Still… I kind of need to stay with our stall. It's taken until just now to even get everything unpacked."
"I guess her reluctance shouldn't overly surprise me, considering how much work she's put into this."
hi "Everything seems to be running fine now, though. Besides, you've got extra help on hand, anyway."
show lilly basic_surprised
with charachange
"A boy in the middle of cooking some soba noodles turns towards us, grinning."
"Student" "Go on Lils, you've earned yourself a break. We can hold down the fort, for now."
show lilly basic_displeased
with charachange
li "If you say it's okay, then I suppose so…"
show lilly basic_reminisce
with charachange
li "But, if you need any help—"
"Student" "Then we'll call you. Go on, we'll be fine."
hide lilly
with charaexit
"Lilly finally gives up her resistance as he waves a spatula at her. She feels her way around the back of the stall, and picks up her cane on the way."
"I guess the first thing we should do is look for Hanako. Lilly seems kind of worried about her, and I doubt she'd be the kind of person to enjoy milling about in crowds like this, all alone."
hi "So, I guess we should search for Hanako. Where to, first?"
show lilly cane_reminisce at center
with charaenter
li "Hmm…"
"The both of us go quiet for a moment to think."
hi "Maybe she's in her dorm room?"
li "I doubt it. She doesn't keep too many things in there, so she'd have nothing to do."
show lilly cane_satisfied
with charachange
li "…Ah! The library?"
"As good a place as any to search for an avid reader, I suppose."
hi "The library it is. We'll check there first, then."
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
scene bg school_lobby
with locationskip
"Aside from the muffled sounds of the crowd seeping in from outside, the inside of the school seems almost deserted."
"In order to make sure everyone had enough room, I guess all the events were organized to be held outside, on school grounds. They're definitely quite large, by any other school's standards."
show lilly cane_smileclosed at center
with charaenter
li "It's nice and quiet in here, isn't it?"
hi "Yeah. Much nicer than the hustle and bustle outside."
stop ambient fadeout 3.0
scene bg school_staircase2
with locationchange
"We take our time and slowly walk through the first floor of the school, eventually reaching the stairs to the second floor."
scene bg school_hallway2
show lilly cane_smileclosed
with locationchange
"I can't help but notice how Lilly anticipates every door and obstacle, her cane remaining still and her hand skating along the hallway railings."
hi "You really know the school well, don't you?"
show lilly cane_smile at center
with charaenter
"She smiles and nods straight ahead."
li "I've been here for a few years now, so I know where everything is."
show lilly cane_sad
with charachange
li "The dorms still trip me up though, sometimes. I haven't been there as long, and they're not as well laid-out as the main building."
li "If I'm remembering right, they used to be unused buildings before being renovated and used as dormitories."
"That explains why the male and female dorms looked different from the outside, and why their rooms seem kind of unusual for sleeping quarters."
"I'd assumed she'd been living in the dormitories since she began attending the school, but now I'm reminded of what she said yesterday."
hi "That's right, you mentioned that before."
hi "I'd assumed that most of the students here lived in the dormitories once they enrolled. A lot of them seem to, in any case."
show lilly cane_reminisce
with charachange
"Lilly's expression becomes somewhat harder to read, my questioning evidently touching on a delicate point."
li "Well… How should I say…"
show lilly cane_weaksmile
with charachange
li "Everyone… has their reasons."
"Something tells me that one of those with “reasons” is Hanako, hence her tiptoeing around the answer. My own predicament is yet another such case."
"I guess it's a choice everyone here would have to make for themselves… or, in my instance, have made for them."
hi "It can't be helped, I suppose. At least Yamaku itself seems like a nice place."
show lilly cane_smile
with charachange
li "It's good to hear you say that. I'd thought you were coming to dislike it."
hi "What about you, though?"
show lilly cane_surprised
with charachange
"My reversal of Lilly's statement takes her by surprise."
li "I've been here for a while, so…"
hi "It's not that. You just seemed pretty depressed about Akira."
show lilly cane_smileclosed
with charachange
li "Hmm~"
hi "What's with that look?"
show lilly cane_smile
with charachange
li "Akira's taken. Sorry, Hisao."
"Lilly never sees how fast my palm meets my face at her sly accusation."
hi "Hey, I was worried about you. That's no way to respond to concern."
show lilly cane_cheerful
with charachange
"While she gives an amused grin, we round the corner of the hallway and enter the library."
scene ev hana_library_read_std
with locationskip
"As we do so, it isn't hard to spot Hanako, considering that the room is completely devoid of anyone else."
scene bg school_library
with locationchange
"Given that there are no staff around, I guess there's no need to heed the usual library rules. I call out to her."
hi "Hey, Hanako."
show lilly cane_surprised at center
with charaenter
li "Hanako is here?"
"As she hears our voices, Hanako's head flicks up from behind a book, probably the same one she'd been reading on Friday."
show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter
ha "Hisao… Lilly?"
hi "Just thought we'd drop by. Lilly just managed to escape from the noodle stall, with a little help."
show lilly cane_pout
with charachange
li "That wasn't really an escape…"
show hanako emb_downsmile
show lilly cane_surprised
with charachange
"Hanako gives a small giggle, briefly surprising both of us."
show hanako basic_bashful
with charachange
ha "I just thought that… Lilly might not be enjoying the festival."
hi "Well, now we can enjoy it together, right?"
show lilly cane_smileclosed
with charachange
"The two nod happily before we set out of the library and towards the festivities."
stop music fadeout 2.0
scene bg school_stalls1_ni
with shorttimeskip
$ renpy.music.set_volume(0.5,0.0, "ambient")
play ambient sfx_cicadas fadein 0.3
"I hand over some change to the girl behind the counter, and take the two styrofoam cups of tea. I try to accentuate my bow a bit to cover for the fact that she's quite obviously deaf."
"Come to think of it, I probably should have asked for help instead of leaving those two in the gardens while I bought drinks."
"Trying to juggle the two cups of hot tea (for them) and a can of coffee (for myself, out of a vending machine) isn't exactly easy."
"With some careful maneuvering, though, I manage to keep everything stable and upright as I walk over to the bench where Lilly and Hanako are sitting and chatting."
scene bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange
"It's actually quite a nice place. Lit only by moonlight, it's tucked away some distance from the main events."
"Compared to how hot it had been during the day, this spot is also pleasantly cool by now."
"Not that it matters all that much. Most of the visitors have moved to areas that are either closer to the fireworks, or higher on the hill in order to view the display apparently planned."
show lilly basic_smile_ni
with charachange
li "Welcome back, Hisao."
show hanako basic_normal_ni
with charachange
"Her ears are good. I'm not exactly close and even Hanako hadn't noticed me."
hi "Here you go. Sorry it's instant, but that's all they had left by now."
"Hanako gingerly takes a cup from my right hand, and I gently place the other into Lilly's outstretched hands."
show hanako basic_smile_ni
show lilly basic_smileclosed_ni
with charachange
li "Did you enjoy the festival then, Hisao?"
hi "Yeah, it was pretty fun."
"An honest answer. Much of the food may have been somewhat subpar, but it was a lot of fun in the end, especially with Hanako and Lilly."
"In fact, I think those two may have enjoyed themselves even more than I did. With both Lilly and I around, much of Hanako's withdrawn nature around others died down enough for her to enjoy herself."
stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0,0.0, "ambient")
play ambient sfx_fireworks
play music music_twinkle fadein 12.0
scene bg misc_sky_ni
show fireworks
with dissolve
"As we sit drinking, the whistle of the first firework rings out before it explodes into a vibrant shower of blue against the night sky, heralding the beginning of the end for the festival."
"Enthusiastic shouts can be heard from the crowds scattered around the school grounds celebrating them."
"For minutes on end, Hanako and I watch the fireworks overhead as Lilly blissfully listens to them with her eyes shut."
"Red, green, yellow, star-shaped, circular and patterned, and all manner of shapes and colors fill the air, one after the other, and dance across the sky."
"No place near where I lived put on such lavish displays. Festivals like this were a thing of the past in such a metropolitan area."
"To be seeing such a sight with these two… it's probably the happiest I've been in a long while."
scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange
li "So… that's it. The festival's finally ending."
hi "Yeah."
"She gives a delicate, wistful sigh."
show lilly basic_concerned_ni
with charachange
li "As much as I might complain about all the stuff we have to do, it's still sad that we'll have graduated before the next Yamaku festival."
show lilly basic_concerned_close_ni
with characlose
"I walk forwards and stand beside Lilly, gently resting a hand on her shoulder."
hi "Don't worry. We still have Tanabata later in the year, right?"
show lilly basic_smile_close_ni
with charachange
li "You're right. It would be nice to go there when it comes."
"Minutes of silence pass, with only the blasts of the fireworks to be heard."
"Seeing these two reminds me of those words of advice Lilly had given me as we walked into town together."
"“Cherish the opportunity to make new friends”, huh?"
hi "Hey, Lilly?"
show lilly basic_smileclosed_close_ni
with charachange
"She turns her head slightly to show that she's listening, Hanako's gaze still firmly fixed on the technicolor fireworks bursting overhead."
hi "You mind if I join you two for tea every now and again?"
"The smile on her face is more than enough to see her answer."
show lilly behind_cheerful_close_ni
with charachange
li "It would be a pleasure, Hisao."
stop music fadeout 2.0
stop ambient fadeout 2.0
window hide
label en_A42:
scene bg school_stalls2
with None
show lilly basic_reminisce at center
with charaenter
"Lilly doesn’t look impressed at all, and I can't really blame her."
"On top of her issues with her stall, she still seems to be worried about Hanako."
"I can't really help her with the former, so I guess the only way I can help is by trying to take her mind off our shy mutual friend."
"Placing the bowl back on the counter, I call out to Lilly."
hi "Hey, Lilly, don't worry about Hanako. I'll go find her and hang out with her, okay?"
show lilly basic_weaksmile
with charachange
"I can see Lilly's relief plainly written across her face."
li "Thanks Hisao. And if you see anyone from my class, can you tell them to come back here please?"
hi "Will do. Have a good one. And make sure you take a break, okay?"
show lilly basic_smile
with charachange
li "I will if I can. See you later, Hisao."
stop music fadeout 10.0
$ renpy.music.set_volume(1.0,1.0, "ambient")
scene bg school_courtyard
show crowd
with locationchange
"I leave Lilly in the stall and head out in search of Hanako."
"In a way, I feel bad for leaving her with the crowds, but even though she was clearly under pressure, I can't help but think that she is enjoying herself."
stop ambient fadeout 0.5
scene bg school_hallway2
show crowd
with locationskip
play ambient sfx_crowd_indoors fadein 0.5
"The halls are packed with swaying crowds meandering throughout the festival."
"If there's one thing I know about Hanako, it's that she's not going to be anywhere near this."
"And with the students showing their friends and family their dorms, I doubt she'll be there either."
"Following blind intuition, I move against the grain of the crowd."
"Thankfully, this crowd seems to be slightly less festive than your usual festival crowd; I assume this is out of consideration for the student body."
stop ambient fadeout 5.0
"As I force my way through the masses, it doesn't take long for them to thin down into nothingness."
hide crowd
with Dissolve(2.0)
"This is not surprising, since I am standing before the library."
"Even the most eager of students don't bother to show anyone this section of the school."
play music music_happiness fadein 2.0
scene bg school_library
with locationchange
"As I enter the library, the noise of the festival fades into a dull background noise, and soon I am in the reading area at the rear of the room."
"Behind one of the partitioned desks I see the top of a head, with straight, dark hair catching my eye."
hi "Hey, Hanako. I had a feeling I'd find you here…"
show hanako def_shock:
    pause 0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 0.5 yanchor 1.0
with charaenter
"The head jumps a little in shock before slowly peeping over the partition."
ha "H-Hisao?"
hi "Hey. Lilly's pretty busy, so she sent me to find you."
show hanako basic_normal at center
with charachange
ha "O-oh. Do you want to sit down?"
hi "Actually, I am feeling a little hungry. Would you to like to get something to eat from one of the stands?"
show hanako defarms_worry
with charachange
ha "Um… I… I brought some food so…"
"I shouldn't be surprised, but it was worth a try. Expecting her to go outside today was a long shot."
hi "How about we eat in the tea room? I passed by it on the way here, and no one was around."
hi "We can make some food there, and it'll be a little more comfortable. What do you say?"
show hanako cover_distant
with charachange
ha "S-sure. Let's go."
show hanako basic_distant
with charachange
"Hanako closes her book and puts it away with deliberate, practiced movements."
hi "Good to go?"
show hanako basic_normal
with charachange
ha "Y…yeah."
stop music fadeout 2.0
scene bg school_hallway2
with locationchange
"We walk side-by-side from the library to the tea room."
"As expected, there is barely a soul around."
"If it weren't for the murmurs through the walls, you wouldn't tell that there was a huge festival going on outside."
show hanako emb_downtimid at tworight
with charaenter
"Hanako carries her bag in both hands and focuses on just the floor ahead of her."
show hanako emb_downsmile
with charaenter
show hanako emb_downtimid
with charaenter
"Every now and again, she seems to break her pace a little and steps in slightly shorter paces."
"The first time it happened, I gave it no mind, but I soon notice that she does it on a regular basis."
hi "Are you all right?"
show hanako defarms_worry
with charachange
"She stops dead in her tracks."
ha "W-what?"
hi "I dunno… it looked like you were tripping or something…"
play music music_another fadein 0.5
show hanako emb_blushing
with charachange
"A pink blush rises into her cheeks as her gaze returns to the floor."
show hanako emb_downtimid
with charachange
ha "It… it's nothing."
hi "You know, when you say “nothing” like that, people are inspired to ask further questions."
"For a second I don't think she is going to answer."
"Prepared to leave it be, I almost set off walking again, when…"
show hanako emb_emb
with charachange
ha "It's a… a game."
hi "Game?"
show hanako emb_downsmile
with charachange
ha "Do you… see the floor here?"
"What a bizarre question. The floor looks just like any other floor; covered in those tiles made up from squares of linoleum."
"Nothing noteworthy."
hi "Well, yes. What about it?"
show hanako emb_downtimid
with charachange
ha "Sometimes… when there's no one around… I only step on the darker ones…"
"Hanako's voice trails off as her explanation continues, until I can barely hear her voice over the roaring silence of the empty hall."
hi "Darker ones?"
"Shuffling her feet, Hanako points the toe of her shoe at a tile that is barely a shade darker than the others."
show hanako emb_downsmile
with charachange
ha "L-like these ones."
hi "Oh, right, so these ones are no good?"
"I point out a nearby tile."
show hanako emb_emb
with charachange
ha "Y-yeah. Something… something like that."
hi "Oh, I see. Do you play this game a lot?"
show hanako emb_downsad
with charachange
"Hanako shakes her head."
hi "Just when the halls are empty?"
show hanako emb_emb
with charachange
"She nods."
hi "Well then, no point in stopping, I'm beginning to get really hungry."
show hanako emb_smile
with charachange
"She nods again, this time with a little more enthusiasm."
hi "Well then, let's go."
hide hanako
with charaexit
stop music fadeout 5.0
"We set off down the hall, and this time I notice that Hanako is paying a little less attention to the floor."
"I wonder; just how lonely does someone have to be to come up with a game like that?"
"But, before I realize what I'm doing, I find myself trying to aim each step so it lands on the correct tiles."
play music music_dreamy fadein 2.0
scene bg school_miyagi
with locationchange
"The noise of the festival is slightly louder inside the tea room, but the breeze coming through the open window makes it worth it."
"Without thinking, I walk to the windowsill and inhale deeply. I sometimes forget how clean the air is here compared to back home."
show hanako basic_bashful at center
with charaenter
ha "Do… would you like some tea?"
hi "That would be great, thanks."
hide hanako
with charaexit
"It occurs to me that this is the first time I've been alone with Hanako without her trying to be somewhere else."
"Turning from the window, I watch as she makes a simple pot of tea and arranges some sandwiches onto a plate."
"I've seen her do this before a number of times, but this time she seems slightly different."
"It's like she's…{w} calm."
"Eventually she places the small tray on the table and pours two cups of tea."
"The fresh scent of brewed tea mingles with the breeze, and for a second I feel like I'm the only one in the world."
hi "I think I know why you like this room now."
show hanako defarms_worry at center
with charaenter
ha "Um… I don't know what you mean."
hi "Well, there are quite a few people out there, but in here it's like another world."
hi "You can pretend that there's no one around for miles."
show hanako emb_downtimid
with charachange
ha "Y-you're right."
ha "It's like the world has forgotten this room."
show hanako emb_emb
with charachange
ha "And b-because of that, you can forget about the outside."
"That would be appealing in some cases."
"As far as I can tell, conventional bullying doesn't exist in this school."
"But then again, I haven't seen a single person talk to Hanako besides Lilly."
"If you're ignored by the world, a place where you can forget its existence would hold a special appeal."
hi "That's a good point. It's like this room gives you some kind of complete freedom."
show hanako emb_smile
with charachange
ha "Y-yeah."
show hanako basic_bashful
with charachange
ha "Say… do you play chess?"
hi "Chess? I've played it a bit, I guess."
hi "I take it you've played before?"
show hanako basic_distant
with charachange
ha "A little…"
hide hanako
with charaexit
"Without saying anything more, Hanako moves to one of the cupboards and digs out a small chess set."
ha "Do… do you want…"
hi "Sure, why not?"
"I cut her off, but she doesn't seem to mind it."
scene bg school_miyagi
show hanako basic_normal_close at center
with shorttimeskip
"We arrange the pieces, and before long we are sending pawns charging to their inevitable fates."
"I take my time and intently examine each move and its consequences, nostalgia for the game taking second place to the matters at hand."
"For a time the game is a lengthy battle of attrition, but I spot an opening and tear a line in her defense."
show hanako basic_worry_close
with charachange
"A few moves later, her king is cornered by several of my pieces."
hi "Checkmate."
hi "You're not bad at this, are you?"
"An honest appraisal. Her technique is pretty good, but several times I was able to exploit her lack of prediction."
"I pick up a piece and examine it. It looks relatively new, yet worn for its age."
show hanako basic_smile_close
with charachange
ha "I… I guess not."
hi "Does Lilly play?"
show hanako def_worry_close
with charachange
"The absence of Hanako's answer causes me to think about my question."
ha "A… A bit…"
ha "T-this is the first time I've played against someone… other than her, or…"
show hanako emb_downsad_close
with charachange
"Or…?"
"She cuts herself off abruptly, leaving the answer hanging in the air. Someone she knew before coming to Yamaku, maybe."
hi "Well then, I'm honored to have played against you."
show hanako emb_smile_close
with charachange
ha "Um… can we play again?"
"She asks as if she were asking me to cut off my own hands. The spirit of competition's gotten into her?"
hi "Sure. Though don't expect me to go easy on you this time…"
"Not that I was before, mind. She seems to appreciate the competitive tone."
show hanako emb_downsmile_close
with charachange
ha "S… same here…"
stop music fadeout 2.0
label en_A43:
scene bg school_dormhallway at bgright
show kenji happy at center
with None
stop music fadeout 2.0
"What am I going to do? I don't have any plans. In hindsight, that's really stupid."
"Maybe I should've asked a girl out? Then again, all things considered, I don't think I could've done anything like that. It's only my first week."
"A week that I have wasted being awkward around almost everyone, stumbling all over myself trying to get the hang of this place."
"Thinking about it, what have I accomplished?"
"Who would I have even asked?"
"Damn, it seems that Kenji is my only realistic option for a date today."
"This is the most depressing thing that has happened to me since I had a heart attack because a girl confessed her love to me."
"It can't be helped."
play music music_kenji fadein 0.5
hi "I don't know really. I don't have anything I guess, but a fort seems a bit excessive."
hi "You sure you don't want to go outside? It's not like visitors won't come to the dorms today."
show kenji tsun
with charachange
"He looks thunderstruck by this revelation."
ke "Damn, you may have a point. This place is not safe today."
ke "We must find somewhere to hide in."
"He falls silent for a moment, thinking."
show kenji neutral
with charachange
ke "The roof."
hi "What about it?"
show kenji happy
with charachange
ke "We are going to hide out on the roof for today."
ke "It's the perfect place, nobody ever goes up there."
show kenji neutral
with charachange
ke "Meet me there in one hour. I have to prepare."
stop music fadeout 1.0
show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None
hide kenji
with charaexit
play sound sfx_doorslam
with vpunch
"He slams the door shut and the locks click closed."
"Damn, what the hell is wrong with Kenji?"
"And to think I'm now going along with his craziness. It really makes me depressed."
"I feel like a failure."
play ambient sfx_crowd_outdoors fadein 0.3
scene bg school_courtyard
show crowd
with locationskip
"Once I step outside, the din of the crowd greets me."
"The whole school is bustling with activity."
"There are stalls everywhere, and the crowd swarming between them is considerable."
"I didn't expect the festival would attract so many visitors."
"I have to admit that the people in charge of decorating the place put a lot of effort into it, and it really shows."
"People seem to be enjoying themselves, and the atmosphere is colorful, bright, and happy."
play music music_rain fadein 1.0
"That is, if I weren't suddenly in such a foul mood."
"At the moment, it's more annoying than anything else."
"Well, it can't be helped. I decide to stick with my original plan and eat, then I guess I have to at least see what Kenji is up to on the roof."
"…"
scene bg school_stalls2 at Fullpan(8.0)
with locationchange
"I do a slow circle around the grounds to kill some time, looking at the stalls, but not feeling like playing any of the games any more."
"The garish colors grind my eyes and I feel more and more ill by the minute."
"I can't even decide what I want to eat, and the large selection combined with the masses of energetic festival visitors isn't helping."
scene bg school_stalls1 at bgright
with locationchange
"I just head towards the nearest stall that seems to offer something halfway edible and get in line."
"It turns out to be noodles."
"It also turns out to be not very good."
"Well, at least it's nourishment. It's not like I demand anything else, at this point."
scene bg misc_sky at Fullpan(25.0)
with locationchange
"As I stir my disagreeable noodles, I idly wonder what the others are doing right now."
"Shizune and Misha are definitely somewhere organizing things."
"I'd better steer clear of them. I guess they wouldn't forgive me so easily for leaving them alone with this thing."
"I expect Emi to be buzzing all over the place, being depressingly cheerful."
"There's no chance to find her, but no chance to avoid her either, so it doesn't matter."
"Lilly would probably be helping her class with that festival event, and entirely too busy for another's company."
"Hanako wouldn't want to talk to anyone anyway, either keeping to herself or helping Lilly."
"Rin should be tending to her mural and is probably being unhelpful to any hypothetical interested parties."
"Going there for some peace and quiet seems like the nicest option of the above, but then again, I can't see having art forced on me raising my mood either, so I'll pass."
scene bg school_stalls1 at bgright
with locationchange
"While I was lost in thought, my food seems to have disappeared, and so has my hunger."
"I guess I just blocked out the experience of eating, which should be a good thing."
"Satiated but unsatisfied, I turn to walk towards the main school building. An hour has almost passed already."
play ambient sfx_crowd_indoors fadein 0.3
scene bg school_lobby
show crowd
with locationskip
"The crowd is even thicker in here than it was outside."
scene bg school_hallway3
show crowd
with locationchange
"The hallways are almost unbearable, and I don't even dare to think what's it like inside the classrooms."
stop ambient fadeout 1.0
scene bg school_staircase1
with locationchange
"I head up the stairs to my destination."
"The roof."
"Thankfully, the door at the top isn't locked, but now there's a handwritten sign on it."
window hide
$ written_note("{size=55}{b}OFF LIMITS{/b}{/size}", quiet=True)
window show
"Don't mind if I don't."
scene bg school_roof at bgright
with locationchange
"The festival noise is surprisingly muted up here, and the rooftop looks deserted, as expected."
"Near a place where the cyclone fence has collapsed, there is a pile of blankets that seems oddly out of place."
stop music fadeout 3.0
"Wait."
play sound sfx_rustling
"Did that pile just move a little?"
"That would be strange, as there is no wind at all."
"I carefully stick my hand out and give it an experimental prod."
play sound sfx_impact
show kenji rage_close:
    pause 0 alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
    easein 0.2 yanchor 1.0 alpha 1.0
with vpunch
$ doublespeak(ke, hi, "AHHHHHHHHHHHHH!")
play music music_comedy fadein 2.0
show kenji rage:
    pause 0 alpha 1.0 center
with charadistant
"Startled, I jump back."
ke "Who is it?"
hi "God damn it, Kenji. It's me."
show kenji tsun at center
with charachange
ke "Oh damn, you scared me, man."
hi "So what are we doing up here?"
show kenji neutral
with charachange
ke "We're having a picnic."
hi "What?"
show kenji happy
with charachange
ke "Yeah. I have blankets, pretzels and whiskey. This is the ultimate setup, man."
hi "Whiskey?"
hi "Aren't you a bit too young to drink alcohol?"
show kenji tsun
with charachange
ke "I'm 20, y'know."
hi "…you're not."
show kenji neutral
with charachange
ke "I am and so are you."
hi "What? That's absurd."
show kenji tsun
with charachange
ke "Hey, at least YOU get something out of it, all I get is this bottle of whiskey…"
"He's rambling incoherently, but I decide to play along."
hi "So why do you have a bottle of whiskey?"
show kenji happy
with charachange
ke "My mom couldn't come visit for the festival, so she sent me some expensive Single Malt instead."
hi "A likely story."
ke "Want some?"
hi "…"
"It's not like I have anything to lose. This day can't possibly get worse."
hi "…why not."
hide kenji
with charaexit
show bg school_roof at center
with charamove_accel
show kenji happy_close at offscreenleft
with None
show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel
"We sit down on the pile of blankets Kenji apparently dragged up here."
"He produces an almost full bottle of whiskey and passes it to me."
hi "You didn't even bring glasses?"
show kenji tsun_close
with charachange
ke "No, this is not some romantic princess picnic. What the hell, man?"
show kenji neutral_close
with charachange
ke "This is a manly picnic."
ke "No glasses."
ke "No napkins."
ke "Whiskey only. The beverage of true men."
hi "Whatever."
show kenji happy_close
with charachange
ke "And pretzels."
"I take a closer look at the bottle."
"12 year old single malt whiskey, as he said."
"Shrugging my shoulders, I take a swig. It burns my throat like acid, but the taste isn't unpleasant."
"I feel it going straight into my head, and the aftertaste lingers in the back of my mouth, craving for another swig."
show kenji neutral_close
with charachange
ke "We should outline our counteroffensive and trashtalk women here, where they can't hear us."
show kenji tsun_close
with charachange
ke "Damn, I forgot to bring my graphs."
"I decide to play a drinking game with myself. Every time Kenji mentions “female conspiracy”, I'll take a swig."
$ wdt_off(False)
stop music fadeout 2.0
scene black
with delayblinds
centered "Four or five hours, or possibly several days later:\n{w}(I lost track)"
play music music_kenji fadein 0.5
scene ev kenji_rooftop
with delayblinds
window show
ke "You shouldn't feel bad, man! Ease the fuck up! Seriously, seriously!"
hi "I am relaxed, god damn it!"
ke "I'm telling it as I see it!"
scene ev kenji_rooftop_kenji
with flash
ke "Think about it. When did housing and land start becoming more and more expensive? When women began entering the work force, because it created two-income nuclear families."
ke "Yeah I forgot my graphs, but, and you'll just have to take my word for it, women are connected to the decay of all society."
show ev kenji_rooftop_large:
    pause 0 crop (288, 376, 800, 600)
    ease 1.0 crop (1024, 260, 800, 600)
hi "I see. That is kind of hard to believe."
"Even if I say that, somehow, everything Kenji says seems to make more sense now."
"It all fits together but I don't know if it's because he can explain things more clearly when drunk, or because I understand everything better when drunk."
show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)
ke "No man, think. Think! Think of the deeper implications!"
ke "People could afford to start saying “Oh well, since two members of the family are now earning money as opposed to one, they can surely afford something like rising costs of ownership.”"
show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)
hi "I see your point. But land in Japan has always been expensive."
show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)
ke "…And the price of land generally goes up when a country starts undergoing industrialization. …But no! It's because of women! Correlation equals causation, you know."
show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)
hi "I thought correlation didn't equal causation. Well, whatever, maybe you're right."
show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)
ke "I am always right. Yeah, I bet women created industrialization, too, to cover their tracks."
ke "How diabolical."
ke "So yeah, everyone can go fuck themselves!"
scene bg school_roof_ni
show kenji rage_ni:
    pause 0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 1.0 yanchor 1.0
with locationchange
"He stands up, impressing me because I'm fairly sure I couldn't even if I wanted. He yells extremely loudly as if he's lost the concept of volume. I wince and almost want to cover my ears."
stop music fadeout 2.0
ke "Aaagh, how nice it would have been if I could have been down there… But no. You see, thinking like that is a trap, you think you're missing out on something, but at the end of that road is nothing but despair…"
show kenji tsun_ni at center
with charachange
play music music_sadness fadein 1.5
"Kenji snatches back the bottle and leans back his head, attempting to pour the alcohol into his mouth, but just ends up drenching himself in it."
show kenji rage_ni
with charachange
ke "Dammit! See, my aim is terrible, and the bad thing about drinking is that it only gets worse the longer you go!"
show kenji tsun_ni
with charachange
ke "Today is the day of despair."
"His voice immediately drops to almost a whisper, but he starts talking much faster than before, slightly slurring his words from the whiskey."
"As he talks, he waves the bottle around, spilling some of it here and there."
ke "Yeah, you know what was the most shocking event of my life?"
"I have a hazy recollection of him telling about the second most shocking event in his life, which was a bird pooping on his head."
"I don't have particularly great expectations of this, but I nod at him to continue anyway."
show kenji neutral_ni
with charachange
ke "You wouldn't think it, but I had a girlfriend here once, I think it was last year."
ke "Yeah, I just blew your mind, huh? See, I have never told that to anyone."
"It's true, the thought does blow my mind. Suddenly, I want the bottle. I take it from Kenji and knock back as much as I can."
show kenji tsun_ni
with charachange
ke "I was more innocent back then, and I thought she was sane, unlike most women. But then one day, we engaged in… sexual intercourse."
ke "It was pretty okay, but then immediately following the event that is the point of all such things, something strange and scary happened."
show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove
"He throws himself up against the fence, leaning on it, his eyes narrowed."
ke "I started feeling incredibly tired and sleepy! That isn't normal, man! What the fuck?"
ke "I mean, normally, that would be a high-tension, adrenaline-pumping moment of anyone's life, but my energy levels were dropping like a brick!"
ke "Something sinister was in the works, I could feel it."
ke "That is when I knew… that women are dangerous, sapping the life force of all men through the one commodity that is almost solely theirs to control!"
ke "Sickening."
show kenji neutral_ni
with charachange
ke "Yeah, you're better off, dude…"
"Kenji was right, this really is the day of despair. I drink more to avoid having to process what he just said."
ke "Now I am the last sane man in an insane world… when other people realize it, there will be a war, a great war between men and the forces of feminism."
ke "But the problem is that not all men would fight on my side… shit sucks. I could set the bar kinda low, any men are fine. But not the dudes raised by their mom or their sister, that's for sure."
show kenji tsun_ni
with charachange
ke "And nobody into dickgirl porn."
hi "Ha… That situation seems unlikely to me, like it wouldn't happen, like… like it's not very likely to happen."
"The alcohol must be working."
"Regardless, I still feel depressed that I'm up here today."
"I wasn't really looking forward to the festival with the same excitement as the rest of the school, but still."
"It would have been nice to have gone with someone. From up here, it certainly sounded like everyone's having fun. Maybe I am missing out."
"It's just that there was no one I could have gone with."
"Or maybe there was. So many opportunities, looking back on it now, and I must have squandered so many of them."
ke "Damn, this is true despair… The worst part is that sometimes I feel like I have no choices in my life, you know?"
ke "Like I never have a chance to make a decision, shit just happens."
ke "Like it was all preprogrammed. Like fate… or something. Like there is no way I can have a say in what I do."
stop music fadeout 0.2
show kenji rage_ni
with vpunch
ke "Quick, ask me a question!"
hi "Uh…"
ke "Now!"
hi "I can't really…"
show kenji tsun_ni
with charachange
ke "See? This is just another example of it! Damn! Shit! Damn! Do you see? Now, when I'm trying to go against my destiny and take charge of my life, the opportunity isn't even there."
ke "Damn, man, you have failed me. Failed me for the last time. Jerk."
show kenji tsun_ni:
    pause 0 xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)
show kenji tsun_ni:
    pause 0 rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3
with Pause(.7)
play sound sfx_impact
with vpunch
hide kenji
with None
"He slides to his knees and then falls over onto his side, lying on the gravel of the roof."
hi "Hey, are you okay?"
ke "No, I'm not okay, can't you see I'm in despair?"
"He's speaking in a sarcastic tone."
show kenji neutral_ni:
    pause 0 xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)
"Suddenly, Kenji sits up, clumsily pats himself clean, and puts his hand out towards me to reach for the bottle. I put it in his hand."
show kenji tsun_ni at Transform(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange
ke "What the hell? Damn, you killed almost the entire bottle. See, it's like I have no options in life…"
ke "Is this how it's going to be for the rest of time?"
hi "Well, I'm pretty sure it's not going to be like that for the rest of time."
"Whatever he's talking about. My head is spinning. I get up and lean against the fence, hoping it'll help me focus a little."
show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove
ke "Yeah, I know. We have to fight the power with all we got. It's the only way to live."
play music music_one fadein 6.0
show kenji neutral_ni
with charachange
ke "You're an all right guy."
show kenji happy_ni
with charachange
ke "This brotherly bond is what keeps me going in these dark times."
show kenji neutral_ni
with charachange
ke "We should go trolling women."
hi "Rolling women? What?"
show kenji neutral_close_ni
with characlose
ke "Trolling women. Trolling for women. But we have to do it now, before I lose this alcohol-related courage."
"He's gesturing wildly. Madly, even."
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None
show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant
"I take a step backward."
show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None
show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose
"He takes a step forward."
show kenji happy_close_ni
with charachange
ke "What's the matter with you? Not in the mood for love?"
hi "To be frank… no."
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None
show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant
"I take another step backward."
show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None
show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose
"He takes another step forward."
"He leans in extremely, uncomfortably close."
hi "What the hell, stop leaning in like that, it bothers me."
ke "Leaning in like what? Hey, you shouldn't lean against the fence like that, it's kind of unsafe."
"I try to move away from Kenji, but my balance isn't so good."
"Reeling from the dizziness, I grab at one of the fenceposts, but then feel it give way as soon as I put my weight on it."
"…this isn't good. Though my alcohol-addled brain doesn't seem to be quite able of registering why."
show black behind bg
with None
show n_vignette:
    pause 0 xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)
show n_vignette:
    pause 0 zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni:
    pause 0 xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop:
    pause 0 xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
"Kenji's face seems to be becoming smaller though, which is a bit of a relief."
"Much smaller, in fact. And rapidly so."
show nightsky rotation
with None
"There seems to be a bit of wind now. Somehow it makes me feel almost weightless."
"I feel dazed, like my mind has gone blank."
hi "I am… falling…?"
"I can see the night sky as I turn over in the air. The bottle floats out of my fingertips and disappears into thin air as I fall."
"I realize that this is the fitting end to a truly, truly bad day."
window hide
stop music fadeout 0.1
play sound sfx_crunchydeath
#	TEMPORARY STOP
	$renpy.quit()