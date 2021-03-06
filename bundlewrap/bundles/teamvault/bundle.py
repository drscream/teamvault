pkg_apt = {
    "python3-setuptools": {},
    "mercurial": {},
    "libpq-dev": {},
    "libffi-dev": {},
    "python3-pip": {
        'triggers': [
            "action:teamvault_install",
        ],
    },
    "python3.4-dev": {},
}

#pkg_pip = {
#    "coveralls": {
#        'needs': ["pkg_apt:python3-pip"],
#    },
#}

symlinks = {
    "/usr/bin/pip": {
        'target': "/usr/bin/pip3",
        'needed_by': ["pkg_pip:"],
    }
}

actions = {
    "teamvault_install": {
        'command': "pip3 install -e /teamvault/",
        'needs': [
            "pkg_apt:",
        ],
        'triggered': True,
        'triggers': [
            "action:teamvault_setup",
        ],
    },
    "teamvault_setup": {
        'command': "teamvault setup",
        'triggered': True,
        'triggers': [
            "action:teamvault_set_base_url",
        ],
    },
    "teamvault_set_base_url": {
        'command': "sed -i 's/^base_url = .*$/base_url = http:\\/\\/teamvault/' /etc/teamvault.cfg",
        'triggered': True,
        'triggers': [
            "action:teamvault_enable_debugging",
        ],
    },
    "teamvault_enable_debugging": {
        'command': "sed -i 's/^insecure_debug_mode = .*$/insecure_debug_mode = enabled/' /etc/teamvault.cfg",
        'triggered': True,
        'triggers': [
            "action:teamvault_upgrade",
        ],
    },
    "teamvault_upgrade": {
        'command': "teamvault upgrade",
        'triggered': True,
    },
    "apt_update": {
        'command': "apt-get update",
        'needed_by': ["pkg_apt:"],
    }
}
