from enum import Enum

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(md:str):
    if 0 < md.split('\n')[0].count("#") < 7:
        return BlockType.heading
    elif md.split('\n')[0][:3]=="```" and md.split('\n')[-1][:3]=="```":
        return BlockType.code
    elif all(x[0]==">" for x in md.split('\n')):
        return BlockType.quote
    elif all(x[:2]=="- " for x in md.split('\n')):
        return BlockType.unordered_list
    elif all(i[0].isdigit() and i[1]=="." for i in [x[:2] for x in md.split('\n')]):
        ordered = [int(x[0]) for x in md.split('\n')]
        if list(range(1,len(ordered)+1)) == [int(x[0]) for x in md.split('\n')]:
            return BlockType.ordered_list
    return BlockType.paragraph

