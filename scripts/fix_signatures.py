import os
import re

def fix_file(filename, partner_name):
    if not os.path.exists(filename):
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove the manual signature from body
    content = re.sub(r'<br><br><br>\s*<div style="display:flex; justify-content:space-between; width:100%; margin-top:20px;">.*?</div>\s*</div>', '</div>', content, flags=re.DOTALL)
    
    # Inject partner signature box into the signature section
    partner_box = f"""
            <div class="signature-box" style="text-align: left;">
                <div class="signature-closing">Agreed & Accepted:</div>
                <div class="signature-line" style="margin: 50px 0 10px 0;"></div>
                <div class="signature-name">Authorized Signatory</div>
                <div class="signature-title" style="color: var(--brand-dark); font-weight: 700;">{partner_name}</div>
            </div>"""
            
    # The signature-section currently has justify-content: flex-end;
    # We need to change it to space-between
    content = content.replace('justify-content: flex-end;', 'justify-content: space-between;')
    
    # Inject the partner box before the Asper signature box
    content = content.replace('<div class="signature-box">', partner_box + '\n            <div class="signature-box" style="text-align: right;">')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {filename}")

fix_file("6_contract_agreement.html", "Tech Solutions LLC.")
fix_file("7_partnership_deal.html", "Global Tech Innovations")
fix_file("Asper-CRM/frontend/public/templates/6_contract_agreement.html", "Tech Solutions LLC.")
fix_file("Asper-CRM/frontend/public/templates/7_partnership_deal.html", "Global Tech Innovations")

