import pkg_resources

from tutor import hooks

from .__about__ import __version__

# Ref: https://discuss.openedx.org/t/tutor-indigo-theme-with-new-plugin/7673/11

################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "WELCOME_MESSAGE": "Welcome to Kayan's Academy",
        "PRIMARY_COLOR": "#1968b0",  # Kayan Blue
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set INDIGO_FOOTER_NAV_LINKS=[] --set INDIGO_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Terms of service", "url": "/tos"},
            {
                "title": "Kayan Academy",
                "url": "https://kayanhr.com",
            },
        ],
    },
    "unique": {},
    "overrides": {},
}

# Theme templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorindigo", "templates")
)
# This is where the theme is rendered in the openedx build directory
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("kayanhr", "build/openedx/themes"),
    ],
)

# Force the rendering of scss files, even though they are included in a "partials" directory
hooks.Filters.ENV_PATTERNS_INCLUDE.add_item(
    r"kayanhr/lms/static/sass/partials/lms/theme/"
)

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"KAYAN_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"KAYAN_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))
