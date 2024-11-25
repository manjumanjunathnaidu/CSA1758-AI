% Facts: Diseases and their recommended diet
diet_for_disease(diabetes, [low_carb, high_fiber, lean_protein, green_vegetables]).
diet_for_disease(hypertension, [low_sodium, high_potassium, whole_grains, fruits, vegetables]).
diet_for_disease(obesity, [low_calorie, high_protein, vegetables, fruits, whole_grains]).
diet_for_disease(cardiovascular, [low_fat, omega_3, whole_grains, nuts, leafy_greens]).
diet_for_disease(anemia, [iron_rich, vitamin_c, lean_meat, spinach, citrus_fruits]).

% Facts: Food categories for better suggestions
food_category(low_carb, [broccoli, cauliflower, eggs, chicken, fish]).
food_category(high_fiber, [oats, lentils, beans, apples, carrots]).
food_category(low_sodium, [fresh_fruits, unsalted_nuts, low_sodium_bread]).
food_category(high_potassium, [bananas, sweet_potatoes, spinach, avocados]).
food_category(iron_rich, [spinach, red_meat, lentils, tofu, pumpkin_seeds]).
food_category(omega_3, [salmon, flaxseeds, walnuts, chia_seeds]).
food_category(low_fat, [low_fat_yogurt, skim_milk, lean_chicken, fish]).

% Rule: Suggest diet based on disease
suggest_diet(Disease, Diet) :-
    diet_for_disease(Disease, Diet).

% Rule: Suggest specific foods for a disease
suggest_foods(Disease, Foods) :-
    diet_for_disease(Disease, Diet),
    findall(Food, (member(Category, Diet), food_category(Category, FoodList), member(Food, FoodList)), Foods).