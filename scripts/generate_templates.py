import os
import re

base_file = "/Users/mac/React-native/Letter Head/src/base_letterhead.html"
out_dir = "/Users/mac/React-native/Letter Head/html_templates"

os.makedirs(out_dir, exist_ok=True)

with open(base_file, 'r') as f:
    html = f.read()

letters = {
    "1_blank_letterhead.html": {
        "ref": "AIT/2026/001",
        "recipient": "Dear [Name],\n      <span>[Designation]<br>[Company/Address]</span>",
        "body": "<p>[Type your letter content here]</p>"
    },
    "4_job_offer_letter.html": {
        "ref": "AIT/OFFER/2026/004",
        "recipient": "Dear [Candidate Name],\n      <span>Software Engineer<br>[Address]<br>[Email]<br>[Phone]</span>",
        "body": """
      <p><strong>Subject: Offer of Employment</strong></p>
      <p>We are delighted to offer you the position of Software Engineer at Asper InfoTech (Private) Limited. Your skills and experience make you an excellent fit for our team.</p>
      <p>Your expected joining date will be [Joining Date]. Your starting salary will be [Salary] per annum, subject to applicable taxes. You will be on a probation period of three (3) months.</p>
      <p>Please sign and return a copy of this letter to indicate your acceptance of this offer.</p>
"""
    },
    "5_appointment_letter.html": {
        "ref": "AIT/APP/2026/005",
        "recipient": "Dear [Employee Name],\n      <span>[Designation]<br>[Address]</span>",
        "body": """
      <p><strong>Subject: Letter of Appointment</strong></p>
      <p>Following your successful interview, we are pleased to officially appoint you as [Designation] at Asper InfoTech (Private) Limited, effective from [Joining Date].</p>
      <p>You will be governed by the company's policies and procedures, which may be amended from time to time. Your total compensation package is detailed in the annexure attached to this letter.</p>
      <p>We welcome you to the team and look forward to a long and successful professional relationship.</p>
"""
    },
    "6_contract_agreement.html": {
        "ref": "AIT/CTR/2026/006",
        "recipient": "Dear [Client/Partner Name],\n      <span>[Company Name]<br>[Address]</span>",
        "body": """
      <p><strong>Subject: Contract Agreement</strong></p>
      <p>This document serves as a formal contract agreement between Asper InfoTech (Private) Limited and [Client/Partner Name] for the provision of [Services/Products].</p>
      <p>The terms and conditions of this agreement are detailed in the attached schedule. Both parties agree to fulfill their respective obligations as outlined in the document.</p>
      <p>Please review and sign to acknowledge your agreement.</p>
"""
    },
    "7_partnership_deal.html": {
        "ref": "AIT/PTR/2026/007",
        "recipient": "Dear [Partner Name],\n      <span>[Company Name]<br>[Address]</span>",
        "body": """
      <p><strong>Subject: Strategic Partnership Agreement</strong></p>
      <p>We are thrilled to officially commence our strategic partnership. We believe this collaboration between Asper InfoTech and [Company Name] will drive significant mutual growth.</p>
      <p>The joint initiatives and revenue-sharing models discussed during our previous meetings are finalized in the enclosed memorandum of understanding (MoU).</p>
      <p>We look forward to achieving great milestones together.</p>
"""
    },
    "8_recommendation_letter.html": {
        "ref": "AIT/REC/2026/008",
        "recipient": "To Whom It May Concern,\n      <span></span>",
        "body": """
      <p><strong>Subject: Letter of Recommendation</strong></p>
      <p>It is my absolute pleasure to recommend [Employee Name] for [Position/Opportunity]. They worked at Asper InfoTech as a [Designation] and consistently exceeded expectations.</p>
      <p>During their time with us, they demonstrated exceptional problem-solving skills and a strong commitment to team goals. I am confident they will be an invaluable asset to your organization.</p>
      <p>Please feel free to contact me if you require further information.</p>
"""
    },
    "9_resignation_acceptance.html": {
        "ref": "AIT/HR/2026/009",
        "recipient": "Dear [Employee Name],\n      <span>[Designation]</span>",
        "body": """
      <p><strong>Subject: Acceptance of Resignation</strong></p>
      <p>This letter is to formally acknowledge and accept your resignation from the position of [Designation] at Asper InfoTech, received on [Date].</p>
      <p>As per your notice period, your last working day will be [Last Working Day]. Please ensure all pending tasks are handed over to your manager and company assets are returned to IT before your departure.</p>
      <p>We thank you for your contributions and wish you success in your future career.</p>
"""
    },
    "10_warning_letter.html": {
        "ref": "AIT/HR/2026/010",
        "recipient": "Dear [Employee Name],\n      <span>[Designation]</span>",
        "body": """
      <p><strong>Subject: Official Warning</strong></p>
      <p>This letter serves as an official warning regarding your recent performance and conduct. On [Date], it was observed that you violated company policies regarding [Reason for warning].</p>
      <p>We expect all employees to adhere to the company's code of conduct. Failure to improve your performance or any further violations may result in severe disciplinary action, up to and including termination of your employment.</p>
      <p>We hope to see an immediate and sustained improvement.</p>
"""
    },
    "11_experience_certificate.html": {
        "ref": "AIT/EXP/2026/011",
        "recipient": "To Whom It May Concern,\n      <span></span>",
        "body": """
      <p><strong>Subject: Experience Certificate</strong></p>
      <p>This is to certify that Mr./Ms. [Employee Name] was employed with Asper InfoTech (Private) Limited as a [Designation] from [Start Date] to [End Date].</p>
      <p>During their tenure, we found them to be highly professional, dedicated, and hardworking. They have consistently demonstrated a strong work ethic and contributed significantly to the team's success.</p>
      <p>We wish them all the best in their future endeavors.</p>
"""
    }
}

for filename, content in letters.items():
    new_html = html
    # Replace Reference
    new_html = re.sub(r'(<strong>Ref //</strong>\s*)[^<]+', r'\g<1>' + content['ref'], new_html)
    # Replace Recipient
    new_html = re.sub(r'<div class="recipient">.*?</div>', f'<div class="recipient">\n      {content["recipient"]}\n    </div>', new_html, flags=re.DOTALL)
    # Replace Body
    new_html = re.sub(r'<div class="body-text">.*?</div>', f'<div class="body-text">\n{content["body"]}\n    </div>', new_html, flags=re.DOTALL)
    
    out_path = os.path.join(out_dir, filename)
    with open(out_path, 'w') as out_f:
        out_f.write(new_html)

print(f"Successfully generated {len(letters)} templates in {out_dir}")
