import os
import re

base_file = "asper_letterhead.html"
with open(base_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Split the content into top, middle, and bottom
# We will replace everything inside <main class="content"> ... </main>
pattern = re.compile(r'(<main class="content">)(.*?)(</main>)', re.DOTALL)
match = pattern.search(html_content)

if not match:
    print("Could not find main content area!")
    exit(1)

top_html = html_content[:match.start(2)]
bottom_html = html_content[match.end(2):]

def create_file(filename, ref_no, date, subject, recipient, body, sign_name="Sannia Aslam", sign_title="Co-Founder & Director"):
    
    # Generate signature block
    signature = f"""
        <div class="signature-section">
            <div class="signature-box">
                <div class="signature-closing">Sincerely,</div>
                <div class="signature-line"></div>
                <div class="signature-name">{sign_name}</div>
                <div class="signature-title">{sign_title}</div>
                <div class="signature-title" style="color: var(--brand-teal); font-weight: 700;">Asper InfoTech (Pvt) Ltd.</div>
            </div>
        </div>
"""

    content = f"""
        <div class="meta-container">
            <div class="meta-box"><span>Ref No //</span> {ref_no}</div>
            <div class="meta-box"><span>Date //</span> {date}</div>
        </div>

        <div class="recipient">
            {recipient}
        </div>

        <div class="subject">
            {subject}
        </div>

        <div class="body-text">
            {body}
        </div>
        {signature}
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(top_html + content + bottom_html)
    print(f"Created: {filename}")

# 1. Blank Letterhead
create_file(
    "1_blank_letterhead.html", 
    "AIT/2026/________", "DD Month YYYY", 
    "SUBJECT / TITLE HERE", 
    "TO WHOM IT MAY CONCERN", 
    "<p><br><br><br><br><br><br><br><br></p>"
)

# 2. Affiliation Hammad Aslam
create_file(
    "2_affiliation_hammad_aslam.html", 
    "AIT/2026/0101", "01 October 2026", 
    "COMPANY AFFILIATION &amp; AUTHORIZATION", 
    "TO WHOM IT MAY CONCERN", 
    """<p>This is to formally certify that <strong>Mr. Hammad Aslam</strong> is officially affiliated with <strong>Asper InfoTech Private Limited</strong>, a technology company based in Hasilpur, Punjab, Pakistan.</p>
       <p>Mr. Hammad Aslam serves as the <strong>Founder &amp; Chief Executive Officer (CEO)</strong> of Asper InfoTech Private Limited and is authorized to represent the company in professional, commercial, business, technology, institutional, and international engagements.</p>
       <p>In his official capacity, Mr. Hammad Aslam may represent Asper InfoTech Private Limited in conferences, forums, meetings, business discussions, professional events, international engagements, and other activities relevant to the company's interests.</p>
       <p>This letter serves as official confirmation of Mr. Hammad Aslam's position, professional affiliation, and authorization to represent Asper InfoTech Private Limited whenever such confirmation is required by a government authority, embassy, consulate, international organization, educational institution, conference organizer, business entity, or other relevant organization.</p>
       <p>This certification is issued upon his request for official and professional purposes.</p>"""
)

# 3. Affiliation Sannia Aslam
create_file(
    "3_affiliation_sannia_aslam.html", 
    "AIT/2026/0102", "01 October 2026", 
    "COMPANY AFFILIATION &amp; AUTHORIZATION", 
    "TO WHOM IT MAY CONCERN", 
    """<p>This is to formally certify that <strong>Ms. Sannia Aslam</strong> is officially affiliated with <strong>Asper InfoTech Private Limited</strong>, a technology company based in Hasilpur, Punjab, Pakistan.</p>
       <p>Ms. Sannia Aslam serves as the <strong>Co-Founder &amp; Director</strong> of Asper InfoTech Private Limited and is authorized to represent the company in professional, commercial, business, technology, institutional, and international engagements.</p>
       <p>In her official capacity, Ms. Sannia Aslam may represent Asper InfoTech Private Limited in conferences, forums, meetings, business discussions, professional events, international engagements, and other activities relevant to the company's interests.</p>
       <p>This letter serves as official confirmation of Ms. Sannia Aslam's position, professional affiliation, and authorization to represent Asper InfoTech Private Limited whenever such confirmation is required by a government authority, embassy, consulate, international organization, educational institution, conference organizer, business entity, or other relevant organization.</p>
       <p>This certification is issued upon her request for official and professional purposes.</p>""",
    sign_name="Hammad Aslam", sign_title="Founder & CEO"
)

# 4. Job Offer Letter
create_file(
    "4_job_offer_letter.html", 
    "AIT/HR/2026/015", "01 October 2026", 
    "PROVISIONAL JOB OFFER", 
    "MR. JOHN DOE<br><span style='font-size: 9pt; color: #64748b;'>Software Engineer Candidate</span>", 
    """<p>Dear John,</p>
       <p>We are delighted to offer you the position of <strong>Senior Software Engineer</strong> at <strong>Asper InfoTech Private Limited</strong>. Your skills and experience will be an ideal fit for our engineering team.</p>
       <p>Your starting salary will be <strong>PKR 150,000/- per month</strong>, subject to applicable taxes. You will be expected to work 40 hours per week from our Hasilpur office.</p>
       <p>If you accept this offer, your tentative start date will be <strong>15 October 2026</strong>. Please sign and return a copy of this letter by 05 October 2026 to indicate your acceptance of this offer.</p>
       <p>We look forward to welcoming you to the Asper InfoTech team.</p>"""
)

# 5. Appointment Letter
create_file(
    "5_appointment_letter.html", 
    "AIT/HR/2026/020", "15 October 2026", 
    "LETTER OF APPOINTMENT", 
    "MR. JOHN DOE", 
    """<p>Dear John,</p>
       <p>Subsequent to your acceptance of our job offer, we are pleased to officially appoint you as a <strong>Senior Software Engineer</strong> at Asper InfoTech Private Limited, effective from <strong>15 October 2026</strong>.</p>
       <p>You will be on a probation period of three (3) months. During this time, your performance will be evaluated. Upon satisfactory completion of your probation, your employment will be confirmed in writing.</p>
       <p>Your employment will be governed by the standard policies, rules, and regulations of the company, which may be amended from time to time at the company's discretion.</p>
       <p>Congratulations and welcome aboard!</p>"""
)

# 6. Contract Agreement
create_file(
    "6_contract_agreement.html", 
    "AIT/LEGAL/2026/004", "01 October 2026", 
    "SOFTWARE DEVELOPMENT CONTRACT AGREEMENT", 
    "TECH SOLUTIONS LLC.", 
    """<p>This Contract Agreement is entered into on <strong>01 October 2026</strong> between <strong>Asper InfoTech Private Limited</strong> (hereinafter referred to as the "Service Provider") and <strong>Tech Solutions LLC.</strong> (hereinafter referred to as the "Client").</p>
       <p><strong>1. Scope of Work:</strong> The Service Provider agrees to develop a customized web application as outlined in the attached technical specification document (Annexure A).</p>
       <p><strong>2. Payment Terms:</strong> The Client agrees to pay a total sum of $5,000 USD. A 30% advance payment is required to commence development, with the remaining 70% payable upon final delivery and deployment.</p>
       <p><strong>3. Confidentiality:</strong> Both parties agree to maintain strict confidentiality regarding all proprietary information shared during the course of this project.</p>
       <p>Please sign below to acknowledge and accept the terms of this contract.</p>
       <br><br><br>
       <div style="display:flex; justify-content:space-between; width:100%; margin-top:20px;">
           <div>______________________<br><strong>Tech Solutions LLC.</strong></div>
       </div>"""
)

# 7. Partnership Deal
create_file(
    "7_partnership_deal.html", 
    "AIT/BD/2026/009", "01 October 2026", 
    "MEMORANDUM OF UNDERSTANDING (MoU)", 
    "GLOBAL TECH INNOVATIONS", 
    """<p>This Memorandum of Understanding (MoU) serves to establish a formal partnership between <strong>Asper InfoTech Private Limited</strong> and <strong>Global Tech Innovations</strong>.</p>
       <p>The purpose of this partnership is to collaborate on <strong>Artificial Intelligence and Cloud Solutions</strong> for the mutual benefit of both organizations. Both companies agree to share technological resources, APIs, and cross-promote each other's digital products.</p>
       <p>This partnership is effective immediately and will remain valid for a period of two (2) years, subject to renewal upon mutual agreement.</p>
       <p>We are excited about the opportunities this collaboration will bring to the technology sector in Pakistan and globally.</p>
       <br><br><br>
       <div style="display:flex; justify-content:space-between; width:100%; margin-top:20px;">
           <div>______________________<br><strong>Global Tech Innovations</strong></div>
       </div>"""
)

# 8. Recommendation Letter
create_file(
    "8_recommendation_letter.html", 
    "AIT/HR/2026/045", "01 October 2026", 
    "LETTER OF RECOMMENDATION", 
    "TO WHOM IT MAY CONCERN", 
    """<p>It is my absolute pleasure to recommend <strong>Mr. Ali Raza</strong> for employment with your organization. Ali has worked with <strong>Asper InfoTech Private Limited</strong> as a <strong>Frontend Developer</strong> from January 2024 to September 2026.</p>
       <p>During his tenure with us, Ali consistently demonstrated exceptional coding skills, a strong work ethic, and a deep understanding of modern web technologies, particularly React and Tailwind CSS. He was a highly valuable member of our engineering team.</p>
       <p>Ali is a quick learner, an excellent team player, and always willing to go the extra mile to ensure project success. I have no doubt that he will be an outstanding asset to any organization he joins.</p>
       <p>I highly recommend Mr. Ali Raza and wish him the very best in his future professional endeavors. Please feel free to contact us if you require any further information.</p>"""
)

# 9. Resignation Acceptance
create_file(
    "9_resignation_acceptance.html", 
    "AIT/HR/2026/051", "01 October 2026", 
    "ACCEPTANCE OF RESIGNATION", 
    "MR. ALI RAZA", 
    """<p>Dear Ali,</p>
       <p>This letter is to formally acknowledge and accept your letter of resignation from the position of <strong>Frontend Developer</strong> at <strong>Asper InfoTech Private Limited</strong>, dated 15 September 2026.</p>
       <p>As per the standard 15-day notice period specified in your employment contract, your final day of employment with the company will be <strong>01 October 2026</strong>.</p>
       <p>We would like to take this opportunity to thank you for your contributions to Asper InfoTech during your time here. Your dedication and hard work have been greatly appreciated by the entire team.</p>
       <p>We wish you the best of luck in your future career endeavors.</p>"""
)

# 10. Warning Letter
create_file(
    "10_warning_letter.html", 
    "AIT/HR/2026/088", "01 October 2026", 
    "OFFICIAL WARNING LETTER", 
    "PRIVATE & CONFIDENTIAL<br><span style='font-size: 9pt; color: #64748b;'>Employee Name Withheld</span>", 
    """<p>Dear Employee,</p>
       <p>This letter serves as an official written warning regarding your recent conduct and performance at <strong>Asper InfoTech Private Limited</strong>.</p>
       <p>It has been brought to our attention that you have consistently violated the company's attendance policy by arriving late for the past two weeks without prior notification or valid justification. This behavior is unacceptable and disrupts the workflow of your team.</p>
       <p>You are hereby advised to strictly adhere to the company's working hours. Failure to show immediate and sustained improvement in your punctuality may result in further disciplinary action, up to and including termination of your employment contract.</p>
       <p>A copy of this warning letter will be placed in your official personnel file.</p>"""
)

# 11. Experience Certificate
create_file(
    "11_experience_certificate.html", 
    "AIT/HR/2026/092", "01 October 2026", 
    "EXPERIENCE CERTIFICATE", 
    "TO WHOM IT MAY CONCERN", 
    """<p>This is to certify that <strong>Mr. Ali Raza</strong> was a full-time employee of <strong>Asper InfoTech Private Limited</strong> from <strong>01 January 2024</strong> to <strong>01 October 2026</strong>.</p>
       <p>During his tenure with us, he served in the capacity of <strong>Frontend Developer</strong>. His key responsibilities included designing user interfaces, developing responsive web applications, and optimizing performance for client projects.</p>
       <p>Throughout his employment, we found him to be a hardworking, dedicated, and highly skilled professional. He successfully completed all assigned projects and maintained excellent professional conduct.</p>
       <p>We wish him all the success in his future endeavors.</p>"""
)

