#!/usr/bin/env python
# coding=utf-8
import os
import shutil


HOME = os.environ['HOME']

PREFERENCES_DIR = os.path.join(os.path.dirname(__file__), "preferences")

PATHS = [
    "Library/Application Support/PyCharm30",
    "Library/Preferences/PyCharm30",
    "Library/Caches/PyCharm30",
    "Library/Logs/PyCharm30"
]

PATHS = [os.path.join(HOME, path) for path in PATHS]

PREFERENCES = [
    "options/colors.scheme.xml",
    "options/editor.xml",
    "options/ide.general.xml",
    "options/options.xml",
    "options/other.xml",
    "options/ui.lnf.xml",
    "options/window.manager.xml",
    "colors",
    "componentVersions",
    "inspection",
    "options/IntelliLang.xml",
    "options/appComponentVersions.xml",
    "options/browsers.xml",
    "options/encoding.xml",
    "options/feature.usage.statistics.xml",
    "options/file.template.settings.xml",
    "options/jdk.table.xml",
    "options/notifications.xml",
    "options/path.macros.xml",
    "options/statistics.application.usages.xml",
    "options/vcs.xml",
    "tasks"
]


def remove():
    for path in PATHS:
        if os.path.exists(path):
            print 'Removing => %s' % path
            shutil.rmtree(path)
        else:
            print 'Does not exist => %s' % path

def apply_preferences():
    for dir_ in os.listdir(PREFERENCES_DIR):
        source = os.path.join(PREFERENCES_DIR, dir_)
        dest = os.path.join(PATHS[1], dir_)
        
        print 'Copy %s => %s' % (source, dest)
        shutil.copytree(source, dest)


def main():
    remove()
    apply_preferences()


if __name__ == '__main__':
    main()
