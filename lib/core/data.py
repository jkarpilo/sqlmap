#!/usr/bin/env python

"""
Copyright (c) 2006-2012 sqlmap developers (http://www.sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.datatype import AttribDict
from lib.core.settings import LOGGER

# sqlmap paths
paths = AttribDict()

# object to store original command line options
cmdLineOptions = AttribDict()

# object to share within function and classes command
# line options and settings
conf = AttribDict()

# object to share within function and classes results
kb = AttribDict()

# object with each database management system specific queries
queries = {}

# logger
logger = LOGGER
