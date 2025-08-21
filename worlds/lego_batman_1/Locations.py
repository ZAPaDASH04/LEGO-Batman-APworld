from BaseClasses import Location
from dataclasses import dataclass

class LB1Location(Location):
    game: str = "Lego Batman: The Videogame"

@dataclass
class LocationData(Location):
    id: int = 0
    region: str = ""


base_location_id: int = 400000

minikit_location_table: dict[str, LocationData] = {
    # You can Bank on Batman
    "You can Bank on Batman: Minikit inside the Garage near Spawn":
        LocationData(base_location_id + 100, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit above the Garage near Spawn":
        LocationData(base_location_id + 101, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit behind Glass Window near Spawn":
        LocationData(base_location_id + 102, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit mind Control Behind Van in Toxic Waste":
        LocationData(base_location_id + 103, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit in the Sewer Grate":
        LocationData(base_location_id + 104, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit behind a High Window by Cement Mixer":
        LocationData(base_location_id + 105, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit on a Balcony Behind Heavy Item near Downward Slope":
        LocationData(base_location_id + 106, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit from Using the Recycler":
        LocationData(base_location_id + 107, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit park Two Cars":
        LocationData(base_location_id + 108, "You can Bank on Batman"),
    "You can Bank on Batman: Minikit destroy Five Phone Booths":
        LocationData(base_location_id + 109, "You can Bank on Batman"),
    # An Icy Reception
    "An Icy Reception: Minikit on a Ledge near Spawn":
        LocationData(base_location_id + 110, "An Icy Reception"),
    "An Icy Reception: Minikit behind the Boarded Window on Ledge near Spawn":
        LocationData(base_location_id + 111, "An Icy Reception"),
    "An Icy Reception: Minikit in the Silver Lego Icecream Stand":
        LocationData(base_location_id + 112, "An Icy Reception"),
    "An Icy Reception: Minikit behind the Icecream Truck":
        LocationData(base_location_id + 113, "An Icy Reception"),
    "An Icy Reception: Minikit in the Alley with Hostage":
        LocationData(base_location_id + 114, "An Icy Reception"),
    "An Icy Reception: Minikit in the Silver Legos Above Icecream Cones":
        LocationData(base_location_id + 115, "An Icy Reception"),
    "An Icy Reception: Minikit in the Female Locked Room":
        LocationData(base_location_id + 116, "An Icy Reception"),
    "An Icy Reception: Minikit in the Silver Legos Behind Toxic Gas":
        LocationData(base_location_id + 117, "An Icy Reception"),
    "An Icy Reception: Minikit in the Vent with Fan":
        LocationData(base_location_id + 118, "An Icy Reception"),
    "An Icy Reception: Minikit in the Hypnosis Room":
        LocationData(base_location_id + 119, "An Icy Reception"),
    # Two-Face Chase
    "Two-Face Chase: Minikit destroy Three Dumpsters":
        LocationData(base_location_id + 120, "Two-Face Chase"),
    "Two-Face Chase: Minikit in the Manhole Cover":
        LocationData(base_location_id + 121, "Two-Face Chase"),
    "Two-Face Chase: Minikit destroy the Southwest Trash Dumpster":
        LocationData(base_location_id + 122, "Two-Face Chase"),
    "Two-Face Chase: Minikit destroy Three Cars":
        LocationData(base_location_id + 123, "Two-Face Chase"),
    "Two-Face Chase: Minikit destroy the North Supports":
        LocationData(base_location_id + 124, "Two-Face Chase"),
    "Two-Face Chase: Minikit destroy the South Supports":
        LocationData(base_location_id + 125, "Two-Face Chase"),
    "Two-Face Chase: Minikit use Joker's Van Panel":
        LocationData(base_location_id + 126, "Two-Face Chase"),
    "Two-Face Chase: Minikit use Harley's Truck Panel":
        LocationData(base_location_id + 127, "Two-Face Chase"),
    "Two-Face Chase: Minikit in the Telephone Booth":
        LocationData(base_location_id + 128, "Two-Face Chase"),
    "Two-Face Chase: Minikit destroy Three Food Carts":
        LocationData(base_location_id + 129, "Two-Face Chase"),
    # A Poisonous Appointment
    "A Poisonous Appointment: Minikit destroy the Carrots":
        LocationData(base_location_id + 130, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit on Top oft the Trees":
        LocationData(base_location_id + 131, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit in the Heated Greenhouse":
        LocationData(base_location_id + 132, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit above the Orange Flowers":
        LocationData(base_location_id + 133, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit near the Rail above the Potted Plant":
        LocationData(base_location_id + 134, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit in the Underwater Pipe":
        LocationData(base_location_id + 135, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit in a Vat near the Second Pitcher Plant":
        LocationData(base_location_id + 136, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit destroy Carrots":
        LocationData(base_location_id + 137, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit above the Heated Pipes":
        LocationData(base_location_id + 138, "A Poisonous Appointment"),
    "A Poisonous Appointment: Minikit in the Toxic Waste Room Above Ledge":
        LocationData(base_location_id + 139, "A Poisonous Appointment"),
    # The Face-Off
    "The Face-Off: Minikit jump on Poles":
        LocationData(base_location_id + 140, "The Face-Off"),
    "The Face-Off: Minikit above Grapple Point to the Right of Spawn":
        LocationData(base_location_id + 141, "The Face-Off"),
    "The Face-Off: Minikit build the Dollar Sign":
        LocationData(base_location_id + 142, "The Face-Off"),
    "The Face-Off: Minikit in the Revolving Door":
        LocationData(base_location_id + 143, "The Face-Off"),
    "The Face-Off: Minikit on the Roof Above Recycler":
        LocationData(base_location_id + 144, "The Face-Off"),
    "The Face-Off: Minikit in the Toxic Waste Room Pipe":
        LocationData(base_location_id + 145, "The Face-Off"),
    "The Face-Off: Minikit underneath the Toxic Waste near the Three Platform Bridge":
        LocationData(base_location_id + 146, "The Face-Off"),
    "The Face-Off: Minikit on the Right Side of Toxic Waste Room":
        LocationData(base_location_id + 147, "The Face-Off"),
    "The Face-Off: Minikit on the Right Side of Vault Room":
        LocationData(base_location_id + 148, "The Face-Off"),
    "The Face-Off: Minikit destroy Five Chests":
        LocationData(base_location_id + 149, "The Face-Off"),
    #There She Goes Again
    "There She Goes Again: Minikit in the Female Locked Room":
        LocationData(base_location_id + 150, "There She Goes Again"),
    "There She Goes Again: Minikit drive the Car Into Garage":
        LocationData(base_location_id + 151, "There She Goes Again"),
    "There She Goes Again: Minikit locked Underwater Behind the Fence":
        LocationData(base_location_id + 152, "There She Goes Again"),
    "There She Goes Again: Minikit destroy Carrots":
        LocationData(base_location_id + 153, "There She Goes Again"),
    "There She Goes Again: Minikit locked Underwater by the Blue Pump":
        LocationData(base_location_id + 154, "There She Goes Again"),
    "There She Goes Again: Minikit from Using the Lawnmower on the Flowers":
        LocationData(base_location_id + 155, "There She Goes Again"),
    "There She Goes Again: Minikit behind the Window Above Dumpster":
        LocationData(base_location_id + 156, "There She Goes Again"),
    "There She Goes Again: Minikit behind the Second Dumpster Under Water Tower":
        LocationData(base_location_id + 157, "There She Goes Again"),
    "There She Goes Again: Minikit in the Glass Roof":
        LocationData(base_location_id + 158, "There She Goes Again"),
    "There She Goes Again: Minikit in the Pipe After Breaking Glass":
        LocationData(base_location_id + 159, "There She Goes Again"),
    #Batboat Battle
    "Batboat Battle: Minikit turn on the Lighthouse":
        LocationData(base_location_id + 160, "Batboat Battle"),
    "Batboat Battle: Minikit blow Up the Silver Lego Box":
        LocationData(base_location_id + 161, "Batboat Battle"),
    "Batboat Battle: Minikit sink the Ship":
        LocationData(base_location_id + 162, "Batboat Battle"),
    "Batboat Battle: Minikit pull the Pipe":
        LocationData(base_location_id + 163, "Batboat Battle"),
    "Batboat Battle: Minikit in Alcove Surrounded by Ice":
        LocationData(base_location_id + 164, "Batboat Battle"),
    "Batboat Battle: Minikit in Silver Lego Crate Surrounded by Toxic Water":
        LocationData(base_location_id + 165, "Batboat Battle"),
    "Batboat Battle: Minikit destroy Silver Legos Around Pipe":
        LocationData(base_location_id + 166, "Batboat Battle"),
    "Batboat Battle: Minikit destroy Buoys":
        LocationData(base_location_id + 167, "Batboat Battle"),
    "Batboat Battle: Minikit in the Corner Surrounded by Ice":
        LocationData(base_location_id + 168, "Batboat Battle"),
    "Batboat Battle: Minikit destroy Silver Lego Boxes in Toxic Water":
        LocationData(base_location_id + 169, "Batboat Battle"),
    #Under the City
    "Under the City: Minikit on Top of the Rafters":
        LocationData(base_location_id + 170, "Under the City"),
    "Under the City: Minikit in the Cage Behind Mind Control Door":
        LocationData(base_location_id + 171, "Under the City"),
    "Under the City: Minikit in the Glass Room":
        LocationData(base_location_id + 172, "Under the City"),
    "Under the City: Minikit on the Pipes Above the Robin Suit Swapper":
        LocationData(base_location_id + 173, "Under the City"),
    "Under the City: Minikit destroy Markers with the Boat Built from the Recycler":
        LocationData(base_location_id + 174, "Under the City"),
    "Under the City: Minikit above the Ladder Across the Toxic Waste":
        LocationData(base_location_id + 175, "Under the City"),
    "Under the City: Minikit jump From the Toilet":
        LocationData(base_location_id + 176, "Under the City"),
    "Under the City: Minikit above the Scissor Lifter":
        LocationData(base_location_id + 177, "Under the City"),
    "Under the City: Minikit underwater Underneath the Hatch":
        LocationData(base_location_id + 178, "Under the City"),
    "Under the City: Minikit on Top of the Pillar by the Generator":
        LocationData(base_location_id + 179, "Under the City"),
    # Zoo's Company
    "Zoo's Company: Minikit hit Buoys with Boat in the Female Locked Room":
        LocationData(base_location_id + 180, "Zoo's Company"),
    "Zoo's Company: Minikit in the Air on Other Side of Toxic Waste Behind the Barred Door":
        LocationData(base_location_id + 181, "Zoo's Company"),
    "Zoo's Company: Minikit from Using the Recycler":
        LocationData(base_location_id + 182, "Zoo's Company"),
    "Zoo's Company: Minikit destroy the Silver Legos Above Recycler":
        LocationData(base_location_id + 183, "Zoo's Company"),
    "Zoo's Company: Minikit in the Air After Building Totem":
        LocationData(base_location_id + 184, "Zoo's Company"),
    "Zoo's Company: Minikit destroy the Silver Legos in Lion Enclosure":
        LocationData(base_location_id + 185, "Zoo's Company"),
    "Zoo's Company: Minikit in the Elephant Enclosure":
        LocationData(base_location_id + 186, "Zoo's Company"),
    "Zoo's Company: Minikit above the Lilypad by the Boat":
        LocationData(base_location_id + 187, "Zoo's Company"),
    "Zoo's Company: Minikit on the Ledge Behind Waterfall":
        LocationData(base_location_id + 188, "Zoo's Company"),
    "Zoo's Company: Minikit behind the Strength Handle by Batman Suit Swapper":
        LocationData(base_location_id + 189, "Zoo's Company"),
    #Penguin's Lair
    "Penguin's Lair: Minikit under the Glass Covered Water":
        LocationData(base_location_id + 190, "Penguin's Lair"),
    "Penguin's Lair: Minikit in the Silver Lego Cage":
        LocationData(base_location_id + 191, "Penguin's Lair"),
    "Penguin's Lair: Minikit on the Roof Above the Robin Suit Swapper":
        LocationData(base_location_id + 192, "Penguin's Lair"),
    "Penguin's Lair: Minikit from Growing Carrots":
        LocationData(base_location_id + 193, "Penguin's Lair"),
    "Penguin's Lair: Minikit on the Icy Ledge":
        LocationData(base_location_id + 194, "Penguin's Lair"),
    "Penguin's Lair: Minikit on the Iceberg in the Final Battle Room":
        LocationData(base_location_id + 195, "Penguin's Lair"),
    "Penguin's Lair: Minikit on the South East Ledge in the Final Battle Room":
        LocationData(base_location_id + 196, "Penguin's Lair"),
    "Penguin's Lair: Minikit behind the Silver Lego in Toxic Waste":
        LocationData(base_location_id + 197, "Penguin's Lair"),
    "Penguin's Lair: Minikit destroy Capacitors with Batarang":
        LocationData(base_location_id + 198, "Penguin's Lair"),
    "Penguin's Lair: Minikit from Building Heated Objects":
        LocationData(base_location_id + 199, "Penguin's Lair"),
    #Joker's Home Turf
    "Joker's Home Turf: Minikit above the Fan Built from Silver Legos":
        LocationData(base_location_id + 200, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit from Cleaning up the Toxic Waste":
        LocationData(base_location_id + 201, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit from Completing the Puzzle Behind the Mind Control Door":
        LocationData(base_location_id + 202, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit above the Ledge Accessed by Joker's Ladder":
        LocationData(base_location_id + 203, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit caged in the Room Accessed by Controlling the Crane":
        LocationData(base_location_id + 204, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit in the Toxic Waste Pipe":
        LocationData(base_location_id + 205, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit high Up in Alcove Behind the Strength Gate":
        LocationData(base_location_id + 206, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit crossing the Toxic Waste Water":
        LocationData(base_location_id + 207, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit in the Pool of Toxic Waste Drained by Generator":
        LocationData(base_location_id + 208, "Joker's Home Turf"),
    "Joker's Home Turf: Minikit behind the Silver Legos in Mad Hatter Fight":
        LocationData(base_location_id + 209, "Joker's Home Turf"),
    #Little Fun at Big Top
    "Little Fun at Big Top: Minikit across the Tightrope Behind the Pushable Bus":
        LocationData(base_location_id + 210, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit carnival Target Game":
        LocationData(base_location_id + 211, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit inside the Water Filled Pipe Above Carnival Game":
        LocationData(base_location_id + 212, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit yellow Duck Carnival Game":
        LocationData(base_location_id + 213, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit behind the Window Above Gumball Machine":
        LocationData(base_location_id + 214, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit from Activating the Teacup Ride":
        LocationData(base_location_id + 215, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit on the Spiral Slide":
        LocationData(base_location_id + 216, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit from Storing the Toy Boats":
        LocationData(base_location_id + 217, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit bumper Cars":
        LocationData(base_location_id + 218, "Little Fun at Big Top"),
    "Little Fun at Big Top: Minikit tightrope on the Other Side of the Toxic Waste":
        LocationData(base_location_id + 219, "Little Fun at Big Top"),
    #Flight of the Bat
    "Flight of the Bat: Minikit destroy the Missile Launchers":
        LocationData(base_location_id + 220, "Flight of the Bat"),
    "Flight of the Bat: Minikit floating by Turrets":
        LocationData(base_location_id + 221, "Flight of the Bat"),
    "Flight of the Bat: Minikit on the Railway":
        LocationData(base_location_id + 222, "Flight of the Bat"),
    "Flight of the Bat: Minikit in the Silver Lego by Hotel Sign":
        LocationData(base_location_id + 223, "Flight of the Bat"),
    "Flight of the Bat: Minikit destroy the Gray Pipe":
        LocationData(base_location_id + 224, "Flight of the Bat"),
    "Flight of the Bat: Minikit from Blowing up the Silver Lego Valves":
        LocationData(base_location_id + 225, "Flight of the Bat"),
    "Flight of the Bat: Minikit destroy Gargoyles":
        LocationData(base_location_id + 226, "Flight of the Bat"),
    "Flight of the Bat: Minikit from Completing the Barrel Puzzle":
        LocationData(base_location_id + 227, "Flight of the Bat"),
    "Flight of the Bat: Minikit platform near the Helicopter Pad":
        LocationData(base_location_id + 228, "Flight of the Bat"),
    "Flight of the Bat: Minikit near the Yellow Barrels on the Rooftop":
        LocationData(base_location_id + 229, "Flight of the Bat"),
    #in the Dark Night
    "In the Dark Night: Minikit from Breaking the Glass Behind the Strength Door":
        LocationData(base_location_id + 230, "In the Dark Night"),
    "In the Dark Night: Minikit back Left Corner of the Rooftop Reached by Grapple":
        LocationData(base_location_id + 231, "In the Dark Night"),
    "In the Dark Night: Minikit destroy Objects to Find Cakes":
        LocationData(base_location_id + 232, "In the Dark Night"),
    "In the Dark Night: Minikit in the Fish Tank":
        LocationData(base_location_id + 233, "In the Dark Night"),
    "In the Dark Night: Minikit from Flying the Helicopter into Lights":
        LocationData(base_location_id + 234, "In the Dark Night"),
    "In the Dark Night: Minikit in the Silver Lego Behind the Garbage Truck":
        LocationData(base_location_id + 235, "In the Dark Night"),
    "In the Dark Night: Minikit on the Ledge Next to the Graffiti Wall":
        LocationData(base_location_id + 236, "In the Dark Night"),
    "In the Dark Night: Minikit inside the Silver Lego Manhole Cover":
        LocationData(base_location_id + 237, "In the Dark Night"),
    "In the Dark Night: Minikit from Exploding the Generator in the Boss Room":
        LocationData(base_location_id + 238, "In the Dark Night"),
    "In the Dark Night: Minikit in Glass Above Joker's Generator":
        LocationData(base_location_id + 239, "In the Dark Night"),
    #To the Top of the Tower
    "To the Top of the Tower: Minikit destroy Silver Lego Gargoyles":
        LocationData(base_location_id + 240, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit use the Buttons on the Ledge Above the Flowerbed":
        LocationData(base_location_id + 241, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit behind the Glass Filled Arch":
        LocationData(base_location_id + 242, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit in the Destroyed Wall From Using the Recycler":
        LocationData(base_location_id + 243, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit floating on the Right Side of the Cathedral":
        LocationData(base_location_id + 244, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit on the Wooden Platform Lowered by Generator":
        LocationData(base_location_id + 245, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit on the Ledge Above Magnet Wall":
        LocationData(base_location_id + 246, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit hidden to the Right of the Lever":
        LocationData(base_location_id + 247, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit use the Orange Buttons on Left Side of Bell Tower":
        LocationData(base_location_id + 248, "To the Top of the Tower"),
    "To the Top of the Tower: Minikit in the Silver Lego Crate next to Statue Path":
        LocationData(base_location_id + 249, "To the Top of the Tower"),
    #The Riddler Makes a Withdrawal
    "The Riddler Makes a Withdrawal: Minikit behind the Garbage Truck":
        LocationData(base_location_id + 250, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit in the Air Above the Parking Lot":
        LocationData(base_location_id + 251, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit from Smashing the Blue Booth":
        LocationData(base_location_id + 252, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit behind the Silver Lego Gate":
        LocationData(base_location_id + 253, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit behind the Window Above the Grapple":
        LocationData(base_location_id + 254, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit inside the Glass House":
        LocationData(base_location_id + 255, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit above the Rails Outside Bank":
        LocationData(base_location_id + 256, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit in the Barrels next to the Bank":
        LocationData(base_location_id + 257, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit behind the Glass Window":
        LocationData(base_location_id + 258, "The Riddler Makes a Withdrawal"),
    "The Riddler Makes a Withdrawal: Minikit in the Car Show Room":
        LocationData(base_location_id + 259, "The Riddler Makes a Withdrawal"),
    # On the Rocks
    "On the Rocks: Minikit parking the Ice Cream Van":
        LocationData(base_location_id + 260, "On the Rocks"),
    "On the Rocks: Minikit destroy Snowmen":
        LocationData(base_location_id + 261, "On the Rocks"),
    "On the Rocks: Minikit behind the Window near the Snowman Billboard":
        LocationData(base_location_id + 262, "On the Rocks"),
    "On the Rocks: Minikit behind the Ice Wall":
        LocationData(base_location_id + 263, "On the Rocks"),
    "On the Rocks: Minikit on the Ledge Accessed by the Magnet Wall":
        LocationData(base_location_id + 264, "On the Rocks"),
    "On the Rocks: Minikit floating below Rails off the Edge":
        LocationData(base_location_id + 265, "On the Rocks"),
    "On the Rocks: Minikit from Using the Recycler":
        LocationData(base_location_id + 266, "On the Rocks"),
    "On the Rocks: Minikit in the Silver Lego Crate by Hypnotised Man":
        LocationData(base_location_id + 267, "On the Rocks"),
    "On the Rocks: Minikit above the Left Vat in the Last Fight":
        LocationData(base_location_id + 268, "On the Rocks"),
    "On the Rocks: Minikit near Worker in the Last Fight":
        LocationData(base_location_id + 269, "On the Rocks"),
    # Green Fingers
    "Green Fingers: Minikit race Around the Track":
        LocationData(base_location_id + 270, "Green Fingers"),
    "Green Fingers: Minikit on the Wooden Platforms in the Garden":
        LocationData(base_location_id + 271, "Green Fingers"),
    "Green Fingers: Minikit above the Rails On Left Side of the Building":
        LocationData(base_location_id + 272, "Green Fingers"),
    "Green Fingers: Minikit complete the Block Puzzle":
        LocationData(base_location_id + 273, "Green Fingers"),
    "Green Fingers: Minikit in the Air After Turning on the Fountain":
        LocationData(base_location_id + 274, "Green Fingers"),
    "Green Fingers: Minikit near the Pipe Above the Toxic Waste":
        LocationData(base_location_id + 275, "Green Fingers"),
    "Green Fingers: Minikit break Machine Behind the Silver Lego Door":
        LocationData(base_location_id + 276, "Green Fingers"),
    "Green Fingers: Minikit in the Hole Above the Heated Pipe":
        LocationData(base_location_id + 277, "Green Fingers"),
    "Green Fingers: Minikit floating Above the Water in the Other Water Tank":
        LocationData(base_location_id + 278, "Green Fingers"),
    "Green Fingers: Minikit in the Metal Cage Below the Hypnotized Man":
        LocationData(base_location_id + 279, "Green Fingers"),
    #An Enterprising Theft
    "An Enterprising Theft: Minikit above the Display Case":
        LocationData(base_location_id + 280, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit from Completing the Car Maze":
        LocationData(base_location_id + 281, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit inside the Elevator":
        LocationData(base_location_id + 282, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit behind the Glass Window":
        LocationData(base_location_id + 283, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit fly the Helicopter in the Toxic Waste Room":
        LocationData(base_location_id + 284, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit in the Metal Pipe that the Hypnotized Man Opens":
        LocationData(base_location_id + 285, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit behind the Silver Lego Grate":
        LocationData(base_location_id + 286, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit from Putting the Weight on the Scale":
        LocationData(base_location_id + 287, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit above the Heated Pipe of the Silver Lego Gate":
        LocationData(base_location_id + 288, "An Enterprising Theft"),
    "An Enterprising Theft: Minikit next to the Glowing Purple Vat":
        LocationData(base_location_id + 289, "An Enterprising Theft"),
    # Breaking Blocks
    "Breaking Blocks: Minikit on the Large Leaves":
        LocationData(base_location_id + 290, "Breaking Blocks"),
    "Breaking Blocks: Minikit destroy Security Cameras":
        LocationData(base_location_id + 291, "Breaking Blocks"),
    "Breaking Blocks: Minikit behind the Painting":
        LocationData(base_location_id + 292, "Breaking Blocks"),
    "Breaking Blocks: Minikit on a Ledge Above the Recycler":
        LocationData(base_location_id + 293, "Breaking Blocks"),
    "Breaking Blocks: Minikit behind the Bookcase":
        LocationData(base_location_id + 294, "Breaking Blocks"),
    "Breaking Blocks: Minikit in the Silver Lego Cage near Hostage":
        LocationData(base_location_id + 295, "Breaking Blocks"),
    "Breaking Blocks: Minikit destroy Golden Piggy Banks":
        LocationData(base_location_id + 296, "Breaking Blocks"),
    "Breaking Blocks: Minikit in the Silver Lego Cage near the Lasers":
        LocationData(base_location_id + 297, "Breaking Blocks"),
    "Breaking Blocks: Minikit push the Metal Legos off the Edge":
        LocationData(base_location_id + 298, "Breaking Blocks"),
    "Breaking Blocks: Minikit behind the Silver Lego Vault Door":
        LocationData(base_location_id + 299, "Breaking Blocks"),
    # Rockin' the Docks
    "Rockin' the Docks: Minikit on the Rails in the Hostage Room":
        LocationData(base_location_id + 300, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit destroy Carrots":
        LocationData(base_location_id + 301, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit inside the Boat":
        LocationData(base_location_id + 302, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit park the Trucks on the Buttons":
        LocationData(base_location_id + 303, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit on the Ledge reached from the Plant Ladder":
        LocationData(base_location_id + 304, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit destroy Water Cannons on Docks":
        LocationData(base_location_id + 305, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit Joker's Pirate Ship Race":
        LocationData(base_location_id + 306, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit beneath the Lily Pads":
        LocationData(base_location_id + 307, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit use the Recycler in the Female Locked Room":
        LocationData(base_location_id + 308, "Rockin' the Docks"),
    "Rockin' the Docks: Minikit on the Narrow Ledge to the Left After Riding the Elevator":
        LocationData(base_location_id + 309, "Rockin' the Docks"),
    #Stealing the Show
    "Stealing the Show: Minikit in the Room Behind the Boarded Up Windows":
        LocationData(base_location_id + 310, "Stealing the Show"),
    "Stealing the Show: Minikit destroy Neon Signs":
        LocationData(base_location_id + 311, "Stealing the Show"),
    "Stealing the Show: Minikit on the Roof Above the Wall Fans":
        LocationData(base_location_id + 312, "Stealing the Show"),
    "Stealing the Show: Minikit behind Glass Roof after Helicopter Fight":
        LocationData(base_location_id + 313, "Stealing the Show"),
    "Stealing the Show: Minikit on the Balcony Near the Edge of the Screen":
        LocationData(base_location_id + 314, "Stealing the Show"),
    "Stealing the Show: Minikit on the Roof Above the Magnetic Wall":
        LocationData(base_location_id + 315, "Stealing the Show"),
    "Stealing the Show: Minikit inside the Glass Display Case":
        LocationData(base_location_id + 316, "Stealing the Show"),
    "Stealing the Show: Minikit inside the Crate Next to the Dinosaurs":
        LocationData(base_location_id + 317, "Stealing the Show"),
    "Stealing the Show: Minikit caged Above the Catapults":
        LocationData(base_location_id + 318, "Stealing the Show"),
    "Stealing the Show: Minikit on the Roof of the Museum Accessed by a Ladder Inside":
        LocationData(base_location_id + 319, "Stealing the Show"),
    #Harbouring a Grudge
    "Harbouring a Grudge: Minikit inside the Toxic Waste Barrel":
        LocationData(base_location_id + 320, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit destroy Mini Oil Rigs":
        LocationData(base_location_id + 321, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit behind Silver Lego Locked Gate":
        LocationData(base_location_id + 322, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit destroy Buoys":
        LocationData(base_location_id + 323, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit destroy the Docked Boat":
        LocationData(base_location_id + 324, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit floating Off of the Ramp":
        LocationData(base_location_id + 325, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit inside the Police Boat in Toxic Water":
        LocationData(base_location_id + 326, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit inside the Orange Crane's Crate":
        LocationData(base_location_id + 327, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit inside the Barrel Floating in Toxic Waste":
        LocationData(base_location_id + 328, "Harbouring a Grudge"),
    "Harbouring a Grudge: Minikit behind the Robin Wall":
        LocationData(base_location_id + 329, "Harbouring a Grudge"),
    #A Daring Rescue
    "A Daring Rescue: Minikit in the Underground Path Accessed through Manhole Cover":
        LocationData(base_location_id + 330, "A Daring Rescue"),
    "A Daring Rescue: Minikit build a Band":
        LocationData(base_location_id + 331, "A Daring Rescue"),
    "A Daring Rescue: Minikit complete the Water Pressure Puzzle":
        LocationData(base_location_id + 332, "A Daring Rescue"),
    "A Daring Rescue: Minikit destroy TVs":
        LocationData(base_location_id + 333, "A Daring Rescue"),
    "A Daring Rescue: Minikit from Using the Recycler":
        LocationData(base_location_id + 334, "A Daring Rescue"),
    "A Daring Rescue: Minikit park Police Vehicles":
        LocationData(base_location_id + 335, "A Daring Rescue"),
    "A Daring Rescue: Minikit up the Stairs after Pulling the Glass Locked Switch":
        LocationData(base_location_id + 336, "A Daring Rescue"),
    "A Daring Rescue: Minikit left Toilet Stall":
        LocationData(base_location_id + 337, "A Daring Rescue"),
    "A Daring Rescue: Minikit in the Case Above Magnet Wall":
        LocationData(base_location_id + 338, "A Daring Rescue"),
    "A Daring Rescue: Minikit locked in Final Room Holding Cell":
        LocationData(base_location_id + 339, "A Daring Rescue"),
    # Arctic World
    "Arctic World: Minikit inside the Ice Cream Shop":
        LocationData(base_location_id + 340, "Arctic World"),
    "Arctic World: Minikit on the Penguin Sign after Powering up the Generator":
        LocationData(base_location_id + 341, "Arctic World"),
    "Arctic World: Minikit in the Cave Blocked by Glass":
        LocationData(base_location_id + 342, "Arctic World"),
    "Arctic World: Minikit slalom Skiing":
        LocationData(base_location_id + 343, "Arctic World"),
    "Arctic World: Minikit the Shark's Minikit":
        LocationData(base_location_id + 344, "Arctic World"),
    "Arctic World: Minikit complete the Button Puzzle":
        LocationData(base_location_id + 345, "Arctic World"),
    "Arctic World: Minikit slide Through the Yellow Gates":
        LocationData(base_location_id + 346, "Arctic World"),
    "Arctic World: Minikit in the Air Above the Silver Legos":
        LocationData(base_location_id + 347, "Arctic World"),
    "Arctic World: Minikit underwater in Final Room":
        LocationData(base_location_id + 348, "Arctic World"),
    "Arctic World: Minikit in the Hanging Silver Cage":
        LocationData(base_location_id + 349, "Arctic World"),
    # A Surprise for the Commissioner
    "A Surprise for the Commissioner: Minikit on Ledge Left of Spawn":
        LocationData(base_location_id + 350, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit behind the Glass Window":
        LocationData(base_location_id + 351, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit freeze Ice Cream Cones":
        LocationData(base_location_id + 352, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit inside the Vending Machine In Hostage Room":
        LocationData(base_location_id + 353, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit behind the Door Above the Grapple":
        LocationData(base_location_id + 354, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit on the Roller Coaster Slope":
        LocationData(base_location_id + 355, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit on the Ledge Above the Silver Lego Antenna":
        LocationData(base_location_id + 356, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit underwater in the Duck Pond":
        LocationData(base_location_id + 357, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit from Parking 4 Trucks":
        LocationData(base_location_id + 358, "A Surprise for the Commissioner"),
    "A Surprise for the Commissioner: Minikit bring Ice Cream Truck to Garage":
        LocationData(base_location_id + 359, "A Surprise for the Commissioner"),
    #Biplane Blast
    "Biplane Blast: Minikit destroy Brown Towers":
        LocationData(base_location_id + 360, "Biplane Blast"),
    "Biplane Blast: Minikit in the Chapel Tower":
        LocationData(base_location_id + 361, "Biplane Blast"),
    "Biplane Blast: Minikit activate the Signal Tower":
        LocationData(base_location_id + 362, "Biplane Blast"),
    "Biplane Blast: Minikit shoot Joker Balloons":
        LocationData(base_location_id + 363, "Biplane Blast"),
    "Biplane Blast: Minikit destroy Cages from the Joker Shield":
        LocationData(base_location_id + 364, "Biplane Blast"),
    "Biplane Blast: Minikit inside the Silver Air Conditioner":
        LocationData(base_location_id + 365, "Biplane Blast"),
    "Biplane Blast: Minikit on Other Side of the Scarecrow Billboard":
        LocationData(base_location_id + 366, "Biplane Blast"),
    "Biplane Blast: Minikit behind the Crane":
        LocationData(base_location_id + 367, "Biplane Blast"),
    "Biplane Blast: Minikit inside Silver Lego Tank":
        LocationData(base_location_id + 368, "Biplane Blast"),
    "Biplane Blast: Minikit inside Silver Lego Cage by Bat Symbol":
        LocationData(base_location_id + 369, "Biplane Blast"),
    #The Joker's Masterpiece
    "The Joker's Masterpiece: Minikit smash Containers":
        LocationData(base_location_id + 370, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit behind the Laser Grid":
        LocationData(base_location_id + 371, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit drop the Statue off the Ledge":
        LocationData(base_location_id + 372, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit open the Painting Behind the Pillars":
        LocationData(base_location_id + 373, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit in Glass Display Case in Gas Room":
        LocationData(base_location_id + 374, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit behind Pushable Wall":
        LocationData(base_location_id + 375, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit build the Joker's Face":
        LocationData(base_location_id + 376, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit in the Wooden Crate Dropped from Hypnotized Man":
        LocationData(base_location_id + 377, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit in the Vent":
        LocationData(base_location_id + 378, "The Joker's Masterpiece"),
    "The Joker's Masterpiece: Minikit from using the Generator Twice":
        LocationData(base_location_id + 379, "The Joker's Masterpiece"),
    # The Lure of the Night
    "The Lure of the Night: Minikit inside the Silver Lego Box Dropped by Hypnotized Man":
        LocationData(base_location_id + 380, "The Lure of the Night"),
    "The Lure of the Night: Minikit build the Green ?":
        LocationData(base_location_id + 381, "The Lure of the Night"),
    "The Lure of the Night: Minikit build and Connect the Battery":
        LocationData(base_location_id + 382, "The Lure of the Night"),
    "The Lure of the Night: Minikit navigate the Boat around the Circuit":
        LocationData(base_location_id + 383, "The Lure of the Night"),
    "The Lure of the Night: Minikit above the Magnet Wall":
        LocationData(base_location_id + 384, "The Lure of the Night"),
    "The Lure of the Night: Minikit behind Silver Lego Door":
        LocationData(base_location_id + 385, "The Lure of the Night"),
    "The Lure of the Night: Minikit destroy Fire Hydrants":
        LocationData(base_location_id + 386, "The Lure of the Night"),
    "The Lure of the Night: Minikit behind the Purple and Green Climbing Set in Playground":
        LocationData(base_location_id + 387, "The Lure of the Night"),
    "The Lure of the Night: Minikit behind Silver Lego Vault Doors":
        LocationData(base_location_id + 388, "The Lure of the Night"),
    "The Lure of the Night: Minikit in the Underwater Glass Cage":
        LocationData(base_location_id + 389, "The Lure of the Night"),
    # Dying of Laughter
    "Dying of Laughter: Minikit on the Tightrope above the Potted Plants":
        LocationData(base_location_id + 390, "Dying of Laughter"),
    "Dying of Laughter: Minikit behind the Glass Window on the Wooden Platform":
        LocationData(base_location_id + 391, "Dying of Laughter"),
    "Dying of Laughter: Minikit from Inside the Altar":
        LocationData(base_location_id + 392, "Dying of Laughter"),
    "Dying of Laughter: Minikit above the Ladder Built from Destroying Silver Legos":
        LocationData(base_location_id + 393, "Dying of Laughter"),
    "Dying of Laughter: Minikit above the Magnet Wall after Second Double Button":
        LocationData(base_location_id + 394, "Dying of Laughter"),
    "Dying of Laughter: Minikit inside the Wooden Box next to the Elevator":
        LocationData(base_location_id + 395, "Dying of Laughter"),
    "Dying of Laughter: Minikit on the Platform Across from the Wooden Box":
        LocationData(base_location_id + 396, "Dying of Laughter"),
    "Dying of Laughter: Minikit build and Destroy the Ice Sculpture":
        LocationData(base_location_id + 397, "Dying of Laughter"),
    "Dying of Laughter: Minikit ring the Left Bell":
        LocationData(base_location_id + 398, "Dying of Laughter"),
    "Dying of Laughter: Minikit ringing Both Bells with the Turret":
        LocationData(base_location_id + 399, "Dying of Laughter"),
}

# hostage_location_table: dict[str, int] = {
#"You can Bank on Batman: Hostage": base_location_id + 400,
# "An Icy Reception: Hostage" base_location_id + 401,
# "A Poisonous Appointment: Hostage", base_location_id + 402,
# "The Face-Off: Hostage", base_location_id + 403,
# "There She Goes Again: Hostage", base_location_id + 404,
# "Under The City: Hostage", base_location_id + 405,
# "Zoo's Company: Hostage", base_location_id + 406,
# "Penguin's Lair: Hostage", base_location_id + 407,
# "Joker's Home Turf: Hostage", base_location_id + 408,
# "Little Fun at the Big Top: Hostage", base_location_id + 409,
# "In the Dark Night: Hostage", base_location_id + 410,
# "To the Top of the Tower: Hostage", base_location_id + 411,
# "The Riddler Makes a Withdrawal: Hostage", base_location_id + 412,
# "On the Rocks: Hostage", base_location_id + 413,
# "Green Fingers: Hostage", base_location_id + 414,
# "An Enterprising Theft: Hostage", base_location_id + 415,
# "Breaking Blocks: Hostage", base_location_id + 416,
# "Rockin' the Docks: Hostage", base_location_id + 417,
# "Stealing the Show: Hostage", base_location_id + 418,
# "A Daring Rescue: Hostage", base_location_id + 419,
# "Arctic World: Hostage", base_location_id + 420,
# "A Surprise for the Commissioner: Hostage", base_location_id + 421,
# "The Joker's Masterpiece: Hostage", base_location_id + 422,
# "The Lure of the Night: Hostage", base_location_id + 423,
# "Dying of Laughter: Hostage", base_location_id + 424,
# }

location_table = {
    **minikit_location_table,
    # **hostage_location_table
}
