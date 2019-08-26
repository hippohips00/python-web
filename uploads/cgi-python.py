#!usrbinpython
# 07-07-04
# v1.0.0

# cgi-shell.py
# A simple CGI that executes arbitrary shell commands.


# Copyright Michael Foord
# You are free to modify, use and relicense this code.

# No warranty express or implied for the accuracy, fitness to purpose or otherwise for this code....
# Use at your own risk !!!

# E-mail michael AT foord DOT me DOT uk
# Maintained at www.voidspace.org.ukatlantibotspythonutils.html


A simple CGI script to execute shell commands via CGI.

################################################################
# Imports
try
    import cgitb; cgitb.enable()
except
    pass
import sys, cgi, os
sys.stderr = sys.stdout
from time import strftime
import traceback
from StringIO import StringIO
from traceback import print_exc

################################################################
# constants

fontline = 'FONT COLOR=#424242 style=font-familytimes;font-size12pt;'
versionstring = 'Version 1.0.0 7th July 2004'

if os.environ.has_key(SCRIPT_NAME)
    scriptname = os.environ[SCRIPT_NAME]
else
    scriptname = 

METHOD = 'POST'

################################################################
# Private functions and variables

def getform(valuelist, theform, notpresent='')
    This function, given a CGI form, extracts the data from it, based on
    valuelist passed in. Any non-present values are set to '' - although this can be changed.
    (e.g. to return None so you can test for missing keywords - where '' is a valid answer but to have the field missing isn't.)
    data = {}
    for field in valuelist
        if not theform.has_key(field)
            data[field] = notpresent
        else
            if  type(theform[field]) != type([])
                data[field] = theform[field].value
            else
                values = map(lambda x x.value, theform[field])     # allows for list type values
                data[field] = values
    return data


theformhead = HTMLHEADTITLEcgi-shell.py - a CGI by FuzzymanTITLEHEAD
BODYCENTER
H1Welcome to cgi-shell.py - BRa Python CGIH1
BIBy FuzzymanBIBR
+fontline +Version   + versionstring + , Running on   + strftime('%I%M %p, %A %d %B, %Y')+'.CENTERBR'

theform = H2Enter CommandH2
FORM METHOD= + METHOD + ' action=' + scriptname + 
input name=cmd type=textBR
input type=submit value=SubmitBR
FORMBRBR
bodyend = 'BODYHTML'
errormess = 'CENTERH2Something Went WrongH2BRPRE'

################################################################
# main body of the script

if __name__ == '__main__'
    print Content-type texthtml         # this is the header to the server
    print                                   # so is this blank line
    form = cgi.FieldStorage()
    data = getform(['cmd'],form)
    thecmd = data['cmd']
    print theformhead
    print theform
    if thecmd
        print 'HRBRBR'
        print 'BCommand  ', thecmd, 'BRBR'
        print 'Result  BRBR'
        try
            child_stdin, child_stdout = os.popen2(thecmd)
            child_stdin.close()
            result = child_stdout.read()
            child_stdout.close()
            print result.replace('n', 'BR')

        except Exception, e                      # an error in executing the command
            print errormess
            f = StringIO()
            print_exc(file=f)
            a = f.getvalue().splitlines()
            for line in a
                print line

    print bodyend



TODOISSUES



CHANGELOG

07-07-04        Version 1.0.0
A very basic system for executing shell commands.
I may expand it into a proper 'environment' with session persistence...
