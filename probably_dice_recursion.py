#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def number_count(dice_number, sides, target):
	if target < dice_number or target > sides * dice_number:
		return 0
	if dice_number == 1:
		return 1
	else:
		counts = 0
		counts = sum([number_count(dice_number - 1, sides, target - i) for i in range(1, sides + 1)]) 
		
		return counts

def probability(dice_number, sides, target):
	if target < dice_number or target > sides * dice_number:
		return 0.0
	total_pbt = pow(sides, dice_number)
	num_count = number_count(dice_number, sides, target)
	
	return num_count / total_pbt
	

if __name__ == '__main__':
	# These are only used for self-checking and are not necessary for auto-testing
	def almost_equal(checked, correct, significant_digits=4):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision

	assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
	assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
	assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
	assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
	assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
	assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
	start = time.time()
	assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
	print time.time() - start
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

