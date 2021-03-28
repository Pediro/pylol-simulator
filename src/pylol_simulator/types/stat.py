class Stat(object):

    def __init__(self, flat, percent, per_level, percent_per_level, percent_base, percent_bonus):
        self.flat = flat
        self.percent = percent
        self.per_level = per_level
        self.percent_per_level = percent_per_level
        self.percent_base = percent_base
        self.percent_bonus = percent_base

    def __str__(self) -> str:
        return f"Flat {self.flat}\t Percent {self.percent}\n"\
            f"Per Level {self.per_level}\t Percent Per Level {self.percent_per_level}\n"\
            f"Percent Base {self.percent_base}\tPercent Bonus {self.percent_bonus}\n"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other):
        return Stat(flat = self.flat + other.flat, \
                    percent = self.percent + other.percent, \
                    per_level = self.per_level + other.per_level, \
                    percent_per_level = self.percent_per_level + other.percent_per_level,\
                    percent_base = self.percent_base + other.percent_base, \
                    percent_bonus = self.percent_bonus + other.percent_bonus)