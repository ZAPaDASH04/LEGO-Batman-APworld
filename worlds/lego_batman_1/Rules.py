from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import add_rule
from .Locations import level_beaten_event_location_table
from .Options import LB1Options, EndGoal
from worlds.AutoWorld import CollectionState


def character_can_cross_toxic(state: CollectionState, player: int):
    return (state.has("Mr. Freeze Unlocked", player) or state.has("Poison Ivy Unlocked", player)
            or state.has("Two-Face Unlocked", player) or state.has("Bane Unlocked", player)
            or state.has("Killer Croc Unlocked", player) or state.has("The Joker Unlocked", player)
            or state.has("The Joker (Tropical) Unlocked", player))


def character_can_double_jump(state: CollectionState, player: int):
    return (state.has("Clayface Unlocked", player) or state.has("Poison Ivy Unlocked", player)
            or state.has("Catwoman Unlocked", player) or state.has("Catwoman (Classic) Unlocked", player)
            or state.has("Harley Quinn Unlocked", player) or state.has("Mad Hatter Unlocked", player))


def character_can_access_female_room(state: CollectionState, player: int):
    return (state.has("Poison Ivy Unlocked", player) or state.has("Harley Quinn Unlocked", player)
            or state.has("Catwoman Unlocked", player) or state.has("Catwoman (Classic) Unlocked", player))


def character_can_hypno(state: CollectionState, player: int):
    return (state.has("The Riddler Unlocked", player) or state.has("The Scarecrow Unlocked", player)
            or state.has("The Mad Hatter Unlocked", player))


def character_joker(state: CollectionState, player: int):
    return state.has("The Joker Unlocked", player) or state.has("The Joker (Tropical) Unlocked", player)


def character_is_strong(state: CollectionState, player: int):
    return (state.has("Clayface Unlocked", player) or state.has("Mr. Freeze Unlocked", player)
            or state.has("Bane Unlocked", player) or state.has("Killer Croc Unlocked", player)
            or state.has("Man-Bat Unlocked", player))


def character_can_glide(state: CollectionState, player: int):
    return (state.has("Glide Suit Unlocked", player) or state.has("Man-Bat Unlocked", player)
            or state.has("The Penguin Unlocked", player) or state.has("Killer Mother Unlocked", player))


def character_can_sink(state: CollectionState, player: int):
    return state.has("Water Suit Unlocked", player) or state.has("Killer Croc Unlocked", player)


def character_can_explode(state: CollectionState, player: int):
    return state.has("Demolition Suit Unlocked", player) or state.has("The Penguin Unlocked", player)


def character_can_techno(state: CollectionState, player: int):
    return state.has("Technology Suit Unlocked", player) or state.has("Scientists Unlocked", player)


def auto_has_cable(state: CollectionState, player: int):
    return (state.has("Batmobile Unlocked", player) or state.has("Batcycle Unlocked", player)
            or state.has("Bat-Tank Unlocked", player) or state.has("Catwoman's Motorcycle Unlocked", player))


def auto_can_explode(state: CollectionState, player: int):
    return (state.has("Police Car Unlocked", player) or state.has("Police Van Unlocked", player)
            or state.has("Harley Quinn's Hammer Truck Unlocked", player)
            or state.has("The Joker's Van Unlocked", player) or state.has("Garbage Truck Unlocked", player))


def auto_can_shoot(state: CollectionState, player: int):
    return (state.has("Batmobile Unlocked", player) or state.has("Batcycle Unlocked", player)
            or state.has("Police Bike Unlocked", player) or state.has("Bat-Tank Unlocked", player)
            or state.has("Catwoman's Motorcycle Unlocked", player)
            or state.has("Two-Face's Armoured Truck Unlocked", player)
            or state.has("Harley Quinn's Hammer Truck Unlocked", player)
            or state.has("The Joker's Van Unlocked", player))


def water_has_torpedo(state: CollectionState, player: int):
    return state.has("Robin's Watercraft Unlocked", player) or state.has("Penguin's Submarine Unlocked", player)


def water_can_sink(state: CollectionState, player: int):
    return (state.has("Robin's Submarine Unlocked", player) or state.has("Penguin's Submarine Unlocked", player)
            or state.has("Penguin Goon Submarine Unlocked", player))


def water_can_cross_toxic(state: CollectionState, player: int):
    return (state.has("Police Watercraft Unlocked", player) or state.has("Killer Croc's Swamp Rider Unlocked", player)
            or state.has("Mr. Freeze's Iceberg Unlocked", player))


def water_can_boost(state: CollectionState, player: int):
    return state.has("Batboat Unlocked", player) or state.has("Killer Croc's Swamp Rider Unlocked", player)


def air_has_cable(state: CollectionState, player: int):
    return (state.has("Batcopter Unlocked", player) or state.has("Harbour Helicopter Unlocked", player)
            or state.has("Police Helicopter Unlocked", player) or state.has("The Joker's Helicopter Unlocked", player)
            or state.has("Goon Helicopter Unlocked", player))


def air_has_torpedo(state: CollectionState, player: int):
    return (state.has("Batwing Unlocked", player) or state.has("The Scarecrow's Biplane Unlocked", player)
            or state.has("Riddler's Jet Unlocked", player))


def air_can_cross_toxic(state: CollectionState, player: int):
    return (state.has("Harbour Helicopter Unlocked", player) or state.has("Police Helicopter Unlocked", player)
            or state.has("The Joker's Helicopter Unlocked", player)
            or state.has("The Scarecrow's Biplane Unlocked", player) or state.has("Goon Helicopter Unlocked", player))


def can_beat_ycbob(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has("Demolition Suit Unlocked", player) and state.has("Technology Suit Unlocked", player)
    else:
        return character_can_explode(state, player) and character_can_techno(state, player)


def can_beat_air(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has("Magnet Suit Unlocked", player) and state.has("Glide Suit Unlocked", player)
    else:
        return state.has("Magnet Suit Unlocked", player) and character_can_glide(state, player)


def can_beat_apa(state: CollectionState, player: int):
    return (state.has("Attract Suit Unlocked", player) and state.has("Sonic Suit Unlocked", player)
            and state.has("Heat Protection Suit Unlocked", player))


def can_beat_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Glide Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Attract Suit Unlocked", player))
    else:
        return (character_can_glide(state, player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Attract Suit Unlocked", player))


def can_beat_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Glide Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Sonic Suit Unlocked", player))
    else:
        return (character_can_glide(state, player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Sonic Suit Unlocked", player))


def can_beat_utc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Glide Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Water Suit Unlocked", player) and state.has("Demolition Suit Unlocked", player))
    else:
        return (character_can_glide(state, player) and state.has("Magnet Suit Unlocked", player)
                and character_can_sink(state, player) and character_can_explode(state, player))


def can_beat_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Glide Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Technology Suit Unlocked", player) and state.has("Demolition Suit Unlocked", player)
                and state.has("Sonic Suit Unlocked", player))
    else:
        return (character_can_glide(state, player) and state.has("Magnet Suit Unlocked", player)
                and character_can_techno(state, player) and character_can_explode(state, player)
                and state.has("Sonic Suit Unlocked", player))


def can_beat_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has("Glide Suit Unlocked", player) and state.has("Water Suit Unlocked", player)
    else:
        return character_can_glide(state, player) and character_can_sink(state, player)


def can_beat_jht(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Glide Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Attract Suit Unlocked", player))
    else:
        return (character_can_glide(state, player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Attract Suit Unlocked", player))


def can_beat_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Demolition Suit Unlocked", player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Sonic Suit Unlocked", player) and state.has("Attract Suit Unlocked", player))
    else:
        return (character_can_explode(state, player) and state.has("Magnet Suit Unlocked", player)
                and state.has("Sonic Suit Unlocked", player) and state.has("Attract Suit Unlocked", player))


def can_beat_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Magnet Suit Unlocked", player) and state.has("Demolition Suit Unlocked", player)
                and state.has("Technology Suit Unlocked", player))
    else:
        return (state.has("Magnet Suit Unlocked", player) and character_can_explode(state, player)
                and character_can_techno(state, player))


def can_beat_tttott(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (state.has("Magnet Suit Unlocked", player) and state.has("Demolition Suit Unlocked", player)
                and state.has("Glide Suit Unlocked", player))
    else:
        return (state.has("Magnet Suit Unlocked", player) and character_can_explode(state, player)
                and character_can_glide(state, player))


def set_entrance_rules(world, player: int):
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


def set_minikit_rules(world, player: int):
    add_rule(world.get_location("You can Bank on Batman: Minikit in the Bar behind the Broken Down Van", player),
             lambda state: character_can_cross_toxic(state, player))


def set_level_beaten_rules(world, options: LB1Options, player: int):
    add_rule(world.get_location("You can Bank on Batman: Level Beaten", player),
             lambda state: can_beat_ycbob(state, options, player))
    add_rule(world.get_location("An Icy Reception: Level Beaten", player),
             lambda state: can_beat_air(state, options, player))
    # Two-Face Chase can be beaten in story
    add_rule(world.get_location("A Poisonous Appointment: Level Beaten", player),
             lambda state: can_beat_apa(state, player))
    add_rule(world.get_location("The Face-Off: Level Beaten", player),
             lambda state: can_beat_tfo(state, options, player))
    add_rule(world.get_location("There She Goes Again: Level Beaten", player),
             lambda state: can_beat_tsga(state, options, player))
    # Batboat Battle can be beaten in story
    add_rule(world.get_location("Under the City: Level Beaten", player),
             lambda state: can_beat_utc(state, options, player))
    add_rule(world.get_location("Zoo's Company: Level Beaten", player),
             lambda state: can_beat_zc(state, options, player))
    add_rule(world.get_location("Penguin's Lair: Level Beaten", player),
             lambda state: can_beat_pl(state, options, player))
    add_rule(world.get_location("Joker's Home Turf: Level Beaten", player),
             lambda state: can_beat_jht(state, options, player))
    add_rule(world.get_location("Little Fun at the Big Top: Level Beaten", player),
             lambda state: can_beat_lfabt(state, options, player))
    # Flight of the Bat can be beaten in story
    add_rule(world.get_location("In the Dark Night: Level Beaten", player),
             lambda state: can_beat_itdn(state, options, player))
    add_rule(world.get_location("To the Top of the Tower: Level Beaten", player),
             lambda state: can_beat_tttott(state, options, player))
    # All Villain Levels can be beaten in story


def set_red_brick_purchase_rules(world, player: int):
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


def set_rules(world, options: LB1Options, player: int):
    set_entrance_rules(world, player)
    # Character rules
    # Hard Character Rules
    # Automobile Rules
    # Watercraft Rules
    # aircraft Rules
    # Suit Rules
    if options.minikit_sanity == 1:
        set_minikit_rules(world, player)
    # Hostage Rules
    set_level_beaten_rules(world, options, player)
    # True Status Rules
    # Red Brick Rules
    # Red Brick Purchase Rules
    set_red_brick_purchase_rules(world, player)

    # Set End Goal
    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = lambda state: state.has("Level Beaten", player, options.levels_to_win)


def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in level_beaten_event_location_table.items():
        event: Location = world.get_location(name, player)
        level_beaten_name = name.removesuffix(" Event")
        add_rule(event, world.get_location(level_beaten_name, player).access_rule)
