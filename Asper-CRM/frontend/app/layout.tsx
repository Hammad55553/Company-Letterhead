export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: 'sans-serif', background: '#f1f5f9' }}>
        <div style={{ display: 'flex', minHeight: '100vh' }}>
            <aside style={{ width: '250px', background: '#052950', color: 'white', padding: '20px' }}>
                <h2>Asper CRM</h2>
                <ul style={{ listStyle: 'none', padding: 0 }}>
                    <li style={{ padding: '10px 0' }}><a href="/" style={{ color: 'white', textDecoration: 'none' }}>Dashboard</a></li>
                    <li style={{ padding: '10px 0' }}><a href="/letters" style={{ color: 'white', textDecoration: 'none' }}>Letter Generator</a></li>
                    <li style={{ padding: '10px 0' }}><a href="/employees" style={{ color: 'white', textDecoration: 'none' }}>Employee Management</a></li>
                </ul>
            </aside>
            <main style={{ flex: 1, padding: '30px' }}>
                {children}
            </main>
        </div>
      </body>
    </html>
  )
}
