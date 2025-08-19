import typing

from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import LB1Options
from .Locations import LocationData, location_table, minikit_location_table


class LB1Region(Region):
    subregions: typing.List[Region] = []


lb1_regions = [
    "Menu",
    "Batcave",
    "Arkham Asylum",
    "You can Bank on Batman",
    "An Icy Reception",
    "Two-Face Chase",
    "A Poisonous Appointment",
    "The Face-Off",
    "There She Goes Again",
    "Batboat Battle",
    "Under the City",
    "Zoo's Company",
    "Penguin's Lair",
    "Joker's Home Turf",
    "Little Fun at Big Top",
    "Flight of the Bat",
    "In the Dark Night",
    "To the Top of the Tower",
    "The Riddler Makes a Withdrawal",
    "On the Rocks",
    "Green Fingers",
    "An Enterprising Theft"
    "Breaking Blocks"
    "Rockin' the Docks",
    "Stealing the Show",
    "Harbouring a Grudge",
    "A Daring Rescue",
    "Arctic World",
    "A Surprise for the Commissioner",
    "Biplane Blast",
    "The Joker's Masterpiece",
    "The Lure of the Night",
    "Dying of Laughter",
]


def create_regions(world: MultiWorld, options: LB1Options, player: int):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    batcave = create_region("Batcave", player, world)
    arkham_asylum = create_region("Arkham Asylum", player, world)
    you_can_bank_on_batman = create_region("You can Bank on Batman", player, world)
    an_icy_reception = create_region("An Icy Reception", player, world)
    two_face_chase = create_region("Two-Face Chase", player, world)
    a_poisonous_appointment = create_region("A Poisonous Appointment", player, world)
    the_face_off = create_region("The Face-Off", player, world)
    there_she_goes_again = create_region("There She Goes Again", player, world)
    batboat_battle = create_region("Batboat Battle", player, world)
    under_the_city = create_region("Under the City", player, world)
    zoos_company = create_region("Zoo's Company", player, world)
    penguins_lair = create_region("Penguin's Lair", player, world)
    jokers_home_turf = create_region("Joker's Home Turf", player, world)
    little_fun_at_big_top = create_region("Little Fun at Big Top", player, world)
    flight_of_the_bat = create_region("Flight of the Bat", player, world)
    in_the_dark_night = create_region("In the Dark Night", player, world)
    to_the_top_of_the_tower = create_region("To the Top of the Tower", player, world)
    the_riddler_makes_a_withdrawal = create_region("The Riddler Makes A Withdrawal", player, world)
    on_the_rocks = create_region("On The Rocks", player, world)
    green_fingers = create_region("Green Fingers", player, world)
    an_enterprising_theft = create_region("An Enterprising Theft", player, world)
    breaking_blocks = create_region("Breaking Blocks", player, world)
    rockin_the_docks = create_region("Rockin' the Docks", player, world)
    stealing_the_show = create_region("Stealing the Show", player, world)
    harbouring_a_grudge = create_region("Harbouring a Grudge", player, world)
    a_daring_rescue = create_region("A Daring Rescue", player, world)
    arctic_world = create_region("Arctic World", player, world)
    a_surprise_for_the_commissioner = create_region("A Surprise for the Commissioner", player, world)
    biplane_blast = create_region("Biplane Blast", player, world)
    the_jokers_masterpiece = create_region("The Joker's Masterpiece", player, world)
    the_lure_of_the_night = create_region("The Lure of the Night", player, world)
    dying_of_laughter = create_region("Dying of Laughter", player, world)

    connect_regions(world, player, "Menu", "Batcave")
    connect_regions(world, player, "Batcave", "Arkham Asylum")

    connect_regions(world, player, "Batcave", "You can Bank on Batman")
    connect_regions(world, player, "Batcave", "An Icy Reception")
    connect_regions(world, player, "Batcave", "Two-Face Chase")
    connect_regions(world, player, "Batcave", "A Poisonous Appointment")
    connect_regions(world, player, "Batcave", "The Face-Off")
    connect_regions(world, player, "Batcave", "There She Goes Again")
    connect_regions(world, player, "Batcave", "Batboat Battle")
    connect_regions(world, player, "Batcave", "Under the City")
    connect_regions(world, player, "Batcave", "Zoo's Company")
    connect_regions(world, player, "Batcave", "Penguin's Lair")
    connect_regions(world, player, "Batcave", "Joker's Home Turf")
    connect_regions(world, player, "Batcave", "Little Fun at Big Top")
    connect_regions(world, player, "Batcave", "Flight of the Bat")
    connect_regions(world, player, "Batcave", "In the Dark Night")
    connect_regions(world, player, "Batcave", "To the Top of the Tower")

    connect_regions(world, player, "Arkham Asylum", "The Riddler Makes A Withdrawal")
    connect_regions(world, player, "Arkham Asylum", "On The Rocks")
    connect_regions(world, player, "Arkham Asylum", "Green Fingers")
    connect_regions(world, player, "Arkham Asylum", "An Enterprising Theft")
    connect_regions(world, player, "Arkham Asylum", "Breaking Blocks")
    connect_regions(world, player, "Arkham Asylum", "Rockin' the Docks")
    connect_regions(world, player, "Arkham Asylum", "Stealing the Show")
    connect_regions(world, player, "Arkham Asylum", "Harbouring a Grudge")
    connect_regions(world, player, "Arkham Asylum", "A Daring Rescue")
    connect_regions(world, player, "Arkham Asylum", "Arctic World")
    connect_regions(world, player, "Arkham Asylum", "A Surprise for the Commissioner")
    connect_regions(world, player, "Arkham Asylum", "Biplane Blast")
    connect_regions(world, player, "Arkham Asylum", "The Joker's Masterpiece")
    connect_regions(world, player, "Arkham Asylum", "The Lure of the Night")
    connect_regions(world, player, "Arkham Asylum", "Dying of Laughter")

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region, rule=rule)


def create_region(name: str, player: int, world: MultiWorld) -> LB1Region:
    region = LB1Region(name, player, world)

    for (key, data) in location_table.items():
        if data.region == name:
            location = LocationData(player, key, data.id, region)
            region.locations.append(location)

    world.regions.append(region)
    return region
