import itertools
# import Q1_Combinations
# import Q2_Combinations
# import Q3_Combinations
# import Q4_Combinations

squares = {}

cell_counter = 0
for i in range(6):
    row = i
    for j in range(6):
        column = j
        cell = {
        "name":cell_counter,
        "indices":[i,j]
        }
        squares[cell_counter] = cell
        cell_counter += 1



def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append([i-1, j])
    if i+1 < m:
        adjacent_indices.append([i+1, j])
    if j > 0:
        adjacent_indices.append([i, j-1])
    if j+1 < n:
        adjacent_indices.append([i, j+1])
    return adjacent_indices


for i in range(0, len(squares)):
    square = squares[i]
    adjacents = get_adjacent_indices(square["indices"][0], square["indices"][1], 6, 6)
    squares[i]["adjacents"] = adjacents


r = "red"
l = "light"
d = "dark"

colors = [
d, d, l, d, l, r,
l, d, l, d, d, d,
l, d, l, d, l, d,
d, l, r, l, l, l,
r, d, d, l, l, r,
d, l, l, d, d, l,
]



for i in range(len(colors)):
    squares[i]["color"] = colors[i]


# q_1_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 24, 25, 30,]
# q_2_cells = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 16, 17, 21, 22, 23, 28, 29, 35,]
# q_3_cells = [5, 10, 11, 15, 16, 17, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,]
# q_4_cells = [0, 6, 7, 12, 13, 14, 18, 19, 20, 21, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35,]


# q_1_cells = [0, 1, 2, 6, 7, 8, 12, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 32,]
# q_2_cells = [3, 4, 5, 9, 10, 11, 15, 16, 17, 21, 22, 23, 27, 28, 29, 33, 34, 35,]
# q_3_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,]
# q_4_cells = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,]

q_1_cells = [0, 1, 2, 6, 7, 8, 12, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 32,]
q_2_cells = [0, 1, 2, 6, 7, 8, 12, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 32,]
q_3_cells = [3, 4, 5, 9, 10, 11, 15, 16, 17, 21, 22, 23, 27, 28, 29, 33, 34, 35,]
q_4_cells = [3, 4, 5, 9, 10, 11, 15, 16, 17, 21, 22, 23, 27, 28, 29, 33, 34, 35,]



def combinations(cells):
    step_1_tups = []
    for combo in itertools.combinations(cells, 9):
        step_1_tups.append(combo)

    # print(len(step_1_tups))



    step_2_tups = []

    def adjacency_checker(tup):
        for sq in tup[1:]:
            # other_square = squares[sq]
            for s in main_blob:
                if squares[sq]['indices'] in squares[s]['adjacents']:
                    main_blob.append(squares[sq]['name'])
                    tup = list(filter(lambda num: num != sq, tup))
                    return adjacency_checker(tup)
                else:
                    other_blob.append(squares[sq]['name'])

        # print(main_blob)
        if len(main_blob) >= 9:
            return main_blob


    for combo in step_1_tups:
        main_blob = [combo[0]]
        other_blob = []
        current = adjacency_checker(combo)
        if current:
            step_2_tups.append(current)

    # print(len(step_2_tups))


    ###### got the recursive function working above.  need to work this into the actual.
    ###### also need to handle that main_blob and other_blob will need to be reset every time.




    step_3_tups = []

    for tup in step_2_tups:
        color_lst = []
        for col in tup:
            color_lst.append(squares[col]['color'])

        if color_lst.count('dark') == 4 and color_lst.count('light') == 4 and color_lst.count('red') == 1:
            step_3_tups.append(tup)


    # print(len(step_3_tups))

    # for tup in step_3_tups:
    #     print(tup)
    return step_3_tups



q1_combinations = combinations(q_1_cells)
q2_combinations = combinations(q_2_cells)
q3_combinations = combinations(q_3_cells)
q4_combinations = combinations(q_4_cells)


possible_combos = []
cycle = 1
for tup1 in q1_combinations:
    temp_combo = [tup1,]
    for tup2 in q2_combinations:
        check2 = any(item in tup1 for item in tup2)
        if not check2:
            temp_combo = [tup1, tup2]
            for tup3 in q3_combinations:
                check3a = any(item in tup1 for item in tup3)
                check3b = any(item in tup2 for item in tup3)
                if not check3a and not check3b:
                    temp_combo = [tup1, tup2, tup3]
                    for tup4 in q4_combinations:
                        check4a = any(item in tup1 for item in tup4)
                        check4b = any(item in tup2 for item in tup4)
                        check4c = any(item in tup3 for item in tup4)
                        if not check4a and not check4b and not check4c:
                            temp_combo = [tup1, tup2, tup3, tup4]
                            temp_combo = sorted(temp_combo)
                            if temp_combo not in possible_combos:
                                possible_combos.append(temp_combo)
    # print(temp_combo)
    # if len(temp_combo) >= 4:
    #     possible_combos.append(temp_combo)
    print(cycle)
    cycle+=1
possible_combos_sorted = []
for combo in possible_combos:
    temp = []
    for tup in combo:
        tup.sort()
        temp.append(tup)
    temp.sort()
    possible_combos_sorted.append(temp)
print("possible combos:")
print(len(possible_combos_sorted))
# for combo in possible_combos_sorted:
#     print(combo)



##############################################
##############################################
##############################################
##############################################


def reverse_coords(coord):
    temp = []
    for num in coord:
        if num == 0:
            temp.append(5)
        if num == 1:
            temp.append(4)
        if num == 2:
            temp.append(3)
        if num == 3:
            temp.append(2)
        if num == 4:
            temp.append(1)
        if num == 5:
            temp.append(0)
    return temp

def reverse_coords_vert_only(coord):
    temp = []
    row = coord[0]
    if row == 0:
        temp=[5, coord[1]]
    if row == 1:
        temp=[4, coord[1]]
    if row == 2:
        temp=[3, coord[1]]
    if row == 3:
        temp=[2, coord[1]]
    if row == 4:
        temp=[1, coord[1]]
    if row == 5:
        temp=[0, coord[1]]
    return temp

def reverse_coords_horiz_only(coord):
    temp = []
    column = coord[1]
    if column == 0:
        temp=[coord[0], 5]
    if column == 1:
        temp=[coord[0], 4]
    if column == 2:
        temp=[coord[0], 3]
    if column == 3:
        temp=[coord[0], 2]
    if column == 4:
        temp=[coord[0], 1]
    if column == 5:
        temp=[coord[0], 0]
    return temp

def flip_along_vert_half(coord):
    temp = []
    column = coord[1]
    if column == 0:
        temp=[coord[0], 2]
    if column == 1:
        temp=[coord[0], 1]
    if column == 2:
        temp=[coord[0], 0]
    if column == 3:
        temp=[coord[0], 5]
    if column == 4:
        temp=[coord[0], 4]
    if column == 5:
        temp=[coord[0], 3]
    return temp

def flip_along_horiz_half(coord):
    temp = []
    row = coord[0]
    if row == 0:
        temp=[2, coord[1]]
    if row == 1:
        temp=[1, coord[1]]
    if row == 2:
        temp=[0, coord[1]]
    if row == 3:
        temp=[5, coord[1]]
    if row == 4:
        temp=[4, coord[1]]
    if row == 5:
        temp=[3, coord[1]]
    return temp

# for sq in squares:
#     print(squares[sq]['name'])
#     print(reverse_coords_horiz_only(squares[sq]['indices']))


def distances(tup):
    inds = []
    for sq in tup:
        inds.append(squares[sq]['indices'])
    inds.sort()
    return inds
    # print(inds)

def compare_shapes(tup1, tup2):
    coords1 = distances(tup1)
    coords2 = distances(tup2)
    reverse_coords2 = []
    for coord in coords2:
        reverse_coords2.append(reverse_coords(coord))
    reverse_coords2.sort()
    reverse_coords2_vert = []
    for coord in coords2:
        reverse_coords2_vert.append(reverse_coords_vert_only(coord))
    reverse_coords2_vert.sort()
    reverse_coords2_horiz = []
    for coord in coords2:
        reverse_coords2_horiz.append(reverse_coords_horiz_only(coord))
    reverse_coords2_horiz.sort()
    flip_coords2_vert_half = []
    for coord in coords2:
        flip_coords2_vert_half.append(flip_along_vert_half(coord))
    flip_coords2_vert_half.sort()
    flip_coords2_vert_half_then_horiz = []
    for coord in flip_coords2_vert_half:
        flip_coords2_vert_half_then_horiz.append(reverse_coords_horiz_only(coord))
    flip_coords2_vert_half_then_horiz.sort()
    flip_coords2_vert_half_then_vert = []
    for coord in flip_coords2_vert_half:
        flip_coords2_vert_half_then_vert.append(reverse_coords_vert_only(coord))
    flip_coords2_vert_half_then_vert.sort()
    flip_coords2_horiz_half = []
    for coord in coords2:
        flip_coords2_horiz_half.append(flip_along_horiz_half(coord))
    flip_coords2_horiz_half.sort()
    flip_coords2_horiz_half_then_vert = []
    for coord in flip_coords2_horiz_half:
        flip_coords2_horiz_half_then_vert.append(reverse_coords_vert_only(coord))
    flip_coords2_horiz_half_then_vert.sort()
    flip_coords2_horiz_half_then_horiz = []
    for coord in flip_coords2_horiz_half:
        flip_coords2_horiz_half_then_horiz.append(reverse_coords_horiz_only(coord))
    flip_coords2_horiz_half_then_horiz.sort()
    # print(coords1)
    # print(coords2)
    if coords1 == reverse_coords2:
        # print(reverse_coords2)
        return True
    elif coords1 == reverse_coords2_vert:
        # print(reverse_coords2_vert)
        return True
    elif coords1 == reverse_coords2_horiz:
        # print(reverse_coords2_horiz)
        return True
    elif coords1 == flip_coords2_vert_half:
        # print(flip_coords2_vert_half)
        return True
    elif coords1 == flip_coords2_vert_half_then_horiz:
        # print(flip_coords2_vert_half_then_horiz)
        return True
    elif coords1 == flip_coords2_vert_half_then_vert:
        # print(flip_coords2_vert_half_then_vert)
        return True
    elif coords1 == flip_coords2_horiz_half:
        # print(flip_coords2_horiz_half)
        return True
    elif coords1 == flip_coords2_horiz_half_then_vert:
        # print(flip_coords2_horiz_half_then_vert)
        return True
    elif coords1 == flip_coords2_horiz_half_then_horiz:
        # print(flip_coords2_horiz_half_then_horiz)
        return True
    else:
        return False

for combo in possible_combos_sorted:
    outcomes = [combo[0],]
    for i in range(1, len(combo)):
        if compare_shapes(combo[0], combo[i]):
            outcomes.append(combo[i])
    if len(outcomes) == 4:
        print(outcomes)
