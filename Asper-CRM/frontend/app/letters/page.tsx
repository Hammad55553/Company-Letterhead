'use client'

export default function LettersPage() {
  const templates = [
    { name: 'Blank Letterhead', file: '1_blank_letterhead.html' },
    { name: 'Job Offer', file: '4_job_offer_letter.html' },
    { name: 'Contract Agreement', file: '6_contract_agreement.html' },
    { name: 'Partnership MoU', file: '7_partnership_deal.html' },
    { name: 'Warning Letter', file: '10_warning_letter.html' },
    { name: 'Resignation Acceptance', file: '9_resignation_acceptance.html' },
    { name: 'Experience Certificate', file: '11_experience_certificate.html' },
    { name: 'CEO Affiliation', file: '2_affiliation_hammad_aslam.html' },
    { name: 'Director Affiliation', file: '3_affiliation_sannia_aslam.html' }
  ];

  return (
    <div>
      <h1 style={{ color: '#052950' }}>Letterhead Generator System</h1>
      <p>Select a letter template below to instantly open the official Asper InfoTech document.</p>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginTop: '20px' }}>
          {templates.map(tpl => (
              <div key={tpl.name} style={{ background: 'white', padding: '20px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}>
                  <h3 style={{ marginBottom: '15px' }}>{tpl.name}</h3>
                  <button 
                      onClick={() => window.open(`/templates/${tpl.file}`, '_blank')}
                      style={{ background: '#11b6aa', color: 'white', border: 'none', padding: '8px 15px', borderRadius: '4px', cursor: 'pointer', width: '100%' }}
                  >
                      Generate & Print
                  </button>
              </div>
          ))}
      </div>
    </div>
  )
}
