from typing import List, Dict, Any

from BaseClasses import Item, ItemClassification, Tutorial, Region, MultiWorld
from ..AutoWorld import World, WebWorld, CollectionState
from Options import OptionError

from .Items import LB1Item, item_table, item_data_table, minikit_item_table, minikit_names_set
from .Locations import location_table, LocationData
from .Options import LB1Options
from .Regions import create_regions, connect_regions, LB1Region, create_events
from .Rules import set_rules

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
    location_name_to_id = location_table
    data_version = 1
    required_client_version = (0, 5, 1)
    web = LB1Web()

    def generate_early(self):
        self.validate_yaml()
        self.multiworld.push_precollected(self.create_item("You can Bank on Batman: Level Unlocked"))
        self.multiworld.push_precollected(self.create_item("The Riddler Makes a Withdrawal: Level Unlocked"))

    def validate_yaml(self):
        if self.options.EndGoal.value == 0 and self.options.minikit_sanity.value == 0:
            raise OptionError("Minikit Win Con Requires Minikit Sanity to be enabled.")

    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)
        create_events(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LB1Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        self.multiworld.itempool += [self.create_item(item_name) for item_name in item_table]

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