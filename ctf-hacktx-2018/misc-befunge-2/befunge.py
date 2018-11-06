#!/usr/bin/python
# Written by Cameron "Camdar" Wong

# See LICENSE for the working terms of this program.

import sys, random

DIRS = {
	'>': lambda x,y:(x+1,y),
	'<': lambda x,y:(x-1,y),
	'^': lambda x,y:(x,y-1),
	'v': lambda x,y:(x,y+1)
}

INSTRUCTIONS = {}

class inst_wrapper():
	__slots__ = ['char']
	def __init__(self, char): self.char = char
	def __call__(self, func):
		INSTRUCTIONS[self.char] = func
		return func


@inst_wrapper('+')
def befunge_add(state):
	b, a = state.pop(), state.pop()
	state.append(a+b)
@inst_wrapper('-')
def befunge_sub(state):
	b, a = state.pop(), state.pop()
	state.append(a-b)
@inst_wrapper('*')
def befunge_mul(state):
	b, a = state.pop(), state.pop()
	state.append(a*b)
@inst_wrapper('/')
def befunge_div(state):
	b, a = state.pop(), state.pop()
	state.append(a//b)
@inst_wrapper('%')
def befunge_mod(state):
	b, a = state.pop(), state.pop()
	state.append(a % b)
@inst_wrapper('!')
def befunge_not(state):
	state.append(int(not bool(state.pop())))
@inst_wrapper('`')
def befunge_gt(state):
	b, a = state.pop(), state.pop()
	state.append(int(a > b))
@inst_wrapper(':')
def befunge_dup(state):
	#state.append(state[-1])
	val = state.pop()
	state.append(val)
	state.append(val)
@inst_wrapper('\\')
def befunge_swap(state):
	b, a = state.pop(), state.pop()
	state.append(b)
	state.append(a)
@inst_wrapper('$')
def befunge_discard(state):
	state.pop()
@inst_wrapper('.')
def befunge_num_out(state):
	print(state.pop(), end='')
@inst_wrapper(',')
def befunge_str_out(state):
	print(chr(state.pop()), end='')
@inst_wrapper('&')
def befunge_num_in(state):
	a = input()
	try: state.append(int(a))
	except ValueError:
		print('Invalid digit. Pushing 0.')
		state.append(0)
@inst_wrapper('~')
def befunge_str_in(state):
	a = input()[0]
	state.append(ord(a))

class prog_state():
	__slots__ = [
		'grid', 'dir', 'coords',
		'stack', 'active', 'jump',
		'width', 'height',
		'strmode'
	]
	def __init__(self, prog):
		self.grid = prog
		self.height = len(prog)
		self.width = len(prog[0])
		self.coords = (0, 0)
		self.dir = DIRS['>']
		self.active = True
		self.stack = []
		self.jump = False
		self.strmode = False

	def handle_next(self):
		y = self.coords[1] % self.height
		x = self.coords[0] % self.width
		inst = self.grid[y][x]
		# Handle strings
		if self.strmode:
			if inst == '"':
				self.strmode = False
				return
			self.stack.append(ord(inst))
			return
		# Handle p and g
		# NOTE: I'm not actually sure that p and g index properly
		if inst == 'p':
			y, x, v = self.stack.pop(), self.stack.pop(), self.stack.pop()
			self.grid[y][x] = chr(v)
		if inst == 'g':
			y, x = self.stack.pop(), self.stack.pop()
			if x > self.width or x < 0 or y > self.height or y < 0:
				self.stack.append(0)
			else:
				self.stack.append(ord(self.grid[y][x]))
		# Handle special characters
		if inst == '@':
			self.active = False
			return
		if inst == '#':
			self.jump = True
			return
		if inst == '|': inst = 'v^'[bool(self.stack.pop())]
		if inst == '_': inst = '><'[bool(self.stack.pop())]
		if inst == '?': inst = random.choice('><^v')
		if inst == '"': self.strmode = True
		# Handle standard instructions
		if inst in '0123456789':
			self.stack.append(int(inst))
			return
		if inst in DIRS:
			self.dir = DIRS[inst]
			return
		if inst in INSTRUCTIONS:
			INSTRUCTIONS[inst](self.stack)
			return

	def step(self):
		self.coords = self.dir(*self.coords)
		if self.jump:
			self.jump = False
			self.coords = self.dir(*self.coords)


def main():
	counter = 0
	if len(sys.argv) != 2:
		print('usage: befunge_interpreter.py bf_file')
		return
	with open(sys.argv[1]) as f:
		prog = list(map(list, f.readlines()))
	grid_width = -1
	for line in prog:
		if '\n' in line: line.remove('\n')
		grid_width = max(len(line), grid_width)
	# pad out each line to the width of the grid
	for line in prog:
		line.extend([chr(0)] * (grid_width-len(line)))
	state = prog_state(prog)
	while state.active:
		state.handle_next()
		state.step()
		counter += 1
		if counter > 100000:
			return

if __name__ == '__main__': main()