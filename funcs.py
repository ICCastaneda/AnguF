#!usr/bin/python
import sys
sys.dont_write_bytecode = True


def bld_json_customers():
    print 'bld_json_customers():started'
    records = {'pathname':'path','records':[{'dp':'chevy/sable'}, {'dp':'dodge/ford'}]}
    return records
