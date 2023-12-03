from functools import reduce
import re
rawdata = ""

with open("data.txt", "r") as file:
    rawdata = file.read()

splitted_engine = rawdata.split('\n')

def get_posible_pieces(engine):
    posible_pieces = []
    for index, engine_line in enumerate(engine):
        for match in re.finditer("\d+", engine_line):
            piece = {
                "number": int(match.group(0)),
                "line": index,
                "positions": [],
                "max_pos": len(engine_line) -1
            }
            for pos in range(match.start(), match.end()):
                piece["positions"].append(pos)
            posible_pieces.append(piece)

    return posible_pieces

def get_true_pieces(posible_pieces, engine):
    true_pieces = []

    def is_piece(piece):
        line = piece['line']
        checks = []

        def check_line(line):
            min_index = piece['positions'][0] if piece['positions'][0] == 0 else piece['positions'][0] - 1
            max_index = piece['positions'][-1] if piece['positions'][-1] == piece['max_pos'] else piece['positions'][-1] + 1
            checks.append(bool(re.search("[^\w.]", engine[line][min_index:max_index + 1])))
            
        if not line == 0: check_line(line - 1)
        check_line(line)
        if not line == len(engine) - 1: check_line(line + 1)

        return reduce(lambda a,b : a or b, checks)

    for posible_piece in posible_pieces:
        if is_piece(posible_piece): true_pieces.append(posible_piece)
    
    return true_pieces
    

posible_pieces =  get_posible_pieces(splitted_engine)
pieces = get_true_pieces(posible_pieces, splitted_engine)
pieces_value = [piece['number'] for piece in pieces]
total_pieces_value = reduce(lambda a,b : a+b, pieces_value)


print(total_pieces_value)