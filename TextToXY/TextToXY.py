import arcpy.mp
arcpy.env.workspace = "c:/data"
arcpy.ExtractLocationsFromText_conversion("wells.txt", "water.gdb/wells")