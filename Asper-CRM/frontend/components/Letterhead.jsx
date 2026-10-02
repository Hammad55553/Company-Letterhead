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
  const hNavy = { fill: '#052950' };
  const hTeal = { fill: '#11b6aa' };
  const hLine = { fill: 'none', stroke: '#11b6aa', strokeWidth: 1.3 };
  const hGrey = { fill: 'none', stroke: '#cbd5e1', strokeWidth: 1.3 };

  const hexMesh = (
    <>
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 0)"   style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 0)" style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 0)" style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 0)" style={hTeal} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 0)" style={hLine} opacity="0.85" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 0)" style={hGrey} opacity="0.6" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(112.1, 0)" style={hGrey} opacity="0.35" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 30)" style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 30)"   style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 30)" style={hLine} opacity="0.9" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 30)" style={hTeal} opacity="0.75" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(164.1, 30)" style={hGrey} opacity="0.5" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(129.4, 30)" style={hGrey} opacity="0.3" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 60)"   style={hNavy} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 60)" style={hTeal} />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 60)" style={hLine} opacity="0.7" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(216.1, 60)" style={hGrey} opacity="0.55" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(181.4, 60)" style={hGrey} opacity="0.35" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(146.8, 60)" style={hTeal} opacity="0.18" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 90)" style={hLine} opacity="0.8" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 90)"   style={hGrey} opacity="0.55" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(233.4, 90)" style={hTeal} opacity="0.45" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(198.7, 90)" style={hGrey} opacity="0.3" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 120)"   style={hGrey} opacity="0.5" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(285.4, 120)" style={hGrey} opacity="0.4" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(250.7, 120)" style={hGrey} opacity="0.22" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(302.7, 150)" style={hGrey} opacity="0.3" />
      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(268, 150)"   style={hTeal} opacity="0.25" />

      <polygon points="0,-18 15.6,-9 15.6,9 0,18 -15.6,9 -15.6,-9" transform="translate(320, 180)"  style={hGrey} opacity="0.2" />
      <circle style={hTeal} cx="302.7" cy="30" r="3.2" />
    </>
  );

  return (
    <div className="letterhead-container">

      {/* ── TOP-RIGHT hex mesh – same rotation trick as bottom ── */}
      <div style={{
        position: 'fixed',
        top: 0,
        right: 0,
        width: '320px',
        height: '190px',
        zIndex: 5,
        pointerEvents: 'none',
        transform: 'rotate(180deg) scaleX(-1)',
      }}>
        <svg style={{ width: '100%', height: '100%', display: 'block' }} viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg">
          {hexMesh}
        </svg>
      </div>

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

      {/* ── BOTTOM-LEFT hex mesh ── */}
      <div style={{
        position: 'fixed',
        bottom: '90px',
        left: 0,
        width: '320px',
        height: '190px',
        zIndex: 5,
        pointerEvents: 'none',
        opacity: 0.15,
        transform: 'rotate(180deg)',
      }}>
        <svg style={{ width: '100%', height: '100%' }} viewBox="0 0 320 190" xmlns="http://www.w3.org/2000/svg">
          {hexMesh}
        </svg>
      </div>

      {/* Footer */}
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
