# ！/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 author : 梦幻骑士
 email  : wp_226@163.com
 @Project : TestTools
 @File  : config.PY
 @Time  : 2022/12/13 17:36
 @Desc  :
"""

from configparser import ConfigParser
import json


class JSON:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.file_path, mode='r', encoding="utf-8") as f:
            data = json.load(f)
        return data

    def write_file(self, data):
        with open(self.file_path, mode='w', encoding="utf-8") as f:
            json.dump(data, f)

    def get_projects(self):
        self.data = self.read_file()
        project_name = list()
        for project in self.data["project"]:
            project_name.append(project["project_name"])
        return project_name

    def get_current_project(self):
        self.data = self.read_file()
        return self.data.get("current_project")

    def get_db_name(self):
        self.data = self.read_file()
        return self.data["project_name"][self.get_current_project()]["DB"]

    def set_current_project(self, project_name):
        self.data["current_project"] = project_name
        self.write_file(self.data)
        return True


class INI:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cnf = ConfigParser()
        self.cnf.read(self.file_path, encoding="utf-8-sig")

    def get_options(self, section, options_key: list):
        if self._is_section(section):
            options_value = list()
            for option_key in options_key:
                options_value.append(self.cnf.get(section, option_key))
            return dict(zip(options_key, options_value))
        else:
            print(f"section: '{section}' is not in config.ini")
            exit(0)

    def get_sections(self):
        return self.cnf.sections()

    def save_options(self, options, section):
        for k, v in options.items():
            self.cnf.set(section, k, v)
        self.cnf.write(open(self.file_path, "w"))

    def _is_section(self, section):
        sections = self.get_sections()
        if section in sections:
            return True
        else:
            return False
