def select_all_columns_and_rows():
    return "Select * from planets;"

def select_name_and_color_of_all_planets():
    return "select name, color from planets;"

def select_all_planets_with_mass_greater_than_one():
    return "select * from planets where mass > 1;"

def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    return "select name, mass from planets where mass <=1;"

def select_name_and_color_of_planets_with_more_than_10_moons():
    return "select name, color from planets where num_of_moons > 10;"

def select_all_planets_with_moons_and_mass_less_than_one():
    return "select * from planets where num_of_moons > 0 and mass < 1;"

def select_name_and_color_of_all_blue_planets():
    return "select name, color from planets where color like '%blue%';"
