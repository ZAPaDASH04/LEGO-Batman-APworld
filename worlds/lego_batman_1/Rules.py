from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import add_rule
from .Locations import level_beaten_event_location_table
from .Options import LB1Options, EndGoal


def set_rules(world, options: LB1Options, player: int):
    # Entrance Rules
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

    # #Shop Rules
    # # TODO: Add multiplier as logic for purchases
    add_rule(world.get_location("Score x2 Purchased", player),
             lambda state: state.has("The Riddler Makes a Withdrawal: Red Brick Collected", player))
    add_rule(world.get_location("Score x4 Purchased", player),
             lambda state: state.has("On the Rocks: Red Brick Collected", player))
    add_rule(world.get_location("Score x6 Purchased", player),
             lambda state: state.has("Green Fingers: Red Brick Collected", player))
    add_rule(world.get_location("Score x8 Purchased", player),
             lambda state: state.has("An Enterprising Theft: Red Brick Collected", player))
    add_rule(world.get_location("Score x10 Purchased", player),
             lambda state: state.has("Breaking Blocks: Red Brick Collected", player))
    add_rule(world.get_location("Stud Magnet Purchased", player),
             lambda state: state.has("Rockin' the Docks: Red Brick Collected", player))
    add_rule(world.get_location("Character Studs Purchased", player),
             lambda state: state.has("Stealing the Show: Red Brick Collected", player))
    add_rule(world.get_location("Minikit Detector Purchased", player),
             lambda state: state.has("Harbouring a Grudge: Red Brick Collected", player))
    add_rule(world.get_location("Power Brick Detector Purchased", player),
             lambda state: state.has("A Daring Rescue: Red Brick Collected", player))
    add_rule(world.get_location("Always Score Multiply Purchased", player),
             lambda state: state.has("Arctic World: Red Brick Collected", player))
    add_rule(world.get_location("Fast Build Purchased", player),
             lambda state: state.has("A Surprise for the Commissioner: Red Brick Collected", player))
    add_rule(world.get_location("Immune to Freeze Purchased", player),
             lambda state: state.has("Biplane Blast: Red Brick Collected", player))
    add_rule(world.get_location("Regenerate Hearts Purchased", player),
             lambda state: state.has("The Joker's Masterpiece: Red Brick Collected", player))
    add_rule(world.get_location("Extra Hearts Purchased", player),
             lambda state: state.has("The Lure of the Night: Red Brick Collected", player))
    add_rule(world.get_location("Invincibility Purchased", player),
             lambda state: state.has("Dying of Laughter: Red Brick Collected", player))
    add_rule(world.get_location("Fast Grapple (All Suits) Purchased", player),
             lambda state: state.has("You can Bank on Batman: Red Brick Collected", player))
    add_rule(world.get_location("Fast Batarangs (All Suits) Purchased", player),
             lambda state: state.has("An Icy Reception: Red Brick Collected", player))
    add_rule(world.get_location("More Batarang Targets (All Suits) Purchased", player),
             lambda state: state.has("Two-Face Chase: Red Brick Collected", player))
    add_rule(world.get_location("Flaming Batarang (Heat Protection Suit) Purchased", player),
             lambda state: state.has("A Poisonous Appointment: Red Brick Collected", player))
    add_rule(world.get_location("Slam (Glide Suit) Purchased", player),
             lambda state: state.has("The Face-Off: Red Brick Collected", player))
    add_rule(world.get_location("More Detonators (Demolition Suit) Purchased", player),
             lambda state: state.has("There She Goes Again: Red Brick Collected", player))
    add_rule(world.get_location("Amour Plating (Demolition Suit) Purchased", player),
             lambda state: state.has("Batboat Battle: Red Brick Collected", player))
    add_rule(world.get_location("Sonic Pain (Sonic Suit) Purchased", player),
             lambda state: state.has("Under the City: Red Brick Collected", player))
    add_rule(world.get_location("Area Effect (Sonic Suit) Purchased", player),
             lambda state: state.has("Zoo's Company: Red Brick Collected", player))
    add_rule(world.get_location("Bats (Sonic Suit) Purchased", player),
             lambda state: state.has("Penguin's Lair: Red Brick Collected", player))
    add_rule(world.get_location("Freeze Batarang (Water Suit) Purchased", player),
             lambda state: state.has("Joker's Home Turf: Red Brick Collected", player))
    add_rule(world.get_location("Decoy (Technology Suit) Purchased", player),
             lambda state: state.has("Little Fun at the Big Top: Red Brick Collected", player))
    add_rule(world.get_location("Fast Walk (Magnet Suit) Purchased", player),
             lambda state: state.has("Flight of the Bat: Red Brick Collected", player))
    add_rule(world.get_location("Faster Pieces (Attract Suit) Purchased", player),
             lambda state: state.has("In the Dark Night: Red Brick Collected", player))
    add_rule(world.get_location("Piece Detector (Attract Suit) Purchased", player),
             lambda state: state.has("To the Top of the Tower: Red Brick Collected", player))

    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = lambda state: state.has("Level Beaten", player, options.levels_to_win)


def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in level_beaten_event_location_table.items():
        event: Location = world.get_location(name, player)
        add_rule(event, world.get_location(name, player).access_rule)
