from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import add_rule
from worlds.AutoWorld import CollectionState

from .Locations import level_beaten_event_location_table
from .Names import LocationName, ItemName
from .Options import LB1Options, EndGoal


def char_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.mrfreeze_unlocked, player)
            or state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.twoface_unlocked, player)
            or state.has(ItemName.bane_unlocked, player)
            or state.has(ItemName.killercroc_unlocked, player)
            or state.has(ItemName.joker_unlocked, player)
            or state.has(ItemName.jokertropical_unlocked, player)
    )


def char_can_double_jump(state: CollectionState, player: int):
    return (
            state.has(ItemName.clayface_unlocked, player)
            or state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.catwoman_unlocked, player)
            or state.has(ItemName.catwomanclassic_unlocked, player)
            or state.has(ItemName.harleyquinn_unlocked, player)
            or state.has(ItemName.madhatter_unlocked, player)
    )


def char_can_access_female_room(state: CollectionState, player: int):
    return (
            state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.harleyquinn_unlocked, player)
            or state.has(ItemName.catwoman_unlocked, player)
            or state.has(ItemName.catwomanclassic_unlocked, player)
    )


def char_can_hypno(state: CollectionState, player: int):
    return (
            state.has(ItemName.riddler_unlocked, player)
            or state.has(ItemName.scarecrow_unlocked, player)
            or state.has(ItemName.madhatter_unlocked, player)
    )


def char_joker(state: CollectionState, player: int):
    return (
            state.has(ItemName.joker_unlocked, player)
            or state.has(ItemName.jokertropical_unlocked, player)
    )


def char_is_strong(state: CollectionState, player: int):
    return (
            state.has(ItemName.clayface_unlocked, player)
            or state.has(ItemName.mrfreeze_unlocked, player)
            or state.has(ItemName.bane_unlocked, player)
            or state.has(ItemName.killercroc_unlocked, player)
            or state.has(ItemName.manbat_unlocked, player)
    )


def char_can_glide(state: CollectionState, player: int):
    return (
            state.has(ItemName.glidesuit, player)
            or state.has(ItemName.manbat_unlocked, player)
            or state.has(ItemName.penguin_unlocked, player)
            or state.has(ItemName.killermoth_unlocked, player)
    )


def char_can_sink(state: CollectionState, player: int):
    return (
            state.has(ItemName.watersuit, player)
            or state.has(ItemName.killercroc_unlocked, player)
    )


def char_can_explode(state: CollectionState, player: int):
    return (
            state.has(ItemName.demolitionsuit, player)
            or state.has(ItemName.penguin_unlocked, player)
    )


def char_can_techno(state: CollectionState, player: int):
    return (
            state.has(ItemName.techsuit, player)
            or state.has(ItemName.scientist_unlocked, player)
    )


def auto_has_cable(state: CollectionState, player: int):
    return (
            state.has(ItemName.batmobile_unlocked, player)
            or state.has(ItemName.batcycle_unlocked, player)
            or state.has(ItemName.battank_unlocked, player)
            or state.has(ItemName.catmotorcycle_unlocked, player)
    )


def auto_can_explode(state: CollectionState, player: int):
    return (
            state.has(ItemName.policecar_unlocked, player)
            or state.has(ItemName.policevan_unlocked, player)
            or state.has(ItemName.hammertruck_unlocked, player)
            or state.has(ItemName.jokervan_unlocked, player)
            or state.has(ItemName.garbagetruck_unlocked, player)
    )


def auto_can_shoot(state: CollectionState, player: int):
    return (
            state.has(ItemName.batmobile_unlocked, player)
            or state.has(ItemName.batcycle_unlocked, player)
            or state.has(ItemName.policebike_unlocked, player)
            or state.has(ItemName.battank_unlocked, player)
            or state.has(ItemName.catmotorcycle_unlocked, player)
            or state.has(ItemName.armouredtruck_unlocked, player)
            or state.has(ItemName.hammertruck_unlocked, player)
            or state.has(ItemName.jokervan_unlocked, player)
    )


def water_has_torpedo(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinswatercraft_unlocked, player)
            or state.has(ItemName.penguinsubmarine_unlocked, player)
    )


def water_can_sink(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinssubmarine_unlocked, player)
            or state.has(ItemName.penguinsubmarine_unlocked, player)
            or state.has(ItemName.penguingoonsub_unlocked, player)
    )


def water_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.policewatercraft_unlocked, player)
            or state.has(ItemName.swamprider_unlocked, player)
            or state.has(ItemName.iceberg_unlocked, player)
    )


def water_can_boost(state: CollectionState, player: int):
    return (
            state.has(ItemName.batboat_unlocked, player)
            or state.has(ItemName.swamprider_unlocked, player)
    )


def air_has_cable(state: CollectionState, player: int):
    return (
            state.has(ItemName.batcopter_unlocked, player)
            or state.has(ItemName.harbourhelicopter_unlocked, player)
            or state.has(ItemName.policehelicopter_unlocked, player)
            or state.has(ItemName.jokerhelicopter_unlocked, player)
            or state.has(ItemName.goonhelicopter_unlocked, player)
    )


def air_has_torpedo(state: CollectionState, player: int):
    return (
            state.has(ItemName.batwing_unlocked, player)
            or state.has(ItemName.scarecrowbiplane_unlocked, player)
            or state.has(ItemName.riddlerjet_unlocked, player)
    )


def air_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.harbourhelicopter_unlocked, player)
            or state.has(ItemName.policehelicopter_unlocked, player)
            or state.has(ItemName.jokerhelicopter_unlocked, player)
            or state.has(ItemName.scarecrowbiplane_unlocked, player)
            or state.has(ItemName.goonhelicopter_unlocked, player)
    )


def can_beat_ycbob(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_air(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_glide(state, player)
        )


def can_beat_apa(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_beat_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_beat_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_utc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.watersuit, player)
                and state.has(ItemName.demolitionsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_sink(state, player)
                and char_can_explode(state, player)
        )


def can_beat_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.techsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_techno(state, player)
                and char_can_explode(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_beat_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.watersuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def can_beat_jht(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_beat_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_beat_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_tttot(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
                and char_can_glide(state, player)
        )


# Free Access functions are needed for moving about in freeplay (moves story characters have)
def free_access_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
        )


def free_access_trmaw(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
    )


def free_access_otr(state: CollectionState, player: int):
    return state.has(ItemName.mrfreeze_unlocked, player)


def free_access_gf(state: CollectionState, player: int):
    return char_can_hypno(state, player)


def free_access_bb(state: CollectionState, player: int):
    return char_can_hypno(state, player)


def free_access_rtd(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
    )


def free_access_sts(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and char_can_access_female_room(state, player)
    )


def free_access_hag(state: CollectionState, player: int):
    return water_has_torpedo(state, player)


def can_ycbob_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_can_cross_toxic(state, player)
                and char_is_strong(state, player)
                and char_can_hypno(state, player)
        )
    else:
        return (
                char_can_cross_toxic(state, player)
                and char_is_strong(state, player)
                and char_can_hypno(state, player)
        )


def can_tsga_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and state.has(ItemName.magsuit, player)
                and char_can_access_female_room(state, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_access_female_room(state, player)
        )


def can_tsga_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )


def can_tsga_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_can_sink(state, player)
                # Explosives checked for as part of can beat tsga
            )
    else:
        return (
                char_can_sink(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                # Explosives checked for as part of can beat tsga
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_can_sink(state, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                char_can_sink(state, player)
                and char_can_cross_toxic(state, player)
        )


def can_tsga_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_tsga_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
                # Explosives checked for as part of can beat tsga
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min9(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_tsga_min10(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_trmaw_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_trmaw_min6_and_9(state: CollectionState, player: int):
    return (
            (char_can_explode(state, player) and state.has(ItemName.sonicsuit, player))
            or (char_can_double_jump(state, player) and state.has(ItemName.sonicsuit, player))
    )


def can_otr_min2(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_can_hypno(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_otr_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_otr_min5(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_otr_min7(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.attractsuit, player)
    )


def can_otr_min8(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and char_can_explode(state, player)
    )


def can_otr_min9(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.magsuit, player)
            and char_can_glide(state, player)
    )


def can_gf_min1(state: CollectionState, player: int):
    return char_can_techno(state, player)


def can_gf_min2(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_double_jump(state, player)
    )


def can_gf_min4(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and char_can_explode(state, player)
    )


def can_gf_min5(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_gf_min6(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_gf_min7(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
            and state.has(ItemName.magsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_gf_min8(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_gf_min9(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_gf_min10(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_min1(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_aet_min2(state: CollectionState, player: int):
    return (
            char_can_techno(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_aet_min3(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_aet_min4(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_aet_min5(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_techno(state, player)
    )


def can_aet_min7(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_aet_min8(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_aet_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.heatprotectsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min2(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_bb_min4(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.attractsuit, player)
            and state.has(ItemName.magsuit, player)
    )


def can_bb_min5(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_bb_min6(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_bb_min7(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_joker(state, player)
    )


def can_bb_min8(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.magsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min10(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_rtd_min1(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_can_double_jump(state, player)
    )


def can_rtd_min2(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_rtd_min5(state: CollectionState, player: int):
    return state.has(ItemName.poisonivy_unlocked, player)


def can_rtd_min7(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_techno(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_rtd_min9(state: CollectionState, player: int):
    return (
            char_can_access_female_room(state, player)
            and state.has(ItemName.attractsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_sts_min1(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and state.has(ItemName.magsuit, player)
    )


def can_sts_min3(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_sts_min6(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_sts_min7(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_is_strong(state, player)
    )


def can_sts_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_sts_min10(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_hag_min3(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def can_hag_min8(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def can_hag_min10(state: CollectionState, player: int):
    return state.has(ItemName.robinswatercraft_unlocked, player)


def can_air_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_hypno(state, player)
        )
    else:
        return char_can_hypno(state, player)


def can_tfo_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_glide(state, player)
                and state.has(ItemName.attractsuit, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.attractsuit, player)
                and char_can_double_jump(state, player)
        )


def can_utc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
        )
    else:
        return char_can_explode(state, player)


def can_zc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                (char_can_explode(state, player)
                 or (state.has(ItemName.magsuit, player)
                     and state.has(ItemName.glidesuit, player)))
                and (state.has(ItemName.sonicsuit, player)
                     or state.has(ItemName.techsuit, player))
        )


def can_pl_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.watersuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def can_jht_host(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_jht(state, options, player)
            and char_joker(state, player)
    )


def can_lfabt_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_itdn_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
                and state.has(ItemName.magsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_explode(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_techno(state, player)
        )


def can_trmaw_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_otr_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_host(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_bb_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_rtd_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_sts_host(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and char_is_strong(state, player)
    )


def can_adr_host(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_joker(state, player)
    )


def can_aw_host(state: CollectionState, player: int):
    return char_can_cross_toxic(state, player)


def can_asftc_host(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_can_explode(state, player)
    )


def can_tjm_host(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_explode(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_tlotn_host(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_dol_host(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_double_jump(state, player)
            and char_can_glide(state, player)
    )


def can_ycbob_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_air_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_is_strong(state, player)
        )


def can_apa_rb(state: CollectionState, player: int):
    return (
            can_beat_apa(state, player)
            and char_can_explode(state, player)
            and char_joker(state, player)
    )


def can_tfo_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_cross_toxic(state, player)
        )


def can_tsga_rb(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_trmaw_rb(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_otr_rb(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.attractsuit, player)
            and char_can_techno(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_rtd_rb(state: CollectionState, player: int):
    return (
            char_can_access_female_room(state, player)
            and char_is_strong(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_sts_rb(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and char_can_techno(state, player)
            and state.has(ItemName.penguin_unlocked, player)
            and char_can_explode(state, player)
    )


def can_hag_rb(state: CollectionState, player: int):
    return state.has(ItemName.robinswatercraft_unlocked, player)


def set_entrance_rules(world: MultiWorld, options: LB1Options, player: int):
    add_rule(world.get_entrance("Batcave -> You can Bank on Batman", player),
             lambda state: state.has(ItemName.ycbob_lvl, player))
    add_rule(world.get_entrance("Batcave -> An Icy Reception", player),
             lambda state: state.has(ItemName.air_lvl, player))
    add_rule(world.get_entrance("Batcave -> Two-Face Chase", player),
             lambda state: state.has(ItemName.tfc_lvl, player))
    add_rule(world.get_entrance("Batcave -> A Poisonous Appointment", player),
             lambda state: state.has(ItemName.apa_lvl, player))
    add_rule(world.get_entrance("Batcave -> The Face-Off", player),
             lambda state: state.has(ItemName.tfo_lvl, player))
    add_rule(world.get_entrance("Batcave -> There She Goes Again", player),
             lambda state: state.has(ItemName.tsga_lvl, player))
    add_rule(world.get_entrance("Batcave -> Batboat Battle", player),
             lambda state: state.has(ItemName.bbb_lvl, player))
    add_rule(world.get_entrance("Batcave -> Under the City", player),
             lambda state: state.has(ItemName.utc_lvl, player))
    add_rule(world.get_entrance("Batcave -> Zoo's Company", player),
             lambda state: state.has(ItemName.zc_lvl, player))
    add_rule(world.get_entrance("Batcave -> Penguin's Lair", player),
             lambda state: state.has(ItemName.pl_lvl, player))
    add_rule(world.get_entrance("Batcave -> Joker's Home Turf", player),
             lambda state: state.has(ItemName.jht_lvl, player))
    add_rule(world.get_entrance("Batcave -> Little Fun at the Big Top", player),
             lambda state: state.has(ItemName.lfabt_lvl, player))
    add_rule(world.get_entrance("Batcave -> Flight of the Bat", player),
             lambda state: state.has(ItemName.fotb_lvl, player))
    add_rule(world.get_entrance("Batcave -> In the Dark Night", player),
             lambda state: state.has(ItemName.itdn_lvl, player))
    add_rule(world.get_entrance("Batcave -> To the Top of the Tower", player),
             lambda state: state.has(ItemName.tttot_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> The Riddler Makes a Withdrawal", player),
             lambda state: state.has(ItemName.trmaw_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> On the Rocks", player),
             lambda state: state.has(ItemName.otr_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Green Fingers", player),
             lambda state: state.has(ItemName.gf_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> An Enterprising Theft", player),
             lambda state: state.has(ItemName.aet_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Breaking Blocks", player),
             lambda state: state.has(ItemName.bb_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Rockin' the Docks", player),
             lambda state: state.has(ItemName.rtd_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Stealing the Show", player),
             lambda state: state.has(ItemName.sts_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Harbouring a Grudge", player),
             lambda state: state.has(ItemName.hag_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> A Daring Rescue", player),
             lambda state: state.has(ItemName.adr_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Arctic World", player),
             lambda state: state.has(ItemName.aw_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> A Surprise for the Commissioner", player),
             lambda state: state.has(ItemName.asftc_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Biplane Blast", player),
             lambda state: state.has(ItemName.bbpl_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> The Joker's Masterpiece", player),
             lambda state: state.has(ItemName.tjm_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> The Lure of the Night", player),
             lambda state: state.has(ItemName.tlotn_lvl, player))
    add_rule(world.get_entrance("Arkham Asylum -> Dying of Laughter", player),
             lambda state: state.has(ItemName.dol_lvl, player))
    # Sub Regions
    add_rule(world.get_entrance("There She Goes Again -> There She Goes Again: Freeplay", player),
             lambda state: free_access_tsga(state, options, player))
    add_rule(world.get_entrance("The Riddler Makes a Withdrawal -> The Riddler Makes a Withdrawal: Freeplay", player),
             lambda state: free_access_trmaw(state, player))
    add_rule(world.get_entrance("On the Rocks -> On the Rocks: Freeplay", player),
             lambda state: free_access_otr(state, player))
    add_rule(world.get_entrance("Green Fingers -> Green Fingers: Freeplay", player),
             lambda state: free_access_gf(state, player))
    add_rule(world.get_entrance("Breaking Blocks -> Breaking Blocks: Freeplay", player),
             lambda state: free_access_bb(state, player))
    add_rule(world.get_entrance("Rockin' the Docks -> Rockin' the Docks: Freeplay", player),
             lambda state: free_access_rtd(state, player))
    add_rule(world.get_entrance("Stealing the Show -> Stealing the Show: Freeplay", player),
             lambda state: free_access_sts(state, player))
    add_rule(world.get_entrance("Harbouring a Grudge -> Harbouring a Grudge: Freeplay", player),
             lambda state: free_access_hag(state, player))


def set_level_beaten_rules(world: MultiWorld, options: LB1Options, player: int):
    add_rule(world.get_location(LocationName.ycbob_beat, player), lambda state: can_beat_ycbob(state, options, player))
    add_rule(world.get_location(LocationName.air_beat, player), lambda state: can_beat_air(state, options, player))
    # Two-Face Chase can be beaten in story
    add_rule(world.get_location(LocationName.apa_beat, player), lambda state: can_beat_apa(state, player))
    add_rule(world.get_location(LocationName.tfo_beat, player), lambda state: can_beat_tfo(state, options, player))
    add_rule(world.get_location(LocationName.tsga_beat, player), lambda state: can_beat_tsga(state, options, player))
    # Batboat Battle can be beaten in story
    add_rule(world.get_location(LocationName.utc_beat, player), lambda state: can_beat_utc(state, options, player))
    add_rule(world.get_location(LocationName.zc_beat, player), lambda state: can_beat_zc(state, options, player))
    add_rule(world.get_location(LocationName.pl_beat, player), lambda state: can_beat_pl(state, options, player))
    add_rule(world.get_location(LocationName.jht_beat, player), lambda state: can_beat_jht(state, options, player))
    add_rule(world.get_location(LocationName.lfabt_beat, player), lambda state: can_beat_lfabt(state, options, player))
    # Flight of the Bat can be beaten in story
    add_rule(world.get_location(LocationName.itdn_beat, player), lambda state: can_beat_itdn(state, options, player))
    add_rule(world.get_location(LocationName.tttot_beat, player), lambda state: can_beat_tttot(state, options, player))
    # All Villain Levels can be beaten in story


def set_minikit_rules(world: MultiWorld, options: LB1Options, player: int):
    add_rule(world.get_location(LocationName.ycbob_min4, player), lambda state: can_ycbob_min4(state, options, player))
    # TSGA Minikit 6 can be done in story (with Glide/Magnet which is region access logic)
    add_rule(world.get_location(LocationName.tsga_min1, player), lambda state: can_tsga_min1(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min2, player), lambda state: can_tsga_min2(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min3, player), lambda state: can_tsga_min3(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min4, player), lambda state: can_tsga_min4(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min5, player), lambda state: can_tsga_min5(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min7, player), lambda state: can_tsga_min7(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min8, player), lambda state: can_tsga_min8(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min9, player), lambda state: can_tsga_min9(state, options, player))
    add_rule(world.get_location(LocationName.tsga_min10, player), lambda state: can_tsga_min10(state, options, player))
    # TRMAW Minikits 1-3, 5, 7, 8, 10 can be done in story
    add_rule(world.get_location(LocationName.trmaw_min4, player), lambda state: can_trmaw_min4(state, player))
    add_rule(world.get_location(LocationName.trmaw_min6, player), lambda state: can_trmaw_min6_and_9(state, player))
    add_rule(world.get_location(LocationName.trmaw_min9, player), lambda state: can_trmaw_min6_and_9(state, player))
    # OTR Minikits 1, 3, 6, 10 can be done in story
    add_rule(world.get_location(LocationName.otr_min2, player), lambda state: can_otr_min2(state, player))
    add_rule(world.get_location(LocationName.otr_min4, player), lambda state: can_otr_min4(state, player))
    add_rule(world.get_location(LocationName.otr_min5, player), lambda state: can_otr_min5(state, player))
    add_rule(world.get_location(LocationName.otr_min7, player), lambda state: can_otr_min7(state, player))
    add_rule(world.get_location(LocationName.otr_min8, player), lambda state: can_otr_min8(state, player))
    add_rule(world.get_location(LocationName.otr_min9, player), lambda state: can_otr_min9(state, player))
    # GF Minikit 3 can be done in story
    add_rule(world.get_location(LocationName.gf_min1, player), lambda state: can_gf_min1(state, player))
    add_rule(world.get_location(LocationName.gf_min2, player), lambda state: can_gf_min2(state, player))
    add_rule(world.get_location(LocationName.gf_min4, player), lambda state: can_gf_min4(state, player))
    add_rule(world.get_location(LocationName.gf_min5, player), lambda state: can_gf_min5(state, player))
    add_rule(world.get_location(LocationName.gf_min6, player), lambda state: can_gf_min6(state, player))
    add_rule(world.get_location(LocationName.gf_min7, player), lambda state: can_gf_min7(state, player))
    add_rule(world.get_location(LocationName.gf_min8, player), lambda state: can_gf_min8(state, player))
    add_rule(world.get_location(LocationName.gf_min9, player), lambda state: can_gf_min9(state, player))
    add_rule(world.get_location(LocationName.gf_min10, player), lambda state: can_gf_min10(state, player))
    # AET Minikits 6 & 10 can be done in story
    add_rule(world.get_location(LocationName.aet_min1, player), lambda state: can_aet_min1(state, player))
    add_rule(world.get_location(LocationName.aet_min2, player), lambda state: can_aet_min2(state, player))
    add_rule(world.get_location(LocationName.aet_min3, player), lambda state: can_aet_min3(state, player))
    add_rule(world.get_location(LocationName.aet_min4, player), lambda state: can_aet_min4(state, player))
    add_rule(world.get_location(LocationName.aet_min5, player), lambda state: can_aet_min5(state, player))
    add_rule(world.get_location(LocationName.aet_min7, player), lambda state: can_aet_min7(state, player))
    add_rule(world.get_location(LocationName.aet_min8, player), lambda state: can_aet_min8(state, player))
    add_rule(world.get_location(LocationName.aet_min9, player), lambda state: can_aet_min9(state, player))
    # BB Minikit 1 can be done in story & 3 can be done in freeplay with batman & region access
    add_rule(world.get_location(LocationName.bb_min2, player), lambda state: can_bb_min2(state, player))
    add_rule(world.get_location(LocationName.bb_min4, player), lambda state: can_bb_min4(state, player))
    add_rule(world.get_location(LocationName.bb_min5, player), lambda state: can_bb_min5(state, player))
    add_rule(world.get_location(LocationName.bb_min6, player), lambda state: can_bb_min6(state, player))
    add_rule(world.get_location(LocationName.bb_min7, player), lambda state: can_bb_min7(state, player))
    add_rule(world.get_location(LocationName.bb_min8, player), lambda state: can_bb_min8(state, player))
    add_rule(world.get_location(LocationName.bb_min9, player), lambda state: can_bb_min9(state, player))
    add_rule(world.get_location(LocationName.bb_min10, player), lambda state: can_bb_min10(state, player))
    # RTD Minikits 3, 4, 6, 8, 10 can be done in story
    add_rule(world.get_location(LocationName.rtd_min1, player), lambda state: can_rtd_min1(state, player))
    add_rule(world.get_location(LocationName.rtd_min2, player), lambda state: can_rtd_min2(state, player))
    add_rule(world.get_location(LocationName.rtd_min5, player), lambda state: can_rtd_min5(state, player))
    add_rule(world.get_location(LocationName.rtd_min7, player), lambda state: can_rtd_min7(state, player))
    add_rule(world.get_location(LocationName.rtd_min9, player), lambda state: can_rtd_min9(state, player))
    # STS Minikits 2, 4, 5, 8 can be done in story
    add_rule(world.get_location(LocationName.sts_min1, player), lambda state: can_sts_min1(state, player))
    add_rule(world.get_location(LocationName.sts_min3, player), lambda state: can_sts_min3(state, player))
    add_rule(world.get_location(LocationName.sts_min6, player), lambda state: can_sts_min6(state, player))
    add_rule(world.get_location(LocationName.sts_min7, player), lambda state: can_sts_min7(state, player))
    add_rule(world.get_location(LocationName.sts_min9, player), lambda state: can_sts_min9(state, player))
    add_rule(world.get_location(LocationName.sts_min10, player), lambda state: can_sts_min10(state, player))
    # HAG Minikits 1, 2, 4-7, 9 can be done in story
    add_rule(world.get_location(LocationName.hag_min3, player), lambda state: can_hag_min3(state, player))
    add_rule(world.get_location(LocationName.hag_min8, player), lambda state: can_hag_min8(state, player))
    add_rule(world.get_location(LocationName.hag_min10, player), lambda state: can_hag_min10(state, player))


def set_host_rules(world: MultiWorld, options: LB1Options, player: int):
    # You Can Bank of Batman host can be obtained during story and for free
    add_rule(world.get_location(LocationName.air_host, player), lambda state: can_air_host(state, options, player))
    # Two-Face Chase does not have host
    add_rule(world.get_location(LocationName.apa_host, player), lambda state: state.has(ItemName.sonicsuit, player))
    add_rule(world.get_location(LocationName.tfo_host, player), lambda state: can_tfo_host(state, options, player))
    # There She Goes Again host can be obtained with Region Access
    # Batboat Battle does not have host
    add_rule(world.get_location(LocationName.utc_host, player), lambda state: can_utc_host(state, options, player))
    add_rule(world.get_location(LocationName.zc_host, player), lambda state: can_zc_host(state, options, player))
    add_rule(world.get_location(LocationName.pl_host, player), lambda state: can_pl_host(state, options, player))
    add_rule(world.get_location(LocationName.jht_host, player), lambda state: can_jht_host(state, options, player))
    add_rule(world.get_location(LocationName.lfabt_host, player), lambda state: can_lfabt_host(state, options, player))
    # Flight of the Bat does not have host
    add_rule(world.get_location(LocationName.itdn_host, player), lambda state: can_itdn_host(state, options, player))
    # To the Top of the Tower host can be obtained during story and for free
    add_rule(world.get_location(LocationName.trmaw_host, player), lambda state: can_trmaw_host(state, player))
    add_rule(world.get_location(LocationName.otr_host, player), lambda state: can_otr_host(state, player))
    add_rule(world.get_location(LocationName.gf_host, player), lambda state: can_gf_host(state, player))
    add_rule(world.get_location(LocationName.aet_host, player), lambda state: can_aet_host(state, player))
    add_rule(world.get_location(LocationName.bb_host, player), lambda state: can_bb_host(state, player))
    add_rule(world.get_location(LocationName.rtd_host, player), lambda state: can_rtd_host(state, player))
    add_rule(world.get_location(LocationName.sts_host, player), lambda state: can_sts_host(state, player))
    # Harbouring a Grudge does not have host
    add_rule(world.get_location(LocationName.adr_host, player), lambda state: can_adr_host(state, player))
    add_rule(world.get_location(LocationName.aw_host, player), lambda state: can_aw_host(state, player))
    add_rule(world.get_location(LocationName.asftc_host, player), lambda state: can_asftc_host(state, player))
    # Biplane Blast does not have host
    add_rule(world.get_location(LocationName.tjm_host, player), lambda state: can_tjm_host(state, player))
    add_rule(world.get_location(LocationName.tlotn_host, player), lambda state: can_tlotn_host(state, player))
    add_rule(world.get_location(LocationName.dol_host, player), lambda state: can_dol_host(state, player))


# Current logic implementation is that multiplier/can beat level. In separate function since always score multiply \
# is a starting item
def set_true_status_rules(world: MultiWorld, options: LB1Options, player: int):
    add_rule(world.get_location(LocationName.ycbob_ts, player), lambda state: can_beat_ycbob(state, options, player))
    add_rule(world.get_location(LocationName.air_ts, player), lambda state: can_beat_air(state, options, player))
    # Two-Face Chase can be beaten in story
    add_rule(world.get_location(LocationName.apa_ts, player), lambda state: can_beat_apa(state, player))
    add_rule(world.get_location(LocationName.tfo_ts, player), lambda state: can_beat_tfo(state, options, player))
    add_rule(world.get_location(LocationName.tsga_ts, player), lambda state: can_beat_tsga(state, options, player))
    # Batboat Battle can be beaten in story
    add_rule(world.get_location(LocationName.utc_ts, player), lambda state: can_beat_utc(state, options, player))
    add_rule(world.get_location(LocationName.zc_ts, player), lambda state: can_beat_zc(state, options, player))
    add_rule(world.get_location(LocationName.pl_ts, player), lambda state: can_beat_pl(state, options, player))
    add_rule(world.get_location(LocationName.jht_ts, player), lambda state: can_beat_jht(state, options, player))
    add_rule(world.get_location(LocationName.lfabt_ts, player), lambda state: can_beat_lfabt(state, options, player))
    # Flight of the Bat can be beaten in story
    add_rule(world.get_location(LocationName.itdn_ts, player), lambda state: can_beat_itdn(state, options, player))
    add_rule(world.get_location(LocationName.tttot_ts, player), lambda state: can_beat_tttot(state, options, player))
    # All Villain Levels can be beaten in story


def set_red_brick_location_rules(world: MultiWorld, options: LB1Options, player: int):
    add_rule(world.get_location(LocationName.ycbob_rb, player), lambda state: can_ycbob_rb(state, options, player))
    add_rule(world.get_location(LocationName.air_rb, player), lambda state: can_air_rb(state, options, player))
    # Two-Face Chase Red Brick can be obtained in story
    add_rule(world.get_location(LocationName.apa_rb, player), lambda state: can_apa_rb(state, player))
    add_rule(world.get_location(LocationName.tfo_rb, player), lambda state: can_tfo_rb(state, options, player))
    add_rule(world.get_location(LocationName.tsga_rb, player), lambda state: can_tsga_rb(state, options, player))
    add_rule(world.get_location(LocationName.trmaw_rb, player), lambda state: can_trmaw_rb(state, player))
    add_rule(world.get_location(LocationName.otr_rb, player), lambda state: can_otr_rb(state, player))
    add_rule(world.get_location(LocationName.gf_rb, player), lambda state: can_gf_rb(state, player))
    add_rule(world.get_location(LocationName.aet_rb, player), lambda state: can_aet_rb(state, player))
    add_rule(world.get_location(LocationName.bb_rb, player), lambda state: can_bb_rb(state, player))
    add_rule(world.get_location(LocationName.rtd_rb, player), lambda state: can_rtd_rb(state, player))
    add_rule(world.get_location(LocationName.sts_rb, player), lambda state: can_sts_rb(state, player))
    add_rule(world.get_location(LocationName.hag_rb, player), lambda state: can_hag_rb(state, player))


def set_red_brick_purchase_rules(world: MultiWorld, player: int):
    add_rule(world.get_location(LocationName.scorex2, player), lambda state: state.has(ItemName.trmaw_rbc, player))
    add_rule(world.get_location(LocationName.scorex4, player), lambda state: state.has(ItemName.otr_rbc, player))
    add_rule(world.get_location(LocationName.scorex6, player), lambda state: state.has(ItemName.gf_rbc, player))
    add_rule(world.get_location(LocationName.scorex8, player), lambda state: state.has(ItemName.aet_rbc, player))
    add_rule(world.get_location(LocationName.scorex10, player), lambda state: state.has(ItemName.bb_rbc, player))
    add_rule(world.get_location(LocationName.studmagnet, player), lambda state: state.has(ItemName.rtd_rbc, player))
    add_rule(world.get_location(LocationName.charstuds, player), lambda state: state.has(ItemName.sts_rbc, player))
    add_rule(world.get_location(LocationName.minikitdetect, player), lambda state: state.has(ItemName.hag_rbc, player))
    add_rule(world.get_location(LocationName.pwrbrickdetect, player), lambda state: state.has(ItemName.adr_rbc, player))
    add_rule(world.get_location(LocationName.alwaysscore, player), lambda state: state.has(ItemName.aw_rbc, player))
    add_rule(world.get_location(LocationName.fastbuild, player), lambda state: state.has(ItemName.asftc_rbc, player))
    add_rule(world.get_location(LocationName.immunefreeze, player), lambda state: state.has(ItemName.bbpl_rbc, player))
    add_rule(world.get_location(LocationName.regenhearts, player), lambda state: state.has(ItemName.tjm_rbc, player))
    add_rule(world.get_location(LocationName.extrahearts, player), lambda state: state.has(ItemName.tlotn_rbc, player))
    add_rule(world.get_location(LocationName.invincibility, player), lambda state: state.has(ItemName.dol_rbc, player))
    add_rule(world.get_location(LocationName.fastgrapple, player), lambda state: state.has(ItemName.ycbob_rbc, player))
    add_rule(world.get_location(LocationName.fastbatarang, player), lambda state: state.has(ItemName.air_rbc, player))
    add_rule(world.get_location(LocationName.moretargets, player), lambda state: state.has(ItemName.tfc_rbc, player))
    add_rule(world.get_location(LocationName.flamingbata, player), lambda state: state.has(ItemName.apa_rbc, player))
    add_rule(world.get_location(LocationName.slam, player), lambda state: state.has(ItemName.tfo_rbc, player))
    add_rule(world.get_location(LocationName.moredet, player), lambda state: state.has(ItemName.tsga_rbc, player))
    add_rule(world.get_location(LocationName.armorplating, player), lambda state: state.has(ItemName.bbb_rbc, player))
    add_rule(world.get_location(LocationName.sonicpain, player), lambda state: state.has(ItemName.utc_rbc, player))
    add_rule(world.get_location(LocationName.areaeffect, player), lambda state: state.has(ItemName.zc_rbc, player))
    add_rule(world.get_location(LocationName.bats, player), lambda state: state.has(ItemName.pl_rbc, player))
    add_rule(world.get_location(LocationName.freezebatarang, player), lambda state: state.has(ItemName.jht_rbc, player))
    add_rule(world.get_location(LocationName.decoy, player), lambda state: state.has(ItemName.lfabt_rbc, player))
    add_rule(world.get_location(LocationName.fastwalk, player), lambda state: state.has(ItemName.fotb_rbc, player))
    add_rule(world.get_location(LocationName.fasterpieces, player), lambda state: state.has(ItemName.itdn_rbc, player))
    add_rule(world.get_location(LocationName.piecedetect, player), lambda state: state.has(ItemName.tttot_rbc, player))


def set_rules(world: MultiWorld, options: LB1Options, player: int):
    set_entrance_rules(world, options, player)
    set_level_beaten_rules(world, options, player)
    # char rules
    # Hard char Rules
    # Automobile Rules
    # Watercraft Rules
    # aircraft Rules
    # Suit Rules
    if options.minikit_sanity == 1:
        set_minikit_rules(world, options, player)
    set_host_rules(world, options, player)
    if options.true_status_sanity == 1:
        set_true_status_rules(world, options, player)
    set_red_brick_location_rules(world, options, player)
    set_red_brick_purchase_rules(world, player)

    # Set End Goal
    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = \
            lambda state: state.has("Level Beaten Token", player, options.levels_to_win)


# TODO: can probably clean this up a bit
def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in level_beaten_event_location_table.items():
        event: Location = world.get_location(name, player)
        level_beaten_name = name.removesuffix(" Event")
        add_rule(event, world.get_location(level_beaten_name, player).access_rule)
