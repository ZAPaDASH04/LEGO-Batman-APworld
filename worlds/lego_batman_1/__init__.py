from typing import Dict

from BaseClasses import Item, Tutorial
from Options import OptionError
from .Items import LB1Item, item_table, item_data_table, minikit_names_set, setup_items, item_group_table
from .Locations import all_location_table, LocationData, setup_locations
from .Options import LB1Options
from .Regions import create_regions, connect_regions, LB1Region, create_events
from .Rules import set_rules
from ..AutoWorld import World, WebWorld, CollectionState


class LB1Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lego Batman: The Videogame for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ZAPaDASH04", "jrad", "Snolid Ice"]
    )]


class LB1World(World):
    """
     When all the villains in Arkham Asylum team up and break loose, only the dynamic duo is bold enough to take them on to save Gotham City. 
     The fun of LEGO, the drama of Batman and the uniqueness of the combination makes for a comical and exciting adventure in LEGO Batman: The Videogame. 
    """ #Lazy Import
    game = "Lego Batman: The Video Game"
    options_dataclass = LB1Options
    options: LB1Options
    topology_present = True

    item_name_to_id = item_table
    location_name_to_id = {name: data.id for name, data in all_location_table.items()}

    seed_location_table: Dict[str, int]
    seed_item_table: Dict[str, int]

    data_version = 1
    required_client_version = (0, 5, 1)
    web = LB1Web()

    item_name_groups = {
        "Minikit": item_group_table["minikit"],
        "Hostage": item_group_table["hostage"],
        "Level": item_group_table["level"],
        "True Status": item_group_table["true status"],
        "Red Brick Collected": item_group_table["red brick collected"],
        "Red Brick Unlocked": item_group_table["red brick unlocked"],
    }

    location_name_groups = {
        "You can Bank on Batman": {name for name, data in all_location_table.items()
                                   if data.region == "You can Bank on Batman"},
        "An Icy Reception": {name for name, data in all_location_table.items() if data.region == "An Icy Reception"},
        "Two-Face Chase": {name for name, data in all_location_table.items() if data.region == "Two-Face Chase"},
        "A Poisonous Appointment": {name for name, data in all_location_table.items()
                                    if data.region == "A Poisonous Appointment"},
        "The Face-Off": {name for name, data in all_location_table.items() if data.region == "The Face-Off"},
        "There She Goes Again": {name for name, data in all_location_table.items()
                                 if data.region == "There She Goes Again"},
        "Batboat Battle": {name for name, data in all_location_table.items() if data.region == "Batboat Battle"},
        "Under the City": {name for name, data in all_location_table.items() if data.region == "Under the City"},
        "Zoo's Company": {name for name, data in all_location_table.items() if data.region == "Zoo's Company"},
        "Penguin's Lair": {name for name, data in all_location_table.items() if data.region == "Penguin's Lair"},
        "Joker's Home Turf": {name for name, data in all_location_table.items() if data.region == "Joker's Home Turf"},
        "Little Fun at the Big Top": {name for name, data in all_location_table.items()
                                      if data.region == "Little Fun at the Big Top"},
        "Flight of the Bat": {name for name, data in all_location_table.items() if data.region == "Flight of the Bat"},
        "In the Dark Night": {name for name, data in all_location_table.items() if data.region == "In the Dark Night"},
        "To the Top of the Tower": {name for name, data in all_location_table.items()
                                    if data.region == "To the Top of the Tower"},
        "The Riddler Makes a Withdrawal": {name for name, data in all_location_table.items()
                                           if data.region == "The Riddler Makes a Withdrawal"},
        "On the Rocks": {name for name, data in all_location_table.items() if data.region == "On the Rocks"},
        "Green Fingers": {name for name, data in all_location_table.items() if data.region == "Green Fingers"},
        "An Enterprising Theft": {name for name, data in all_location_table.items()
                                  if data.region == "An Enterprising Theft"},
        "Breaking Blocks": {name for name, data in all_location_table.items() if data.region == "Breaking Blocks"},
        "Rockin' the Docks": {name for name, data in all_location_table.items() if data.region == "Rockin' the Docks"},
        "Stealing the Show": {name for name, data in all_location_table.items() if data.region == "Stealing the Show"},
        "Harbouring a Grudge": {name for name, data in all_location_table.items()
                                if data.region == "Harbouring a Grudge"},
        "A Daring Rescue": {name for name, data in all_location_table.items() if data.region == "A Daring Rescue"},
        "Arctic World": {name for name, data in all_location_table.items() if data.region == "Arctic World"},
        "A Surprise for the Commissioner": {name for name, data in all_location_table.items()
                                            if data.region == "A Surprise for the Commissioner"},
        "Biplane Blast": {name for name, data in all_location_table.items() if data.region == "Biplane Blast"},
        "The Joker's Masterpiece": {name for name, data in all_location_table.items()
                                    if data.region == "The Joker's Masterpiece"},
        "The Lure of the Night": {name for name, data in all_location_table.items()
                                  if data.region == "The Lure of the Night"},
        "Dying of Laughter": {name for name, data in all_location_table.items() if data.region == "Dying of Laughter"},
    }

    def generate_early(self):
        self.validate_yaml()
        self.multiworld.push_precollected(self.create_item("You can Bank on Batman: Level Unlocked"))
        self.multiworld.push_precollected(self.create_item("The Riddler Makes a Withdrawal: Level Unlocked"))

    def validate_yaml(self):
        if self.options.EndGoal.value == 0 and self.options.minikit_sanity.value == 0:
            raise OptionError("Minikit Win Con Requires Minikit Sanity to be enabled.")

    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        create_regions(self.multiworld, self.player, self.seed_location_table)
        create_events(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LB1Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        self.seed_item_table = setup_items(self.options)
        self.multiworld.itempool += [self.create_item(item_name) for item_name in self.seed_item_table]

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    def collect(self, state: CollectionState, item: Item) -> bool:
        changed = super().collect(state, item)
        if changed:
            name = item.name
            if name in minikit_names_set and state.count(name, self.player) == 1 and self.options.EndGoal.value == 0:
                # Count was 0 before super().collect().
                # Increase unique minikit count.
                state.prog_items[self.player]["UNIQUE_MINIKITS"] += 1
        return changed

    def remove(self, state: CollectionState, item: Item) -> bool:
        changed = super().remove(state, item)
        if changed:
            name = item.name
            if name in minikit_names_set and state.count(name, self.player) == 0 and self.options.EndGoal.value == 0:
                # Count was 1 before super().remove().
                # Decrease unique minikit count.
                state.prog_items[self.player]["UNIQUE_MINIKITS"] -= 1
        return changed

    def fill_slot_data(self):
        return {
            "EndGoal": self.options.EndGoal.value,
            "MinikitSanity": self.options.minikit_sanity.value,
            "MinikitsToWin": self.options.minikits_to_win.value,
            "LevelsToWin": self.options.levels_to_win.value,
            "TrueStatusSanity": self.options.true_status_sanity.value,
            "FreeplayOrStory": self.options.freeplay_or_story.value,
        }