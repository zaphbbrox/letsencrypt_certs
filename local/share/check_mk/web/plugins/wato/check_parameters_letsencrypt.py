#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""
Web configuration for letsencrypt_cert check
"""
# pylint: disable=undefined-variable
# +-----------------------------------------------------------------+
# |                                                                 |
# |        (  ___ \     | \    /\|\     /||\     /|( (    /|        |
# |        | (   ) )    |  \  / /| )   ( || )   ( ||  \  ( |        |
# |        | (__/ /     |  (_/ / | |   | || (___) ||   \ | |        |
# |        |  __ (      |   _ (  | |   | ||  ___  || (\ \) |        |
# |        | (  \ \     |  ( \ \ | |   | || (   ) || | \   |        |
# |        | )___) )_   |  /  \ \| (___) || )   ( || )  \  |        |
# |        |/ \___/(_)  |_/    \/(_______)|/     \||/    )_)        |
# |                                                                 |
# | Copyright Bastian Kuhn 2018                mail@bastian-kuhn.de |
# +-----------------------------------------------------------------+
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

register_check_parameters(
            subgroup_applications,
                "letsencrypt",
                    _("LetsEncrypt Certificates"),
                        Dictionary(
                            elements = [
                                ( "long",
                                  Integer(
                                  title = _("Days when check will give a warning (if not specified otherwise)."),
                                  default_value = 30,
                                  )),
                                  ( "long_state",
                                    MonitoringState(
                                    title = _("State when there are less days specified in long variable until cert becomes invalid."),
                                    default_value = 1,
                                )),
                                ( "short",
                                  Integer(
                                  title = _("Days when check will give a critical warning (if not specified otherwise)."),
                                  default_value = 15,
                                )),
                                ( "short_state",
                                  MonitoringState(
                                  title = _("State when there are less days specified in short variable until cert becomes invalid."),
                                  default_value = 2,
                                )),
                            ]
                        ),
        TextAscii(
                title = _("Description"),
                    allow_empty = True),
        match_type = "dict",
)
