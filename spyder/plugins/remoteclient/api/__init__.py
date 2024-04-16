# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""
spyder.plugins.remoteclient.api
===============================

Remote Client Plugin API.
"""

# ---- Constants
# -----------------------------------------------------------------------------
class RemoteClientActions:
    ManageConnections = "manage connections"


class RemoteClientMenus:
    RemoteConsoles = "remote_consoles_menu"


class RemoteConsolesMenuSections:
    ManagerSection = "manager_section"
    ConsolesSection = "consoles_section"
