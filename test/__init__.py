#	OpenProximity2.0 is a proximity marketing OpenSource system.
#	Copyright (C) 2009,2008 Naranjo Manuel Francisco <manuel@aircable.net>
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation version 2 of the License.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License along
#	with this program; if not, write to the Free Software Foundation, Inc.,
#	51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# A test plugin

__version_info__=('0','0','1')
__version__ = '.'.join(__version_info__)

def post_environ():
	print "Test post environ"

def find_plugins():
	print "Test post environ"

def statistics_reset(connection):
	print "Test statics reset" 
	