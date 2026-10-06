from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from BaseClasses import Location
from Options import Option
from rule_builder.options import OptionFilter, Operator
from rule_builder.rules import Rule, Has, HasAll, HasFromListUnique, True_, Or, CanReachLocation

if TYPE_CHECKING:
    from . import LB1World

from .Locations import all_location_table, event_location_table
from .Names import LocationName, ItemName, RegionName
from .Options import EndGoal, HardPurchases, SimplifiedEpisodeCharacters

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
                                     itm.biplane_unlocked,
                                     itm.goonhelicopter_unlocked, itm.riddlerjet_unlocked, itm.glider_unlocked, count=2)

air_has_cable = (Has(itm.batcopter_unlocked) | Has(itm.harbourhelicopter_unlocked) | Has(itm.policehelicopter_unlocked)
                 | Has(itm.jokerhelicopter_unlocked) | Has(itm.goonhelicopter_unlocked))

air_can_cross_toxic = (Has(itm.harbourhelicopter_unlocked) | Has(itm.policehelicopter_unlocked) |
                       Has(itm.jokerhelicopter_unlocked) | Has(itm.biplane_unlocked) |
                       Has(itm.goonhelicopter_unlocked))

has_high_multi = (Has(itm.scorex6) | Has(itm.scorex8) | Has(itm.scorex10) |
                  HasAll(itm.scorex2, itm.scorex4))

has_low_multi = (Has(itm.scorex2) | Has(itm.scorex4))

# You Can Bank on Batman Logic
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
can_get_ycbob_rb = char_can_techno

# An Icy Reception Logic
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
can_get_air_rb = char_is_strong

# Two Face Chase Logic
can_access_tfc_free = auto_has_cable
can_access_tfc = Has(itm.tfc_lvl) & has_two_auto
can_get_tfc_min5 = Has(itm.jokervan_unlocked)
can_get_tfc_min6 = Has(itm.hammertruck_unlocked)
can_get_tfc_min10 = auto_can_explode

# A Poisonous Appointment Logic
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
can_get_apa_rb = char_can_explode & char_is_joker & Has(itm.heatprotectsuit)

# The Face Off Logic
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
can_get_tfo_rb = char_can_cross_toxic

# There She Goes Again Logic
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
can_get_tsga_rb = Has(itm.sonicsuit)

# Batboat Battle Logic
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

# Under The City Logic
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

# Zoo's Company Logic
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
can_get_zc_rb = char_can_double_jump & char_can_sink

# Penguin's Lair Logic
can_access_pl_free = char_can_glide & char_can_sink
can_beat_pl = char_can_glide & char_can_sink
can_get_pl_min1 = Has(itm.sonicsuit)
can_get_pl_min2 = Has(itm.mrfreeze_unlocked) & char_can_explode
can_get_pl_min3 = char_can_glide & char_can_double_jump
can_get_pl_min5 = Has(itm.glidesuit) & char_can_sink
can_get_pl_min7 = char_can_double_jump
can_get_pl_min8 = char_can_cross_toxic & Has(itm.penguin_unlocked)
can_get_pl_min10 = HasAll(itm.heatprotectsuit, itm.sonicsuit)
can_get_pl_rb = Has(itm.sonicsuit)

# Joker's Home Turf Logic
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

# Little Fun at the Big Top Logic
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

# Flight of the Bat Logic
can_access_fotb_free = air_has_cable
can_access_fotb = Has(itm.fotb_lvl) & has_two_aircraft & Has(itm.batwing_unlocked)
can_get_fotb_min7 = air_can_cross_toxic
can_get_fotb_min9 = air_can_cross_toxic
can_get_fotb_rb = air_can_cross_toxic

# In the Dark Night Logic
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
can_get_itdn_rb = char_can_glide & Has(itm.heatprotectsuit)

# To the Top of the Tower Logic
can_access_tttot_free = Has(itm.magsuit)
can_beat_tttot = Has(itm.magsuit) & char_can_glide
can_get_tttot_min1 = char_can_explode
can_get_tttot_min3 = Has(itm.sonicsuit)
can_get_tttot_min4 = Has(itm.attractsuit)
can_get_tttot_min5 = char_can_long_jump
can_get_tttot_min6 = char_is_joker
can_get_tttot_min9 = char_can_glide & char_can_double_jump
can_get_tttot_min10 = can_beat_tttot & char_can_explode
can_get_tttot_rb = char_is_strong

# The Riddler Makes A Withdrawal Logic
can_leave_trmaw_garage = char_is_strong & char_can_hypno
can_access_trmaw_free = can_leave_trmaw_garage & (char_can_double_jump | char_can_explode)
can_get_trmaw_min1 = char_is_strong
can_get_trmaw_min2 = char_can_double_jump & can_leave_trmaw_garage
can_get_trmaw_min3 = char_can_double_jump & char_can_hypno
can_get_trmaw_min4 = char_can_explode
can_get_trmaw_min6 = Has(itm.sonicsuit) & (char_can_explode | char_can_double_jump)
can_get_trmaw_min7 = char_can_double_jump
can_get_trmaw_min9 = Has(itm.sonicsuit)
can_get_trmaw_host = Has(itm.sonicsuit)
can_get_trmaw_rb = Has(itm.magsuit)

# On The Rocks Logic
can_access_otr = char_is_strong
can_access_otr_free = Has(itm.mrfreeze_unlocked) & char_can_hypno
can_get_otr_min2 = Has(itm.sonicsuit) & char_can_hypno
can_get_otr_min4 = Has(itm.mrfreeze_unlocked) & char_can_explode
can_get_otr_min5 = HasAll(itm.mrfreeze_unlocked, itm.magsuit)
can_get_otr_min6 = Has(itm.mrfreeze_unlocked)
can_get_otr_min7 = Has(itm.attractsuit)
can_get_otr_min8 = char_can_explode
can_get_otr_min9 = char_can_glide & Has(itm.magsuit)
can_get_otr_host = char_can_explode & Has(itm.mrfreeze_unlocked)
can_get_otr_rb = char_can_explode & Has(itm.mrfreeze_unlocked)

# Green Fingers Logic
can_access_gf_free = char_can_cross_toxic & char_can_hypno
can_beat_gf = Has(itm.poisonivy_unlocked)
can_get_gf_min1 = char_can_techno
can_get_gf_min2 = char_can_explode & char_can_double_jump
can_get_gf_min4 = char_can_explode
can_get_gf_min5 = char_can_sink & Has(itm.sonicsuit)
can_get_gf_min6 = HasAll(itm.magsuit, itm.sonicsuit)
can_get_gf_min7 = char_can_explode & char_is_strong & Has(itm.magsuit)
can_get_gf_min8 = Has(itm.heatprotectsuit)
can_get_gf_min9 = char_can_sink & Has(itm.sonicsuit)
can_get_gf_min10 = char_can_explode
can_get_gf_host = char_can_explode & Has(itm.poisonivy_unlocked)
can_get_gf_rb = char_can_explode & char_can_techno & HasAll(itm.attractsuit, itm.poisonivy_unlocked)

# An Enterprising Threat Logic
can_access_aet_free = char_can_hypno & char_can_cross_toxic
can_get_aet_min1 = Has(itm.sonicsuit) & char_can_double_jump
can_get_aet_min2 = Has(itm.sonicsuit) & char_can_techno
can_get_aet_min3 = char_can_explode
can_get_aet_min4 = Has(itm.sonicsuit)
can_get_aet_min5 = char_can_explode & char_can_techno
can_get_aet_min7 = char_can_double_jump
can_get_aet_min8 = Has(itm.sonicsuit)
can_get_aet_min9 = Has(itm.heatprotectsuit)
can_get_aet_host = Has(itm.sonicsuit)
can_get_aet_rb = char_is_joker & char_can_explode & HasAll(itm.attractsuit, itm.heatprotectsuit, itm.sonicsuit)

# Breaking Blocks Logic
can_access_bb_free = char_can_hypno
can_beat_bb = char_can_cross_toxic
can_get_bb_min2 = char_can_double_jump
can_get_bb_min4 = HasAll(itm.sonicsuit, itm.attractsuit, itm.magsuit)
can_get_bb_min5 = char_is_strong
can_get_bb_min6 = char_can_explode
can_get_bb_min7 = char_is_joker & char_can_double_jump
can_get_bb_min8 = char_can_explode & char_can_cross_toxic
can_get_bb_min9 = HasAll(itm.sonicsuit, itm.magsuit) & char_can_cross_toxic
can_get_bb_min10 = char_can_explode & char_can_cross_toxic
can_get_bb_host = Has(itm.sonicsuit) & char_is_strong
can_get_bb_rb = char_can_explode

# Rockin The Dock Logic
can_access_rtd = char_is_strong & char_can_explode & Has(itm.rtd_lvl)
can_access_rtd_free = char_can_cross_toxic
can_get_rtd_min1 = char_can_double_jump & Has(itm.sonicsuit)
can_get_rtd_min2 = char_can_double_jump
can_get_rtd_min5 = Has(itm.poisonivy_unlocked)
can_get_rtd_min7 = char_is_joker & char_can_techno
can_get_rtd_min9 = char_is_female & Has(itm.attractsuit)
can_get_rtd_host = Has(itm.sonicsuit)
can_get_rtd_rb = char_is_female & char_is_strong & Has(itm.penguin_unlocked)

# Stealing The Show Logic
can_access_sts_free = char_can_glide & char_is_female
can_beat_sts = Has(itm.penguin_unlocked)
can_get_sts_min1 = char_is_strong & Has(itm.magsuit)
can_get_sts_min2 = char_can_glide
can_get_sts_min3 = char_can_glide & Has(itm.poisonivy_unlocked)
can_get_sts_min6 = Has(itm.magsuit)
can_get_sts_min7 = Has(itm.sonicsuit) & char_is_strong
can_get_sts_min9 = HasAll(itm.sonicsuit, itm.penguin_unlocked)
can_get_sts_min10 = char_is_strong = Has(itm.penguin_unlocked)
can_get_sts_host = Has(itm.magsuit) & char_is_strong
can_get_sts_rb = (HasAll(itm.attractsuit, itm.penguin_unlocked) & char_can_techno &
                  char_can_explode)

# Harbouring A Grudge Logic
can_access_hag = has_two_watercraft & water_has_torpedo & Has(itm.hag_lvl)
can_get_hag_min3 = Has(itm.batboat_unlocked)
can_get_hag_min7 = water_can_cross_toxic
can_get_hag_min8 = Has(itm.batboat_unlocked)
can_get_hag_min10 = Has(itm.robinswatercraft_unlocked)
can_get_hag_rb = Has(itm.robinswatercraft_unlocked)

# A Daring Rescue Logic
can_access_adr_free = char_is_strong & char_can_cross_toxic & (char_can_double_jump | char_can_glide)
can_get_adr_min1 = char_can_explode & char_can_cross_toxic
can_get_adr_min2 = char_is_joker
can_get_adr_min3 = Has(itm.heatprotectsuit)
can_get_adr_min5 = HasAll(itm.attractsuit, itm.penguin_unlocked)
can_get_adr_min6 = char_can_hypno & HasAll(itm.mrfreeze_unlocked, itm.penguin_unlocked)
can_get_adr_min7 = Has(itm.sonicsuit)
can_get_adr_min9 = HasAll(itm.magsuit, itm.penguin_unlocked)
can_get_adr_host = char_is_joker
can_get_adr_rb = char_can_techno & HasAll(itm.penguin_unlocked, itm.sonicsuit)

# Arctic World Logic
can_access_aw_free = char_can_double_jump & Has(itm.penguin_unlocked)
can_beat_aw = char_is_female
can_get_aw_min1 = char_can_sink
can_get_aw_min2 = HasAll(itm.sonicsuit, itm.magsuit) & char_is_joker & char_is_strong & char_can_double_jump
can_get_aw_min3 = Has(itm.sonicsuit) & char_can_double_jump
can_get_aw_min4 = char_is_strong & char_is_female & char_can_double_jump & char_can_explode
can_get_aw_min5 = Has(itm.sonicsuit)
can_get_aw_min6 = char_is_strong & char_can_cross_toxic
can_get_aw_min7 = char_is_female
can_get_aw_min8 = char_can_explode & char_is_female
can_get_aw_min9 = char_can_sink & char_is_female
can_get_aw_min10 = Has(itm.mrfreeze_unlocked) & char_is_female
can_get_aw_host = char_can_cross_toxic
can_get_aw_rb = char_can_cross_toxic & Has(itm.attractsuit)

# A Surprise for the Commissioner Logic
can_access_asftc_free = char_can_double_jump
can_beat_asftc = char_is_joker
can_get_asftc_min1 = char_is_strong
can_get_asftc_min2 = Has(itm.sonicsuit)
can_get_asftc_min3 = Has(itm.mrfreeze_unlocked) & char_is_joker
can_get_asftc_min4 = char_can_explode
can_get_asftc_min5 = Has(itm.magsuit)
can_get_asftc_min6 = Has(itm.magsuit) | char_is_joker
can_get_asftc_min7 = Has(itm.magsuit) & char_can_explode
can_get_asftc_min8 = char_can_sink & char_is_joker
can_get_asftc_min9 = Has(itm.attractsuit) & char_is_joker & char_can_techno
can_get_asftc_min10 = char_is_joker
can_get_asftc_host = char_can_explode
can_get_asftc_rb = char_can_glide & char_can_explode & char_is_joker

# Biplane Blast Logic
can_access_bbpl = air_has_cable & Has(itm.bbpl_lvl)
can_access_bbpl_free = Has(itm.biplane_unlocked)
can_get_bbpl_min1 = Has(itm.batwing_unlocked)
can_get_bbpl_min3 = Has(itm.batwing_unlocked)
can_get_bbpl_min8 = Has(itm.batwing_unlocked)
can_get_bbpl_min9 = Has(itm.batwing_unlocked)
can_get_bbpl_min10 = Has(itm.batwing_unlocked)

# The Joker's Masterpiece Logic
can_access_tjm_free = char_is_joker & char_can_hypno
can_get_tjm_min3 = char_can_double_jump
can_get_tjm_min5 = Has(itm.sonicsuit)
can_get_tjm_min6 = char_is_strong
can_get_tjm_min7 = HasAll(itm.sonicsuit, itm.heatprotectsuit) & char_can_explode
can_get_tjm_min8 = char_can_double_jump
can_get_tjm_min9 = char_can_double_jump
can_get_tjm_host = char_is_joker & char_can_explode & Has(itm.heatprotectsuit)
can_get_tjm_rb = char_is_joker & char_can_explode & Has(itm.heatprotectsuit)

# The Lure of the Night Logic
can_access_tlotn_free = char_is_joker
can_beat_tlotn = char_can_long_jump
can_get_tlotn_min1 = char_can_hypno & char_can_explode
can_get_tlotn_min2 = char_can_double_jump & char_can_explode
can_get_tlotn_min3 = char_can_double_jump
can_get_tlotn_min4 = char_is_strong & char_can_long_jump
can_get_tlotn_min5 = Has(itm.magsuit) & char_can_long_jump
can_get_tlotn_min6 = char_can_long_jump
can_get_tlotn_min7 = char_can_long_jump
can_get_tlotn_min8 = char_can_long_jump
can_get_tlotn_min9 = char_can_explode & char_can_long_jump
can_get_tlotn_min10 = char_can_sink & Has(itm.sonicsuit) & char_can_long_jump
can_get_tlotn_host = char_can_double_jump
can_get_tlotn_rb = HasAll(itm.poisonivy_unlocked, itm.attractsuit) & char_can_double_jump

# Dying of Laugher Logic
can_access_dol_free = char_is_joker & char_can_double_jump
can_get_dol_min1 = Has(itm.poisonivy_unlocked)
can_get_dol_min2 = char_can_double_jump & Has(itm.sonicsuit)
can_get_dol_min3 = char_is_strong
can_get_dol_min4 = char_can_explode
can_get_dol_min5 = Has(itm.magsuit)
can_get_dol_min7 = char_can_glide
can_get_dol_min8 = Has(itm.mrfreeze_unlocked)
can_get_dol_min10 = char_can_explode
can_get_dol_host = char_can_glide

# Suit Logic
can_unlock_heat_suit = CanReachLocation(locn.apa_beat)

glide_suit_air = CanReachLocation(locn.air_beat)
glide_suit_tfo = Has(itm.tfo_lvl)
glide_suit_tsga = HasAll(itm.tsga_lvl, itm.magsuit)
glide_suit_utc = CanReachLocation(locn.utc_beat)
glide_suit_pl = Has(itm.pl_lvl)
glide_suit_jht = HasAll(itm.jht_lvl, itm.attractsuit)
glide_suit_tttot = CanReachLocation(locn.tttot_beat)
can_unlock_glide_suit = Has(itm.glidesuit) & (glide_suit_air | glide_suit_tfo | glide_suit_tsga | glide_suit_utc |
                                              glide_suit_pl | glide_suit_jht | glide_suit_tttot)

demo_suit_ycbob = Has(itm.ycbob_lvl)
demo_suit_tsga = CanReachLocation(locn.tsga_beat)
demo_suit_utc = HasAll(itm.utc_lvl, itm.magsuit)
demo_suit_zc = CanReachLocation(locn.zc_beat)
demo_suit_lfabt = Has(itm.lfabt_lvl)
demo_suit_itdn = Has(itm.itdn_lvl)
demo_suit_tttot = Has(itm.tttot_lvl)
can_unlock_demo_suit = Has(itm.demosuit) & (demo_suit_ycbob | demo_suit_tsga | demo_suit_utc | demo_suit_zc |
                                            demo_suit_lfabt | demo_suit_itdn | demo_suit_tttot)

mag_suit_air = Has(itm.air_lvl)
mag_suit_tfo = Has(itm.tfo_lvl) & char_can_glide
mag_suit_tsga = Has(itm.tsga_lvl)
mag_suit_utc = Has(itm.utc_lvl)
mag_suit_zc = Has(itm.zc_lvl)
mag_suit_jht = CanReachLocation(locn.jht_beat)
mag_suit_lfabt = HasAll(itm.lfabt_lvl, itm.sonicsuit) & char_can_explode
mag_suit_itdn = CanReachLocation(locn.itdn_beat)
mag_suit_tttot = Has(itm.tttot_lvl) & char_can_explode
can_unlock_mag_suit = Has(itm.magsuit) & (mag_suit_air | mag_suit_tfo | mag_suit_tsga | mag_suit_utc | mag_suit_zc |
                                          mag_suit_jht | mag_suit_lfabt | mag_suit_itdn | mag_suit_tttot)

sonic_suit_apa = Has(itm.apa_lvl)
sonic_suit_zc = Has(itm.zc_lvl) & (char_can_explode | char_can_glide)
sonic_suit_lfabt = Has(itm.lfabt_lvl) & char_can_explode
can_unlock_sonic_suit = Has(itm.sonicsuit) & (sonic_suit_apa | sonic_suit_zc | sonic_suit_lfabt)

water_suit_utc = Has(itm.utc_lvl) & char_can_explode
water_suit_zc = Has(itm.zc_lvl) & char_can_glide
can_unlock_water_suit = Has(itm.watersuit) & (water_suit_utc | water_suit_zc)

tech_suit_ycbob = Has(itm.ycbob_lvl) & char_can_explode
tech_suit_tsga = HasAll(itm.tsga_lvl, itm.magsuit) & char_can_glide
tech_suit_zc = Has(itm.zc_lvl) & (char_can_explode | (Has(itm.magsuit) & char_can_glide))
tech_suit_itdn = Has(itm.itdn_lvl) & char_can_explode
can_unlock_tech_suit = Has(itm.techsuit) & (tech_suit_ycbob | tech_suit_tsga | tech_suit_zc | tech_suit_itdn)

attract_suit_apa = HasAll(itm.apa_lvl, itm.sonicsuit)
attract_suit_tfo = HasAll(itm.tfo_lvl, itm.magsuit) & char_can_glide
attract_suit_jht = Has(itm.jht_lvl)
attract_suit_lfabt = HasAll(itm.lfabt_lvl, itm.magsuit, itm.sonicsuit) & char_can_explode
can_unlock_attract_suit = Has(itm.attractsuit) & (attract_suit_apa | attract_suit_tfo | attract_suit_jht |
                                                  attract_suit_lfabt)


# Shop Logic
def from_option(option: type[Option], value: Any, operator: Operator = "eq") -> Rule:
    return True_(options=[OptionFilter(option, value, operator)])


def has_needed_multi(location_name: str) -> Rule:
    return Or(from_option(HardPurchases, 1), HasMultiplier(location_name))


@dataclasses.dataclass
class HasMultiplier(Rule, game="Lego Batman The Video Game"):
    location_name: str

    @override
    def _instantiate(self, world: "LB1World") -> Rule.Resolved:
        # Look up the price
        data = all_location_table[self.location_name]
        cheaper_shop_amount = world.options.cheaper_shops
        price = data.price / cheaper_shop_amount

        # Get Multiplier Requirements
        low = world.options.low_multiplier_price_minimum
        high = world.options.high_multiplier_price_minimum

        # Compare and Return
        if price < low:
            return True_().resolve(world)
        elif price < high:
            return has_low_multi.resolve(world)
        else:
            return has_high_multi.resolve(world)


can_purchase_silhouettes = has_needed_multi(locn.silhouettes)
can_purchase_beepbeep = has_needed_multi(locn.beepbeep)
can_purchase_icerink = has_needed_multi(locn.icerink)
can_purchase_disguise = has_needed_multi(locn.disguise)
can_purchase_extratoggle = has_needed_multi(locn.extratoggle)
can_purchase_scorex2 = has_needed_multi(locn.scorex2) & can_get_trmaw_rb & CanReachLocation(locn.trmaw_beat)
can_purchase_scorex4 = has_needed_multi(locn.scorex4) & can_get_otr_rb & CanReachLocation(locn.otr_beat)
can_purchase_scorex6 = has_needed_multi(locn.scorex6) & can_get_gf_rb & CanReachLocation(locn.gf_beat)
can_purchase_scorex8 = has_needed_multi(locn.scorex8) & can_get_aet_rb & CanReachLocation(locn.aet_beat)
can_purchase_scorex10 = has_needed_multi(locn.scorex10) & can_get_bb_rb & CanReachLocation(locn.bb_beat)
can_purchase_stud_magnet = has_needed_multi(locn.studmagnet) & can_get_rtd_rb & CanReachLocation(locn.rtd_beat)
can_purchase_char_studs = has_needed_multi(locn.charstuds) & can_get_sts_rb & CanReachLocation(locn.sts_beat)
can_purchase_minikit_detect = has_needed_multi(locn.minidetect) & can_get_hag_rb & CanReachLocation(locn.hag_beat)
can_purchase_pwr_brick_detect = has_needed_multi(locn.powerdetect) & can_get_adr_rb & CanReachLocation(locn.adr_beat)
can_purchase_always_multi = has_needed_multi(locn.alwaysscore) & can_get_aw_rb & CanReachLocation(locn.aw_beat)
can_purchase_fast_build = has_needed_multi(locn.fastbuild) & can_get_asftc_rb & CanReachLocation(locn.asftc_beat)
can_purchase_freeze_immune = has_needed_multi(locn.immunefreeze) & CanReachLocation(locn.bbpl_beat)
can_purchase_regen_hearts = has_needed_multi(locn.regenhearts) & can_get_tjm_rb & CanReachLocation(locn.tjm_beat)
can_purchase_extra_hearts = has_needed_multi(locn.extrahearts) & can_get_tlotn_rb & CanReachLocation(locn.tlotn_beat)
can_purchase_invincibility = has_needed_multi(locn.invincibility) & CanReachLocation(locn.dol_beat)
can_purchase_fast_grapple = has_needed_multi(locn.fastgrap) & can_get_ycbob_rb & CanReachLocation(locn.ycbob_beat)
can_purchase_fast_bat = has_needed_multi(locn.fastbat) & can_get_air_rb & CanReachLocation(locn.air_beat)
can_purchase_more_bat = has_needed_multi(locn.moretargets) & CanReachLocation(locn.tfc_beat)
can_purchase_flame_bat = has_needed_multi(locn.flamingbat) & can_get_apa_rb & CanReachLocation(locn.apa_beat)
can_purchase_slam = has_needed_multi(locn.slam) & can_get_tfo_rb & CanReachLocation(locn.tfo_beat)
can_purchase_more_det = has_needed_multi(locn.moredet) & can_get_tsga_rb & CanReachLocation(locn.tsga_beat)
can_purchase_armour_plat = has_needed_multi(locn.armourplating) & CanReachLocation(locn.bbb_beat)
can_purchase_sonic_pain = has_needed_multi(locn.sonicpain) & can_get_utc_rb & CanReachLocation(locn.utc_beat)
can_purchase_area_effect = has_needed_multi(locn.areaeffect) & can_get_zc_rb & CanReachLocation(locn.zc_beat)
can_purchase_bats = has_needed_multi(locn.bats) & can_get_pl_rb & CanReachLocation(locn.pl_beat)
can_purchase_freeze_bat = has_needed_multi(locn.freezebatarang) & can_get_jht_rb & CanReachLocation(locn.jht_beat)
can_purchase_decoy = has_needed_multi(locn.decoy) & can_get_lfabt_rb & CanReachLocation(locn.lfabt_beat)
can_purchase_fast_walk = has_needed_multi(locn.fastwalk) & can_get_fotb_rb & CanReachLocation(locn.fotb_beat)
can_purchase_faster_piece = has_needed_multi(locn.fasterpieces) & can_get_itdn_rb & CanReachLocation(locn.itdn_beat)
can_purchase_piece_detect = has_needed_multi(locn.piecedetect) & can_get_tttot_rb & CanReachLocation(locn.tttot_beat)

# Characters
can_complete_any_hero_level = (CanReachLocation(locn.ycbob_beat) | CanReachLocation(locn.air_beat) |
                               CanReachLocation(locn.tfc_beat) | CanReachLocation(locn.apa_beat) |
                               CanReachLocation(locn.tfo_beat) | CanReachLocation(locn.tsga_beat) |
                               CanReachLocation(locn.bbb_beat) | CanReachLocation(locn.utc_beat) |
                               CanReachLocation(locn.zc_beat) | CanReachLocation(locn.pl_beat) |
                               CanReachLocation(locn.jht_beat) | CanReachLocation(locn.lfabt_beat) |
                               CanReachLocation(locn.fotb_beat) | CanReachLocation(locn.itdn_beat) |
                               CanReachLocation(locn.tttot_beat))

can_complete_hero_episode_1 = (CanReachLocation(locn.ycbob_beat) & CanReachLocation(locn.air_beat) &
                               CanReachLocation(locn.tfc_beat) & CanReachLocation(locn.apa_beat) &
                               CanReachLocation(locn.tfo_beat))

can_complete_hero_episode_2 = (CanReachLocation(locn.tsga_beat) & CanReachLocation(locn.bbb_beat) &
                               CanReachLocation(locn.utc_beat) & CanReachLocation(locn.zc_beat) &
                               CanReachLocation(locn.pl_beat))

can_complete_hero_episode_3 = (CanReachLocation(locn.jht_beat) & CanReachLocation(locn.lfabt_beat) &
                               CanReachLocation(locn.fotb_beat) & CanReachLocation(locn.itdn_beat) &
                               CanReachLocation(locn.tttot_beat))

can_complete_any_hero_episode = can_complete_hero_episode_1 | can_complete_hero_episode_2 | can_complete_hero_episode_3
can_complete_all_hero_episodes = can_complete_hero_episode_1 & can_complete_hero_episode_2 & can_complete_hero_episode_3
can_complete_any_lvl_5 = (CanReachLocation(locn.tfo_beat) | CanReachLocation(locn.pl_beat) |
                          CanReachLocation(locn.tttot_beat))
can_complete_all_lvl_5 = (CanReachLocation(locn.tfo_beat) & CanReachLocation(locn.pl_beat) &
                          CanReachLocation(locn.tttot_beat))

episode_mode = from_option(SimplifiedEpisodeCharacters, 0)
lvl5_mode = from_option(SimplifiedEpisodeCharacters, 1)

can_unlock_batman = can_complete_any_hero_level
can_unlock_robin = can_complete_any_hero_level
can_unlock_bruce_wayne = has_needed_multi(locn.brucewayne_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_alfred = has_needed_multi(locn.alfred_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_batgirl = has_needed_multi(locn.batgirl_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_nightwing = has_needed_multi(locn.nightwing_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_commissioner = has_needed_multi(locn.commissionergordon_unlocked) & CanReachLocation(locn.asftc_beat)
can_unlock_police_officer = has_needed_multi(locn.policeofficer_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_fishmonger = has_needed_multi(locn.fishmonger_unlocked) & CanReachLocation(locn.tsga_beat)
can_unlock_military_poli = has_needed_multi(locn.militarypoliceman_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_security_guard = has_needed_multi(locn.securityguard_unlocked) & (
    (episode_mode & can_complete_any_hero_episode) | (lvl5_mode & can_complete_any_lvl_5))
can_unlock_swat = has_needed_multi(locn.swat_unlocked) & CanReachLocation(locn.bb_beat)
can_unlock_scientist = has_needed_multi(locn.scientist_unlocked) & CanReachLocation(locn.aet_beat)
can_unlock_sailor = has_needed_multi(locn.sailor_unlocked) & CanReachLocation(locn.rtd_beat)
can_unlock_police_marksman = has_needed_multi(locn.policemarksman_unlocked) & CanReachLocation(locn.dol_beat)
can_unlock_clayface = CanReachLocation(locn.trmaw_beat)
can_unlock_mrfreeze = CanReachLocation(locn.otr_beat)
can_unlock_poisonivy = CanReachLocation(locn.gf_beat)
can_unlock_two_face = CanReachLocation(locn.aet_beat) | CanReachLocation(locn.bb_beat)
can_unlock_riddler = (CanReachLocation(locn.trmaw_beat) | CanReachLocation(locn.otr_beat) |
                      CanReachLocation(locn.gf_beat) | CanReachLocation(locn.aet_beat) | CanReachLocation(locn.bb_beat))
can_unlock_bane = CanReachLocation(locn.rtd_beat)
can_unlock_catwomen = CanReachLocation(locn.sts_beat) | CanReachLocation(locn.aw_beat)
can_unlock_catwomen_classic = has_needed_multi(locn.catwomanclassic_unlocked) & CanReachLocation(locn.sts_beat)
can_unlock_killer_croc = CanReachLocation(locn.adr_beat)
can_unlock_manbat = has_needed_multi(locn.manbat_unlocked) & CanReachLocation(locn.pl_beat)
can_unlock_penguin = (CanReachLocation(locn.rtd_beat) | CanReachLocation(locn.sts_beat) |
                      CanReachLocation(locn.hag_beat) | CanReachLocation(locn.adr_beat) |
                      CanReachLocation(locn.aw_beat))
can_unlock_harley = CanReachLocation(locn.asftc_beat) | CanReachLocation(locn.dol_beat)
can_unlock_scarecrow = CanReachLocation(locn.tjm_beat)
can_unlock_killer_moth = CanReachLocation(locn.tlotn_beat)
can_unlock_mad_hat = has_needed_multi(locn.madhatter_unlocked) & CanReachLocation(locn.jht_beat)
can_unlock_joker = (CanReachLocation(locn.asftc_beat) | CanReachLocation(locn.bbpl_beat) |
                    CanReachLocation(locn.tjm_beat) | CanReachLocation(locn.tlotn_beat) |
                    CanReachLocation(locn.dol_beat))
can_unlock_joker_tropic = has_needed_multi(locn.jokertropical_unlocked) & CanReachLocation(locn.dol_beat)
can_unlock_poisonivy_goon = has_needed_multi(locn.poisonivygoon_unlocked) & CanReachLocation(locn.apa_beat)
can_unlock_zoosweeper = has_needed_multi(locn.zoosweeper_unlocked) & CanReachLocation(locn.zc_beat)
can_unlock_freeze_girl = has_needed_multi(locn.freezegirl_unlocked) & CanReachLocation(locn.air_beat)
can_unlock_yeti = has_needed_multi(locn.yeti_unlocked) & CanReachLocation(locn.pl_beat)
can_unlock_riddler_goon = has_needed_multi(locn.riddlergoon_unlocked) & CanReachLocation(locn.ycbob_beat)
can_unlock_riddler_henchman = has_needed_multi(locn.riddlerhenchman_unlocked) & CanReachLocation(locn.ycbob_beat)
can_unlock_penguin_goon = has_needed_multi(locn.penguingoon_unlocked) & CanReachLocation(locn.tsga_beat)
can_unlock_penguin_henchman = has_needed_multi(locn.penguinhenchman_unlocked) & CanReachLocation(locn.tsga_beat)
can_unlock_penguin_minion = has_needed_multi(locn.penguinminion_unlocked) & CanReachLocation(locn.pl_beat)
can_unlock_joker_goon = has_needed_multi(locn.jokergoon_unlocked) & CanReachLocation(locn.jht_beat)
can_unlock_joker_henchman = has_needed_multi(locn.jokerhenchman_unlocked) & CanReachLocation(locn.jht_beat)
can_unlock_clown = has_needed_multi(locn.clowngoon_unlocked) & CanReachLocation(locn.lfabt_beat)

can_unlock_batmobile = CanReachLocation(locn.tfc_beat)
can_unlock_batcycle = CanReachLocation(locn.tfc_beat)
can_unlock_police_car = has_needed_multi(locn.policecar_unlocked) & CanReachLocation(locn.tfc_beat)
can_unlock_police_bike = has_needed_multi(locn.policebike_unlocked) & CanReachLocation(locn.tfc_beat)
can_unlock_police_van = has_needed_multi(locn.policevan_unlocked) & CanReachLocation(locn.tfc_beat)
can_unlock_bat_tank = (has_needed_multi(locn.battank_unlocked) &
                       (episode_mode & can_complete_all_hero_episodes) | (lvl5_mode & can_complete_all_lvl_5))
can_unlock_cat_moto = has_needed_multi(locn.catmotorcycle_unlocked) & CanReachLocation(locn.sts_beat)
can_unlock_armoured_truck = has_needed_multi(locn.armouredtruck_unlocked) & CanReachLocation(locn.aet_beat)
can_unlock_freeze_kart = has_needed_multi(locn.freezekart_unlocked) & CanReachLocation(locn.otr_beat)
can_unlock_hammer_truck = has_needed_multi(locn.hammertruck_unlocked) & CanReachLocation(locn.asftc_beat)
can_unlock_joker_van = has_needed_multi(locn.jokervan_unlocked) & CanReachLocation(locn.tfc_beat)
can_unlock_garbage_truck = has_needed_multi(locn.garbagetruck_unlocked) & CanReachLocation(locn.tlotn_beat)

can_unlock_batboat = CanReachLocation(locn.bbb_beat)
can_unlock_robinswatercraft = CanReachLocation(locn.bbb_beat)
can_unlock_robinssub = has_needed_multi(locn.robinssubmarine_unlocked) & CanReachLocation(locn.bbb_beat)
can_unlock_police_water = has_needed_multi(locn.policewatercraft_unlocked) & CanReachLocation(locn.hag_beat)
can_unlock_police_boat = has_needed_multi(locn.policeboat_unlocked) & CanReachLocation(locn.hag_beat)
can_unlock_penguin_sub = CanReachLocation(locn.hag_beat)
can_unlock_swamp_rider = CanReachLocation(locn.hag_beat)
can_unlock_goon_sub = has_needed_multi(locn.penguinsubmarine_unlocked) & CanReachLocation(locn.bbb_beat)
can_unlock_iceberg = has_needed_multi(locn.iceberg_unlocked) & CanReachLocation(locn.otr_beat)
can_unlock_steam_boat = has_needed_multi(locn.steamboat_unlocked) & CanReachLocation(locn.jht_beat)

can_unlock_batwing = CanReachLocation(locn.fotb_beat)
can_unlock_batcopter = CanReachLocation(locn.fotb_beat)
can_unlock_harbour_heli = has_needed_multi(locn.harbourhelicopter_unlocked) & CanReachLocation(locn.bbb_beat)
can_unlock_police_heli = has_needed_multi(locn.policehelicopter_unlocked) & CanReachLocation(locn.bbpl_beat)
can_unlock_private_jet = has_needed_multi(locn.privatejet_unlocked) & CanReachLocation(locn.fotb_beat)
can_unlock_joker_heli = CanReachLocation(locn.bbpl_beat)
can_unlock_biplane = CanReachLocation(locn.bbpl_beat)
can_unlock_goon_heli = has_needed_multi(locn.goonhelicopter_unlocked) & CanReachLocation(locn.bbpl_beat)
can_unlock_riddler_jet = has_needed_multi(locn.riddlerjet_unlocked) & CanReachLocation(locn.bb_beat)
can_unlock_glider = has_needed_multi(locn.glider_unlocked) & CanReachLocation(locn.jht_beat)


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
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.otr), can_access_otr)
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.gf), Has(ItemName.gf_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aet), Has(ItemName.aet_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bb), Has(ItemName.bb_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.rtd), can_access_rtd)
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.sts), Has(ItemName.sts_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.hag), can_access_hag)
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.adr), Has(ItemName.adr_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aw), Has(ItemName.aw_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.asftc), Has(ItemName.asftc_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bbpl), Has(ItemName.bbpl_lvl))
    world.set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.tjm), can_access_bbpl)
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
    world.set_rule(world.get_entrance(RegionName.trmaw + " -> " + RegionName.trmawf), can_access_trmaw_free)
    world.set_rule(world.get_entrance(RegionName.otr + " -> " + RegionName.otrf), can_access_otr_free)
    world.set_rule(world.get_entrance(RegionName.gf + " -> " + RegionName.gff), can_access_gf_free)
    world.set_rule(world.get_entrance(RegionName.aet + " -> " + RegionName.aetf), can_access_aet_free)
    world.set_rule(world.get_entrance(RegionName.bb + " -> " + RegionName.bbf), can_access_bb_free)
    world.set_rule(world.get_entrance(RegionName.rtd + " -> " + RegionName.rtdf), can_access_rtd_free)
    world.set_rule(world.get_entrance(RegionName.sts + " -> " + RegionName.stsf), can_access_sts_free)
    world.set_rule(world.get_entrance(RegionName.adr + " -> " + RegionName.adrf), can_access_adr_free)
    world.set_rule(world.get_entrance(RegionName.aw + " -> " + RegionName.awf), can_access_aw_free)
    world.set_rule(world.get_entrance(RegionName.asftc + " -> " + RegionName.asftcf), can_access_asftc_free)
    world.set_rule(world.get_entrance(RegionName.bbpl + " -> " + RegionName.bbplf), can_access_bbpl_free)
    world.set_rule(world.get_entrance(RegionName.tjm + " -> " + RegionName.tjmf), can_access_tjm_free)
    world.set_rule(world.get_entrance(RegionName.tlotn + " -> " + RegionName.tlotnf), can_access_tlotn_free)
    world.set_rule(world.get_entrance(RegionName.dol + " -> " + RegionName.dolf), can_access_dol_free)


def set_char_rules(world):
    # Characters
    world.set_rule(world.get_location(LocationName.brucewayne_unlocked), can_unlock_bruce_wayne)
    world.set_rule(world.get_location(LocationName.alfred_unlocked), can_unlock_alfred)
    world.set_rule(world.get_location(LocationName.batgirl_unlocked), can_unlock_batgirl)
    world.set_rule(world.get_location(LocationName.nightwing_unlocked), can_unlock_nightwing)
    world.set_rule(world.get_location(LocationName.commissionergordon_unlocked), can_unlock_commissioner)
    world.set_rule(world.get_location(LocationName.policeofficer_unlocked), can_unlock_police_officer)
    world.set_rule(world.get_location(LocationName.fishmonger_unlocked), can_unlock_fishmonger)
    world.set_rule(world.get_location(LocationName.militarypoliceman_unlocked), can_unlock_military_poli)
    world.set_rule(world.get_location(LocationName.securityguard_unlocked), can_unlock_security_guard)
    world.set_rule(world.get_location(LocationName.swat_unlocked), can_unlock_swat)
    world.set_rule(world.get_location(LocationName.scientist_unlocked), can_unlock_scientist)
    world.set_rule(world.get_location(LocationName.sailor_unlocked), can_unlock_sailor)
    world.set_rule(world.get_location(LocationName.policemarksman_unlocked), can_unlock_police_marksman)
    world.set_rule(world.get_location(LocationName.clayface_unlocked), can_unlock_clayface)
    world.set_rule(world.get_location(LocationName.mrfreeze_unlocked), can_unlock_mrfreeze)
    world.set_rule(world.get_location(LocationName.poisonivy_unlocked), can_unlock_poisonivy)
    world.set_rule(world.get_location(LocationName.twoface_unlocked), can_unlock_two_face)
    world.set_rule(world.get_location(LocationName.riddler_unlocked), can_unlock_riddler)
    world.set_rule(world.get_location(LocationName.bane_unlocked), can_unlock_bane)
    world.set_rule(world.get_location(LocationName.catwoman_unlocked), can_unlock_catwomen)
    world.set_rule(world.get_location(LocationName.catwomanclassic_unlocked), can_unlock_catwomen_classic)
    world.set_rule(world.get_location(LocationName.killercroc_unlocked), can_unlock_killer_croc)
    world.set_rule(world.get_location(LocationName.manbat_unlocked), can_unlock_manbat)
    world.set_rule(world.get_location(LocationName.penguin_unlocked), can_unlock_penguin)
    world.set_rule(world.get_location(LocationName.harleyquinn_unlocked), can_unlock_harley)
    world.set_rule(world.get_location(LocationName.scarecrow_unlocked), can_unlock_scarecrow)
    world.set_rule(world.get_location(LocationName.killermoth_unlocked), can_unlock_killer_moth)
    world.set_rule(world.get_location(LocationName.madhatter_unlocked), can_unlock_mad_hat)
    world.set_rule(world.get_location(LocationName.joker_unlocked), can_unlock_joker)
    world.set_rule(world.get_location(LocationName.jokertropical_unlocked), can_unlock_joker_tropic)
    world.set_rule(world.get_location(LocationName.poisonivygoon_unlocked), can_unlock_poisonivy_goon)
    world.set_rule(world.get_location(LocationName.zoosweeper_unlocked), can_unlock_zoosweeper)
    world.set_rule(world.get_location(LocationName.freezegirl_unlocked), can_unlock_freeze_girl)
    world.set_rule(world.get_location(LocationName.yeti_unlocked), can_unlock_yeti)
    world.set_rule(world.get_location(LocationName.riddlergoon_unlocked), can_unlock_riddler_goon)
    world.set_rule(world.get_location(LocationName.riddlerhenchman_unlocked), can_unlock_riddler_henchman)
    world.set_rule(world.get_location(LocationName.penguingoon_unlocked), can_unlock_penguin_goon)
    world.set_rule(world.get_location(LocationName.penguinhenchman_unlocked), can_unlock_penguin_henchman)
    world.set_rule(world.get_location(LocationName.penguinminion_unlocked), can_unlock_penguin_minion)
    world.set_rule(world.get_location(LocationName.jokergoon_unlocked), can_unlock_joker_goon)
    world.set_rule(world.get_location(LocationName.jokerhenchman_unlocked), can_unlock_joker_henchman)
    world.set_rule(world.get_location(LocationName.clowngoon_unlocked), can_unlock_clown)
    # Auto
    world.set_rule(world.get_location(LocationName.batmobile_unlocked), can_unlock_batmobile)
    world.set_rule(world.get_location(LocationName.batcycle_unlocked), can_unlock_batcycle)
    world.set_rule(world.get_location(LocationName.policecar_unlocked), can_unlock_police_car)
    world.set_rule(world.get_location(LocationName.policebike_unlocked), can_unlock_police_bike)
    world.set_rule(world.get_location(LocationName.policevan_unlocked), can_unlock_police_van)
    world.set_rule(world.get_location(LocationName.battank_unlocked), can_unlock_bat_tank)
    world.set_rule(world.get_location(LocationName.catmotorcycle_unlocked), can_unlock_cat_moto)
    world.set_rule(world.get_location(LocationName.armouredtruck_unlocked), can_unlock_armoured_truck)
    world.set_rule(world.get_location(LocationName.freezekart_unlocked), can_unlock_freeze_kart)
    world.set_rule(world.get_location(LocationName.hammertruck_unlocked), can_unlock_hammer_truck)
    world.set_rule(world.get_location(LocationName.jokervan_unlocked), can_unlock_joker_van)
    world.set_rule(world.get_location(LocationName.garbagetruck_unlocked), can_unlock_garbage_truck)
    # Boat
    world.set_rule(world.get_location(LocationName.batboat_unlocked), can_unlock_batboat)
    world.set_rule(world.get_location(LocationName.robinswatercraft_unlocked), can_unlock_robinswatercraft)
    world.set_rule(world.get_location(LocationName.robinssubmarine_unlocked), can_unlock_robinssub)
    world.set_rule(world.get_location(LocationName.policewatercraft_unlocked), can_unlock_police_water)
    world.set_rule(world.get_location(LocationName.policeboat_unlocked), can_unlock_police_boat)
    world.set_rule(world.get_location(LocationName.penguingoonsub_unlocked), can_unlock_penguin_sub)
    world.set_rule(world.get_location(LocationName.swamprider_unlocked), can_unlock_swamp_rider)
    world.set_rule(world.get_location(LocationName.penguinsubmarine_unlocked), can_unlock_goon_sub)
    world.set_rule(world.get_location(LocationName.iceberg_unlocked), can_unlock_iceberg)
    world.set_rule(world.get_location(LocationName.steamboat_unlocked), can_unlock_steam_boat)
    # Air
    world.set_rule(world.get_location(LocationName.batwing_unlocked), can_unlock_batwing)
    world.set_rule(world.get_location(LocationName.batcopter_unlocked), can_unlock_batcopter)
    world.set_rule(world.get_location(LocationName.harbourhelicopter_unlocked), can_unlock_harbour_heli)
    world.set_rule(world.get_location(LocationName.policehelicopter_unlocked), can_unlock_police_heli)
    world.set_rule(world.get_location(LocationName.privatejet_unlocked), can_unlock_private_jet)
    world.set_rule(world.get_location(LocationName.jokerhelicopter_unlocked), can_unlock_joker_heli)
    world.set_rule(world.get_location(LocationName.scarecrowbiplane_unlocked), can_unlock_biplane)
    world.set_rule(world.get_location(LocationName.goonhelicopter_unlocked), can_unlock_goon_heli)
    world.set_rule(world.get_location(LocationName.riddlerjet_unlocked), can_unlock_riddler_jet)
    world.set_rule(world.get_location(LocationName.glider_unlocked), can_unlock_glider)


def set_hard_char_rules(world):
    world.set_rule(world.get_location(LocationName.hush_unlocked), has_needed_multi(locn.hush_unlocked) &
                   Has("UNIQUE_HOSTAGES", world.options.hush_purchase_requirements.value))
    hush_minikits = world.options.hush_purchase_requirements.value
    minikit_grouping = world.options.minikit_grouping.value
    required_count: int = hush_minikits // minikit_grouping
    if hush_minikits % minikit_grouping > 0:
        required_count += 1
    world.set_rule(world.get_location(LocationName.rasalghul_unlocked), has_needed_multi(locn.rasalghul_unlocked) &
                   Has("UNIQUE_MINIKITS", required_count))


def set_suit_rules(world):
    world.set_rule(world.get_location(LocationName.heatprotectsuit), can_unlock_heat_suit)
    world.set_rule(world.get_location(LocationName.glidesuit), can_unlock_glide_suit)
    world.set_rule(world.get_location(LocationName.demosuit), can_unlock_demo_suit)
    world.set_rule(world.get_location(LocationName.sonicsuit), can_unlock_sonic_suit)
    world.set_rule(world.get_location(LocationName.watersuit), can_unlock_water_suit)
    world.set_rule(world.get_location(LocationName.techsuit), can_unlock_tech_suit)
    world.set_rule(world.get_location(LocationName.magsuit), can_unlock_mag_suit)
    world.set_rule(world.get_location(LocationName.attractsuit), can_unlock_attract_suit)


def set_minikit_rules(world):
    # You Can Bank on Batman Logic
    world.set_rule(world.get_location(locn.ycbob_min3), can_get_ycbob_min3)
    world.set_rule(world.get_location(locn.ycbob_min4), can_get_ycbob_min4)
    world.set_rule(world.get_location(locn.ycbob_min5), can_get_ycbob_min5)
    world.set_rule(world.get_location(locn.ycbob_min6), can_get_ycbob_min6)
    world.set_rule(world.get_location(locn.ycbob_min7), can_get_ycbob_min7)
    world.set_rule(world.get_location(locn.ycbob_min8), can_get_ycbob_min8)
    world.set_rule(world.get_location(locn.ycbob_min9), can_get_ycbob_min9)
    world.set_rule(world.get_location(locn.ycbob_min10), can_get_ycbob_min10)
    # An Icy Reception Logic
    world.set_rule(world.get_location(locn.air_min1), can_get_air_min1)
    world.set_rule(world.get_location(locn.air_min2), can_get_air_min2)
    world.set_rule(world.get_location(locn.air_min4), can_get_air_min4)
    world.set_rule(world.get_location(locn.air_min5), can_get_air_min5)
    world.set_rule(world.get_location(locn.air_min6), can_get_air_min6)
    world.set_rule(world.get_location(locn.air_min7), can_get_air_min7)
    world.set_rule(world.get_location(locn.air_min8), can_get_air_min8)
    world.set_rule(world.get_location(locn.air_min9), can_get_air_min9)
    world.set_rule(world.get_location(locn.air_min10), can_get_air_min10)
    # Two Face Chase Logic
    world.set_rule(world.get_location(locn.tfc_min5), can_get_tfc_min5)
    world.set_rule(world.get_location(locn.tfc_min6), can_get_tfc_min6)
    world.set_rule(world.get_location(locn.tfc_min10), can_get_tfc_min10)
    # A Poisonous Appointment Logic
    world.set_rule(world.get_location(locn.apa_min2), can_get_apa_min2)
    world.set_rule(world.get_location(locn.apa_min3), can_get_apa_min3)
    world.set_rule(world.get_location(locn.apa_min4), can_get_apa_min4)
    world.set_rule(world.get_location(locn.apa_min5), can_get_apa_min5)
    world.set_rule(world.get_location(locn.apa_min6), can_get_apa_min6)
    world.set_rule(world.get_location(locn.apa_min7), can_get_apa_min7)
    world.set_rule(world.get_location(locn.apa_min8), can_get_apa_min8)
    world.set_rule(world.get_location(locn.apa_min9), can_get_apa_min9)
    world.set_rule(world.get_location(locn.apa_min10), can_get_apa_min10)
    # The Face Off Logic
    world.set_rule(world.get_location(locn.tfo_min4), can_get_tfo_min4)
    world.set_rule(world.get_location(locn.tfo_min5), can_get_tfo_min5)
    world.set_rule(world.get_location(locn.tfo_min6), can_get_tfo_min6)
    world.set_rule(world.get_location(locn.tfo_min7), can_get_tfo_min7)
    world.set_rule(world.get_location(locn.tfo_min8), can_get_tfo_min8)
    world.set_rule(world.get_location(locn.tfo_min9), can_get_tfo_min9)
    world.set_rule(world.get_location(locn.tfo_min10), can_get_tfo_min10)
    # There She Goes Again Logic
    world.set_rule(world.get_location(locn.tsga_min1), can_get_tsga_min1)
    world.set_rule(world.get_location(locn.tsga_min2), can_get_tsga_min2)
    world.set_rule(world.get_location(locn.tsga_min3), can_get_tsga_min3)
    world.set_rule(world.get_location(locn.tsga_min4), can_get_tsga_min4)
    world.set_rule(world.get_location(locn.tsga_min5), can_get_tsga_min5)
    world.set_rule(world.get_location(locn.tsga_min7), can_get_tsga_min7)
    world.set_rule(world.get_location(locn.tsga_min8), can_get_tsga_min8)
    world.set_rule(world.get_location(locn.tsga_min9), can_get_tsga_min9)
    world.set_rule(world.get_location(locn.tsga_min10), can_get_tsga_min10)
    # Batboat Battle Logic
    world.set_rule(world.get_location(locn.bbb_min2), can_get_bbb_min2)
    world.set_rule(world.get_location(locn.bbb_min3), can_get_bbb_min3)
    world.set_rule(world.get_location(locn.bbb_min5), can_get_bbb_min5)
    world.set_rule(world.get_location(locn.bbb_min6), can_get_bbb_min6)
    world.set_rule(world.get_location(locn.bbb_min7), can_get_bbb_min7)
    world.set_rule(world.get_location(locn.bbb_min8), can_get_bbb_min8)
    world.set_rule(world.get_location(locn.bbb_min9), can_get_bbb_min9)
    world.set_rule(world.get_location(locn.bbb_min10), can_get_bbb_min10)
    # Under The City Logic
    world.set_rule(world.get_location(locn.utc_min1), can_get_utc_min1)
    world.set_rule(world.get_location(locn.utc_min2), can_get_utc_min2)
    world.set_rule(world.get_location(locn.utc_min3), can_get_utc_min3)
    world.set_rule(world.get_location(locn.utc_min4), can_get_utc_min4)
    world.set_rule(world.get_location(locn.utc_min5), can_get_utc_min5)
    world.set_rule(world.get_location(locn.utc_min6), can_get_utc_min6)
    world.set_rule(world.get_location(locn.utc_min7), can_get_utc_min7)
    world.set_rule(world.get_location(locn.utc_min8), can_get_utc_min8)
    world.set_rule(world.get_location(locn.utc_min10), can_get_utc_min10)
    # Zoo's Company Logic
    world.set_rule(world.get_location(locn.zc_min1), can_get_zc_min1)
    world.set_rule(world.get_location(locn.zc_min2), can_get_zc_min2)
    world.set_rule(world.get_location(locn.zc_min3), can_get_zc_min3)
    world.set_rule(world.get_location(locn.zc_min4), can_get_zc_min4)
    world.set_rule(world.get_location(locn.zc_min5), can_get_zc_min5)
    world.set_rule(world.get_location(locn.zc_min6), can_get_zc_min6)
    world.set_rule(world.get_location(locn.zc_min8), can_get_zc_min8)
    world.set_rule(world.get_location(locn.zc_min9), can_get_zc_min9)
    world.set_rule(world.get_location(locn.zc_min10), can_get_zc_min10)
    # Penguin's Lair Logic
    world.set_rule(world.get_location(locn.pl_min1), can_get_pl_min1)
    world.set_rule(world.get_location(locn.pl_min2), can_get_pl_min2)
    world.set_rule(world.get_location(locn.pl_min3), can_get_pl_min3)
    world.set_rule(world.get_location(locn.pl_min5), can_get_pl_min5)
    world.set_rule(world.get_location(locn.pl_min7), can_get_pl_min7)
    world.set_rule(world.get_location(locn.pl_min8), can_get_pl_min8)
    world.set_rule(world.get_location(locn.pl_min10), can_get_pl_min10)
    # Joker's Home Turf Logic
    world.set_rule(world.get_location(locn.jht_min1), can_get_jht_min1)
    world.set_rule(world.get_location(locn.jht_min3), can_get_jht_min3)
    world.set_rule(world.get_location(locn.jht_min4), can_get_jht_min4)
    world.set_rule(world.get_location(locn.jht_min5), can_get_jht_min5)
    world.set_rule(world.get_location(locn.jht_min6), can_get_jht_min6)
    world.set_rule(world.get_location(locn.jht_min7), can_get_jht_min7)
    world.set_rule(world.get_location(locn.jht_min8), can_get_jht_min8)
    world.set_rule(world.get_location(locn.jht_min9), can_get_jht_min9)
    world.set_rule(world.get_location(locn.jht_min10), can_get_jht_min_10)
    # Little Fun at the Big Top Logic
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
    # Flight of the Bat Logic
    world.set_rule(world.get_location(locn.fotb_min7), can_get_fotb_min7)
    world.set_rule(world.get_location(locn.fotb_min9), can_get_fotb_min9)
    # In the Dark Night Logic
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
    # To the Top of the Tower Logic
    world.set_rule(world.get_location(locn.tttot_min1), can_get_tttot_min1)
    world.set_rule(world.get_location(locn.tttot_min3), can_get_tttot_min3)
    world.set_rule(world.get_location(locn.tttot_min4), can_get_tttot_min4)
    world.set_rule(world.get_location(locn.tttot_min5), can_get_tttot_min5)
    world.set_rule(world.get_location(locn.tttot_min6), can_get_tttot_min6)
    world.set_rule(world.get_location(locn.tttot_min9), can_get_tttot_min9)
    world.set_rule(world.get_location(locn.tttot_min10), can_get_tttot_min10)
    # The Riddler Makes A Withdrawal Logic
    world.set_rule(world.get_location(locn.trmaw_min1), can_get_trmaw_min1)
    world.set_rule(world.get_location(locn.trmaw_min2), can_get_trmaw_min2)
    world.set_rule(world.get_location(locn.trmaw_min3), can_get_trmaw_min3)
    world.set_rule(world.get_location(locn.trmaw_min4), can_get_trmaw_min4)
    world.set_rule(world.get_location(locn.trmaw_min6), can_get_trmaw_min6)
    world.set_rule(world.get_location(locn.trmaw_min7), can_get_trmaw_min7)
    world.set_rule(world.get_location(locn.trmaw_min9), can_get_trmaw_min9)
    # On The Rocks Logic
    world.set_rule(world.get_location(locn.otr_min2), can_get_otr_min2)
    world.set_rule(world.get_location(locn.otr_min4), can_get_otr_min4)
    world.set_rule(world.get_location(locn.otr_min5), can_get_otr_min5)
    world.set_rule(world.get_location(locn.otr_min6), can_get_otr_min6)
    world.set_rule(world.get_location(locn.otr_min7), can_get_otr_min7)
    world.set_rule(world.get_location(locn.otr_min8), can_get_otr_min8)
    world.set_rule(world.get_location(locn.otr_min9), can_get_otr_min9)
    # Green Fingers Logic
    world.set_rule(world.get_location(locn.gf_min1), can_get_gf_min1)
    world.set_rule(world.get_location(locn.gf_min2), can_get_gf_min2)
    world.set_rule(world.get_location(locn.gf_min4), can_get_gf_min4)
    world.set_rule(world.get_location(locn.gf_min5), can_get_gf_min5)
    world.set_rule(world.get_location(locn.gf_min6), can_get_gf_min6)
    world.set_rule(world.get_location(locn.gf_min7), can_get_gf_min7)
    world.set_rule(world.get_location(locn.gf_min8), can_get_gf_min8)
    world.set_rule(world.get_location(locn.gf_min9), can_get_gf_min9)
    world.set_rule(world.get_location(locn.gf_min10), can_get_gf_min10)
    # An Enterprising Threat Logic
    world.set_rule(world.get_location(locn.aet_min1), can_get_aet_min1)
    world.set_rule(world.get_location(locn.aet_min2), can_get_aet_min2)
    world.set_rule(world.get_location(locn.aet_min3), can_get_aet_min3)
    world.set_rule(world.get_location(locn.aet_min4), can_get_aet_min4)
    world.set_rule(world.get_location(locn.aet_min5), can_get_aet_min5)
    world.set_rule(world.get_location(locn.aet_min7), can_get_aet_min7)
    world.set_rule(world.get_location(locn.aet_min8), can_get_aet_min8)
    world.set_rule(world.get_location(locn.aet_min9), can_get_aet_min9)
    # Breaking Blocks Logic
    world.set_rule(world.get_location(locn.bb_min2), can_get_bb_min2)
    world.set_rule(world.get_location(locn.bb_min4), can_get_bb_min4)
    world.set_rule(world.get_location(locn.bb_min5), can_get_bb_min5)
    world.set_rule(world.get_location(locn.bb_min6), can_get_bb_min6)
    world.set_rule(world.get_location(locn.bb_min7), can_get_bb_min7)
    world.set_rule(world.get_location(locn.bb_min8), can_get_bb_min8)
    world.set_rule(world.get_location(locn.bb_min9), can_get_bb_min9)
    world.set_rule(world.get_location(locn.bb_min10), can_get_bb_min10)
    # Rockin The Dock Logic
    world.set_rule(world.get_location(locn.rtd_min1), can_get_rtd_min1)
    world.set_rule(world.get_location(locn.rtd_min2), can_get_rtd_min2)
    world.set_rule(world.get_location(locn.rtd_min5), can_get_rtd_min5)
    world.set_rule(world.get_location(locn.rtd_min7), can_get_rtd_min7)
    world.set_rule(world.get_location(locn.rtd_min9), can_get_rtd_min9)
    # Stealing The Show Logic
    world.set_rule(world.get_location(locn.sts_min1), can_get_sts_min1)
    world.set_rule(world.get_location(locn.sts_min2), can_get_sts_min2)
    world.set_rule(world.get_location(locn.sts_min3), can_get_sts_min3)
    world.set_rule(world.get_location(locn.sts_min6), can_get_sts_min6)
    world.set_rule(world.get_location(locn.sts_min7), can_get_sts_min7)
    world.set_rule(world.get_location(locn.sts_min9), can_get_sts_min9)
    world.set_rule(world.get_location(locn.sts_min10), can_get_sts_min10)
    # Harbouring A Grudge Logic
    world.set_rule(world.get_location(locn.hag_min3), can_get_hag_min3)
    world.set_rule(world.get_location(locn.hag_min7), can_get_hag_min7)
    world.set_rule(world.get_location(locn.hag_min8), can_get_hag_min8)
    world.set_rule(world.get_location(locn.hag_min10), can_get_hag_min10)
    # A Daring Rescue Logic
    world.set_rule(world.get_location(locn.adr_min1), can_get_adr_min1)
    world.set_rule(world.get_location(locn.adr_min2), can_get_adr_min2)
    world.set_rule(world.get_location(locn.adr_min3), can_get_adr_min3)
    world.set_rule(world.get_location(locn.adr_min5), can_get_adr_min5)
    world.set_rule(world.get_location(locn.adr_min6), can_get_adr_min6)
    world.set_rule(world.get_location(locn.adr_min7), can_get_adr_min7)
    world.set_rule(world.get_location(locn.adr_min9), can_get_adr_min9)
    # Arctic World Logic
    world.set_rule(world.get_location(locn.aw_min1), can_get_aw_min1)
    world.set_rule(world.get_location(locn.aw_min2), can_get_aw_min2)
    world.set_rule(world.get_location(locn.aw_min3), can_get_aw_min3)
    world.set_rule(world.get_location(locn.aw_min4), can_get_aw_min4)
    world.set_rule(world.get_location(locn.aw_min5), can_get_aw_min5)
    world.set_rule(world.get_location(locn.aw_min6), can_get_aw_min6)
    world.set_rule(world.get_location(locn.aw_min7), can_get_aw_min7)
    world.set_rule(world.get_location(locn.aw_min8), can_get_aw_min8)
    world.set_rule(world.get_location(locn.aw_min9), can_get_aw_min9)
    world.set_rule(world.get_location(locn.aw_min10), can_get_aw_min10)
    # A Surprise for the Commissioner Logic
    world.set_rule(world.get_location(locn.asftc_min1), can_get_asftc_min1)
    world.set_rule(world.get_location(locn.asftc_min2), can_get_asftc_min2)
    world.set_rule(world.get_location(locn.asftc_min3), can_get_asftc_min3)
    world.set_rule(world.get_location(locn.asftc_min4), can_get_asftc_min4)
    world.set_rule(world.get_location(locn.asftc_min5), can_get_asftc_min5)
    world.set_rule(world.get_location(locn.asftc_min6), can_get_asftc_min6)
    world.set_rule(world.get_location(locn.asftc_min7), can_get_asftc_min7)
    world.set_rule(world.get_location(locn.asftc_min8), can_get_asftc_min8)
    world.set_rule(world.get_location(locn.asftc_min9), can_get_asftc_min9)
    world.set_rule(world.get_location(locn.asftc_min10), can_get_asftc_min10)
    # Biplane Blast Logic
    world.set_rule(world.get_location(locn.bbpl_min1), can_get_bbpl_min1)
    world.set_rule(world.get_location(locn.bbpl_min3), can_get_bbpl_min3)
    world.set_rule(world.get_location(locn.bbpl_min8), can_get_bbpl_min8)
    world.set_rule(world.get_location(locn.bbpl_min9), can_get_bbpl_min9)
    world.set_rule(world.get_location(locn.bbpl_min10), can_get_bbpl_min10)
    # The Joker's Masterpiece Logic
    world.set_rule(world.get_location(locn.tjm_min3), can_get_tjm_min3)
    world.set_rule(world.get_location(locn.tjm_min5), can_get_tjm_min5)
    world.set_rule(world.get_location(locn.tjm_min6), can_get_tjm_min6)
    world.set_rule(world.get_location(locn.tjm_min7), can_get_tjm_min7)
    world.set_rule(world.get_location(locn.tjm_min8), can_get_tjm_min8)
    world.set_rule(world.get_location(locn.tjm_min9), can_get_tjm_min9)
    # The Lure of the Night Logic
    world.set_rule(world.get_location(locn.tlotn_min1), can_get_tlotn_min1)
    world.set_rule(world.get_location(locn.tlotn_min2), can_get_tlotn_min2)
    world.set_rule(world.get_location(locn.tlotn_min3), can_get_tlotn_min3)
    world.set_rule(world.get_location(locn.tlotn_min4), can_get_tlotn_min4)
    world.set_rule(world.get_location(locn.tlotn_min5), can_get_tlotn_min5)
    world.set_rule(world.get_location(locn.tlotn_min6), can_get_tlotn_min6)
    world.set_rule(world.get_location(locn.tlotn_min7), can_get_tlotn_min7)
    world.set_rule(world.get_location(locn.tlotn_min8), can_get_tlotn_min8)
    world.set_rule(world.get_location(locn.tlotn_min9), can_get_tlotn_min9)
    world.set_rule(world.get_location(locn.tlotn_min10), can_get_tlotn_min10)
    # Dying of Laughter Logic
    world.set_rule(world.get_location(locn.dol_min1), can_get_dol_min1)
    world.set_rule(world.get_location(locn.dol_min2), can_get_dol_min2)
    world.set_rule(world.get_location(locn.dol_min3), can_get_dol_min3)
    world.set_rule(world.get_location(locn.dol_min4), can_get_dol_min4)
    world.set_rule(world.get_location(locn.dol_min5), can_get_dol_min5)
    world.set_rule(world.get_location(locn.dol_min7), can_get_dol_min7)
    world.set_rule(world.get_location(locn.dol_min8), can_get_dol_min8)
    world.set_rule(world.get_location(locn.dol_min10), can_get_dol_min10)


def set_host_rules(world):
    world.set_rule(world.get_location(locn.air_host), can_get_air_host)
    world.set_rule(world.get_location(locn.apa_host), can_get_apa_host)
    world.set_rule(world.get_location(locn.tfo_host), can_get_tfo_host)
    world.set_rule(world.get_location(locn.utc_host), can_get_utc_host)
    world.set_rule(world.get_location(locn.zc_host), can_get_zc_host)
    world.set_rule(world.get_location(locn.jht_host), can_get_jht_host)
    world.set_rule(world.get_location(locn.lfabt_host), can_get_lfabt_host)
    world.set_rule(world.get_location(locn.itdn_host), can_get_itdn_host)
    world.set_rule(world.get_location(locn.trmaw_host), can_get_trmaw_host)
    world.set_rule(world.get_location(locn.otr_host), can_get_otr_host)
    world.set_rule(world.get_location(locn.gf_host), can_get_gf_host)
    world.set_rule(world.get_location(locn.aet_host), can_get_aet_host)
    world.set_rule(world.get_location(locn.bb_host), can_get_bb_host)
    world.set_rule(world.get_location(locn.rtd_host), can_get_rtd_host)
    world.set_rule(world.get_location(locn.sts_host), can_get_sts_host)
    world.set_rule(world.get_location(locn.adr_host), can_get_adr_host)
    world.set_rule(world.get_location(locn.aw_host), can_get_aw_host)
    world.set_rule(world.get_location(locn.asftc_host), can_get_asftc_host)
    world.set_rule(world.get_location(locn.tjm_host), can_get_tjm_host)
    world.set_rule(world.get_location(locn.tlotn_host), can_get_tlotn_host)
    world.set_rule(world.get_location(locn.dol_host), can_get_dol_host)


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
    world.set_rule(world.get_location(locn.gf_beat), can_beat_gf)
    world.set_rule(world.get_location(locn.gf_ts), can_beat_gf)
    world.set_rule(world.get_location(locn.bb_beat), can_beat_bb)
    world.set_rule(world.get_location(locn.bb_ts), can_beat_bb)
    world.set_rule(world.get_location(locn.sts_beat), can_beat_sts)
    world.set_rule(world.get_location(locn.sts_ts), can_beat_sts)
    world.set_rule(world.get_location(locn.aw_beat), can_beat_aw)
    world.set_rule(world.get_location(locn.aw_ts), can_beat_aw)
    world.set_rule(world.get_location(locn.asftc_beat), can_beat_asftc)
    world.set_rule(world.get_location(locn.asftc_ts), can_beat_asftc)
    world.set_rule(world.get_location(locn.tlotn_beat), can_beat_tlotn)
    world.set_rule(world.get_location(locn.tlotn_ts), can_beat_tlotn)


def set_red_brick_rules(world):
    world.set_rule(world.get_location(LocationName.silhouettes), can_purchase_silhouettes)
    world.set_rule(world.get_location(LocationName.beepbeep), can_purchase_beepbeep)
    world.set_rule(world.get_location(LocationName.icerink), can_purchase_icerink)
    world.set_rule(world.get_location(LocationName.disguise), can_purchase_disguise)
    world.set_rule(world.get_location(LocationName.extratoggle), can_purchase_extratoggle)
    world.set_rule(world.get_location(LocationName.scorex2), can_purchase_scorex2)
    world.set_rule(world.get_location(LocationName.scorex4), can_purchase_scorex4)
    world.set_rule(world.get_location(LocationName.scorex6), can_purchase_scorex6)
    world.set_rule(world.get_location(LocationName.scorex8), can_purchase_scorex8)
    world.set_rule(world.get_location(LocationName.scorex10), can_purchase_scorex10)
    world.set_rule(world.get_location(LocationName.studmagnet), can_purchase_stud_magnet)
    world.set_rule(world.get_location(LocationName.charstuds), can_purchase_stud_magnet)
    world.set_rule(world.get_location(LocationName.minidetect), can_purchase_minikit_detect)
    world.set_rule(world.get_location(LocationName.powerdetect), can_purchase_pwr_brick_detect)
    world.set_rule(world.get_location(LocationName.alwaysscore), can_purchase_always_multi)
    world.set_rule(world.get_location(LocationName.fastbuild), can_purchase_fast_build)
    world.set_rule(world.get_location(LocationName.immunefreeze), can_purchase_freeze_immune)
    world.set_rule(world.get_location(LocationName.regenhearts), can_purchase_regen_hearts)
    world.set_rule(world.get_location(LocationName.extrahearts), can_purchase_extra_hearts)
    world.set_rule(world.get_location(LocationName.invincibility), can_purchase_invincibility)
    world.set_rule(world.get_location(LocationName.fastgrap), can_purchase_fast_grapple)
    world.set_rule(world.get_location(LocationName.fastbat), can_purchase_fast_bat)
    world.set_rule(world.get_location(LocationName.moretargets), can_purchase_more_bat)
    world.set_rule(world.get_location(LocationName.flamingbat), can_purchase_flame_bat)
    world.set_rule(world.get_location(LocationName.slam), can_purchase_slam)
    world.set_rule(world.get_location(LocationName.moredet), can_purchase_more_det)
    world.set_rule(world.get_location(LocationName.armourplating), can_purchase_armour_plat)
    world.set_rule(world.get_location(LocationName.sonicpain), can_purchase_sonic_pain)
    world.set_rule(world.get_location(LocationName.areaeffect), can_purchase_area_effect)
    world.set_rule(world.get_location(LocationName.bats), can_purchase_bats)
    world.set_rule(world.get_location(LocationName.freezebatarang), can_purchase_freeze_bat)
    world.set_rule(world.get_location(LocationName.decoy), can_purchase_decoy)
    world.set_rule(world.get_location(LocationName.fastwalk), can_purchase_fast_walk)
    world.set_rule(world.get_location(LocationName.fasterpieces), can_purchase_faster_piece)
    world.set_rule(world.get_location(LocationName.piecedetect), can_purchase_piece_detect)


def set_rules(world):
    set_entrance_rules(world)
    set_suit_rules(world)
    set_char_rules(world)
    if world.options.shuffle_hush_and_ras == 1:
        set_hard_char_rules(world)
    if world.options.minikit_sanity == 1:
        set_minikit_rules(world)
    set_host_rules(world)
    set_level_beaten_rules(world)
    set_red_brick_rules(world)
    set_event_rules(world)
    set_win_con(world)


def set_event_rules(world):
    if world.options.EndGoal == EndGoal.option_minikits:
        minikit_to_win = world.options.minikits_to_win.value
        minikit_grouping = world.options.minikit_grouping.value
        required_count: int = minikit_to_win // minikit_grouping
        if minikit_to_win % minikit_grouping > 0:
            required_count += 1
        world.set_rule(world.get_location("All Required Minikits Received"),
                       Has("UNIQUE_MINIKITS", required_count))

    if world.options.EndGoal == EndGoal.option_levels_beaten:
        for (name, data) in event_location_table.items():
            event: Location = world.get_location(name)
            level_beaten_name = name.removesuffix(" Token")
            world.set_rule(event, CanReachLocation(level_beaten_name))

        world.set_rule(world.get_location("All Required Levels Beaten"),
                       Has("Level Beaten", world.options.levels_to_win.value))


def set_win_con(world):
    if world.options.EndGoal == EndGoal.option_minikits:
        world.set_completion_rule(Has("All Required Minikits Received"))
    if world.options.EndGoal == EndGoal.option_levels_beaten:
        world.set_completion_rule(Has("All Required Levels Beaten"))
