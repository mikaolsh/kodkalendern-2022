lista = [[22, 6, 191], [12, 6, 159], [12, 37, 301], [20, 29, 23], [12, 19, 9], [22, 31, 42], [15, 26, 101], [7, 42, 257], [23, 8, 298], [16, 5, 220], [9, 43, 70], [21, 21, 1], [26, 47, 58], [29, 50, 271], [7, 1, 221], [14, 13, 122], [23, 30, 208], [22, 16, 132], [13, 17, 245], [8, 16, 277], [23, 49, 59], [19, 39, 135], [12, 9, 236], [14, 50, 111], [15, 23, 21], [29, 48, 117], [20, 37, 305], [18, 25, 164], [29, 40, 61], [13, 43, 206], [30, 46, 48], [15, 18, 158], [22, 1, 267], [5, 11, 145], [6, 48, 131], [11, 45, 223], [18, 50, 188], [12, 17, 203], [6, 9, 136], [9, 33, 169], [5, 33, 229], [9, 1, 263], [6, 7, 155], [16, 37, 298], [23, 23, 122], [31, 42, 298], [23, 14, 154], [17, 32, 282], [8, 26, 140], [31, 37, 80], [15, 1, 305], [26, 18, 11], [12, 28, 251], [12, 23, 106], [27, 8, 64], [19, 30, 152], [25, 23, 74], [28, 43, 120], [7, 20, 143], [12, 31, 258], [29, 21, 270], [27, 1, 68], [16, 20, 17], [13, 37, 125], [19, 40, 256], [27, 24, 25], [15, 3, 232], [32, 17, 226], [26, 6, 246], [12, 39, 303], [20, 29, 168], [5, 0, 19], [31, 36, 278], [23, 14, 225], [22, 13, 237], [23, 26, 56], [27, 45, 209], [24, 48, 96], [13, 29, 1], [10, 18, 35], [21, 6, 118], [12, 49, 59], [21, 41, 152], [13, 40, 41], [13, 17, 243], [22, 32, 66], [14, 37, 6], [13, 13, 169], [26, 3, 189], [29, 37, 153], [14, 33, 228], [22, 29, 281], [10, 40, 27], [17, 36, 77], [23, 9, 34], [5, 35, 172], [20, 18, 185], [19, 44, 48], [14, 49, 221], [26, 0, 288]]

qualified = 0

for age in lista:
    if age[0] * 16 * 26 + age[1] * 26 + age[2] >= 10_000:
        qualified += 1

print(qualified)
