#################################################################

# ENTER PCB SHRINK-SIZE IN MM - take 0 for maximum enclosure size
shrink = 2

# ENTER DIMENSIONS IN MM TAKEN FROM DATASHEET
screw_h_len = 90.5  # Top view of assembly
screw_v_len = 40.5  # Top view of assembly
inner_h_len = 84.4  # Top view looking inside box
inner_v_len = 34.4  # Top view looking inside box
outer_h_len = 96.2  # Top view looking inside box
outer_v_len = 46.2  # Top view looking inside box

# Helper holes and lines - set to 1 for debug purposes
draw_screwholes = 0
draw_inner_helper = 0

# Module info
modulename = "Hammond_1590G_2mm_python"

# These are not yet incorporated 
tags = "Hammond_1590G_2mm_python"
value = "Hammond_1590G_2mm_python"
description = "Hammond_1590G_2mm_python"
reference = "REF**"

#################################################################

inner_h_len = inner_h_len - shrink # Adjust for PCB shrink size
inner_v_len = inner_v_len - shrink # Adjust for PCB shrink size
outer_h_len = outer_h_len - shrink # Adjust for PCB shrink size
outer_v_len = outer_v_len - shrink # Adjust for PCB shrink size

# ALL POINTS WILL BE REFERENCED FROM CENTER OF THE BOX

# Calculate screw coordinates 
screw_tl = [-screw_h_len/2, -screw_v_len/2]
screw_bl = [-screw_h_len/2, screw_v_len/2]
screw_tr = [screw_h_len/2, -screw_v_len/2]
screw_br = [screw_h_len/2, screw_v_len/2]

# Calculate arc coordinates
arc_tl_start = screw_tl
arc_tl_end = [-inner_h_len/2, screw_tl[1]]

arc_bl_start = screw_bl
arc_bl_end = [screw_bl[0], inner_v_len/2]

arc_tr_start = screw_tr
arc_tr_end = [screw_tr[0], -inner_v_len/2]

arc_br_start = screw_br
arc_br_end = [inner_h_len/2, screw_bl[1]]



# Inner maximum coordinates
line_inner_left_start = [-outer_h_len/2, -inner_v_len/2]
line_inner_left_end = [-outer_h_len/2, inner_v_len/2]

line_inner_right_start = [outer_h_len/2, -inner_v_len/2]
line_inner_right_end = [outer_h_len/2, inner_v_len/2]

line_inner_top_start = [-outer_h_len/2, -inner_v_len/2]
line_inner_top_end = [outer_h_len/2, -inner_v_len/2]

line_inner_bottom_start = [-outer_h_len/2, inner_v_len/2]
line_inner_bottom_end = [outer_h_len/2, inner_v_len/2]

# Inner maximum coordinates
line_outer_left_start = [-inner_h_len/2, -outer_v_len/2]
line_outer_left_end = [-inner_h_len/2, outer_v_len/2]

line_outer_right_start = [inner_h_len/2, -outer_v_len/2]
line_outer_right_end = [inner_h_len/2, outer_v_len/2]

line_outer_top_start = [-inner_h_len/2, -outer_v_len/2]
line_outer_top_end = [inner_h_len/2, -outer_v_len/2]

line_outer_bottom_start = [-inner_h_len/2, outer_v_len/2]
line_outer_bottom_end = [inner_h_len/2, outer_v_len/2]


def DrawHole( pos ):
    h = '  (pad 1 thru_hole circle (at ' + str( pos[0] ) + ' ' + str( pos[1] ) + ') (size 6 6) (drill 4) (layers *.Cu))'
    return h

def DrawLine( pos_start, pos_end):
    l = '  (fp_line (start ' + str( pos_start[0] ) + ' ' + str( pos_start[1] ) + ') (end ' + str( pos_end[0] ) + ' ' + str( pos_end[1] ) + ') (layer Edge.Cuts) (width 0.05))'
    return l

def DrawArc( arc_start, arc_end):
    a = '  (fp_arc (start ' + str(arc_start[0]) + ' ' + str(arc_start[1]) + ') (end ' + str(arc_end[0]) + ' ' + str(arc_end[1]) + ') (angle 90) (layer Edge.Cuts) (width 0.05))'
    return a


with open( modulename + '.kicad_mod', 'a') as the_file:

    # Write module info
    # The module description needs to be variable aswell
    moduleinfo = """(module Hammond_1590G_2mm_python (layer F.Cu) (tedit 56C35386)
  (descr Hammond_1590G_2mm_python)
  (tags Hammond_1590G_2mm_python)
  (fp_text reference REF** (at -0.05 1.35) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value Hammond_1590G_2mm_python (at -0.05 -1.15) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )"""
    
    the_file.write( moduleinfo + '\n')

    # Write screwholes    
    if draw_screwholes:
        the_file.write( DrawHole( screw_tl ) + '\n')
        the_file.write( DrawHole( screw_bl ) + '\n')
        the_file.write( DrawHole( screw_tr ) + '\n')
        the_file.write( DrawHole( screw_br ) + '\n')

    # Write arcs
    the_file.write( DrawArc( arc_tl_start, arc_tl_end ) + '\n')
    the_file.write( DrawArc( arc_bl_start, arc_bl_end ) + '\n')
    the_file.write( DrawArc( arc_tr_start, arc_tr_end ) + '\n')
    the_file.write( DrawArc( arc_br_start, arc_br_end ) + '\n')

    # Write outer lines
    the_file.write( DrawLine( line_inner_left_start, line_inner_left_end ) + '\n')
    the_file.write( DrawLine( line_outer_top_start, line_outer_top_end ) + '\n')
    the_file.write( DrawLine( line_inner_right_start, line_inner_right_end ) + '\n')
    the_file.write( DrawLine( line_outer_bottom_start, line_outer_bottom_end ) + '\n')

    # Write inner lines
    if draw_inner_helper:
        the_file.write( DrawLine( line_outer_left_start, line_outer_left_end ) + '\n')
        the_file.write( DrawLine( line_inner_top_start, line_inner_top_end ) + '\n')
        the_file.write( DrawLine( line_outer_right_start, line_outer_right_end ) + '\n')
        the_file.write( DrawLine( line_inner_bottom_start, line_inner_bottom_end ) + '\n')

    # Connecting lines to arcs
  
    # Top left screwhole, left line
    the_file.write( DrawLine( [arc_tl_end[0], arc_tl_end[1]], [arc_tl_end[0], line_outer_top_start[1]]) + '\n')
    # Top left screwhole, right line
    the_file.write( DrawLine( [arc_tl_start[0], line_inner_left_start[1]], [line_inner_top_start[0], line_inner_top_start[1]]) + '\n')   
    # Bottom left screwhole, left line
    the_file.write( DrawLine( [arc_bl_end[0], arc_bl_end[1]], [line_inner_bottom_start[0], line_inner_bottom_start[1]]) + '\n')
    # Bottom left screwhole, right line
    the_file.write( DrawLine( [line_outer_left_start[0], arc_bl_start[1]],[line_outer_bottom_start[0], line_outer_bottom_start[1]]) + '\n')
    # Top right screwhole, left line
    the_file.write( DrawLine( [line_outer_top_end[0], arc_tr_start[1]], [line_outer_right_start[0], line_outer_right_start[1]]) + '\n')
    # Top right screwhole, right line
    the_file.write( DrawLine( [arc_tr_end[0], arc_tr_end[1]], [line_inner_right_start[0], line_inner_right_start[1]]) + '\n')   
    # Bottom right screwhole, left line
    the_file.write( DrawLine( [arc_br_end[0], arc_br_end[1]], [line_outer_bottom_end[0], line_outer_bottom_end[1]]) + '\n')
    # Bottom right screwhole, right line
    the_file.write( DrawLine( [arc_br_start[0], line_inner_bottom_start[1]], [line_inner_bottom_end[0], line_inner_bottom_end[1]] ) + '\n')    

    # Close module
    the_file.write( ")" + '\n')



# Print all calculated coordinates in console for manual drawings.


print("All measurements referenced from center anchor of the enclosure.")

print("  ------------------ " )
print(" DATASHEET DIMENSIONS - ABSOLUTE ")
print("- Horizontal distance between screws: " + str(screw_h_len) + " mm.")
print("- Vertical distance between screws: " + str(screw_v_len) + " mm.")
print("- Horizontal inner length: " + str(inner_h_len) + " mm.")
print("- Vertical inner length: " + str(inner_v_len) + " mm.")
print("- Horizontal outer length: " + str(outer_h_len) + " mm.")
print("- Vertical outer length: " + str(outer_v_len) + " mm.")

print("  ------------------ " )
print(" SCREWHOLE POSITIONS ")
print("- Top left screwhole: " + str(screw_tl) + " mm.")
print("- Top right screwhole: " + str(screw_tr) + " mm.")
print("- Bottom left screwhole: " + str(screw_bl) + " mm.")
print("- Bottom right screwhole: " + str(screw_br) + " mm.")
print("  ------------------ " )

print(" ARC POSITIONS ")
print("- Top left: " + str(arc_tl_start) + " to " + str(arc_tl_end) )
print("- Bottom left: " + str(arc_bl_start) + " to " + str(arc_bl_end) )
print("- Top right: " + str(arc_tr_start) + " to " + str(arc_tr_end) )
print("- Bottom right: " + str(arc_br_start) + " to " + str(arc_br_end) )
print("  ------------------ " )

print(" INNER DIMENSIONS ")
print("- Left line: " + str(line_inner_left_start) + " to " + str(line_inner_left_end) + " mm.")
print("- Bottom line: " + str(line_inner_bottom_start) + " to " + str(line_inner_bottom_end) + " mm.")
print("- Right line: " + str(line_inner_right_start) + " to " + str(line_inner_right_end) + " mm.")
print("- Top line: " + str(line_inner_top_start) + " to " + str(line_inner_top_end) + " mm.")
print("  ------------------ " )
print(" OUTER DIMENSIONS ")
print("- Left line: " + str(line_outer_left_start) + " to " + str(line_outer_left_end) + " mm.")
print("- Bottom line: " + str(line_outer_bottom_start) + " to " + str(line_outer_bottom_end) + " mm.")
print("- Right line: " + str(line_outer_right_start) + " to " + str(line_outer_right_end) + " mm.")
print("- Top line: " + str(line_outer_top_start) + " to " + str(line_outer_top_end) + " mm.")

