from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions

class EndGoal(Choice):
    """
    Determine the goal for the seed

    Minikits: Collect all the Minikits to win.
    """
    display_name = "Goal"
    option_minikits = 0
    default = 0


class MiniKitSanity(DefaultOnToggle):
    """
    Puts all 300 Minikits into the pool.
    """
    display_name = "MinikitSanity"


class MinikitsToWin(Range):
    """
    Number of Minikits needed to win.
    """
    display_name = "Total Minikits"
    range_start = 50
    range_end = 300
    default = 250


# class HostageSanity(Toggle):
#     """
#     Puts all 25 Hostages into the pool.
#     """
#     display_name = "HostageSanity"

#TODO: look into what option groups are

@dataclass
class LB1Options(PerGameCommonOptions):
    EndGoal: EndGoal
    kit_sanity: MiniKitSanity
    minikits_to_win: MinikitsToWin
