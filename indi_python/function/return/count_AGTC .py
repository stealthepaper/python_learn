def count_AGTC(nucleotide_str):
    a_nuc = nucleotide_str.count("A")
    g_nuc = nucleotide_str.count("G")
    c_nuc = nucleotide_str.count("C")
    t_nuc = nucleotide_str.count("T")
    count_list = [a_nuc,g_nuc,t_nuc,c_nuc]
    return tuple(count_list)


print(count_AGTC('AGGTC')) #(1, 2, 1, 1)
print(count_AGTC('AAAATTT')) #(4, 0, 3, 0)
print(count_AGTC('AGTTTTT')) #(1, 1, 5, 0)
print(count_AGTC('CCT')) #(0, 0, 1, 2)