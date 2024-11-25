% Facts: planet(Name, Size, DistanceFromSun, NumberOfMoons, Type).
% Name: Name of the planet
% Size: Size of the planet in kilometers (approx. diameter)
% DistanceFromSun: Distance from the sun in million kilometers
% NumberOfMoons: Number of moons the planet has
% Type: Planet type (e.g., terrestrial, gas giant, ice giant)

planet("Mercury", 4879, 58, 0, terrestrial).
planet("Venus", 12104, 108, 0, terrestrial).
planet("Earth", 12742, 149, 1, terrestrial).
planet("Mars", 6779, 228, 2, terrestrial).
planet("Jupiter", 139820, 778, 79, gas_giant).
planet("Saturn", 116460, 1429, 83, gas_giant).
planet("Uranus", 50724, 2871, 27, ice_giant).
planet("Neptune", 49244, 4495, 14, ice_giant).

% Rules to retrieve information

% Find planets closer to the sun than a given distance
planets_closer_than(Distance, Name) :-
    planet(Name, _, DistFromSun, _, _),
    DistFromSun < Distance.

% Find planets of a specific type
planets_by_type(Type, Name) :-
    planet(Name, _, _, _, Type).

% Find planets with more than a specific number of moons
planets_with_moons(MinMoons, Name) :-
    planet(Name, _, _, NumMoons, _),
    NumMoons > MinMoons.

% Find planets larger than a given size
planets_larger_than(Size, Name) :-
    planet(Name, PlanetSize, _, _, _),
    PlanetSize > Size.