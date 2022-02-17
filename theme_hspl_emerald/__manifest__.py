# © 2020 Heliconia Solutions Pvt. Ltd., < hello@heliconia.io >

{
    "name": "Theme Emerald",
    "description": "A Responsive Bootstrap Theme for Odoo CMS",
    "category": "Theme/Business",
    "summary": "",
    "version": "15.0.0.1.0",
    "license": "OPL-1",
    "depends": ["base", "website", "website_crm", "website_sale"],
    "data": [
        "templates/headers.xml",
        "templates/footer.xml",
        "templates/customize_options.xml",
        "templates/snippets.xml",
        "templates/contact.xml",
    ],
    "images": [
        "static/description/Emerald_description.png",
        "static/description/emerald_screenshot.png",
    ],
    "author": "Heliconia Solutions Pvt. Ltd.",
    "application": False,
    "installable": True,
    "auto_install": False,
    # primary color not set because of css not map with 15.0
    "assets": {
        "web.assets_frontend": [
            "theme_hspl_emerald/static/src/scss/animate.css",
            "theme_hspl_emerald/static/src/scss/all.css",
            "theme_hspl_emerald/static/src/scss/Pe-icon-7-stroke.css",
            "theme_hspl_emerald/static/src/scss/themify-icons.css",
            "theme_hspl_emerald/static/src/scss/leaflet.css",
            "theme_hspl_emerald/static/src/scss/theme_styles.scss",
            "theme_hspl_emerald/static/src/scss/front.scss",
            "theme_hspl_emerald/static/lib/popper.min.js",
            "theme_hspl_emerald/static/lib/jquery.easing.1.3.js",
            "theme_hspl_emerald/static/lib/leaflet.js",
            "theme_hspl_emerald/static/src/js/main.js",
        ],
        "web._assets_primary_variables": [
            "theme_hspl_emerald/static/lib/theme/font.scss",
            "theme_hspl_emerald/static/src/scss/theme_colors.scss",
        ],
        "web._assets_frontend_helpers": [
            ("include", "theme_hspl_emerald/static/lib/theme/variables.scss"),
        ],
    },
}
