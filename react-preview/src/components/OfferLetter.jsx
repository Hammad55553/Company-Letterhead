import React from 'react';
import Letterhead from './Letterhead';

export default function OfferLetter({ candidateName, joiningDate, salary }) {
  const recipientNode = (
    <>
      Dear {candidateName || '[Candidate Name]'},<br />
      <span>Software Engineer<br />[Address]<br />[Email]<br />[Phone]</span>
    </>
  );

  return (
    <Letterhead 
      reference="AIT/OFFER/2026/004"
      recipient={recipientNode}
    >
      <p><strong>Subject: Offer of Employment</strong></p>
      <p>
        We are delighted to offer you the position of Software Engineer at Asper InfoTech (Private) Limited. 
        Your skills and experience make you an excellent fit for our team.
      </p>
      <p>
        Your expected joining date will be {joiningDate || '[Joining Date]'}. Your starting salary will be 
        {salary || '[Salary]'} per annum, subject to applicable taxes. You will be on a probation period of three (3) months.
      </p>
      <p>
        Please sign and return a copy of this letter to indicate your acceptance of this offer.
      </p>
    </Letterhead>
  );
}
