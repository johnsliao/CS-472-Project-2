## John Liao
## CS 472 - SUMMER 2015
## Project #1

def parse_bits_26_31(instruction):
    return instruction & 0xFC000000

def parse_bits_21_25(instruction):
    return instruction & 0x3E00000

def parse_bits_16_20(instruction):
    return instruction & 0x1F0000

def parse_bits_11_15(instruction):
    return instruction & 0xF800

def parse_bits_0_5(instruction):
    return instruction & 0x3F

def parse_bits_0_15(instruction):
    return instruction & 0xFFFF

def twos_comp(val):
    if val >> 15 == 1: # if signed bit is set
        val -= 2**16 # convert value as signed *int* [val - 2^16]
    return val # else return as normal

def main():
    instructions = [0x022DA822, 0x8EF30018, 0x12A70004, 0x02689820, 0xAD930018, 0x02697824, 0xAD8FFFF4, 
0x018C6020, 0x02A4A825, 0x158FFFF6, 0x8E59FFF0]

    current_address = 0x7A060 # start @ address 0x7A060

    for instruction in instructions:
        assy_instruction = hex(current_address) + ' '

        opcode = parse_bits_26_31(instruction) >> 26

        if opcode == 0: # R format
            src1 = parse_bits_21_25(instruction)
            src2 = parse_bits_16_20(instruction)
            dest = parse_bits_11_15(instruction)
            # disregard bits 6-10...
            func = parse_bits_0_5(instruction)

            if func == 32:
                assy_instruction += 'add'
            elif func == 34:
                assy_instruction += 'sub'
            elif func == 36:
                assy_instruction += 'and'            
            elif func == 37:
                assy_instruction += 'or'
            elif func == 42:
                assy_instruction += 'slt'
            else:
                assy_instruction += 'ERROR NOT FOUND'

            # $dest, $src1, $src2
            assy_instruction += ' $'
            assy_instruction += str(dest>>11)
            assy_instruction += ', $'
            assy_instruction += str(src1>>21)
            assy_instruction += ', $'
            assy_instruction += str(src2>>16)
            
        else: # I FORMAT
            src1 = parse_bits_21_25(instruction)
            dest = parse_bits_16_20(instruction)
            offset = parse_bits_0_15(instruction)

            if opcode == 4:
                assy_instruction += 'beq'
            elif opcode == 5:
                assy_instruction += 'bne'
            elif opcode == 35:
                assy_instruction += 'lw'
            elif opcode == 43:
                assy_instruction += 'sw'
            else:
                assy_instruction += 'ERROR NOT FOUND'

            offset = twos_comp(offset) # account for signed integer, which isn't directly supported in Python

            if opcode == 35 or opcode == 43: # lw/sw
                # $dest, offset ($src)
                assy_instruction += ' $'
                assy_instruction += str(dest>>16)
                assy_instruction += ', '
                assy_instruction += str(offset)
                assy_instruction += '($'
                assy_instruction += str(src1>>21)
                assy_instruction += ')'
            elif opcode == 4 or opcode == 5: # bne/beq
                print offset, hex(offset)
                print 'current address is', hex(current_address)
                print hex(current_address+offset)

                assy_instruction += ' $'
                assy_instruction += str(src1>>21)
                assy_instruction += ', $'
                assy_instruction += str(dest>>16)
                assy_instruction += ', address '
                assy_instruction += hex(current_address + 4 * offset + 4) # extra +4 for finished instruction, then "decompress" by multiplying by 4, then offset the address
            else:
                assy_instruction += 'ERROR NOT FOUND'

        current_address += 4
        print assy_instruction
        
if __name__ == '__main__':
    main()
