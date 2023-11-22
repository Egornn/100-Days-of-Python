import pytest


class AverageCalculator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, input_list):
        if not input_list:
            return 0
        return sum(input_list) / len(input_list)

    def compare_averages(self):
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


def test_compare_averages_list1_greater():
    calc = AverageCalculator([1, 2, 3], [1, 2, 2])
    assert calc.compare_averages() == "Первый список имеет большее среднее значение"


def test_compare_averages_list2_greater():
    calc = AverageCalculator([1, 2, 2], [1, 2, 3])
    assert calc.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_equal():
    calc = AverageCalculator([1, 2, 3], [1, 2, 3])
    assert calc.compare_averages() == "Средние значения равны"


def test_compare_averages_empty_lists():
    calc = AverageCalculator([], [])
    assert calc.compare_averages() == "Средние значения равны"


def test_compare_averages_one_empty_list():
    calc = AverageCalculator([1, 2, 3], [])
    assert calc.compare_averages() == "Первый список имеет большее среднее значение"
