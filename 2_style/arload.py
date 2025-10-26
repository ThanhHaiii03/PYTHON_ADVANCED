import os
import re
import sys
import shutil
import getpass
import datetime
import subprocess

from Qt import QtWidgets, QtGui, QtCore, QtCompat

import libLog
import libData
import libFunc
import arNotice

from arUtil import ArUtil
from tank import Tank


TITLE = "load"
LOG = libLog.init(script=TITLE)

class ArLoad(ArUtil):
    def __init__(self):
        super(ArLoad, self).__init__()
        path_ui = "/".join([os.path.dirname(__file__), "ui", TITLE + ".ui"])
        self.wgLoad = QtCompat.loadUi(path_ui)
        self.load_dir = ''
        self.load_file = ''

        self.software_format = { software_name : extension.upper()
                                 for software_name,extension in self.data['software']['EXTENSION'].items() }

        self.software_keys = list(self.software_format.keys())
        self.wgLoad.lst_scene.clear()
        self.wgLoad.lst_status.clear()
        self.wgLoad.lst_set.clear()
        self.clear_meta()
        self.resize_widget(self.wgLoad)
        self.wgLoad.show()
        LOG.info('START : ArLoad')

    def press_btn_accept(self):
        MSG_TYPE = 3
        if not os.path.exists(self.load_file):
            self.set_status('FAILED LOADING : Path doesn\'t exists: {}'.format(self.load_file), MSG_TYPE)
            return False

    def press_menu_item_add_folder(self):
        import arSaveAs
        self.save_as = arSaveAs.start(new_file=False)

    def press_menu_sort(self, list_widget, reverse=False):
        file_list = []
        for index in xrange(list_widget.count()):
            file_list.append(list_widget.item(index).text())
        list_widget.clear()
        list_widget.addItems(sorted(file_list, reverse=reverse))

    def change_lst_scene(self):
        self.load_dir = self.data['project']['PATH'][self.wgLoad.lst_scene.currentItem().text()]
        tmp_content = libFunc.get_file_list(self.load_dir)
        self.scene_steps = len(self.data['rules']['SCENES'][self.wgLoad.lst_scene.currentItem().text()].split('/'))
        if self.scene_steps < 5:
            self.wgLoad.lst_asset.hide()
        else:
            self.wgLoad.lst_asset.itemSelectionChanged.connect(self.change_lst_asset)
            self.wgLoad.lst_asset.show()
        self.wgLoad.lst_set.clear()
        if tmp_content:
            self.wgLoad.lst_set.addItems(sorted(tmp_content))
            self.wgLoad.lst_set.setCurrentRow(0)

    def change_lst_set(self):
        new_path = os.path.join(self.load_dir,self.wgLoad.lst_set.currentItem().text())
        tmp_content = libFunc.get_file_list(new_path)
        if self.scene_steps < 5:
            self.wgLoad.lst_task.clear()
            if tmp_content:
                self.wgLoad.lst_task.addItems(sorted(tmp_content))
                self.wgLoad.lst_task.setCurrentRow(0)
        else:
            self.wgLoad.lst_asset.clear()
            if tmp_content:
                self.wgLoad.lst_asset.addItems(sorted(tmp_content))
                self.wgLoad.lst_asset.setCurrentRow(0)

    def change_lst_asset(self):
        new_path = os.path.join(self.load_dir, 
                                self.wgLoad.lst_set.currentItem().text(),
                                self.wgLoad.lst_asset.currentItem().text())
        tmp_content = libFunc.get_file_list(new_path)
        self.wgLoad.lst_task.clear()
        if tmp_content:
            self.wgLoad.lst_task.addItems(sorted(tmp_content))
            self.wgLoad.lst_task.setCurrentRow(0)

    def fill_meta(self):
        self.wgPreview.lblTitle.setText(self.file_name)
        self.wgPreview.lblDate.setText(str(datetime.datetime.fromtimestamp(os.path.getmtime(self.load_file))).split(".")[0])
        self.wgPreview.lblSize.setText(str("{0:.2f}".format(os.path.getsize(self.load_file)/(1024*1024.0)) + " MB"))

    def clear_meta(self):
        self.wgPreview.lblUser.setText('')
        self.wgPreview.lblTitle.setText('')
        self.wgPreview.lblDate.setText('')

def execute_the_class_ar_load():
    global main_widget
    main_widget = ArLoad()
