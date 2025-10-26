# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2025-03-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrl_list=None, color=None):

    color_map   = {1:4,2:13,3:25,4:17,
                   5:17,6:15,7:6,8:16}


    for ctrl_name in ctrl_list:
        mc.setAttr(ctrl_name + 'Shape.overrideEnabled', 1)
        final_color = color_map[old_color]
        mc.setAttr(ctrl_name + 'Shape.overrideColor', final_color)


# EXAMPLE
# set_color(['circle','circle1'], 8)
