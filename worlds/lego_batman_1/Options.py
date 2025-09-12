from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Choice, PerGameCommonOptions

class EndGoal(Choice):
    """
    Determine the goal for the seed

    Minikits: Collect Minikits to win.
    Levels Beaten: Beat Levels to win.
    """
    display_name = "Goal"
    option_minikits = 0
    option_levels_beaten = 1
    default = 0


class MiniKitSanity(DefaultOnToggle):
    """
    Puts all 300 Minikits into the pool.
    """
    display_name = "Minikit Sanity"


class MinikitsToWin(Range):
    """
    Number of Minikits needed to win. Only applicable if win con is set to Minikits Collected.
    """
    display_name = "Total Minikits"
    range_start = 50
    range_end = 300
    default = 200


class LevelsToWin(Range):
    """
    Number of Levels Beaten needed to win. Only applicable if win con is set to Levels Beaten.
    """
    display_name = "Total Levels"
    range_start = 5
    range_end = 30
    default = 20


class TrueStatusSanity(DefaultOnToggle):
    """
    Shuffles the true status of each level.
    """
    display_name = "True Status Sanity"


# class HostageSanity(Toggle):
#     """
#     Puts all 25 Hostages into the pool.
#     """
#     display_name = "HostageSanity"

#TODO: look into what option groups are

@dataclass
class LB1Options(PerGameCommonOptions):
    EndGoal: EndGoal
    minikit_sanity: MiniKitSanity
    minikits_to_win: MinikitsToWin
    levels_to_win: LevelsToWin
    true_status_sanity: TrueStatusSanity
    # hostage_sanity: HostageSanity
