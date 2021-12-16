#!/usr/bin/env python

from math import prod


PACKET_TYPE_LITERAL_VALUE = 4
LENGTH_TYPE_BITS = 0
LENGTH_TYPE_PACKETS = 1
OPERATOR_TYPE_SUM = 0
OPERATOR_TYPE_PROD = 1
OPERATOR_TYPE_MIN = 2
OPERATOR_TYPE_MAX = 3
OPERATOR_TYPE_GT = 5
OPERATOR_TYPE_LT = 6
OPERATOR_TYPE_EQ = 7


class Packet:
    def __init__(self, version, type_id, number=0):
        self.version = version
        self.type_id = type_id
        self.number = number
        self.subpackets = []

    def add_subpacket(self, packet):
        self.subpackets.append(packet)

    def get_value(self):
        if self.type_id == PACKET_TYPE_LITERAL_VALUE:
            return self.number
        elif self.type_id == OPERATOR_TYPE_SUM:
            return sum(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_PROD:
            return prod(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_MIN:
            return min(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_MAX:
            return max(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_GT:
            if len(self.subpackets) != 2:
                raise AssertionError("Operator '>' needs exactly two subpackets")
            return int(self.subpackets[0].get_value() > self.subpackets[1].get_value())
        elif self.type_id == OPERATOR_TYPE_LT:
            if len(self.subpackets) != 2:
                raise AssertionError("Operator '<' needs exactly two subpackets")
            return int(self.subpackets[0].get_value() < self.subpackets[1].get_value())
        elif self.type_id == OPERATOR_TYPE_EQ:
            if len(self.subpackets) != 2:
                raise AssertionError("Operator '==' needs exactly two subpackets")
            return int(self.subpackets[0].get_value() == self.subpackets[1].get_value())

    def get_version_sum(self):
        return self.version + sum(p.get_version_sum() for p in self.subpackets)


def read_bits(data, start, length):
    return int(data[start : start + length], 2), start + length


def read_packet(data, pointer):
    """
    Reads a single packet from data, starting at pointer. Includes subpackets and assumes the data is correct.
    Returns the subtree and the new pointer.
    """
    version, pointer = read_bits(data, pointer, 3)
    type_id, pointer = read_bits(data, pointer, 3)

    if type_id == PACKET_TYPE_LITERAL_VALUE:
        number_bits = ""
        read_next = True
        while read_next:
            read_next = data[pointer] == "1"
            number_bits += data[pointer + 1 : pointer + 5]
            pointer += 5
        number = int(number_bits, 2)
        return Packet(version, type_id, number), pointer
    else:
        length_type_id, pointer = read_bits(data, pointer, 1)
        length_size = 15 if length_type_id == LENGTH_TYPE_BITS else 11
        length, pointer = read_bits(data, pointer, length_size)
        packet = Packet(version, type_id)
        if length_type_id == LENGTH_TYPE_PACKETS:
            for _ in range(length):
                subpacket, pointer = read_packet(data, pointer)
                packet.add_subpacket(subpacket)
        else:  # LENGTH_TYPE_BITS
            pointer_target = pointer + length
            while pointer < pointer_target:
                subpacket, pointer = read_packet(data, pointer)
                packet.add_subpacket(subpacket)
        return packet, pointer


with open("../input/16") as f:
    rawdata = f.readline().strip()
    # TEST: literal packet
    # rawdata = "D2FE28"
    # TEST: operator packet, length type 0
    # rawdata = "38006F45291200"
    fulldata = bin(int(rawdata, 16))[2:].rjust(4 * len(rawdata), "0")

# Assume just 1 packet at the outermost level
expression, _ = read_packet(fulldata, 0)
print(f"Part 1: {expression.get_version_sum()}")
print(f"Part 2: {expression.get_value()}")
