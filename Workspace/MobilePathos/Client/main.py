
'''
  DOCUMENTATION
'''

# IMPORTS
import entry as en
import recording as rec
import previous as prev
import processing as proc

# ENTRY POINT
en.animate() ;

# START RECORDING
rec.record()

# IMPORT PREVIOUS CALCULATIONS DATA
prev.importPrevious()

# BEGIN PROCESSING
proc.processing()

# DISPLAY RESULTS
