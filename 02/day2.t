fun tab_len(tab) {
	return ..tab
}

fun tab_addr(tab, i) {
	return .tab + .i + 1
}

fun tab_index(tab, i) {
	return .(tab_addr(.tab, .i))
}

fun splitString(str, delim) {
	var c, i, n, tab, newword, wp
	i : 0
	n : 0
# Get tab_length
	loop {
		c : .str + .i
		until ..c == 0
		if ..c == .delim {
			n : .n + 1
		}
		i : .i + 1
	}
	n : .n + 1
# Split, store pointers
	i : 0
	tab : alloc(.n + 1)
	newword : 1
	wp : 1
# First entry is size, rest are pointers
	.tab : .n
	loop {
		c : .str + .i
		until ..c == 0
		if .newword == 1 {
			(.tab + .wp) : .c
			wp : .wp + 1
			newword : 0
		}
		if ..c == .delim {
			.c : 0
			newword : 1
		}
		i : .i + 1
	}
# Return pointer to array of words
	return .tab
}

fun stringToNumber(str) {
	var result, c, i
	result : 0
	i : 0
	loop {
		c : .str + .i
		until ..c == 0
# ASCII to int conversion
		c : ..c - '0'
# Left shift
		result : 10 * .result
# Add latest
		result : .result + .c
		i : .i + 1
	}
	return .result
}

fun stringsToNumbers(strtab) {
	var n, i, c, result
	n : tab_len(strtab)
	i : 0
	loop {
		until .i == .n
		c : tab_index(.strtab, .i)
# c is tab_address of string
		result : stringToNumber(.c)
# modify in-place
		tab_addr(.strtab, .i) : .result
		i : .i + 1
	}
	return .strtab
}

fun splitStrings(strtab, delim) {
	var n, i, c, result
	n : tab_len(.strtab)
	i : 0
	loop {
		until .i == .n
		c : tab_index(.strtab, .i)
# c is tab_address of string
		result : splitString(.c, .delim)
# modify in-place
		tab_addr(.strtab, .i) : .result
		i : .i + 1
	}
	return .strtab
}

fun stringComp(str1, str2) {
	var i, c1, c2
	i : 0
	loop {
		c1 : .(.str1 + .i)
		c2 : .(.str2 + .i)
		if .c1 != .c2 {
			return 0
		}
# Equal here
		if .c1 == 0 {
			return 1
		}
		i : .i + 1
	}
}

fun p1(lines) {
	var n, i, dir, amt, h, d
	n : tab_len(.lines)
	i : 0
	h : 0
	d : 0
	loop {
		until .i == .n
		dir : tab_index(tab_index(.lines, .i), 0)
		amt : stringToNumber(tab_index(tab_index(.lines, .i), 1))
		if stringComp(.dir, "forward") == 1 {
			h : .h + .amt
		}
		else if stringComp(.dir, "down") == 1 {
			d : .d + .amt
		}
		else if stringComp(.dir, "up") == 1 {
			d : .d - .amt
		}
		i : .i + 1
	}
	iprint(.h * .d)
}

fun p2(lines) {
	var n, i, dir, amt, h, d, a
	n : tab_len(.lines)
	i : 0
	h : 0
	d : 0
	a : 0
	loop {
		until .i == .n
		dir : tab_index(tab_index(.lines, .i), 0)
		amt : stringToNumber(tab_index(tab_index(.lines, .i), 1))
		if stringComp(.dir, "forward") == 1 {
			h : .h + .amt
			d : .d + (.amt * .a)
		}
		else if stringComp(.dir, "down") == 1 {
			a : .a + .amt
		}
		else if stringComp(.dir, "up") == 1 {
			a : .a - .amt
		}
		i : .i + 1
	}
	iprint(.h * .d)
}

fun init() {
	var input, lines
	input : "forward 5
down 9
forward 2
up 2
forward 4
forward 4
up 5
down 3
forward 2
forward 9
down 7
forward 2
down 2
forward 1
up 9
forward 1
forward 4
up 5
down 9
forward 8
forward 3
up 1
down 2
down 3
forward 7
forward 2
up 3
forward 9
forward 9
down 3
up 8
forward 5
forward 7
forward 2
down 7
forward 5
down 4
up 7
forward 8
forward 1
down 3
down 1
forward 6
up 7
forward 6
down 3
forward 9
forward 6
up 3
down 1
forward 8
up 7
down 9
down 2
down 1
down 5
forward 4
down 8
forward 2
down 5
down 6
down 5
forward 5
down 8
up 8
forward 3
forward 4
forward 8
forward 9
down 2
forward 7
forward 3
forward 9
down 3
up 1
down 5
forward 2
down 9
down 2
down 5
down 2
down 9
up 3
forward 6
up 9
down 1
forward 8
up 6
down 1
forward 1
up 1
forward 3
down 8
down 1
down 9
forward 4
forward 1
down 3
forward 8
down 9
forward 7
up 6
down 8
down 6
down 8
down 7
down 1
down 8
down 1
forward 5
down 9
forward 4
down 2
forward 8
up 1
forward 7
down 7
down 6
forward 4
forward 6
down 2
down 2
up 7
down 2
up 9
forward 6
forward 3
down 8
forward 9
down 9
down 9
down 8
forward 2
forward 5
forward 8
forward 1
down 3
forward 1
forward 2
forward 9
up 5
forward 4
forward 2
down 6
forward 3
forward 7
forward 1
forward 8
down 7
forward 4
up 3
down 9
up 2
forward 2
forward 7
down 9
up 9
forward 9
up 8
up 7
down 8
down 9
forward 1
forward 5
up 7
down 3
up 9
forward 9
down 4
down 7
down 7
down 1
down 4
down 5
up 2
forward 2
forward 2
forward 6
down 7
forward 7
down 5
forward 8
down 7
forward 6
down 2
up 2
down 5
down 1
up 4
down 8
up 9
forward 1
down 9
down 6
down 8
up 7
up 1
forward 7
down 8
forward 1
down 4
down 2
forward 3
forward 6
forward 8
down 2
forward 7
forward 8
up 3
down 1
down 8
up 3
down 4
down 5
forward 6
forward 9
down 3
up 2
down 9
up 2
down 3
down 9
forward 4
forward 6
down 7
down 8
down 4
forward 7
up 2
down 5
up 3
down 5
up 1
up 1
forward 5
forward 9
down 9
up 4
up 4
up 8
up 5
forward 7
forward 6
up 6
down 5
forward 4
forward 3
up 6
down 6
forward 5
up 6
up 7
forward 1
forward 2
forward 5
down 3
forward 6
down 6
down 3
up 9
down 4
down 5
down 4
forward 1
down 1
forward 3
up 4
forward 1
forward 5
up 3
forward 6
forward 5
forward 9
forward 6
down 2
forward 2
down 1
down 4
forward 6
forward 8
down 8
up 5
forward 8
forward 3
forward 1
forward 3
forward 6
down 1
down 9
up 7
down 2
forward 6
down 4
down 7
down 5
forward 2
down 1
forward 2
forward 8
forward 4
up 3
down 1
forward 6
forward 3
down 3
down 9
forward 1
up 5
forward 3
forward 3
up 5
down 7
forward 8
up 5
forward 2
forward 2
down 6
up 8
up 5
forward 2
forward 1
down 9
forward 7
down 5
forward 3
down 3
down 5
down 5
up 7
down 8
forward 2
forward 4
forward 5
forward 1
down 6
forward 3
down 1
down 7
forward 3
forward 7
down 5
down 3
forward 6
down 3
down 2
down 4
down 9
forward 7
down 2
up 2
up 6
up 9
up 8
forward 9
down 1
forward 4
forward 2
forward 7
forward 2
down 8
down 3
forward 4
forward 6
down 8
forward 7
forward 6
up 3
down 6
down 1
down 3
down 8
down 2
down 7
down 9
forward 4
forward 7
forward 8
forward 5
forward 9
up 5
down 2
forward 9
forward 6
up 6
forward 7
down 2
down 3
forward 4
down 6
down 1
down 2
down 8
forward 3
down 3
forward 3
down 5
up 8
down 5
forward 8
down 1
forward 1
forward 4
forward 7
down 2
down 5
forward 5
down 8
forward 2
down 2
forward 5
forward 6
forward 4
down 7
up 7
down 1
forward 7
forward 8
down 6
up 7
forward 6
up 6
down 8
forward 5
forward 8
up 4
up 2
up 1
down 8
down 6
up 2
down 5
down 1
forward 5
forward 7
down 2
up 3
up 3
forward 9
down 1
forward 6
down 2
forward 2
down 1
down 9
forward 7
down 5
down 8
up 1
forward 1
down 7
forward 3
down 4
up 4
down 6
forward 1
forward 3
down 2
forward 3
forward 5
forward 6
up 2
up 9
forward 4
down 4
up 1
up 3
forward 8
forward 1
down 9
down 9
forward 2
down 1
up 9
up 3
up 1
up 5
forward 6
down 9
forward 6
forward 9
forward 6
forward 4
up 2
down 6
up 3
forward 3
forward 1
up 4
forward 7
down 9
down 3
forward 9
down 4
down 8
down 3
up 8
down 8
down 8
forward 2
forward 8
up 9
forward 2
up 6
forward 7
down 1
forward 5
forward 4
forward 1
forward 7
up 9
down 8
forward 1
up 5
forward 9
forward 2
forward 8
down 1
forward 7
down 2
up 8
down 6
up 9
up 3
down 6
forward 5
down 1
forward 1
forward 6
forward 6
up 1
forward 5
forward 1
up 2
forward 9
forward 6
down 3
up 1
forward 7
forward 2
down 1
forward 6
down 3
up 2
down 3
down 8
forward 4
down 2
up 7
down 6
up 5
down 7
forward 4
down 9
down 3
forward 2
up 5
up 4
forward 9
down 1
up 2
forward 4
down 9
down 8
forward 5
forward 2
down 5
forward 6
down 4
forward 7
forward 1
forward 6
down 3
down 9
forward 9
forward 2
forward 6
down 7
down 5
down 3
forward 7
down 3
down 3
down 4
down 4
down 7
down 7
down 7
up 7
up 9
up 7
up 3
up 4
down 9
down 4
up 3
forward 2
up 1
down 9
down 6
up 1
up 2
down 7
down 9
up 2
forward 7
down 4
forward 3
down 1
down 7
forward 7
up 7
forward 3
forward 1
forward 6
forward 2
down 9
forward 8
up 8
down 8
down 9
up 1
down 4
down 6
down 8
up 4
down 1
forward 1
forward 1
forward 4
forward 7
forward 1
down 4
forward 5
up 3
forward 4
down 5
down 1
up 2
down 7
forward 7
down 7
up 9
down 9
down 3
up 2
up 8
up 8
up 7
forward 7
forward 5
forward 3
forward 2
down 5
forward 4
forward 1
down 6
down 1
forward 8
down 6
down 3
down 5
down 9
down 3
forward 7
forward 6
down 6
forward 9
up 7
forward 3
up 5
down 5
down 5
forward 4
up 6
down 6
forward 3
up 2
forward 4
up 1
down 5
forward 6
forward 9
down 2
up 2
down 2
up 7
forward 3
up 2
forward 9
forward 5
down 5
down 7
down 8
down 6
up 9
up 5
forward 7
down 8
down 1
forward 7
up 2
forward 4
forward 2
up 9
down 8
forward 1
forward 7
down 2
down 3
down 6
down 3
forward 1
up 6
forward 8
down 9
down 9
forward 8
up 8
down 6
forward 4
up 1
forward 5
down 3
down 7
down 7
down 3
up 2
forward 4
down 9
forward 2
down 9
forward 9
forward 4
forward 5
down 4
forward 1
up 1
forward 4
up 3
up 4
forward 7
down 9
forward 6
down 1
down 1
down 2
down 4
forward 7
forward 8
forward 6
down 8
forward 2
down 3
up 5
forward 2
up 5
forward 8
down 8
down 8
up 8
forward 6
up 1
down 3
forward 6
down 1
forward 9
up 1
forward 7
forward 7
down 1
forward 5
forward 2
up 7
down 1
forward 2
down 4
forward 3
down 9
forward 6
up 5
forward 1
forward 5
down 7
forward 6
down 8
forward 9
down 1
forward 9
down 1
forward 5
up 9
forward 1
forward 6
forward 5
down 7
down 6
down 5
down 9
forward 9
down 2
down 8
down 8
forward 2
forward 3
forward 3
down 3
forward 8
forward 8
down 8
forward 1
up 1
forward 4
down 7
forward 1
up 2
forward 9
forward 1
down 6
up 9
down 3
down 1
up 1
up 6
up 7
forward 9
up 2
forward 4
up 8
down 6
forward 3
forward 7
down 6
down 5
down 3
forward 5
down 1
forward 2
forward 9
down 8
up 6
forward 3
forward 2
up 7
down 3
forward 5
forward 9
down 5
down 1
up 4
down 8
forward 1
forward 3
forward 3
down 2
forward 5
down 1
forward 2
up 3
forward 8
down 2
up 8
down 6
down 8
forward 4
down 4
up 7
up 6
down 7
forward 2
up 3
forward 3
down 8
forward 8
down 5
forward 5
down 3
up 7
down 1
down 2
up 8
down 6
up 6
down 7
forward 5
up 3
forward 7
forward 2
down 9
down 1
down 4
down 7
forward 9
up 7
forward 5
up 8
forward 8
up 1
forward 2
down 7
down 5
down 6
down 4
up 4
forward 5
forward 6
up 4
forward 8
forward 4
forward 3
up 5
down 6
up 4
forward 8
down 7
forward 3
down 2
down 7
down 5
down 4
forward 5
up 4
forward 4
down 7
down 3
down 9
down 7
forward 2
forward 1
down 7
down 8
forward 1
forward 2
down 5
up 1
down 1
forward 5
down 2
forward 9
forward 7
down 2
forward 6
forward 9
up 5
forward 3
up 5
forward 7
down 6
down 3
up 3
down 4
forward 2
up 4
forward 5
up 9
down 3
up 1
down 1
up 3
forward 4
forward 5
down 3
forward 5
down 6
down 2
forward 5
forward 3
down 7
down 8
forward 4
down 5
forward 7
forward 2
forward 7
down 7
up 1
forward 6
down 1
forward 1
down 4
forward 1
up 6
forward 8
forward 6
forward 7
up 6
up 7
up 2
down 9
forward 4
up 3
down 1
down 1
forward 3
down 4
down 6
down 8
forward 9
forward 6
down 1
forward 5"
	lines : splitStrings(splitString(.input, 10), ' ')
	p1(.lines)
	nl()
	p2(.lines)
	nl()
}

