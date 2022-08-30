# Leetcode 13 - Roman to Integer [Easy]

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Lager en dict med korresponderende verdier:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        t = []

        # Vi mapper rett verdi til rett romertall og legger i lista:
        for letter in s:
            t.append(dict[letter])

        # Sammenligner størrelse på hvert tall med det neste tallet i lista:
        u = 0

        while u < len(t) - 1:
            if t[u] < t[u + 1]:
                t[u] = t[u] * (-1) # multipliserer med -1 dersom tallet er mindre enn det neste

            u = u + 1

        return sum(t)
