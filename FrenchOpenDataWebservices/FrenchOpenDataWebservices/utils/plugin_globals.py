# -*- coding: utf-8 -*-

import os
from FrenchOpenDataWebservices.utils.singleton import Singleton
from qgis.PyQt.QtCore import QSettings


@Singleton
class PluginGlobals:
    """ """

    # Plugin properties
    iface = None
    plugin_path = None

    # Plugin infos
    PLUGIN_TAG = u"FrenchOpenDataWebservices"
    PLUGIN_VERSION = u"0.1.0"
    PLUGIN_SOURCE_REPOSITORY = u""

    # Tree nodes types
    NODE_TYPE_FOLDER = "folder"
    NODE_TYPE_WS = "web_service"
    NODE_TYPE_UNIVERSAL_WMS_WMTS_LAYER = "wms_wmts_universal_layer"
    NODE_TYPE_VOID_LAYER = "void_layer"
    NODE_TYPE_VECTOR_TILES_LAYER = "vector_layer"

    # Node status values
    NODE_STATUS_WARN = "warn"

    # Image directories and filenames
    IMAGES_DIR_NAME = "images"
    LOGO_FILE_NAME = ""

    ICON_WARN_FILE_NAME = "Icon_Simple_Warn.png"
    ICON_WMS_LAYER_FILE_NAME = "mIconWms.svg"
    ICON_WMS_STYLE_FILE_NAME = "mIconWmsStyle.svg"
    ICON_WFS_LAYER_FILE_NAME = "mIconWfs.svg"
    ICON_RASTER_LAYER_FILE_NAME = "mIconRaster.svg"

    # Config files dir
    CONFIG_FILES_DOWNLOAD_AT_STARTUP = True
    CONFIG_DIR_NAME = "config"
    CONFIG_FILE_NAMES = ["config.json"]
    CONFIG_FILE_URLS = [
        "https://raw.githubusercontent.com/LucasJumMou/config/main/config.json"
    ]

    # Hide resources with status = warn
    HIDE_RESOURCES_WITH_WARN_STATUS = True

    # Hide empty group in the resources tree
    HIDE_EMPTY_GROUPS = True

    def __init__(self):
        """ """

        self.default_qsettings = {
            "CONFIG_FILES_DOWNLOAD_AT_STARTUP": self.CONFIG_FILES_DOWNLOAD_AT_STARTUP,
            "CONFIG_FILE_NAMES": self.CONFIG_FILE_NAMES,
            "CONFIG_FILE_URLS": self.CONFIG_FILE_URLS,
            "HIDE_RESOURCES_WITH_WARN_STATUS": self.HIDE_RESOURCES_WITH_WARN_STATUS,
            "HIDE_EMPTY_GROUPS": self.HIDE_EMPTY_GROUPS,
        }

        self.config_dir_path = None
        self.config_file_path = None
        self.images_dir_path = None
        self.logo_file_path = None

    def set_plugin_path(self, plugin_path):
        """ """

        # system_encoding = sys.getfilesystemencoding()
        # self.plugin_path = plugin_path.decode(system_encoding)

        self.plugin_path = plugin_path

    def set_plugin_iface(self, iface):
        """ """

        self.iface = iface

    def reload_globals_from_qgis_settings(self):
        """
        Reloads the global variables of the plugin
        """

        # Read the qgis plugin settings
        s = QSettings()
        # False by default and u"0" so that parameter is checked the 1st time user opens plugin, else invert
        self.CONFIG_FILES_DOWNLOAD_AT_STARTUP = (
            False
            if s.value(
                u"{0}/config_files_download_at_startup".format(self.PLUGIN_TAG),
                self.CONFIG_FILES_DOWNLOAD_AT_STARTUP,
            )
            == u"0"
            else True
        )

        self.CONFIG_DIR_NAME = s.value(
            u"{0}/config_dir_name".format(self.PLUGIN_TAG), self.CONFIG_DIR_NAME
        )

        self.CONFIG_FILE_NAMES = s.value(
            u"{0}/config_file_names".format(self.PLUGIN_TAG), self.CONFIG_FILE_NAMES
        )

        self.CONFIG_FILE_URLS = s.value(
            u"{0}/config_file_urls".format(self.PLUGIN_TAG), self.CONFIG_FILE_URLS
        )

        # False by default so that parameter is checked the 1st time user opens plugin, else invert
        self.HIDE_RESOURCES_WITH_WARN_STATUS = (
            False
            if s.value(
                u"{0}/hide_resources_with_warn_status".format(self.PLUGIN_TAG),
                self.HIDE_RESOURCES_WITH_WARN_STATUS,
            )
            == u"0"
            else True
        )

        # False by default so that parameter is checked the 1st time user opens plugin, else invert
        self.HIDE_EMPTY_GROUPS = (
            False
            if s.value(
                u"{0}/hide_empty_groups".format(self.PLUGIN_TAG), self.HIDE_EMPTY_GROUPS
            )
            == u"0"
            else True
        )

        self.config_dir_path = os.path.join(self.plugin_path, self.CONFIG_DIR_NAME)
        self.config_file_path = os.path.join(
            self.config_dir_path, self.CONFIG_FILE_NAMES[0]
        )

        self.images_dir_path = os.path.join(self.plugin_path, self.IMAGES_DIR_NAME)
        self.logo_file_path = os.path.join(self.images_dir_path, self.LOGO_FILE_NAME)

    def reset_to_defaults(self):
        """
        Reset global variables to default values
        """

        s = QSettings()
        s.setValue(u"{0}/hide_resources_with_warn_status".format(self.PLUGIN_TAG), u"1")
        s.setValue(u"{0}/hide_empty_groups".format(self.PLUGIN_TAG), u"1")
        s.setValue(
            u"{0}/config_files_download_at_startup".format(self.PLUGIN_TAG), u"1"
        )  # 0
        s.setValue(u"{0}/config_file_names".format(self.PLUGIN_TAG), ["config.json"])
        s.setValue(
            u"{0}/config_file_urls".format(self.PLUGIN_TAG),
            [""],
        )

    def get_qgis_setting_default_value(self, setting):
        """ """

        return self.default_qsettings.get(setting, None)

    def set_qgis_settings_value(self, setting, value):
        """
        Update a settings value
        """

        s = QSettings()

        # Convert boolean in unicode string
        if type(value) == bool:
            value = u"1" if value else u"0"

        # Save the settings value
        s.setValue(u"{0}/{1}".format(self.PLUGIN_TAG, setting), value)

        # Reload all settings values
        self.reload_globals_from_qgis_settings()
