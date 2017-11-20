#!usr/bin/python
# -*- coding: utf-8 -*-

import re
def golf(p):
	return re.match(r"^(?=.*[\d])(?=.*[a-z])(?=.*[A-Z])([\w]{10,})$", p)
