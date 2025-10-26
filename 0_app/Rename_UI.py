import maya.cmds as cmds
from PySide6.QtWidgets import QMessageBox
import webbrowser

def rename_function_rename():
	selection = cmds.ls(selection=True)
	text_input_rename = cmds.textField('rename', query = True, text = True)
	if not selection:
		QMessageBox.warning(None, 'Warning', 'Please select at least 1 object')
		return
	for obj in selection:
		new_name= cmds.rename(obj,text_input_rename)
		print(new_name)

def rename_function_prefix():
	selection = cmds.ls(selection=True)
	text_input_prefix = cmds.textField('prefix', query = True, text = True)

	if not selection:
		QMessageBox.warning(None, 'Warning', 'Please select at least 1 object')
		return

	for obj in selection:
		new_name = str(text_input_prefix) + "_" + str(obj) 
		cmds.rename(obj,new_name)
		print(new_name)
		


def rename_function_suffix():
	selection = cmds.ls(selection=True)
	text_input_prefix = cmds.textField('suffix', query = True, text = True)
	if not selection:
		QMessageBox.warning(None, 'Warning', 'Please select at least 1 object')
		return

	for obj in selection:
		new_name = str(obj) + "_" + str(text_input_prefix)
		cmds.rename(obj,new_name)
		print(new_name)

def reset_name():
	selection = cmds.ls(selection=True)
	if not selection:
		QMessageBox.warning(None, 'Warning', 'Please select at least 1 object')
		return
	for obj in selection:
		reset_Name=obj.split(':')[-1]
		cmds.rename(obj,reset_Name)

def number():
	selection = cmds.ls(sl=True)
	base_name = cmds.textField('rename', query=True, text=True)
	start_number= cmds.intField('startnumber', query=True, value=True)
	padding_number=cmds.intField('paddingnumber', query=True, value=True)
	if not selection:
		QMessageBox.warning(None, 'Warning', 'Please select at least 1 object')
		return
	count= start_number
	for obj in selection:
		new_name = f"{base_name}_{count:0{padding_number}d}"
		cmds.rename(obj,new_name)
		count += 1


def adaptive_ui():
	ui_title = 'MyUI'
	if cmds.window(ui_title, exists=True):
		print('CLOSE duplicate window')
		cmds.deleteUI(ui_title)

	cmds.window(ui_title,title="My_UI", widthHeight=(388, 500))
	cmds.columnLayout(adjustableColumn=True)
	
	cmds.image(image='E:\\Tech_Art\\TechArt_TD_Alex\\Week_8\\Assignment\\Rename.jpg', width= 300, height= 210)
	cmds.rowLayout( numberOfColumns=5,          # 2 cột: nhãn + ô gõ
                	columnWidth2=(60, 1),       # cột 1 cố định 60 px, cột 2 tạm 1 px
                	adjustableColumn=2,         # cột 2 được phép giãn hết
                	columnAlign2=('left','left'),
                	columnAttach=[(1,'left',5), (2,'both',5)] )

	cmds.text( label='Rename:', align='left' )
	text_user_rename = cmds.textField('rename',placeholderText="Rename")
	cmds.setParent('..')
	
	cmds.rowLayout(numberOfColumns=5,
                	columnWidth3=(1,3,1),       # cột 1 cố định 60 px, cột 2 tạm 1 px
                	        # cột 2 được phép giãn hết
                	columnAlign4=('left','left','right','right'),
                	columnAttach=[(3,'both',5), (1,'both',5), (3,'both',5)] )
	cmds.text(label='Start:',align='center')
	number_user = cmds.intField('startnumber',width=50)
	cmds.text(label='Padding:',align='center')
	padding_user = cmds.intField('paddingnumber',width=50)
	cmds.setParent('..')

	cmds.rowLayout( numberOfColumns=3,          # 2 cột: nhãn + ô gõ
                	columnWidth3=(100, 100, 100),
                	columnAlign3=('left', 'center', 'right'),
                	adjustableColumn3=2,
                	columnAttach=[(1, 'both', 5), (2, 'both', 5), (3, 'both', 5)])

	cmds.button(label='Rename', command= 'rename_function_rename()')
	cmds.button(label='Default Names', command= 'reset_name()')
	cmds.button(label='Number', command='number()')
	cmds.setParent('..')




	text_user_suffix = cmds.textField('suffix',placeholderText="Add_suffix")
	text_user_prefix = cmds.textField('prefix',placeholderText="Add_prefix")
	

	
	cmds.button(label='Add_suffix', command= 'rename_function_suffix()')
	cmds.button(label='Add_prefix', command= 'rename_function_prefix()')
	cmds.button(label= 'Help', command= "webbrowser.open('www.alexanderrichtertd.com')")
	cmds.showWindow()
adaptive_ui()