from worlds.AutoWorld import CollectionState
from BaseClasses import MultiWorld, Region, Entrance, Location
from worlds.generic.Rules import add_rule, set_rule
from .Options import LB1Options, EndGoal, LevelsToWin
from .Locations import level_beaten_event_location_table
from .Regions import lb1_hero_regions, lb1_villain_regions


def set_rules(world, options: LB1Options, player: int):
    # #Entrance Rules
    for name in lb1_hero_regions:
        add_rule(world.get_entrance(f"Batcave -> {name}", player),
                 lambda state: state.has(f"{name}: Level Unlocked", player))

    for name in lb1_villain_regions:
        add_rule(world.get_entrance(f"Arkham Asylum -> {name}", player),
                 lambda state: state.has(f"{name}: Level Unlocked", player))

    # #Shop Rules
    # # TODO: Add multiplier as logic for purchases
    add_rule(world.get_location("Fast Grapple Purchased", player),
             lambda state: state.has("You can Bank on Batman: Red Brick Collected", player))
    add_rule(world.get_location("Fast Batarangs Purchased", player),
            lambda state: state.has("An Icy Reception: Red Brick Collected", player))
    add_rule(world.get_location("More Batarang Targets Purchased", player),
            lambda state: state.has("Two-Face Chase: Red Brick Collected", player))
    add_rule(world.get_location("Flaming Batarang Purchased", player),
            lambda state: state.has("A Poisonous Appointment: Red Brick Collected", player))
    add_rule(world.get_location("Slam Purchased", player),
            lambda state: state.has("The Face-Off: Red Brick Collected", player))
    add_rule(world.get_location("More Detonators Purchased", player),
            lambda state: state.has("There She Goes Again: Red Brick Collected", player))
    add_rule(world.get_location("Amour Plating Purchased", player),
            lambda state: state.has("Batboat Battle: Red Brick Collected", player))
    add_rule(world.get_location("Sonic Pain Purchased", player),
            lambda state: state.has("Under the City: Red Brick Collected", player))
    add_rule(world.get_location("Area Effect Purchased", player),
            lambda state: state.has("Zoo's Company: Red Brick Collected", player))
    add_rule(world.get_location("Bats Purchased", player),
            lambda state: state.has("Penguin's Lair: Red Brick Collected", player))
    add_rule(world.get_location("Freeze Batarang Purchased", player),
            lambda state: state.has("Joker's Home Turf: Red Brick Collected", player))
    add_rule(world.get_location("Decoy Purchased", player),
            lambda state: state.has("Little Fun at the Big Top: Red Brick Collected", player))
    add_rule(world.get_location("Fast Walk Purchased", player),
            lambda state: state.has("Flight of the Bat: Red Brick Collected", player))
    add_rule(world.get_location("Faster Pieces Purchased", player),
            lambda state: state.has("In the Dark Night: Red Brick Collected", player))
    add_rule(world.get_location("Piece Detector Purchased", player),
            lambda state: state.has("To the Top of the Tower: Red Brick Collected", player))
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

    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = lambda state: state.has("Level Beaten", player, options.levels_to_win)

def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in level_beaten_event_location_table.items():
        event: Location = world.get_location(name, player)
        add_rule(event, world.get_location(name, player).access_rule)
