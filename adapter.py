"""
AMD AI Developer Program Site Adapter.
Automated onboarding adapter for AMD AI Developer Program & Token Lab
Target: https://developer.amd.com/ai-developer-program/
"""
import time
import re
from typing import Dict, Any, Optional

from core.adapter import BaseSiteAdapter
from core.identity import generate_identity
from core.pilot import human_type, smart_click
from core.mail_client import DisposableMailClient


class AmdAdapter(BaseSiteAdapter):
    """
    Registration adapter for AMD AI Developer Program.
    Form URL: https://www.amd.com/en/registration/ai-dev-program-sign-up-form.html?custtarg=aHR0cHM6Ly9kZXZlbG9wZXIuYW1kLmNvbT9SZWxheVN0YXRlPQ==
    """

    def __init__(self, page, context, config=None):
        super().__init__(page, context, config)
        self.mail_client: Optional[DisposableMailClient] = None
        self.form_submitted: bool = False

    def target_url(self) -> str:
        return "https://www.amd.com/en/registration/ai-dev-program-sign-up-form.html?custtarg=aHR0cHM6Ly9kZXZlbG9wZXIuYW1kLmNvbT9SZWxheVN0YXRlPQ=="

    def prepare_identity(self) -> Dict[str, Any]:
        """Generate synthetic credentials matching AMD requirements."""
        use_disposable = self.config.get("use_disposable_mail", True)
        if use_disposable:
            self.mail_client = DisposableMailClient()
            ident = generate_identity(locale="US", mail_client=self.mail_client)
        else:
            ident = generate_identity(locale="US")

        self.account_data = ident
        return self.account_data

    def _clear_overlays(self):
        """Remove OneTrust cookie consent banners and dark backdrops."""
        try:
            self.page.evaluate('''() => {
                const ids = ["onetrust-consent-sdk", "onetrust-pc-dark-filter", "onetrust-banner-sdk"];
                ids.forEach(id => {
                    const el = document.getElementById(id);
                    if (el) el.remove();
                });
                document.body.style.overflow = "auto";
            }''')
        except Exception:
            pass

    def fill_form(self, identity: Dict[str, Any]) -> bool:
        """Fill AMD AI Developer Program application form."""
        self._clear_overlays()
        self.page.wait_for_selector('input[name="Email"]', timeout=30000)

        # 1. Fill basic personal and company information
        email = identity["email"]
        first_name = identity.get("first_name", "Alex")
        last_name = identity.get("last_name", "Schmidt")

        human_type(self.page, 'input[name="First_Name"]', first_name)
        human_type(self.page, 'input[name="Last_Name"]', last_name)
        human_type(self.page, 'input[name="Email"]', email)
        human_type(self.page, 'input[name="Company"]', "Independent AI Lab")

        self.page.mouse.wheel(0, 250)
        time.sleep(0.5)

        # 2. Select Country and Locale
        try:
            self.page.select_option('select[name="Country"]', value="US")
            time.sleep(0.2)
            self.page.select_option('select[name="Locale"]', value="en_US")
            time.sleep(0.2)
        except Exception:
            pass

        # 3. Check technical interest checkboxes
        def check_box(selector, text_label):
            lbl = self.page.locator(f'label:has-text("{text_label}"), span:has-text("{text_label}")').first
            if lbl.count() > 0:
                lbl.scroll_into_view_if_needed()
                smart_click(self.page, lbl)
                time.sleep(0.1)
            self.page.evaluate(f'''() => {{
                const el = document.querySelector('{selector}');
                if (el && !el.checked) {{
                    el.checked = true;
                    el.dispatchEvent(new Event("input", {{bubbles: true}}));
                    el.dispatchEvent(new Event("change", {{bubbles: true}}));
                }}
            }}''')

        check_box('input[value="Cloud/data center"]', "Cloud/data center")
        check_box('input[value="Workstation or desktop"]', "Workstation or desktop")
        check_box('input[name="marketoProgramInterestField-1230871231"]', "By checking this box")

        self._clear_overlays()

        # 4. Human-like interaction pause to allow Akamai telemetry scripts to collect entropy
        print("[*] [AMD] Simulating human browsing behavior for Akamai telemetry verification (6s)...")
        for i in range(3):
            self.page.mouse.move(200 + i * 50, 300 + i * 30)
            time.sleep(2)

        return True

    def submit_and_confirm(self) -> bool:
        """Submit form and monitor activation response."""
        submit_btn = self.page.locator('#form-button-1857186030, button[type="submit"], button:has-text("Join")').first
        submit_btn.scroll_into_view_if_needed()
        time.sleep(0.5)

        if not smart_click(self.page, submit_btn):
            submit_btn.click(force=True)

        print("[*] [AMD] Form submitted, waiting for confirmation or activation redirect...")
        try:
            self.page.wait_for_url("**/activate-account.html*", timeout=35000)
            print("[+] [AMD] Registration accepted! Redirected to account activation portal.")
            self.form_submitted = True
            return True
        except Exception:
            # Check for inline success confirmation text
            content = self.page.content()
            if any(k in content.lower() for k in ["thank you", "check your email", "activation", "we have received"]):
                print("[+] [AMD] Confirmation message visible on page.")
                self.form_submitted = True
                return True

        return False
