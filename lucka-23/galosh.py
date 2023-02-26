problem = "7<7g1<3g2<8g3g2g2<8g5<7g3<5g1g3<1g8<2g6g3g2<3g8<4<3g6<5<9g5<7<9<7<2g3<7<6<7g5g5g1<7<8g8g7g3g7g6g7<4<4g7<6g5<8g2<8<2<8g5<8g1g5<5g7<2<3<9g3<6g4<8<3<5g1g3g5<5g3g2g7g5g6g9<3g7g7<8g4<2<3g3<8g9g8g9<4<5<8g9g2g8<2<2<9<3<5<4g7g4g7<3g6g5<8g9<1g8<4<3<4<8<5g9<9g8<4g3<6<1<3g7<6g6g2g1g2<1<2g4<6<3<5<2g9<7<5<6<4g7<2<9<8g7<9g8<1<1g3<7<1g3<5g3<3<5<5<1g6g8<8g7g1g1<3g4<7<4g5g3g6<2<5<6<8<5<5<6<2<1g4g8<2g4g5g3g3g7<2<7<3g2g9<9g5<6<4g4<4g4<1<7g5g7g8g9g5<9<5<7g2g8g5<1<6g8<3g2<7<6g6g1<9<6g8g1g3g4<2g9<3<3g6<2<5g5g6g4g5g8g5<3<8<2<6g5<7<4g8g5<1g2g7<7g9g1g6g4g8g2g9<4<4<7g8g9<2g6g9g8<4<3<3g2g8g6<1<4g7g2<3g7<6<4g8<6<9<2g4g6g7<8<2g7<9<5g8<6<3<5g1g3g3<3<5<7<9<1<1g2g1<7<8<2<3<6<1<8g1<3<3<9g2g5<4<1<5<3g7<1g9<5<8g4g8g4<9<4g6g5<7<7<3g6<2g5<5<1g2<1g2g3<2<8g9<1<8g7g7<3<4g1g6<7<8<7g5g2g9g3<1<7<8g6g8g4<4<9<7g8g4<1<6<2<8g9g6g3g7g2<7<3g4g3g2g1<1<8<8<8g5g2<6<4<3g1g8g6g2<6<5g4<8g7g2<3<2g7g7g1<3g4g1<8<3g4<4<1<1<8<8<6<1<2g3g5<8<8<9<1<5<6<1g4<9<4<6<1<7g7g4g6g6g9<4g4g1<8<2g7g3g8<7g1<2<4<3<2<9g5g7g4<9<8g7<9g5g9<9<2<1<8g6<2g3<2<1<2<3g7<6"

problem2 = ""
for index, char in enumerate(problem):
    if char == '<':
        # if i is a <, check if it can be divided by 3. If it can be divided by three, replace < with + , else replace with -.
        prev = int(problem[index-1])
        if prev % 3 > 0:
            problem2 += '+'
        else:
            problem2 += '-'
    elif char == 'g':
        # if i is a g, check if the number before can't be divided by 2. If it can be divided by two, replace g with -, else replace with +.
        prev = int(problem[index-1])
        if prev % 2 > 0:
            problem2 += '-'
        else:
            problem2 += '+'
    else:
        problem2 += char

result = eval(problem2)
print(result)
