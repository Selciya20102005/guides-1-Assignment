from frappe.website.page_renderers.base_renderer import BaseRenderer


class CustomPage(BaseRenderer):

    def can_render(self):
        return self.path == "custom_page"

    def render(self):
        return self.build_response("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>My Custom Page</title>
            </head>
            <body>
                <h1>Custom Renderer Works!</h1>
                <p>This page is coming from my custom renderer.</p>
            </body>
            </html>
        """)