from worlds.AutoWorld import CollectionState
from BaseClasses import MultiWorld, Region, Entrance
from worlds.generic.Rules import add_rule, set_rule
from .Options import EndGoal, MinikitsToWin


def set_rules(world, options, player: int):
    add_rule(world.get_entrance("Batcave -> You can Bank on Batman", player),
             lambda state: state.has("You can Bank on Batman: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> An Icy Reception", player),
             lambda state: state.has("An Icy Reception: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Two-Face Chase", player),
             lambda state: state.has("Two-Face Chase: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> A Poisonous Appointment", player),
             lambda state: state.has("A Poisonous Appointment: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> The Face-Off", player),
             lambda state: state.has("The Face-Off: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> There She Goes Again", player),
             lambda state: state.has("There She Goes Again: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Batboat Battle", player),
             lambda state: state.has("Batboat Battle: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Under the City", player),
             lambda state: state.has("Under the City: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Zoo's Company", player),
             lambda state: state.has("Zoo's Company: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Penguin's Lair", player),
             lambda state: state.has("Penguin's Lair: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Joker's Home Turf", player),
             lambda state: state.has("Joker's Home Turf: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Little Fun at the Big Top", player),
             lambda state: state.has("Little Fun at the Big Top: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> Flight of the Bat", player),
             lambda state: state.has("Flight of the Bat: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> In the Dark Night", player),
             lambda state: state.has("In the Dark Night: Level Unlocked", player))
    add_rule(world.get_entrance("Batcave -> To the Top of the Tower", player),
             lambda state: state.has("To the Top of the Tower: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> The Riddler Makes a Withdrawal", player),
             lambda state: state.has("The Riddler Makes a Withdrawal: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> On the Rocks", player),
             lambda state: state.has("On the Rocks: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Green Fingers", player),
             lambda state: state.has("Green Fingers: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> An Enterprising Theft", player),
             lambda state: state.has("An Enterprising Theft: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Breaking Blocks", player),
             lambda state: state.has("Breaking Blocks: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Rockin' the Docks", player),
             lambda state: state.has("Rockin' the Docks: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Stealing the Show", player),
             lambda state: state.has("Stealing the Show: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Harbouring a Grudge", player),
             lambda state: state.has("Harbouring a Grudge: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> A Daring Rescue", player),
             lambda state: state.has("A Daring Rescue: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Arctic World", player),
             lambda state: state.has("Arctic World: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> A Surprise for the Commissioner", player),
             lambda state: state.has("A Surprise for the Commissioner: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Biplane Blast", player),
             lambda state: state.has("Biplane Blast: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> The Joker's Masterpiece", player),
             lambda state: state.has("The Joker's Masterpiece: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> The Lure of the Night", player),
             lambda state: state.has("The Lure of the Night: Level Unlocked", player))
    add_rule(world.get_entrance("Arkham Asylum -> Dying of Laughter", player),
             lambda state: state.has("Dying of Laughter: Level Unlocked", player))

    if options.EndGoal == EndGoal.option_Minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)