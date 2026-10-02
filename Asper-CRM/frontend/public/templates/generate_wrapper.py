import re

with open("asper_letterhead_stemp.html", "r") as f:
    stamp_html = f.read()

# Extract styles and SVG filters and the container
style_match = re.search(r'<style>(.*?)</style>', stamp_html, re.DOTALL)
styles = style_match.group(1) if style_match else ""

# Remove body flex centering from stamp styles so it doesn't break letterhead
styles = re.sub(r'body\s*{[^}]*}', '', styles)

# Add scale to stamp
styles += "\n.stamp-container { transform: scale(0.65) rotate(-3deg); position: absolute; bottom: 50mm; right: 30mm; opacity: 0.85; z-index: -1; }\n"

# Extract body contents
body_match = re.search(r'<body>(.*?)</body>', stamp_html, re.DOTALL)
stamp_body = body_match.group(1) if body_match else ""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  body {{
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
    font-family: 'Arial', sans-serif;
  }}
  .page {{
    background-color: white;
    width: 210mm;
    min-height: 297mm;
    margin: 0 auto;
    padding: 20mm;
    box-sizing: border-box;
    position: relative;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }}
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #052950;
    padding-bottom: 20px;
    margin-bottom: 40px;
  }}
  .header img {{
    width: 150px;
  }}
  .header-text {{
    text-align: right;
    color: #052950;
  }}
  .content {{
    min-height: 150mm;
  }}
  /* Letter meta etc */
  .meta-container {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    font-weight: bold;
    color: #555;
  }}
  .recipient {{
    margin-bottom: 20px;
    font-weight: bold;
    font-size: 16px;
  }}
  .subject {{
    margin-bottom: 30px;
    font-weight: bold;
    font-size: 18px;
    text-decoration: underline;
    text-align: center;
  }}
  .body-text {{
    line-height: 1.6;
    margin-bottom: 40px;
    text-align: justify;
  }}
  /* Signature area */
  .signature-section {{
    margin-top: 50px;
  }}
  .signature-box {{
    width: 250px;
  }}
  .signature-line {{
    border-top: 1px solid #000;
    margin: 40px 0 10px 0;
  }}
  
  {styles}
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <img src="unnamed-removebg-preview.png" alt="Asper InfoTech Logo" />
    <div class="header-text">
      <h2 style="margin:0;">Asper InfoTech (Pvt) Ltd.</h2>
      <p style="margin:5px 0 0 0;">Hasilpur, Punjab, Pakistan</p>
    </div>
  </div>
  
  <main class="content">
    <!-- CONTENT -->
  </main>
  
  {stamp_body}
</div>
</body>
</html>
"""

with open("asper_letterhead_stemp.html", "w") as f:
    f.write(full_html)
