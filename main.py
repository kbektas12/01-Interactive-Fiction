#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "216ACD94-C70D-42CE-80F1-FA90A0D7F747",
  "name": "Zork",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631408452513,
  "passages": [
    {
      "name": "Start",
      "tags": "",
      "id": "1",
      "text": "Welcome to Pan's Labyrinth. You will be tested based on your wits and abilities in these trials to obtain the holy grail. Once you obtain the sacred item, you will earn the right to make a wish. Now, please state your identity: are you a WARRIOR, SAGE or THIEF?\n\n[[WARRIOR->Warrior Room 1]]\n[[SAGE->Sage Room 1]]\n[[THIEF->Thief Room 1]]",
      "links": [
        {
          "linkText": "WARRIOR",
          "passageName": "Warrior Room 1",
          "original": "[[WARRIOR->Warrior Room 1]]"
        },
        {
          "linkText": "SAGE",
          "passageName": "Sage Room 1",
          "original": "[[SAGE->Sage Room 1]]"
        },
        {
          "linkText": "THIEF",
          "passageName": "Thief Room 1",
          "original": "[[THIEF->Thief Room 1]]"
        }
      ],
      "hooks": [],
      "cleanText": "Welcome to Pan's Labyrinth. You will be tested based on your wits and abilities in these trials to obtain the holy grail. Once you obtain the sacred item, you will earn the right to make a wish. Now, please state your identity: are you a WARRIOR, SAGE or THIEF?"
    },
    {
      "name": "Warrior Room 1",
      "tags": "",
      "id": "2",
      "text": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit. \n\n[[DOOR->Door fail]]\n[[ATTACK->Warrior Room 2]]\n[[SNEAK->Sneak Fail]]",
      "links": [
        {
          "linkText": "DOOR",
          "passageName": "Door fail",
          "original": "[[DOOR->Door fail]]"
        },
        {
          "linkText": "ATTACK",
          "passageName": "Warrior Room 2",
          "original": "[[ATTACK->Warrior Room 2]]"
        },
        {
          "linkText": "SNEAK",
          "passageName": "Sneak Fail",
          "original": "[[SNEAK->Sneak Fail]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit."
    },
    {
      "name": "Sage Room 1",
      "tags": "",
      "id": "3",
      "text": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit. \n\n[[DOOR->Sage Room 2]]\n[[ATTACK->Attack Fail]]\n[[SNEAK->Sneak Fail]]",
      "links": [
        {
          "linkText": "DOOR",
          "passageName": "Sage Room 2",
          "original": "[[DOOR->Sage Room 2]]"
        },
        {
          "linkText": "ATTACK",
          "passageName": "Attack Fail",
          "original": "[[ATTACK->Attack Fail]]"
        },
        {
          "linkText": "SNEAK",
          "passageName": "Sneak Fail",
          "original": "[[SNEAK->Sneak Fail]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit."
    },
    {
      "name": "Thief Room 1",
      "tags": "",
      "id": "4",
      "text": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit. \n\n[[DOOR->Door fail]]\n[[ATTACK->Attack Fail]]\n[[SNEAK->Thief Room 2]]",
      "links": [
        {
          "linkText": "DOOR",
          "passageName": "Door fail",
          "original": "[[DOOR->Door fail]]"
        },
        {
          "linkText": "ATTACK",
          "passageName": "Attack Fail",
          "original": "[[ATTACK->Attack Fail]]"
        },
        {
          "linkText": "SNEAK",
          "passageName": "Thief Room 2",
          "original": "[[SNEAK->Thief Room 2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter a large hall. You see two gates. One is guarded by a sleeping giant, and the other has glowing arcane carvings on it. You weigh your options. You can SNEAK past the sleeping monster, try your luck with the arcane DOOR, or ATTACK the sleeping beast for a critical hit."
    },
    {
      "name": "Door fail",
      "tags": "",
      "id": "5",
      "text": "You try to understand the workings of this strange door. The strange markings probably mean something but your lack of knowledge for the arcane does not register it. You press your hand on the door. It glows brightly and makes a loud noise, then slowly dims down and becomes silent. Puzzled, you look at the strange magical door. You suddenly hear a loud growl and thunderous footsteps. The sound woke the giant up. It approaches and attacks you. You have no chance against the ferocious beast. Right before it crushes all your bones you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You try to understand the workings of this strange door. The strange markings probably mean something but your lack of knowledge for the arcane does not register it. You press your hand on the door. It glows brightly and makes a loud noise, then slowly dims down and becomes silent. Puzzled, you look at the strange magical door. You suddenly hear a loud growl and thunderous footsteps. The sound woke the giant up. It approaches and attacks you. You have no chance against the ferocious beast. Right before it crushes all your bones you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again."
    },
    {
      "name": "Warrior Room 2",
      "tags": "",
      "id": "6",
      "text": "You gather all your strength and strike the giant. Your fists are so strong that the beast dies without even getting the chance to suffer the impact. You move ahead to a new room.\n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A mighty HAMMER or an unbreakable SHIELD for the mighty warrior.\" The spirit says. You aproach the stand.\n\n[[HAMMER->Warrior Room Hammer]]\n[[SHIELD->Warrior Room Shield]]",
      "links": [
        {
          "linkText": "HAMMER",
          "passageName": "Warrior Room Hammer",
          "original": "[[HAMMER->Warrior Room Hammer]]"
        },
        {
          "linkText": "SHIELD",
          "passageName": "Warrior Room Shield",
          "original": "[[SHIELD->Warrior Room Shield]]"
        }
      ],
      "hooks": [],
      "cleanText": "You gather all your strength and strike the giant. Your fists are so strong that the beast dies without even getting the chance to suffer the impact. You move ahead to a new room.\n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A mighty HAMMER or an unbreakable SHIELD for the mighty warrior.\" The spirit says. You aproach the stand."
    },
    {
      "name": "Sneak Fail",
      "tags": "",
      "id": "7",
      "text": "You try to sneak past the sleeping giant. However, just as you are about to pass the creature, you step on a broken twig and make noise. Thinking that the beast is still asleep, you make your way to the door. However, the giant wakes up to the noise and hits you with its giant club. As you draw your last breath you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You try to sneak past the sleeping giant. However, just as you are about to pass the creature, you step on a broken twig and make noise. Thinking that the beast is still asleep, you make your way to the door. However, the giant wakes up to the noise and hits you with its giant club. As you draw your last breath you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again."
    },
    {
      "name": "Sage Room 2",
      "tags": "",
      "id": "8",
      "text": "You read the ancient runes. This is a language that is familiar to you. You chant the spell written on it and the arcane door opens. \n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A WAND of untouchable power or a mysterious RUNE for the clever sage.\" The spirit says. You aproach the stand.\n\n[[WAND->Sage Room Wand]]\n[[RUNE->Sage Room Rune]]",
      "links": [
        {
          "linkText": "WAND",
          "passageName": "Sage Room Wand",
          "original": "[[WAND->Sage Room Wand]]"
        },
        {
          "linkText": "RUNE",
          "passageName": "Sage Room Rune",
          "original": "[[RUNE->Sage Room Rune]]"
        }
      ],
      "hooks": [],
      "cleanText": "You read the ancient runes. This is a language that is familiar to you. You chant the spell written on it and the arcane door opens. \n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A WAND of untouchable power or a mysterious RUNE for the clever sage.\" The spirit says. You aproach the stand."
    },
    {
      "name": "Attack Fail",
      "tags": "",
      "id": "9",
      "text": "You muster up your courage and hit the beast in the head as hard as you can. The monster only wakes up and attacks you for your insolence. Your weak arms couldn't stun the creature let alone kill it. Right before you draw your last breath you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You muster up your courage and hit the beast in the head as hard as you can. The monster only wakes up and attacks you for your insolence. Your weak arms couldn't stun the creature let alone kill it. Right before you draw your last breath you think to yourself: \"Maybe a different choice would work better.\" \n\nYou died: type START to begin again."
    },
    {
      "name": "Thief Room 2",
      "tags": "",
      "id": "10",
      "text": "Your concentrate on your walk, your moves become shadow, your feet make no noise. You easily walk past the sleeping giant, making less sound than a piece of cotton falling on the ground.\n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A CLOAK of invisibility or a DAGGER that can kill any foe for the cunning thief.\" The spirit says. You aproach the stand.\n\n[[CLOAK->Thief Room Cloak]]\n[[DAGGER->Thief Room Dagger]]",
      "links": [
        {
          "linkText": "CLOAK",
          "passageName": "Thief Room Cloak",
          "original": "[[CLOAK->Thief Room Cloak]]"
        },
        {
          "linkText": "DAGGER",
          "passageName": "Thief Room Dagger",
          "original": "[[DAGGER->Thief Room Dagger]]"
        }
      ],
      "hooks": [],
      "cleanText": "Your concentrate on your walk, your moves become shadow, your feet make no noise. You easily walk past the sleeping giant, making less sound than a piece of cotton falling on the ground.\n\nAhead of you are two legendary artifacts. A spirit appears and tells you you may only choose one, and it will help you complete your journey. \n\n\"A CLOAK of invisibility or a DAGGER that can kill any foe for the cunning thief.\" The spirit says. You aproach the stand."
    },
    {
      "name": "Warrior Room Hammer",
      "tags": "",
      "id": "11",
      "text": "You select the mighty hammer and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you there are two gigantic tunnels. One of them is blocked by a giant piece of rock, and in the other you see a fire breathing dragon guarding the passage. \n\nYou think that you can either try and break the BOULDER, or face the DRAGON head on. \n\n[[BOULDER->Warrior Room 3a]]\n[[DRAGON->Dragon Fail]]",
      "links": [
        {
          "linkText": "BOULDER",
          "passageName": "Warrior Room 3a",
          "original": "[[BOULDER->Warrior Room 3a]]"
        },
        {
          "linkText": "DRAGON",
          "passageName": "Dragon Fail",
          "original": "[[DRAGON->Dragon Fail]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the mighty hammer and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you there are two gigantic tunnels. One of them is blocked by a giant piece of rock, and in the other you see a fire breathing dragon guarding the passage. \n\nYou think that you can either try and break the BOULDER, or face the DRAGON head on."
    },
    {
      "name": "Warrior Room Shield",
      "tags": "",
      "id": "12",
      "text": "You select the unbreakable shield and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you there are two gigantic tunnels. One of them is blocked by a giant piece of rock, and in the other you see a fire breathing dragon guarding the passage. \n\nYou think that you can either try and break the ROCK, or face the DRAGON head on. \n\n[[ROCK->Boulder Fail]]\n[[DRAGON->Warrior Room 3b]]",
      "links": [
        {
          "linkText": "ROCK",
          "passageName": "Boulder Fail",
          "original": "[[ROCK->Boulder Fail]]"
        },
        {
          "linkText": "DRAGON",
          "passageName": "Warrior Room 3b",
          "original": "[[DRAGON->Warrior Room 3b]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the unbreakable shield and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you there are two gigantic tunnels. One of them is blocked by a giant piece of rock, and in the other you see a fire breathing dragon guarding the passage. \n\nYou think that you can either try and break the ROCK, or face the DRAGON head on."
    },
    {
      "name": "Thief Room Cloak",
      "tags": "",
      "id": "13",
      "text": "You select the invisibility cloak and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you lies two chambers. One contains a pit of hungry CROCODILES, the other has a mighty KNIGHT with glowing eyes in the middle of it. \n\n[[CROCODILES-> Thief Room 3a]]\n[[KNIGHT -> Knight Fail]]",
      "links": [
        {
          "linkText": "CROCODILES",
          "passageName": "Thief Room 3a",
          "original": "[[CROCODILES-> Thief Room 3a]]"
        },
        {
          "linkText": "KNIGHT",
          "passageName": "Knight Fail",
          "original": "[[KNIGHT -> Knight Fail]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the invisibility cloak and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you lies two chambers. One contains a pit of hungry CROCODILES, the other has a mighty KNIGHT with glowing eyes in the middle of it."
    },
    {
      "name": "Thief Room Dagger",
      "tags": "",
      "id": "14",
      "text": "You select the sharp dagger and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you lies two chambers. One contains a pit of hungry CROCODILES, the other has a mighty KNIGHT with glowing eyes in the middle of it. \n\n[[CROCODILES-> Crocodiles Fail]]\n[[KNIGHT -> Thief Room 3b]]",
      "links": [
        {
          "linkText": "CROCODILES",
          "passageName": "Crocodiles Fail",
          "original": "[[CROCODILES-> Crocodiles Fail]]"
        },
        {
          "linkText": "KNIGHT",
          "passageName": "Thief Room 3b",
          "original": "[[KNIGHT -> Thief Room 3b]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the sharp dagger and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nAhead of you lies two chambers. One contains a pit of hungry CROCODILES, the other has a mighty KNIGHT with glowing eyes in the middle of it."
    },
    {
      "name": "Sage Room Wand",
      "tags": "",
      "id": "15",
      "text": "You select the powerful wand and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nYou enter a hall. Right by your side, there is a glowing rock with a circular hole on it. In the middle of the room, an evil spirit of great arcane energy stands. Guarding the passage to the next room. The spirit hasn't noticed your presence yet. You must make a choice.\n\nYou think that you can either try and beat the SPIRIT, or try to understand what the glowing ROCK does.\n\n[[SPIRIT->Sage Room 3a]]\n[[ROCK->Rock Fail]]",
      "links": [
        {
          "linkText": "SPIRIT",
          "passageName": "Sage Room 3a",
          "original": "[[SPIRIT->Sage Room 3a]]"
        },
        {
          "linkText": "ROCK",
          "passageName": "Rock Fail",
          "original": "[[ROCK->Rock Fail]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the powerful wand and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nYou enter a hall. Right by your side, there is a glowing rock with a circular hole on it. In the middle of the room, an evil spirit of great arcane energy stands. Guarding the passage to the next room. The spirit hasn't noticed your presence yet. You must make a choice.\n\nYou think that you can either try and beat the SPIRIT, or try to understand what the glowing ROCK does."
    },
    {
      "name": "Sage Room Rune",
      "tags": "",
      "id": "16",
      "text": "You select the powerful wand and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nYou enter a hall. Right by your side, there is a glowing rock with a circular hole on it. In the middle of the room, an evil spirit of great arcane energy stands. Guarding the passage to the next room. The spirit hasn't noticed your presence yet. You must make a choice.\n\nYou think that you can either try and beat the SPIRIT, or try to understand what the glowing ROCK does.\n\n[[SPIRIT->Spirit Fail]]\n[[ROCK->Sage Room 3b]]",
      "links": [
        {
          "linkText": "SPIRIT",
          "passageName": "Spirit Fail",
          "original": "[[SPIRIT->Spirit Fail]]"
        },
        {
          "linkText": "ROCK",
          "passageName": "Sage Room 3b",
          "original": "[[ROCK->Sage Room 3b]]"
        }
      ],
      "hooks": [],
      "cleanText": "You select the powerful wand and continue on your journey. After making your way through the labyrinth's tight corridors, you arrive at yet another choice: \n\nYou enter a hall. Right by your side, there is a glowing rock with a circular hole on it. In the middle of the room, an evil spirit of great arcane energy stands. Guarding the passage to the next room. The spirit hasn't noticed your presence yet. You must make a choice.\n\nYou think that you can either try and beat the SPIRIT, or try to understand what the glowing ROCK does."
    },
    {
      "name": "Warrior Room 3a",
      "tags": "",
      "id": "17",
      "text": "You break the boulder easily with your strong hammer. \n\nAhead of you, you see your end goal. The magical holy grail that grants you a wish. You take the grail in your hand. And wish for your hammer to be even bigger and stronger. With your new hammer upgrade, no foe will stand before your way. You will be the greatest warrior to ever live. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You break the boulder easily with your strong hammer. \n\nAhead of you, you see your end goal. The magical holy grail that grants you a wish. You take the grail in your hand. And wish for your hammer to be even bigger and stronger. With your new hammer upgrade, no foe will stand before your way. You will be the greatest warrior to ever live. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": "Dragon Fail",
      "tags": "",
      "id": "18",
      "text": "You run towards the creature with all your might, ready to smack the hammer on its head. But before you know, the dragon lights up the entire tunnel with its breath of fire. As you are being burned alive, you think that picking the shield might have protected you from the flames. \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You run towards the creature with all your might, ready to smack the hammer on its head. But before you know, the dragon lights up the entire tunnel with its breath of fire. As you are being burned alive, you think that picking the shield might have protected you from the flames. \n\nYou died: type START to begin again."
    },
    {
      "name": "Boulder Fail",
      "tags": "",
      "id": "19",
      "text": "You hit the boulder as hard as you can with your shield. The shield bounces off from the boulder, not even leaving a scratch. If only you had picked the hammer, maybe you would have a better shot. You try a few more times but you are hardly able to dent the giant rock. However, during this time, the dragon's acute senses picked up the noise and the slithering animal crept up behind you. An unexpected sneak attack from the beast leaves you with your guts hanging out, soon to be dragon food. \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You hit the boulder as hard as you can with your shield. The shield bounces off from the boulder, not even leaving a scratch. If only you had picked the hammer, maybe you would have a better shot. You try a few more times but you are hardly able to dent the giant rock. However, during this time, the dragon's acute senses picked up the noise and the slithering animal crept up behind you. An unexpected sneak attack from the beast leaves you with your guts hanging out, soon to be dragon food. \n\nYou died: type START to begin again."
    },
    {
      "name": "Sage Room 3a",
      "tags": "",
      "id": "20",
      "text": "You aim your powerful wand at the spirit and cast a spell on it. The spirit shrieks a horrible cry as it fades. It says \"THE TREASURE IS CURSED, YOU HAVE FREED ME FROM MY PRISON\" \n\nYou contemplate on this. If the grail is truly cursed, and the spirit is right. This journey would be all for nothing. But if you are cursed, then it's going to be an everlasting existence of misery. You choose to be smart about it and not even touch the grail. You realize perhaps the foes you have conquered along the way were mere twisted souls, past conquerers of the labyrinth that got cursed and bound to this place by the great treasure. You think to yourself what might have happened if you took a different path...\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You aim your powerful wand at the spirit and cast a spell on it. The spirit shrieks a horrible cry as it fades. It says \"THE TREASURE IS CURSED, YOU HAVE FREED ME FROM MY PRISON\" \n\nYou contemplate on this. If the grail is truly cursed, and the spirit is right. This journey would be all for nothing. But if you are cursed, then it's going to be an everlasting existence of misery. You choose to be smart about it and not even touch the grail. You realize perhaps the foes you have conquered along the way were mere twisted souls, past conquerers of the labyrinth that got cursed and bound to this place by the great treasure. You think to yourself what might have happened if you took a different path...\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": "Rock Fail",
      "tags": "",
      "id": "21",
      "text": "You point your mighty wand towards the strange rock, the rock absorbs the wand's energy. However, it seems like nothing is happening. You think that the energy signature between the wand and the rock is not the same, so you now have a powered down wand and you gained nothing from the rock. You realize that you have to fight the spirit now. You point your wand at it and cast a magic curse, but the spirit is unaffected by your powered down wand. It immediately attacks back and consumes your soul. \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You point your mighty wand towards the strange rock, the rock absorbs the wand's energy. However, it seems like nothing is happening. You think that the energy signature between the wand and the rock is not the same, so you now have a powered down wand and you gained nothing from the rock. You realize that you have to fight the spirit now. You point your wand at it and cast a magic curse, but the spirit is unaffected by your powered down wand. It immediately attacks back and consumes your soul. \n\nYou died: type START to begin again."
    },
    {
      "name": "Spirit Fail",
      "tags": "",
      "id": "22",
      "text": "You have no clue how this rune will destroy the spirit, but you are willing to try. You throw the piece of magical rock at the creature, but it just goes through its corporeal form. The spirit then attacks you and consumes your soul.\n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have no clue how this rune will destroy the spirit, but you are willing to try. You throw the piece of magical rock at the creature, but it just goes through its corporeal form. The spirit then attacks you and consumes your soul.\n\nYou died: type START to begin again."
    },
    {
      "name": "Sage Room 3b",
      "tags": "",
      "id": "23",
      "text": "You place the rune on the large stone. It glows and immediately teleports you out of the room. You are now in the chamber of the grail. You aproach the treasure calmly and claim it. You twist it around in your hand and  sense its energy. You make your wish. You wish for all the knowledge in the world. You wish for power and greatness. Your wish gets granted. Within your infinite knowledge you realize something. The wish is a pact. After your death. You will serve an eternity as Pan's slave. Yet another creature of the labyrinth. You quickly fall into despair. You leave the labyrinth with dredd and ambition. Hoping that with your newly gained magical prowess you can break the binding curse and free your soul from servitude one day. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You place the rune on the large stone. It glows and immediately teleports you out of the room. You are now in the chamber of the grail. You aproach the treasure calmly and claim it. You twist it around in your hand and  sense its energy. You make your wish. You wish for all the knowledge in the world. You wish for power and greatness. Your wish gets granted. Within your infinite knowledge you realize something. The wish is a pact. After your death. You will serve an eternity as Pan's slave. Yet another creature of the labyrinth. You quickly fall into despair. You leave the labyrinth with dredd and ambition. Hoping that with your newly gained magical prowess you can break the binding curse and free your soul from servitude one day. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": "Warrior Room 3b",
      "tags": "",
      "id": "24",
      "text": "You wield your shield and charge the dragon. It breathes hell upon you, yet your great shield can absorb and deflect the flames. Once you close the gap, you bash the creature with your strong shield. The shield has become scorching hot and burns the dragon's flesh. Having slain the beast, you move on to the chamber that holds the holy grail. \n\nYou wish for a great banquet that can satisfy only your appetite. You've conquered the labyrinth, proving that you are the greatest of your warrior peers. You bask in the glory of the moment and enjoy your feast. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You wield your shield and charge the dragon. It breathes hell upon you, yet your great shield can absorb and deflect the flames. Once you close the gap, you bash the creature with your strong shield. The shield has become scorching hot and burns the dragon's flesh. Having slain the beast, you move on to the chamber that holds the holy grail. \n\nYou wish for a great banquet that can satisfy only your appetite. You've conquered the labyrinth, proving that you are the greatest of your warrior peers. You bask in the glory of the moment and enjoy your feast. \n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": " Thief Room 3a",
      "tags": "",
      "id": "25",
      "text": "You pass through the crocodiles with your invisibility cloak. You make it to the end of the labyrinth where your reward awaits you. You take the grail and make your wish. You wish to have all the riches of the world. You wish wealth beyond your comprehension. And you get it. You are the world's greatest thief. Holding the world's greatest net worth.\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pass through the crocodiles with your invisibility cloak. You make it to the end of the labyrinth where your reward awaits you. You take the grail and make your wish. You wish to have all the riches of the world. You wish wealth beyond your comprehension. And you get it. You are the world's greatest thief. Holding the world's greatest net worth.\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": " Knight Fail",
      "tags": "",
      "id": "26",
      "text": "You don your cloak and attempt to sneak past the knight. He screams \" I SEE ALL YOU INSOLENT BANDIT\" and chops your head off. Right before the blade hits your throat, you think to yourself if it was smarter to try another method. \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You don your cloak and attempt to sneak past the knight. He screams \" I SEE ALL YOU INSOLENT BANDIT\" and chops your head off. Right before the blade hits your throat, you think to yourself if it was smarter to try another method. \n\nYou died: type START to begin again."
    },
    {
      "name": " Thief Room 3b",
      "tags": "",
      "id": "27",
      "text": "You dash onto the knight and quickly stab him with your dagger. The knife slices his armor like butter and pierces his heart. He dies quickly. But before he leaves he mutters some words about the curse. You don't pay much attention to it and make your way to the final room. You enter the grail's chamber and make your wish. You wish to have all the riches of the world. You wish wealth beyond your comprehension. And you get it. You are the world's greatest thief. Holding the world's greatest net worth.\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices.\n\n[[RESTART->Start]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Start",
          "original": "[[RESTART->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You dash onto the knight and quickly stab him with your dagger. The knife slices his armor like butter and pierces his heart. He dies quickly. But before he leaves he mutters some words about the curse. You don't pay much attention to it and make your way to the final room. You enter the grail's chamber and make your wish. You wish to have all the riches of the world. You wish wealth beyond your comprehension. And you get it. You are the world's greatest thief. Holding the world's greatest net worth.\n\nYou have beaten the game!\n\nType QUIT to exit, or RESTART to play a new adventure and make different choices."
    },
    {
      "name": " Crocodiles Fail",
      "tags": "",
      "id": "28",
      "text": "You are sure that you can take on all of those crocodiles with your dagger. If you had to face one of them, you could. But this herd is hungry and they attack you immediately. You realize the lack of judgement that you had, right before you become crocodile food. \n\nYou died: type START to begin again.\n\n[[START->Start]]",
      "links": [
        {
          "linkText": "START",
          "passageName": "Start",
          "original": "[[START->Start]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are sure that you can take on all of those crocodiles with your dagger. If you had to face one of them, you could. But this herd is hungry and they attack you immediately. You realize the lack of judgement that you had, right before you become crocodile food. \n\nYou died: type START to begin again."
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world: 
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Start"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")