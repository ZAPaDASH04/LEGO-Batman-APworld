import typing

from BaseClasses import MultiWorld, Region, Entrance, Location, ItemClassification
from .Options import LB1Options
from .Locations import all_location_table, LB1Location, level_beaten_event_location_table
from .Items import LB1Item


class LB1Region(Region):
    subregions: typing.List[Region] = []


lb1_hub_regions = [
    "Batcave",
    "Arkham Asylum",
    "Shop"
]

lb1_hero_regions = [
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
    "Little Fun at the Big Top",
    "Flight of the Bat",
    "In the Dark Night",
    "To the Top of the Tower",
]

lb1_villain_regions = [
    "The Riddler Makes a Withdrawal",
    "On the Rocks",
    "Green Fingers",
    "An Enterprising Theft",
    "Breaking Blocks",
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

lb1_all_regions = [
    *lb1_hub_regions,
    *lb1_hero_regions,
    *lb1_villain_regions,
]


def create_regions(world: MultiWorld, options: LB1Options, player: int):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    for region in lb1_all_regions:
        create_regions_and_locations(region, player, world)

    connect_regions(world, player, "Menu", "Batcave")
    connect_regions(world, player, "Batcave", "Arkham Asylum")
    connect_regions(world, player, "Batcave", "Shop")

    for region in lb1_hero_regions:
        connect_regions(world, player, "Batcave", region)

    for region in lb1_villain_regions:
        connect_regions(world, player, "Arkham Asylum", region)


def connect_regions(world: MultiWorld, player: int, source: str, target: str) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region)


def create_regions_and_locations(name: str, player: int, world: MultiWorld) -> Region:
    region = Region(name, player, world)

    for (key, data) in all_location_table.items():
        if data.region == name:
            location = LB1Location(player, key, data.id, region)
            region.locations.append(location)

    world.regions.append(region)
    return region

def create_events(world: MultiWorld, player: int) -> int:
    count = 0

    for (name, data) in level_beaten_event_location_table.items():
        item_name = "Level Beaten"
        event: Location = create_event(name, item_name, world.get_region(data.region, player), world, player)
        event.show_in_spoiler = True
        count += 1

    return count

def create_event(name: str, item_name: str, region: Region, world: MultiWorld, player: int) -> Location:
    event = LB1Location(player, name, None, region)
    region.locations.append(event)
    event.place_locked_item(LB1Item(item_name, ItemClassification.progression, None, player))
    return event