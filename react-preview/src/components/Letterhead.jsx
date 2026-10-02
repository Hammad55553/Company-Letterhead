import React from 'react';
import './Letterhead.css';

const Letterhead = ({
  reference = "AIT/2026/001",
  date = "01 October 2026",
  recipient,
  children,
  signatureName = "Hammad Aslam",
  signatureRole = "Founder & CEO"
}) => {
  return (
    <div className="letterhead-container">
      {/* Top Right Corner: Hex Mesh */}
      <svg className="top-tech" viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 0)" className="h-teal" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 0)" className="h-line" opacity="0.85" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 0)" className="h-grey" opacity="0.6" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(112.1, 0)" className="h-grey" opacity="0.35" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 30)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 30)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 30)" className="h-line" opacity="0.9" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 30)" className="h-teal" opacity="0.75" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(164.1, 30)" className="h-grey" opacity="0.5" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(129.4, 30)" className="h-grey" opacity="0.3" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 60)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 60)" className="h-teal" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 60)" className="h-line" opacity="0.7" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 60)" className="h-grey" opacity="0.55" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 60)" className="h-grey" opacity="0.35" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 60)" className="h-teal" opacity="0.18" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 90)" className="h-line" opacity="0.8" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 90)" className="h-grey" opacity="0.55" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 90)" className="h-teal" opacity="0.45" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 90)" className="h-grey" opacity="0.3" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 120)" className="h-grey" opacity="0.5" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 120)" className="h-grey" opacity="0.4" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 120)" className="h-grey" opacity="0.22" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 150)" className="h-grey" opacity="0.3" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 150)" className="h-teal" opacity="0.25" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 180)" className="h-grey" opacity="0.2" />

        <circle className="h-dot" cx="302.7" cy="30" r="3.2" />
      </svg>

      {/* Header */}
      <header className="header">
        <img src="/assets/unnamed-removebg-preview.png" className="main-logo" alt="Asper InfoTech Logo" />
        <div className="company-info">
          <h1 className="company-name">Asper InfoTech</h1>
          <p className="company-tagline">(Private) Limited</p>
        </div>
      </header>

      {/* Content */}
      <main className="content">
        <img src="/assets/unnamed-removebg-preview.png" className="watermark" alt="" />

        <div className="date-ref">
          <span><strong>Ref //</strong> {reference}</span>
          <span><strong>Date //</strong> {date}</span>
        </div>

        {recipient && (
          <div className="recipient">
            {recipient}
          </div>
        )}

        <div className="body-text">
          {children}
        </div>

        <div className="signature">
          <div className="closing">Sincerely,</div>
          <img src="/assets/stamp.jpg" className="company-stamp" alt="Company Stamp" />
          <div className="sig-line"></div>
          <div className="name">{signatureName}</div>
          <div className="role">{signatureRole}</div>
        </div>
      </main>

      {/* Bottom Left Corner: Hex Mesh Watermark */}
      <svg className="bottom-tech" viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 0)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 0)" className="h-teal" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 0)" className="h-line" opacity="0.85" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 0)" className="h-grey" opacity="0.6" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(112.1, 0)" className="h-grey" opacity="0.35" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 30)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 30)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 30)" className="h-line" opacity="0.9" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 30)" className="h-teal" opacity="0.75" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(164.1, 30)" className="h-grey" opacity="0.5" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(129.4, 30)" className="h-grey" opacity="0.3" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 60)" className="h-navy" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 60)" className="h-teal" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 60)" className="h-line" opacity="0.7" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 60)" className="h-grey" opacity="0.55" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 60)" className="h-grey" opacity="0.35" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 60)" className="h-teal" opacity="0.18" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 90)" className="h-line" opacity="0.8" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 90)" className="h-grey" opacity="0.55" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 90)" className="h-teal" opacity="0.45" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 90)" className="h-grey" opacity="0.3" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 120)" className="h-grey" opacity="0.5" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 120)" className="h-grey" opacity="0.4" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 120)" className="h-grey" opacity="0.22" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 150)" className="h-grey" opacity="0.3" />
        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 150)" className="h-teal" opacity="0.25" />

        <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 180)" className="h-grey" opacity="0.2" />

        <circle className="h-dot" cx="302.7" cy="30" r="3.2" />
      </svg>

      {/* Footer (text only) */}
      <footer className="footer">
        <div className="footer-text">
          <span><strong style={{ color: 'var(--accent-color)' }}>Address:</strong> <span style={{ color: 'var(--primary-color)' }}>Quaid-e-Azam colony Hasilpur, Punjab Pakistan</span></span>
          <span><strong style={{ color: 'var(--accent-color)' }}>Phone:</strong> <span style={{ color: 'var(--primary-color)' }}>+923120441431</span></span>
          <span><strong style={{ color: 'var(--accent-color)' }}>Email:</strong> <span style={{ color: 'var(--primary-color)' }}>info@asperinfotech.com</span></span>
        </div>
      </footer>
    </div>
  );
};

export default Letterhead;
