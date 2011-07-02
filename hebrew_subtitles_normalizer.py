################################################################################
#                   Subtitles Normalizer                                       #
#                -------------------------                                     #
#   Putpose:                                                                   #
#           Convert subtitle files to utf-8.                                   #
#                                                                              #
#   Author:                                                                    #
#           Michael Sverdlin 12/2008                                           #
#                                                                              #
#------------------------------------------------------------------------------#
#   Version:                                                                   #
#           Alpha (v0.1)                                                       #
#                                                                              #
################################################################################

###--IMPORTS--###

import os
import sys

###----MAIN---###

if "__main__" == __name__:
    try:
        old_file = open(sys.argv[1], 'r')
        old_text = old_file.read()
        old_file.close()

        new_text = old_text.decode("cp1255").encode("utf-8")
        os.rename(sys.argv[1], sys.argv[1] + ".old")

        new_file = open(sys.argv[1], 'w')
        new_file.write(new_text)
        new_file.close()
        
    except Exception, error:
        import traceback
        traceback.print_exc()
