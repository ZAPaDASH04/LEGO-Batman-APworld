from typing import List, Callable

from BaseClasses import Location
from worlds.generic.Rules import set_rule
from rule_builder.options import OptionFilter, Operator
from rule_builder.rules import Rule, Has, HasAll, HasFromListUnique, True_, And, Or, CanReachLocation, CanReachRegion

from .Locations import event_location_table, purchase_location_table
from .Names import LocationName, ItemName, RegionName
from .Options import LB1Options, EndGoal

itm = ItemName
locn = LocationName
regn = RegionName

# Helper Rules
char_is_joker = Has(itm.joker_unlocked) | Has(itm.jokertropical_unlocked)

char_is_catwoman = Has(itm.catwoman_unlocked) | Has(itm.catwomanclassic_unlocked)

char_can_cross_toxic = (Has(itm.mrfreeze_unlocked) | Has(itm.poisonivy_unlocked) | Has(itm.twoface_unlocked) |
                        Has(itm.bane_unlocked) | Has(itm.killercroc_unlocked) | char_is_joker)

char_can_double_jump = (Has(itm.clayface_unlocked) | Has(itm.poisonivy_unlocked) | Has(itm.catwoman_unlocked) |
                        char_is_catwoman | Has(itm.harleyquinn_unlocked) | Has(itm.madhatter_unlocked))

char_is_female = Has(itm.poisonivy_unlocked) | Has(itm.harleyquinn_unlocked) | char_is_catwoman

char_can_hypno = Has(itm.riddler_unlocked) | Has(itm.scarecrow_unlocked) | Has(itm.madhatter_unlocked)

char_is_strong = (Has(itm.clayface_unlocked) | Has(itm.mrfreeze_unlocked) | Has(itm.bane_unlocked) |
                  Has(itm.killercroc_unlocked) | Has(itm.manbat_unlocked))

char_is_strong_and_toxic = Has(itm.mrfreeze_unlocked) | Has(itm.bane_unlocked) | Has(itm.killercroc_unlocked)

char_can_glide = (Has(itm.glidesuit) | Has(itm.manbat_unlocked) | Has(itm.penguin_unlocked) |
                  Has(itm.killermoth_unlocked))

char_can_long_jump = char_can_double_jump | char_can_glide

char_can_sink = Has(itm.watersuit) | Has(itm.killercroc_unlocked)

char_can_explode = Has(itm.demosuit) | Has(itm.penguin_unlocked)

char_can_techno = Has(itm.techsuit) | Has(itm.scientist_unlocked)

has_two_auto = HasFromListUnique(itm.batmobile_unlocked, itm.batcycle_unlocked, itm.policecar_unlocked,
                                 itm.policebike_unlocked, itm.policevan_unlocked, itm.battank_unlocked,
                                 itm.catmotorcycle_unlocked, itm.armouredtruck_unlocked, itm.freezekart_unlocked,
                                 itm.hammertruck_unlocked, itm.jokervan_unlocked, itm.garbagetruck_unlocked, count=2)

auto_has_cable = (Has(itm.batmobile_unlocked) | Has(itm.batcycle_unlocked) | Has(itm.battank_unlocked) |
                  Has(itm.catmotorcycle_unlocked))

auto_can_explode = (Has(itm.policecar_unlocked) | Has(itm.policevan_unlocked) | Has(itm.hammertruck_unlocked) |
                    Has(itm.jokervan_unlocked) | Has(itm.garbagetruck_unlocked))

has_two_watercraft = HasFromListUnique(itm.batboat_unlocked, itm.robinswatercraft_unlocked,
                                       itm.robinssubmarine_unlocked, itm.policewatercraft_unlocked,
                                       itm.policeboat_unlocked, itm.penguinsubmarine_unlocked, itm.swamprider_unlocked,
                                       itm.penguingoonsub_unlocked, itm.iceberg_unlocked, itm.steamboat_unlocked,
                                       count=2)

water_has_torpedo = Has(itm.robinswatercraft_unlocked) | Has(itm.penguinsubmarine_unlocked)

water_can_sink = (Has(itm.robinssubmarine_unlocked) | Has(itm.penguinsubmarine_unlocked) |
                  Has(itm.penguingoonsub_unlocked))

water_can_cross_toxic = Has(itm.policewatercraft_unlocked) | Has(itm.swamprider_unlocked) | Has(itm.iceberg_unlocked)

has_two_aircraft = HasFromListUnique(itm.batwing_unlocked, itm.batcopter_unlocked,
                                     itm.harbourhelicopter_unlocked, itm.policehelicopter_unlocked,
                                     itm.privatejet_unlocked, itm.jokerhelicopter_unlocked,
                                     itm.scarecrowbiplane_unlocked,
                                     itm.goonhelicopter_unlocked, itm.riddlerjet_unlocked, itm.glider_unlocked, count=2)

air_has_cable = (Has(itm.batcopter_unlocked) | Has(itm.harbourhelicopter_unlocked) | Has(itm.policehelicopter_unlocked)
                 | Has(itm.jokerhelicopter_unlocked) | Has(itm.goonhelicopter_unlocked))

air_can_cross_toxic = (Has(itm.harbourhelicopter_unlocked) | Has(itm.policehelicopter_unlocked) |
                       Has(itm.jokerhelicopter_unlocked) | Has(itm.scarecrowbiplane_unlocked) |
                       Has(itm.goonhelicopter_unlocked))

has_high_multi = (Has(itm.scorex6) | Has(itm.scorex8) | Has(itm.scorex10) |
                  HasAll(itm.scorex2, itm.scorex4))

has_low_multi = (Has(itm.scorex2) | Has(itm.scorex4))

# YCBOB Logic
can_access_ycbob_free = char_can_explode
can_beat_ycbob = char_can_explode & char_can_techno
can_get_ycbob_min3 = Has(itm.sonicsuit)
can_get_ycbob_min4 = char_can_cross_toxic & char_is_strong & char_can_hypno
can_get_ycbob_min5 = char_is_strong
can_get_ycbob_min6 = char_is_strong
can_get_ycbob_min7 = char_is_strong
can_get_ycbob_min8 = HasAll(itm.attractsuit, itm.sonicsuit)
can_get_ycbob_min9 = char_can_hypno & char_can_techno
can_get_ycbob_min10 = char_can_techno
can_get_ycbob_rb = char_can_techno & can_access_ycbob_free

# AIR Logic
can_access_air_free = Has(itm.magsuit) & char_can_glide
can_beat_air = Has(itm.magsuit) & char_can_glide
can_get_air_min1 = char_can_double_jump
can_get_air_min2 = char_can_double_jump
can_get_air_min4 = char_is_strong
can_get_air_min5 = char_can_double_jump & char_can_hypno
can_get_air_min6 = char_can_double_jump & char_can_explode
can_get_air_min7 = char_is_female
can_get_air_min8 = char_can_cross_toxic & char_can_explode
can_get_air_min9 = char_can_explode
can_get_air_min10 = char_can_hypno
can_get_air_host = char_can_hypno
can_get_air_rb = char_is_strong & can_access_air_free

# TFC Logic
can_access_tfc_free = auto_has_cable
can_access_tfc = Has(itm.tfc_lvl) & has_two_auto
can_get_tfc_min5 = Has(itm.jokervan_unlocked)
can_get_tfc_min6 = Has(itm.hammertruck_unlocked)
can_get_tfc_min10 = auto_can_explode

# APA Logic
can_access_apa_free = HasAll(itm.attractsuit, itm.sonicsuit)
can_beat_apa = HasAll(itm.attractsuit, itm.sonicsuit, itm.heatprotectsuit)
can_get_apa_min2 = char_can_double_jump & char_can_glide
can_get_apa_min3 = HasAll(itm.sonicsuit, itm.heatprotectsuit) & char_can_techno
can_get_apa_min4 = char_is_strong & char_can_double_jump & Has(itm.sonicsuit)
can_get_apa_min5 = Has(itm.sonicsuit)
can_get_apa_min6 = char_can_sink
can_get_apa_min7 = Has(itm.magsuit) & char_can_explode
can_get_apa_min8 = Has(itm.heatprotectsuit) & char_can_double_jump
can_get_apa_min9 = Has(itm.heatprotectsuit)
can_get_apa_min10 = Has(itm.heatprotectsuit)
can_get_apa_host = Has(itm.sonicsuit)
can_get_apa_rb = char_can_explode & char_is_joker & Has(itm.heatprotectsuit) & can_access_apa_free

# TFO Logic
can_access_tfo = Has(itm.tfo_lvl) & char_can_glide
can_access_tfo_free = Has(itm.magsuit)
can_beat_tfo = Has(itm.magsuit) & (Has(itm.attractsuit) | char_can_cross_toxic)
can_get_tfo_min4 = char_can_techno
can_get_tfo_min5 = char_can_double_jump & Has(itm.attractsuit)
can_get_tfo_min6 = char_can_cross_toxic
can_get_tfo_min7 = char_can_cross_toxic
can_get_tfo_min8 = HasAll(itm.mrfreeze_unlocked, itm.poisonivy_unlocked)
can_get_tfo_min9 = Has(itm.attractsuit) | char_can_cross_toxic
can_get_tfo_min10 = Has(itm.attractsuit) | char_can_cross_toxic
can_get_tfo_host = Has(itm.attractsuit) & char_can_double_jump
can_get_tfo_rb = char_can_cross_toxic & can_access_tfo_free

# TSGA Logic
can_access_tsga_free = char_can_glide & Has(itm.magsuit)
can_beat_tsga = char_can_explode & char_can_techno & Has(itm.magsuit) & char_can_glide
can_get_tsga_min1 = Has(itm.magsuit) & char_is_female
can_get_tsga_min2 = char_is_strong & char_can_double_jump
can_get_tsga_min3 = char_can_sink & char_can_explode
can_get_tsga_min4 = char_is_strong & char_can_explode
can_get_tsga_min5 = char_can_sink & char_can_cross_toxic
can_get_tsga_min7 = char_is_strong
can_get_tsga_min8 = char_is_strong & char_can_double_jump & char_can_explode
can_get_tsga_min9 = Has(itm.sonicsuit) & can_beat_tsga
can_get_tsga_min10 = can_beat_tsga & char_can_sink & Has(itm.sonicsuit)
can_get_tsga_rb = can_beat_tsga & Has(itm.sonicsuit) & can_access_tsga_free

# BBB Logic
can_access_bbb = Has(itm.bbb_lvl) & has_two_watercraft & Has(itm.batboat_unlocked)
can_get_bbb_min2 = Has(itm.robinswatercraft_unlocked)
can_get_bbb_min3 = water_can_sink & Has(itm.robinswatercraft_unlocked)
can_get_bbb_min5 = water_can_sink
can_get_bbb_min6 = water_can_cross_toxic
can_get_bbb_min7 = Has(itm.robinswatercraft_unlocked)
can_get_bbb_min8 = Has(itm.robinswatercraft_unlocked)
can_get_bbb_min9 = HasAll(itm.robinswatercraft_unlocked, itm.penguinsubmarine_unlocked)
can_get_bbb_min10 = can_get_bbb_min9 & water_can_cross_toxic
can_get_bbb_rb = HasAll(itm.robinswatercraft_unlocked, itm.penguinsubmarine_unlocked)

# UTC Logic
can_access_utc_free = char_can_explode & char_can_sink & (Has(itm.magsuit) | char_can_glide)
can_beat_utc = char_can_glide & char_can_sink & char_can_explode
can_get_utc_min1 = char_can_double_jump & char_can_explode
can_get_utc_min2 = char_can_hypno & char_can_explode & char_can_glide & char_is_strong_and_toxic
can_get_utc_min3 = char_can_explode & char_can_sink & char_is_strong & Has(itm.sonicsuit)
can_get_utc_min4 = char_can_double_jump & char_can_explode & char_can_sink
can_get_utc_min5 = Has(itm.attractsuit)
can_get_utc_min6 = char_can_cross_toxic
can_get_utc_min7 = char_is_strong
can_get_utc_min8 = Has(itm.magsuit)
can_get_utc_min10 = char_is_joker
can_get_utc_host = char_can_explode
can_get_utc_rb = char_can_techno

# ZC Logic
can_access_zc_free = char_can_explode | (char_can_glide & Has(itm.magsuit))
can_beat_zc = char_can_glide & char_can_explode & HasAll(itm.magsuit, itm.sonicsuit)
can_get_zc_min1 = char_is_female & char_can_explode
can_get_zc_min2 = char_is_strong & char_can_double_jump & char_can_cross_toxic
can_get_zc_min3 = Has(itm.attractsuit) & (char_is_female | (char_can_cross_toxic & char_is_strong))
can_get_zc_min4 = char_can_double_jump & char_can_explode
can_get_zc_min5 = Has(itm.poisonivy_unlocked)
can_get_zc_min6 = char_can_long_jump
can_get_zc_min8 = char_can_glide & Has(itm.sonicsuit)
can_get_zc_min9 = char_can_glide & HasAll(itm.sonicsuit, itm.mrfreeze_unlocked)
can_get_zc_min10 = char_can_glide & char_is_strong & Has(itm.sonicsuit)
can_get_zc_host = Has(itm.sonicsuit) | (char_can_glide & char_can_techno)
can_get_zc_rb = char_can_double_jump & char_can_sink & can_access_zc_free

# PL Logic
can_access_pl_free = char_can_glide & char_can_sink
can_beat_pl = char_can_glide & char_can_sink
can_get_pl_min1 = Has(itm.sonicsuit)
can_get_pl_min2 = Has(itm.mrfreeze_unlocked) & char_can_explode
can_get_pl_min3 = char_can_glide & char_can_double_jump
can_get_pl_min5 = Has(itm.glidesuit) & char_can_sink
can_get_pl_min7 = char_can_double_jump
can_get_pl_min8 = char_can_cross_toxic & Has(itm.penguin_unlocked)
can_get_pl_min10 = HasAll(itm.heatprotectsuit, itm.sonicsuit)
can_get_pl_rb = Has(itm.sonicsuit) & can_access_pl_free

# JHT Logic
can_access_jht = HasAll(itm.attractsuit, itm.jht_lvl) & char_can_glide
can_beat_jht = char_can_glide & HasAll(itm.magsuit, itm.attractsuit)
can_get_jht_min1 = char_can_explode
can_get_jht_min3 = char_can_hypno & char_can_explode & Has(itm.heatprotectsuit)
can_get_jht_min4 = char_is_joker & char_can_double_jump
can_get_jht_min5 = char_can_techno
can_get_jht_min6 = char_can_cross_toxic
can_get_jht_min7 = char_is_strong & char_can_double_jump
can_get_jht_min8 = char_can_cross_toxic
can_get_jht_min9 = char_is_joker & Has(itm.magsuit)
can_get_jht_min_10 = char_can_explode & Has(itm.magsuit)
can_get_jht_host = can_beat_jht & char_is_joker
can_get_jht_rb = HasAll(itm.mrfreeze_unlocked, itm.sonicsuit) & char_can_double_jump

# LFABT Logic
can_access_lfabt_free = char_can_explode & Has(itm.sonicsuit)
can_beat_lfabt = char_can_explode & HasAll(itm.magsuit, itm.attractsuit)
can_get_lfabt_min1 = char_is_strong & char_can_double_jump
can_get_lfabt_min2 = char_can_long_jump & Has(itm.sonicsuit)
can_get_lfabt_min3 = char_can_sink
can_get_lfabt_min4 = char_can_techno
can_get_lfabt_min5 = char_can_explode
can_get_lfabt_min6 = char_is_joker & Has(itm.magsuit)
can_get_lfabt_min7 = HasAll(itm.magsuit, itm.attractsuit)
can_get_lfabt_min8 = HasAll(itm.magsuit, itm.attractsuit) & char_can_techno & char_can_cross_toxic
can_get_lfabt_min9 = HasAll(itm.attractsuit, itm.magsuit) & char_is_strong
can_get_lfabt_min_10 = HasAll(itm.attractsuit, itm.magsuit) & char_can_cross_toxic
can_get_lfabt_host = Has(itm.magsuit)
can_get_lfabt_rb = char_can_glide & char_can_techno

# FOTB Logic
can_access_fotb_free = air_has_cable
can_access_fotb = Has(itm.fotb_lvl) & has_two_aircraft & Has(itm.batwing_unlocked)
can_get_fotb_min7 = air_can_cross_toxic
can_get_fotb_min9 = air_can_cross_toxic
can_get_fotb_rb = air_can_cross_toxic & can_access_fotb_free

# ITDN Logic
can_access_itdn_free = char_can_explode
can_beat_itdn = Has(itm.magsuit) & char_can_explode & char_can_techno
can_get_itdn_min1 = char_is_strong & Has(itm.sonicsuit)
can_get_itdn_min2 = char_can_long_jump
can_get_itdn_min3 = (char_can_hypno & char_is_strong & char_can_cross_toxic & char_can_double_jump &
                     Has(itm.penguin_unlocked))
can_get_itdn_min4 = char_can_sink & Has(itm.poisonivy_unlocked)
can_get_itdn_min5 = Has(itm.attractsuit) & char_can_techno
can_get_itdn_min6 = char_is_strong & char_can_techno
can_get_itdn_min7 = can_beat_itdn
can_get_itdn_min8 = can_beat_itdn
can_get_itdn_min9 = can_beat_itdn & char_is_joker & Has(itm.sonicsuit)
can_get_itdn_min10 = char_is_joker & char_can_double_jump & Has(itm.sonicsuit)
can_get_itdn_host = char_can_explode & char_can_techno
can_get_itdn_rb = can_beat_itdn & char_can_glide & Has(itm.heatprotectsuit) & can_access_itdn_free

# TTTOT Logic
can_access_tttot_free = Has(itm.magsuit)
can_beat_tttot = Has(itm.magsuit) & char_can_glide
can_get_tttot_min1 = char_can_explode
can_get_tttot_min3 = Has(itm.sonicsuit)
can_get_tttot_min4 = Has(itm.attractsuit)
can_get_tttot_min5 = char_can_long_jump
can_get_tttot_min6 = char_is_joker
can_get_tttot_min9 = char_can_glide & char_can_double_jump
can_get_tttot_min10 = can_beat_tttot & char_can_explode
can_get_tttot_rb = can_beat_tttot & char_is_strong


# TRMAW Logic


def set_entrance_rules(world):
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.ycbob), Has(ItemName.ycbob_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.air), Has(ItemName.air_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tfc), can_access_tfc)
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.apa), Has(ItemName.apa_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tfo), can_access_tfo)
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tsga), Has(ItemName.tsga_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.bbb), can_access_bbb)
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.utc), Has(ItemName.utc_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.zc), Has(ItemName.zc_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.pl), Has(ItemName.pl_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.jht), can_access_jht)
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.lfabt), Has(ItemName.lfabt_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.fotb), can_access_fotb)
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.itdn), Has(ItemName.itdn_lvl))
    world.set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tttot), Has(ItemName.tttot_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.trmaw), Has(ItemName.trmaw_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.otr), Has(ItemName.otr_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.gf), Has(ItemName.gf_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aet), Has(ItemName.aet_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bb), Has(ItemName.bb_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.rtd), Has(ItemName.rtd_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.sts), Has(ItemName.sts_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.hag), Has(ItemName.hag_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.adr), Has(ItemName.adr_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aw), Has(ItemName.aw_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.asftc), Has(ItemName.asftc_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bbpl), Has(ItemName.bbpl_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.tjm), Has(ItemName.tjm_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.tlotn), Has(ItemName.tlotn_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.dol), Has(ItemName.dol_lvl))
    # Sub Regions
    world.set_rule(world.get_entrance(RegionName.ycbob + " -> " + RegionName.ycbobf), can_access_ycbob_free)
    world.set_rule(world.get_entrance(RegionName.air + " -> " + RegionName.airf), can_access_air_free)
    world.set_rule(world.get_entrance(RegionName.tfc + " -> " + RegionName.tfcf), can_access_tfc_free)
    world.set_rule(world.get_entrance(RegionName.apa + " -> " + RegionName.apaf), can_access_apa_free)
    world.set_rule(world.get_entrance(RegionName.tfo + " -> " + RegionName.tfof), can_access_tfo_free)
    world.set_rule(world.get_entrance(RegionName.tsga + " -> " + RegionName.tsgaf), can_access_tsga_free)
    world.set_rule(world.get_entrance(RegionName.utc + " -> " + RegionName.utcf), can_access_utc_free)
    world.set_rule(world.get_entrance(RegionName.zc + " -> " + RegionName.zcf), can_access_zc_free)
    world.set_rule(world.get_entrance(RegionName.pl + " -> " + RegionName.plf), can_access_pl_free)
    world.set_rule(world.get_entrance(RegionName.lfabt + " -> " + RegionName.lfabtf), can_access_lfabt_free)
    world.set_rule(world.get_entrance(RegionName.fotb + " -> " + RegionName.fotbf), can_access_fotb_free)
    world.set_rule(world.get_entrance(RegionName.itdn + " -> " + RegionName.itdnf), can_access_itdn_free)
    world.set_rule(world.get_entrance(RegionName.tttot + " -> " + RegionName.tttotf), can_access_tttot_free)
    # world.set_rule(world.get_entrance(RegionName.trmaw + " -> " + RegionName.trmawf),
    #                lambda state: free_access_trmaw(state))
    # world.set_rule(world.get_entrance(RegionName.otr + " -> " + RegionName.otrf),
    #                lambda state: free_access_otr(state))
    # world.set_rule(world.get_entrance(RegionName.gf + " -> " + RegionName.gff),
    #                lambda state: free_access_gf(state))
    # world.set_rule(world.get_entrance(RegionName.bb + " -> " + RegionName.bbf),
    #                lambda state: free_access_bb(state))
    # world.set_rule(world.get_entrance(RegionName.rtd + " -> " + RegionName.rtdf),
    #                lambda state: free_access_rtd(state))
    # world.set_rule(world.get_entrance(RegionName.sts + " -> " + RegionName.stsf),
    #                lambda state: free_access_sts(state))
    # world.set_rule(world.get_entrance(RegionName.hag + " -> " + RegionName.hagf),
    #                lambda state: free_access_hag(state))
    # world.set_rule(world.get_entrance(RegionName.adr + " -> " + RegionName.adrf),
    #                lambda state: free_access_adr(state))
    # world.set_rule(world.get_entrance(RegionName.aw + " -> " + RegionName.awf),
    #                lambda state: free_access_aw(state))
    # world.set_rule(world.get_entrance(RegionName.asftc + " -> " + RegionName.asftcf),
    #                lambda state: free_access_asftc(state))
    # world.set_rule(world.get_entrance(RegionName.bbpl + " -> " + RegionName.bbplf),
    #                lambda state: free_access_bbpl(state))
    # world.set_rule(world.get_entrance(RegionName.tjm + " -> " + RegionName.tjmf),
    #                lambda state: free_access_tjm(state))
    # world.set_rule(world.get_entrance(RegionName.tlotn + " -> " + RegionName.tlotnf),
    #                lambda state: free_access_tlotn(state))
    # world.set_rule(world.get_entrance(RegionName.dol + " -> " + RegionName.dolf),
    #                lambda state: free_access_dol(state))


#
#
# def set_char_rules(world: MultiWorld, options: LB1Options, player: int):
#     # set_rule(world.get_location(LocationName.batman_collected, player),
#     #          lambda state: can_complete_any_hero_level(state, options, player))
#     # set_rule(world.get_location(LocationName.robin_collected, player),
#     #          lambda state: can_complete_any_hero_level(state, options, player))
#     # Batmobile, Cycle, Boat, Sub, Wing, Copter don't require anything to beat level
#     set_rule(world.get_location(LocationName.twoface_unlocked, player),
#              lambda state: can_unlock_two_face(state, player))
#     set_rule(world.get_location(LocationName.riddler_unlocked, player),
#              lambda state: can_unlock_riddler(state, player))
#     set_rule(world.get_location(LocationName.catwoman_unlocked, player),
#              lambda state: can_unlock_catwoman(state, player))
#     set_rule(world.get_location(LocationName.penguin_unlocked, player),
#              lambda state: can_unlock_penguin(state, player))
#     set_rule(world.get_location(LocationName.harleyquinn_unlocked, player),
#              lambda state: can_unlock_harley(state, player))
#     set_rule(world.get_location(LocationName.joker_unlocked, player),
#              lambda state: can_unlock_joker(state, player))
#     # Villain levels can be beaten in story
#
#
# def set_suit_rules(world: MultiWorld, options: LB1Options, player: int):
#     set_rule(world.get_location(LocationName.heatprotectsuit, player),
#              lambda state: can_unlock_heat_suit(state, player))
#     set_rule(world.get_location(LocationName.glidesuit, player),
#              lambda state: can_unlock_glide_suit(state, options, player))
#     set_rule(world.get_location(LocationName.demosuit, player),
#              lambda state: can_unlock_demo_suit(state, options, player))
#     set_rule(world.get_location(LocationName.sonicsuit, player),
#              lambda state: can_unlock_sonic_suit(state, options, player))
#     set_rule(world.get_location(LocationName.watersuit, player),
#              lambda state: can_unlock_water_suit(state, options, player))
#     set_rule(world.get_location(LocationName.techsuit, player),
#              lambda state: can_unlock_tech_suit(state, options, player))
#     set_rule(world.get_location(LocationName.magsuit, player),
#              lambda state: can_unlock_mag_suit(state, options, player))
#     set_rule(world.get_location(LocationName.attractsuit, player),
#              lambda state: can_unlock_attract_suit(state, options, player))
#
#
def set_minikit_rules(world):
    # YCBOB
    world.set_rule(world.get_location(locn.ycbob_min3), can_get_ycbob_min3)
    world.set_rule(world.get_location(locn.ycbob_min4), can_get_ycbob_min4)
    world.set_rule(world.get_location(locn.ycbob_min5), can_get_ycbob_min5)
    world.set_rule(world.get_location(locn.ycbob_min6), can_get_ycbob_min6)
    world.set_rule(world.get_location(locn.ycbob_min7), can_get_ycbob_min7)
    world.set_rule(world.get_location(locn.ycbob_min8), can_get_ycbob_min8)
    world.set_rule(world.get_location(locn.ycbob_min9), can_get_ycbob_min9)
    world.set_rule(world.get_location(locn.ycbob_min10), can_get_ycbob_min10)
    # AIR
    world.set_rule(world.get_location(locn.air_min1), can_get_air_min1)
    world.set_rule(world.get_location(locn.air_min2), can_get_air_min2)
    world.set_rule(world.get_location(locn.air_min4), can_get_air_min4)
    world.set_rule(world.get_location(locn.air_min5), can_get_air_min5)
    world.set_rule(world.get_location(locn.air_min6), can_get_air_min6)
    world.set_rule(world.get_location(locn.air_min7), can_get_air_min7)
    world.set_rule(world.get_location(locn.air_min8), can_get_air_min8)
    world.set_rule(world.get_location(locn.air_min9), can_get_air_min9)
    world.set_rule(world.get_location(locn.air_min10), can_get_air_min10)
    # TFC
    world.set_rule(world.get_location(locn.tfc_min5), can_get_tfc_min5)
    world.set_rule(world.get_location(locn.tfc_min6), can_get_tfc_min6)
    world.set_rule(world.get_location(locn.tfc_min10), can_get_tfc_min10)
    # APA
    world.set_rule(world.get_location(locn.apa_min2), can_get_apa_min2)
    world.set_rule(world.get_location(locn.apa_min3), can_get_apa_min3)
    world.set_rule(world.get_location(locn.apa_min4), can_get_apa_min4)
    world.set_rule(world.get_location(locn.apa_min5), can_get_apa_min5)
    world.set_rule(world.get_location(locn.apa_min6), can_get_apa_min6)
    world.set_rule(world.get_location(locn.apa_min7), can_get_apa_min7)
    world.set_rule(world.get_location(locn.apa_min8), can_get_apa_min8)
    world.set_rule(world.get_location(locn.apa_min9), can_get_apa_min9)
    world.set_rule(world.get_location(locn.apa_min10), can_get_apa_min10)
    # TFO Logic
    world.set_rule(world.get_location(locn.tfo_min4), can_get_tfo_min4)
    world.set_rule(world.get_location(locn.tfo_min5), can_get_tfo_min5)
    world.set_rule(world.get_location(locn.tfo_min6), can_get_tfo_min6)
    world.set_rule(world.get_location(locn.tfo_min7), can_get_tfo_min7)
    world.set_rule(world.get_location(locn.tfo_min8), can_get_tfo_min8)
    world.set_rule(world.get_location(locn.tfo_min9), can_get_tfo_min9)
    world.set_rule(world.get_location(locn.tfo_min10), can_get_tfo_min10)
    # TSGA Logic
    world.set_rule(world.get_location(locn.tsga_min1), can_get_tsga_min1)
    world.set_rule(world.get_location(locn.tsga_min2), can_get_tsga_min2)
    world.set_rule(world.get_location(locn.tsga_min3), can_get_tsga_min3)
    world.set_rule(world.get_location(locn.tsga_min4), can_get_tsga_min4)
    world.set_rule(world.get_location(locn.tsga_min5), can_get_tsga_min5)
    world.set_rule(world.get_location(locn.tsga_min7), can_get_tsga_min7)
    world.set_rule(world.get_location(locn.tsga_min8), can_get_tsga_min8)
    world.set_rule(world.get_location(locn.tsga_min9), can_get_tsga_min9)
    world.set_rule(world.get_location(locn.tsga_min10), can_get_tsga_min10)
    # BBB Logic
    world.set_rule(world.get_location(locn.bbb_min2), can_get_bbb_min2)
    world.set_rule(world.get_location(locn.bbb_min3), can_get_bbb_min3)
    world.set_rule(world.get_location(locn.bbb_min5), can_get_bbb_min5)
    world.set_rule(world.get_location(locn.bbb_min6), can_get_bbb_min6)
    world.set_rule(world.get_location(locn.bbb_min7), can_get_bbb_min7)
    world.set_rule(world.get_location(locn.bbb_min8), can_get_bbb_min8)
    world.set_rule(world.get_location(locn.bbb_min9), can_get_bbb_min9)
    world.set_rule(world.get_location(locn.bbb_min10), can_get_bbb_min10)
    # UTC Logic
    world.set_rule(world.get_location(locn.utc_min1), can_get_utc_min1)
    world.set_rule(world.get_location(locn.utc_min2), can_get_utc_min2)
    world.set_rule(world.get_location(locn.utc_min3), can_get_utc_min3)
    world.set_rule(world.get_location(locn.utc_min4), can_get_utc_min4)
    world.set_rule(world.get_location(locn.utc_min5), can_get_utc_min5)
    world.set_rule(world.get_location(locn.utc_min6), can_get_utc_min6)
    world.set_rule(world.get_location(locn.utc_min7), can_get_utc_min7)
    world.set_rule(world.get_location(locn.utc_min8), can_get_utc_min8)
    world.set_rule(world.get_location(locn.utc_min10), can_get_utc_min10)
    # ZC Logic
    world.set_rule(world.get_location(locn.zc_min1), can_get_zc_min1)
    world.set_rule(world.get_location(locn.zc_min2), can_get_zc_min2)
    world.set_rule(world.get_location(locn.zc_min3), can_get_zc_min3)
    world.set_rule(world.get_location(locn.zc_min4), can_get_zc_min4)
    world.set_rule(world.get_location(locn.zc_min5), can_get_zc_min5)
    world.set_rule(world.get_location(locn.zc_min6), can_get_zc_min6)
    world.set_rule(world.get_location(locn.zc_min8), can_get_zc_min8)
    world.set_rule(world.get_location(locn.zc_min9), can_get_zc_min9)
    world.set_rule(world.get_location(locn.zc_min10), can_get_zc_min10)
    # PL Logic
    world.set_rule(world.get_location(locn.pl_min1), can_get_pl_min1)
    world.set_rule(world.get_location(locn.pl_min2), can_get_pl_min2)
    world.set_rule(world.get_location(locn.pl_min3), can_get_pl_min3)
    world.set_rule(world.get_location(locn.pl_min5), can_get_pl_min5)
    world.set_rule(world.get_location(locn.pl_min7), can_get_pl_min7)
    world.set_rule(world.get_location(locn.pl_min8), can_get_pl_min8)
    world.set_rule(world.get_location(locn.pl_min10), can_get_pl_min10)
    # JHT Logic
    world.set_rule(world.get_location(locn.jht_min1), can_get_jht_min1)
    world.set_rule(world.get_location(locn.jht_min3), can_get_jht_min3)
    world.set_rule(world.get_location(locn.jht_min4), can_get_jht_min4)
    world.set_rule(world.get_location(locn.jht_min5), can_get_jht_min5)
    world.set_rule(world.get_location(locn.jht_min6), can_get_jht_min6)
    world.set_rule(world.get_location(locn.jht_min7), can_get_jht_min7)
    world.set_rule(world.get_location(locn.jht_min8), can_get_jht_min8)
    world.set_rule(world.get_location(locn.jht_min9), can_get_jht_min9)
    world.set_rule(world.get_location(locn.jht_min10), can_get_jht_min_10)
    # LFABT Logic
    world.set_rule(world.get_location(locn.lfabt_min1), can_get_lfabt_min1)
    world.set_rule(world.get_location(locn.lfabt_min2), can_get_lfabt_min2)
    world.set_rule(world.get_location(locn.lfabt_min3), can_get_lfabt_min3)
    world.set_rule(world.get_location(locn.lfabt_min4), can_get_lfabt_min4)
    world.set_rule(world.get_location(locn.lfabt_min5), can_get_lfabt_min5)
    world.set_rule(world.get_location(locn.lfabt_min6), can_get_lfabt_min6)
    world.set_rule(world.get_location(locn.lfabt_min7), can_get_lfabt_min7)
    world.set_rule(world.get_location(locn.lfabt_min8), can_get_lfabt_min8)
    world.set_rule(world.get_location(locn.lfabt_min9), can_get_lfabt_min9)
    world.set_rule(world.get_location(locn.lfabt_min10), can_get_lfabt_min_10)
    # FOTB Logic
    world.set_rule(world.get_location(locn.fotb_min7), can_get_fotb_min7)
    world.set_rule(world.get_location(locn.fotb_min9), can_get_fotb_min9)
    # ITDN Logic
    world.set_rule(world.get_location(locn.itdn_min1), can_get_itdn_min1)
    world.set_rule(world.get_location(locn.itdn_min2), can_get_itdn_min2)
    world.set_rule(world.get_location(locn.itdn_min3), can_get_itdn_min3)
    world.set_rule(world.get_location(locn.itdn_min4), can_get_itdn_min4)
    world.set_rule(world.get_location(locn.itdn_min5), can_get_itdn_min5)
    world.set_rule(world.get_location(locn.itdn_min6), can_get_itdn_min6)
    world.set_rule(world.get_location(locn.itdn_min7), can_get_itdn_min7)
    world.set_rule(world.get_location(locn.itdn_min8), can_get_itdn_min8)
    world.set_rule(world.get_location(locn.itdn_min9), can_get_itdn_min9)
    world.set_rule(world.get_location(locn.itdn_min10), can_get_itdn_min10)
    # TTTOT Logic
    world.set_rule(world.get_location(locn.tttot_min1), can_get_tttot_min1)
    world.set_rule(world.get_location(locn.tttot_min3), can_get_tttot_min3)
    world.set_rule(world.get_location(locn.tttot_min4), can_get_tttot_min4)
    world.set_rule(world.get_location(locn.tttot_min5), can_get_tttot_min5)
    world.set_rule(world.get_location(locn.tttot_min6), can_get_tttot_min6)
    world.set_rule(world.get_location(locn.tttot_min9), can_get_tttot_min9)
    world.set_rule(world.get_location(locn.tttot_min10), can_get_tttot_min10)


def set_host_rules(world):
    world.set_rule(world.get_location(locn.air_host), can_get_air_host)
    world.set_rule(world.get_location(locn.apa_host), can_get_apa_host)
    world.set_rule(world.get_location(locn.tfo_host), can_get_tfo_host)
    world.set_rule(world.get_location(locn.utc_host), can_get_utc_host)
    world.set_rule(world.get_location(locn.zc_host), can_get_zc_host)
    world.set_rule(world.get_location(locn.jht_host), can_get_jht_host)
    world.set_rule(world.get_location(locn.lfabt_host), can_get_lfabt_host)
    world.set_rule(world.get_location(locn.itdn_host), can_get_itdn_host)


def set_level_beaten_rules(world):
    world.set_rule(world.get_location(locn.ycbob_beat), can_beat_ycbob)
    world.set_rule(world.get_location(locn.ycbob_ts), can_beat_ycbob)
    world.set_rule(world.get_location(locn.air_beat), can_beat_air)
    world.set_rule(world.get_location(locn.air_ts), can_beat_air)
    world.set_rule(world.get_location(locn.tfo_beat), can_beat_tfo)
    world.set_rule(world.get_location(locn.tfo_ts), can_beat_tfo)
    world.set_rule(world.get_location(locn.tsga_beat), can_beat_tsga)
    world.set_rule(world.get_location(locn.tsga_ts), can_beat_tsga)
    world.set_rule(world.get_location(locn.utc_beat), can_beat_utc)
    world.set_rule(world.get_location(locn.utc_ts), can_beat_utc)
    world.set_rule(world.get_location(locn.zc_beat), can_beat_zc)
    world.set_rule(world.get_location(locn.zc_ts), can_beat_zc)
    world.set_rule(world.get_location(locn.pl_beat), can_beat_pl)
    world.set_rule(world.get_location(locn.pl_ts), can_beat_pl)
    world.set_rule(world.get_location(locn.jht_beat), can_beat_jht)
    world.set_rule(world.get_location(locn.jht_ts), can_beat_jht)
    world.set_rule(world.get_location(locn.lfabt_beat), can_beat_lfabt)
    world.set_rule(world.get_location(locn.lfabt_ts), can_beat_lfabt)
    world.set_rule(world.get_location(locn.itdn_beat), can_beat_itdn)
    world.set_rule(world.get_location(locn.itdn_ts), can_beat_itdn)
    world.set_rule(world.get_location(locn.tttot_beat), can_beat_tttot)
    world.set_rule(world.get_location(locn.tttot_ts), can_beat_tttot)


#
# def set_true_status_rules(world: MultiWorld, options: LB1Options, player: int):
#     set_rule(world.get_location(LocationName.ycbob_ts, player), lambda state: can_beat_ycbob(state, options, player))
#     set_rule(world.get_location(LocationName.air_ts, player), lambda state: can_beat_air(state, options, player))
#     # Two-Face Chase can be beaten in story
#     set_rule(world.get_location(LocationName.apa_ts, player), lambda state: can_beat_apa(state, player))
#     set_rule(world.get_location(LocationName.tfo_ts, player), lambda state: can_beat_tfo(state, options, player))
#     set_rule(world.get_location(LocationName.tsga_ts, player), lambda state: can_beat_tsga(state, options, player))
#     # Batboat Battle can be beaten in story
#     set_rule(world.get_location(LocationName.utc_ts, player), lambda state: can_beat_utc(state, options, player))
#     set_rule(world.get_location(LocationName.zc_ts, player), lambda state: can_beat_zc(state, options, player))
#     set_rule(world.get_location(LocationName.pl_ts, player), lambda state: can_beat_pl(state, options, player))
#     set_rule(world.get_location(LocationName.jht_ts, player), lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.lfabt_ts, player), lambda state: can_beat_lfabt(state, options, player))
#     # Flight of the Bat can be beaten in story
#     set_rule(world.get_location(LocationName.itdn_ts, player), lambda state: can_beat_itdn(state, options, player))
#     set_rule(world.get_location(LocationName.tttot_ts, player), lambda state: can_beat_tttot(state, options, player))
#     # All Villain Levels can be beaten in story

#
#
# def set_shop_rules(world: MultiWorld, options: LB1Options, player: int):
#     set_rule(world.get_location(LocationName.riddlergoon_unlocked, player),
#              lambda state: can_purchase_riddler_goon(state, options, player))
#     set_rule(world.get_location(LocationName.riddlerhenchman_unlocked, player),
#              lambda state: can_purchase_riddler_henchman(state, options, player))
#     set_rule(world.get_location(LocationName.freezegirl_unlocked, player),
#              lambda state: can_purchase_freeze_girl(state, options, player))
#     set_rule(world.get_location(LocationName.policecar_unlocked, player),
#              lambda state: can_purchase_police_car(state, options, player))
#     set_rule(world.get_location(LocationName.policebike_unlocked, player),
#              lambda state: can_purchase_police_bike(state, options, player))
#     set_rule(world.get_location(LocationName.policevan_unlocked, player),
#              lambda state: can_purchase_police_van(state, options, player))
#     set_rule(world.get_location(LocationName.jokervan_unlocked, player),
#              lambda state: can_purchase_joker_van(state, options, player))
#     set_rule(world.get_location(LocationName.poisonivygoon_unlocked, player),
#              lambda state: can_purchase_poison_ivy_goon(state, options, player))
#     set_rule(world.get_location(LocationName.fishmonger_unlocked, player),
#              lambda state: can_purchase_fishmonger(state, options, player))
#     set_rule(world.get_location(LocationName.penguingoon_unlocked, player),
#              lambda state: can_purchase_penguin_goon(state, options, player))
#     set_rule(world.get_location(LocationName.penguinhenchman_unlocked, player),
#              lambda state: can_purchase_penguin_henchman(state, options, player))
#     set_rule(world.get_location(LocationName.robinssubmarine_unlocked, player),
#              lambda state: can_purchase_robin_sub(state, options, player))
#     set_rule(world.get_location(LocationName.penguingoonsub_unlocked, player),
#              lambda state: can_purchase_goon_sub(state, options, player))
#     set_rule(world.get_location(LocationName.harbourhelicopter_unlocked, player),
#              lambda state: can_purchase_harbour_heli(state, options, player))
#     set_rule(world.get_location(LocationName.zoosweeper_unlocked, player),
#              lambda state: can_purchase_zoo_sweeper(state, options, player))
#     set_rule(world.get_location(LocationName.manbat_unlocked, player),
#              lambda state: can_purchase_manbat(state, options, player))
#     set_rule(world.get_location(LocationName.yeti_unlocked, player),
#              lambda state: can_purchase_yeti(state, options, player))
#     set_rule(world.get_location(LocationName.penguinminion_unlocked, player),
#              lambda state: can_purchase_penguin_minion(state, options, player))
#     set_rule(world.get_location(LocationName.madhatter_unlocked, player),
#              lambda state: can_purchase_mad_hatter(state, options, player))
#     set_rule(world.get_location(LocationName.jokergoon_unlocked, player),
#              lambda state: can_purchase_joker_goon(state, options, player))
#     set_rule(world.get_location(LocationName.jokerhenchman_unlocked, player),
#              lambda state: can_purchase_joker_henchman(state, options, player))
#     set_rule(world.get_location(LocationName.steamboat_unlocked, player),
#              lambda state: can_purchase_steamboat(state, options, player))
#     set_rule(world.get_location(LocationName.glider_unlocked, player),
#              lambda state: can_purchase_glider(state, options, player))
#     set_rule(world.get_location(LocationName.clowngoon_unlocked, player),
#              lambda state: can_purchase_clown(state, options, player))
#     set_rule(world.get_location(LocationName.privatejet_unlocked, player),
#              lambda state: can_purchase_private_jet(state, options, player))
#     set_rule(world.get_location(LocationName.brucewayne_unlocked, player),
#              lambda state: can_purchase_bruce_wayne(state, options, player))
#     set_rule(world.get_location(LocationName.alfred_unlocked, player),
#              lambda state: can_purchase_alfred(state, options, player))
#     set_rule(world.get_location(LocationName.batgirl_unlocked, player),
#              lambda state: can_purchase_batgirl(state, options, player))
#     set_rule(world.get_location(LocationName.nightwing_unlocked, player),
#              lambda state: can_purchase_nightwing(state, options, player))
#     set_rule(world.get_location(LocationName.policeofficer_unlocked, player),
#              lambda state: can_purchase_police_officer(state, options, player))
#     set_rule(world.get_location(LocationName.militarypoliceman_unlocked, player),
#              lambda state: can_purchase_military_police(state, options, player))
#     set_rule(world.get_location(LocationName.securityguard_unlocked, player),
#              lambda state: can_purchase_security_guard(state, options, player))
#     set_rule(world.get_location(LocationName.battank_unlocked, player),
#              lambda state: can_purchase_bat_tank(state, options, player))
#     set_rule(world.get_location(LocationName.freezekart_unlocked, player),
#              lambda state: can_purchase_freeze_kart(state, options, player))
#     set_rule(world.get_location(LocationName.iceberg_unlocked, player),
#              lambda state: can_purchase_iceberg(state, options, player))
#     set_rule(world.get_location(LocationName.scientist_unlocked, player),
#              lambda state: can_purchase_scientist(state, options, player))
#     set_rule(world.get_location(LocationName.armouredtruck_unlocked, player),
#              lambda state: can_purchase_armoured_truck(state, options, player))
#     set_rule(world.get_location(LocationName.swat_unlocked, player),
#              lambda state: can_purchase_swat(state, options, player))
#     set_rule(world.get_location(LocationName.riddlerjet_unlocked, player),
#              lambda state: can_purchase_riddler_jet(state, options, player))
#     set_rule(world.get_location(LocationName.sailor_unlocked, player),
#              lambda state: can_purchase_sailor(state, options, player))
#     set_rule(world.get_location(LocationName.catwomanclassic_unlocked, player),
#              lambda state: can_purchase_catwoman_classic(state, options, player))
#     set_rule(world.get_location(LocationName.catmotorcycle_unlocked, player),
#              lambda state: can_purchase_cat_motorcycle(state, options, player))
#     set_rule(world.get_location(LocationName.policewatercraft_unlocked, player),
#              lambda state: can_purchase_police_watercraft(state, options, player))
#     set_rule(world.get_location(LocationName.policeboat_unlocked, player),
#              lambda state: can_purchase_police_boat(state, options, player))
#     set_rule(world.get_location(LocationName.commissionergordon_unlocked, player),
#              lambda state: can_purchase_commissioner(state, options, player))
#     set_rule(world.get_location(LocationName.hammertruck_unlocked, player),
#              lambda state: can_purchase_hammer_truck(state, options, player))
#     set_rule(world.get_location(LocationName.policehelicopter_unlocked, player),
#              lambda state: can_purchase_police_heli(state, options, player))
#     set_rule(world.get_location(LocationName.goonhelicopter_unlocked, player),
#              lambda state: can_purchase_goon_heli(state, options, player))
#     set_rule(world.get_location(LocationName.garbagetruck_unlocked, player),
#              lambda state: can_purchase_garbage_truck(state, options, player))
#     set_rule(world.get_location(LocationName.policemarksman_unlocked, player),
#              lambda state: can_purchase_police_marksman(state, options, player))
#     set_rule(world.get_location(LocationName.jokertropical_unlocked, player),
#              lambda state: can_purchase_joker_tropic(state, options, player))
#     set_rule(world.get_location(LocationName.hush_unlocked, player),
#              lambda state: can_purchase_hush(state, options, player))
#     set_rule(world.get_location(LocationName.rasalghul_unlocked, player),
#              lambda state: can_purchase_ras(state, options, player))
#
#     set_rule(world.get_location(LocationName.silhouettes, player),
#              lambda state: can_purchase_silhouettes(state, options, player))
#     set_rule(world.get_location(LocationName.beepbeep, player),
#              lambda state: can_purchase_beepbeep(state, options, player))
#     set_rule(world.get_location(LocationName.icerink, player),
#              lambda state: can_purchase_ice_rink(state, options, player))
#     set_rule(world.get_location(LocationName.disguise, player),
#              lambda state: can_purchase_disguise(state, options, player))
#     set_rule(world.get_location(LocationName.extratoggle, player),
#              lambda state: can_purchase_extra_toggle(state, options, player))
#     set_rule(world.get_location(LocationName.scorex2, player),
#              lambda state: can_purchase_scorex2(state, options, player))
#     set_rule(world.get_location(LocationName.scorex4, player),
#              lambda state: can_purchase_scorex4(state, options, player))
#     set_rule(world.get_location(LocationName.scorex6, player),
#              lambda state: can_purchase_scorex6(state, options, player))
#     set_rule(world.get_location(LocationName.scorex8, player),
#              lambda state: can_purchase_scorex8(state, options, player))
#     set_rule(world.get_location(LocationName.scorex10, player),
#              lambda state: can_purchase_scorex10(state, options, player))
#     set_rule(world.get_location(LocationName.studmagnet, player),
#              lambda state: can_purchase_stud_magnet(state, options, player))
#     set_rule(world.get_location(LocationName.charstuds, player),
#              lambda state: can_purchase_char_studs(state, options, player))
#     set_rule(world.get_location(LocationName.minikitdetect, player),
#              lambda state: can_purchase_minikit_detect(state, options, player))
#     set_rule(world.get_location(LocationName.pwrbrickdetect, player),
#              lambda state: can_purchase_powerbrick_detect(state, options, player))
#     set_rule(world.get_location(LocationName.alwaysscore, player),
#              lambda state: can_purchase_always_score(state, options, player))
#     set_rule(world.get_location(LocationName.fastbuild, player),
#              lambda state: can_purchase_fast_build(state, options, player))
#     set_rule(world.get_location(LocationName.immunefreeze, player),
#              lambda state: can_purchase_immune_freeze(state, options, player))
#     set_rule(world.get_location(LocationName.regenhearts, player),
#              lambda state: can_purchase_regen_hearts(state, options, player))
#     set_rule(world.get_location(LocationName.extrahearts, player),
#              lambda state: can_purchase_extra_hearts(state, options, player))
#     set_rule(world.get_location(LocationName.invincibility, player),
#              lambda state: can_purchase_invincibility(state, options, player))
#     set_rule(world.get_location(LocationName.fastgrapple, player),
#              lambda state: can_purchase_fast_grapple(state, options, player))
#     set_rule(world.get_location(LocationName.fastbatarang, player),
#              lambda state: can_purchase_fast_batarang(state, options, player))
#     set_rule(world.get_location(LocationName.moretargets, player),
#              lambda state: can_purchase_more_targets(state, options, player))
#     set_rule(world.get_location(LocationName.flamingbata, player),
#              lambda state: can_purchase_flaming_bat(state, options, player))
#     set_rule(world.get_location(LocationName.slam, player),
#              lambda state: can_purchase_slam(state, options, player))
#     set_rule(world.get_location(LocationName.moredet, player),
#              lambda state: can_purchase_more_det(state, options, player))
#     set_rule(world.get_location(LocationName.armorplating, player),
#              lambda state: can_purchase_armor_plating(state, options, player))
#     set_rule(world.get_location(LocationName.sonicpain, player),
#              lambda state: can_purchase_sonic_pain(state, options, player))
#     set_rule(world.get_location(LocationName.areaeffect, player),
#              lambda state: can_purchase_area_effect(state, options, player))
#     set_rule(world.get_location(LocationName.bats, player),
#              lambda state: can_purchase_bats(state, options, player))
#     set_rule(world.get_location(LocationName.freezebatarang, player),
#              lambda state: can_purchase_freeze_bat(state, options, player))
#     set_rule(world.get_location(LocationName.decoy, player),
#              lambda state: can_purchase_decoy(state, options, player))
#     set_rule(world.get_location(LocationName.fastwalk, player),
#              lambda state: can_purchase_fast_walk(state, options, player))
#     set_rule(world.get_location(LocationName.fasterpieces, player),
#              lambda state: can_purchase_faster_pieces(state, options, player))
#     set_rule(world.get_location(LocationName.piecedetect, player),
#              lambda state: can_purchase_piece_detect(state, options, player))
#
#
# def set_token_rules(world: MultiWorld, options: LB1Options, player: int):
#     set_rule(world.get_location(LocationName.riddlergoon_collected, player),
#              lambda state: can_beat_ycbob(state, options, player))
#     set_rule(world.get_location(LocationName.riddlerhenchman_collected, player),
#              lambda state: can_beat_ycbob(state, options, player))
#     set_rule(world.get_location(LocationName.freezegirl_collected, player),
#              lambda state: can_beat_air(state, options, player))
#     # TFC can be completed in story - police car, bike, van, joker van don't require anything besides region logic
#     set_rule(world.get_location(LocationName.poisonivygoon_collected, player),
#              lambda state: can_beat_apa(state, player))
#     set_rule(world.get_location(LocationName.fishmonger_collected, player),
#              lambda state: can_beat_tsga(state, options, player))
#     set_rule(world.get_location(LocationName.penguingoon_collected, player),
#              lambda state: can_beat_tsga(state, options, player))
#     set_rule(world.get_location(LocationName.penguinhenchman_collected, player),
#              lambda state: can_beat_tsga(state, options, player))
#     # BBB can be completed in story - robin sub, penguin goon sub, harbour helicopter don't require anything besides
#     # region logic
#     set_rule(world.get_location(LocationName.zoosweeper_collected, player),
#              lambda state: can_beat_zc(state, options, player))
#     set_rule(world.get_location(LocationName.manbat_collected, player),
#              lambda state: can_beat_pl(state, options, player))
#     set_rule(world.get_location(LocationName.yeti_collected, player),
#              lambda state: can_beat_pl(state, options, player))
#     set_rule(world.get_location(LocationName.penguinminion_collected, player),
#              lambda state: can_beat_pl(state, options, player))
#     set_rule(world.get_location(LocationName.madhatter_collected, player),
#              lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.jokergoon_collected, player),
#              lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.jokerhenchman_collected, player),
#              lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.steamboat_collected, player),
#              lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.glider_collected, player),
#              lambda state: can_beat_jht(state, options, player))
#     set_rule(world.get_location(LocationName.clowngoon_collected, player),
#              lambda state: can_beat_lfabt(state, options, player))
#     # FOTB can be completed in story - private jet doesn't require anything besides region logic
#     set_rule(world.get_location(LocationName.brucewayne_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.alfred_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.batgirl_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.nightwing_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.policeofficer_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.militarypoliceman_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.securityguard_collected, player),
#              lambda state: can_complete_any_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.battank_collected, player),
#              lambda state: can_complete_all_hero_episode(state, options, player))
#     set_rule(world.get_location(LocationName.hush_collected, player),
#              lambda state: state.has("UNIQUE_HOSTAGES", player, options.hush_purchase_requirements.value))
#     set_rule(world.get_location(LocationName.rasalghul_collected, player),
#              lambda state: state.has("UNIQUE_MINIKITS", player, options.ras_purchase_requirements.value))
#     # All villain levels can be completed in story - no additional logic needed besides region


def set_rules(world):
    set_entrance_rules(world)
    # set_char_rules(world, options, player)
    # # Hard char Rules
    # set_suit_rules(world, options, player)
    if world.options.minikit_sanity == 1:
        set_minikit_rules(world)
    set_host_rules(world)
    set_level_beaten_rules(world)
    # set_shop_rules(world, options, player)
    if world.options.EndGoal == EndGoal.option_levels_beaten:
        set_event_rules(world)
    set_win_con(world)


def set_event_rules(world):
    for (name, data) in event_location_table.items():
        event: Location = world.get_location(name)
        level_beaten_name = name.removesuffix(" Event")
        world.set_rule(event, world.get_location(level_beaten_name).access_rule)

    if world.options.EndGoal == EndGoal.option_levels_beaten:
        world.set_rule(world.get_location("All Required Levels Beaten"),
                       Has("Level Beaten", world.options.levels_to_win.value))


def set_win_con(world):
    if world.options.EndGoal == EndGoal.option_levels_beaten:
        world.set_completion_rule(Has("All Required Levels Beaten"))
