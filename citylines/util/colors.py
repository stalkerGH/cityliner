from dataclasses import dataclass


@dataclass
class ColorScheme:
    funicular_cable_gondola: str
    ferry_water: str
    bus: str
    rail: str
    subway: str
    tram: str


# Default Scheme
default_scheme = ColorScheme(
    funicular_cable_gondola="#F761BF",
    ferry_water="#FF8000",
    bus="#E31B1C",
    rail="#708A91",
    subway="#4DAF4A",
    tram="#1A75D1"
)

# Pastel Scheme
pastel_scheme = ColorScheme(
    funicular_cable_gondola="#FFA8D8",
    ferry_water="#85acff",
    bus="#FF9999",
    rail="#A6A6A6",
    subway="#98E2A2",
    tram="#99CCFF"
)

inferno_scheme = ColorScheme(
    funicular_cable_gondola="#FF5733",  # Bright Orange
    ferry_water="#C70039",  # Dark Red
    bus="#FFC300",  # Bright Yellow
    rail="#DAF7A6",  # Pale Green
    subway="#581845",  # Dark Purple
    tram="#900C3F"  # Dark Magenta
)

# Earthy Scheme
earthy_scheme = ColorScheme(
    funicular_cable_gondola="#E89005",
    ferry_water="#55AA77",
    bus="#B36500",
    rail="#5D5D5D",
    subway="#44BB44",
    tram="#3377AA"
)

# Cool Scheme
cool_scheme = ColorScheme(
    funicular_cable_gondola="#8E2DE2",
    ferry_water="#2193B0",
    bus="#C32BAD",
    rail="#5D5DAA",
    subway="#4DFFB3",
    tram="#6761A8"
)

# GreenBlue Scheme
greenblue_scheme = ColorScheme(
    funicular_cable_gondola="#D0FF00",
    ferry_water="#90FF00",
    bus="#51FF00",
    rail="#00FF7D",
    subway="#00FFBC",
    tram="#00C2FF"
)

# BrwnYl Scheme (based on CartoColor scheme)
brownyellow_scheme = ColorScheme(
    funicular_cable_gondola="#11CC80",
    ferry_water="#6C2146",
    bus="#DC217F",
    rail="#F3E7D5",
    subway="#A3A3A3",
    tram="#DC7E76"
)

# Purp Scheme (based on CartoColor scheme)
purple_scheme = ColorScheme(
    funicular_cable_gondola="#654792",
    ferry_water="#C7A4E0",
    bus="#EDCFF2",
    rail="#DEB9EA",
    subway="#8E7BC1",
    tram="#FAE4F7"
)

# Mint Scheme (based on CartoColor scheme)
mint_scheme = ColorScheme(
    funicular_cable_gondola="#E3F3E6",
    ferry_water="#40B0AC",
    bus="#AEDED3",
    rail="#7AC8C0",
    subway="#00656C",
    tram="#009897"
)

# Prism Scheme (based on CartoColor scheme)
prism_scheme = ColorScheme(
    funicular_cable_gondola="#684D9E",
    ferry_water="#AF146D",
    bus="#00A773",
    rail="#0078A1",
    subway="#ED3F29",
    tram="#FFB100"
)

color_schemes = {
    'default': default_scheme,
    'pastel': pastel_scheme,
    'inferno': inferno_scheme,
    'earthy': earthy_scheme,
    'cool': cool_scheme,
    'greenblue': greenblue_scheme,
    'brownyellow': brownyellow_scheme,
    'purple': purple_scheme,
    'mint': mint_scheme,
    'prism': prism_scheme
}
