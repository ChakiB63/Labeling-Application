import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import requirements as rqr
print(rqr.days_of_archieve)
