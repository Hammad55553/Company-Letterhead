# Company Letterhead

Professional corporate letterhead for **Asper InfoTech (Private) Limited** built with React + Vite.

## Features
- Hex mesh geometric shapes (top-right & bottom-left corners)
- Professional navy & teal color scheme
- Company stamp / signature block
- Multi-page print support with `@media print`
- A4 size optimized

## Stack
- React 18
- Vite
- CSS (no Tailwind)

## Run locally

```bash
cd react-preview
npm install
npm run dev
```

Open http://localhost:5173

## Usage

```jsx
import Letterhead from './components/Letterhead';

<Letterhead
  reference="AIT/2026/001"
  date="02 October 2026"
  recipient={<>Mr. John Doe</>}
  signatureName="Hammad Aslam"
  signatureRole="Founder & CEO"
>
  <p>Letter body goes here...</p>
</Letterhead>
```
