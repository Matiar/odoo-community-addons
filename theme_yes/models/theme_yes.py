from odoo import models


class ThemeYes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_yes_post_copy(self, mod):
        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')
