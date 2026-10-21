import json

with open('/Users/pavankumars/.gemini/antigravity/scratch/all-projects-portfolio/PROJECTS.json') as f:
    projects = json.load(f)

projects_json_str = json.dumps(projects, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no" />
  
  <title>Master Portfolio (53 Projects) | HRL International Private Limited</title>
  <meta name="title" content="Master Portfolio (53 Projects) | HRL International Private Limited" />
  <meta name="description" content="The complete engineering portfolio of 53 sovereign software systems, GPU runtimes, open-source repositories, and brand identity architectures created by Pavan Kumar Sadashiv (hrlpavan) for HRL International Private Limited." />
  <meta name="author" content="Pavan Kumar Sadashiv (hrlpavan)" />
  <link rel="canonical" href="https://hrlpavan.github.io/all-projects-portfolio/" />
  <meta name="theme-color" content="#F5F5F7" />

  <link rel="icon" type="image/png" href="https://hrlpavan.github.io/hrl-international-website-/assets/favicon.png" />
  <link rel="stylesheet" href="https://fonts.cdnfonts.com/css/sf-pro-display" />

  <style>
    :root {{
      --bg-page: #F5F5F7;
      --surface-card: #FFFFFF;
      --surface-elevated: #FFFFFF;
      --border-subtle: rgba(0, 0, 0, 0.08);
      --border-hover: rgba(0, 0, 0, 0.16);
      --text-dark: #1D1D1F;
      --text-body: #515154;
      --text-muted: #86868B;
      --hrl-crimson: #D1002D;
      --hrl-crimson-dark: #A50024;
      --hrl-crimson-tint: rgba(209, 0, 45, 0.08);
      --hrl-crimson-glow: rgba(209, 0, 45, 0.25);
      --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --radius-pill: 9999px;
      --radius-card: 16px;
      --transition-smooth: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-page);
      color: var(--text-dark);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
    }}

    .apple-ribbon {{
      background: #FFFFFF;
      color: var(--text-muted);
      font-size: 13px;
      text-align: center;
      padding: 8px 16px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .apple-ribbon a {{
      color: var(--hrl-crimson);
      text-decoration: none;
      font-weight: 600;
      margin-left: 6px;
    }}

    .apple-nav {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .nav-container {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 24px;
      height: 54px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-dark);
      font-weight: 700;
      font-size: 15px;
    }}
    .nav-brand img {{
      height: 20px;
      width: auto;
      object-fit: contain;
      vertical-align: middle;
      box-shadow: none !important;
      border: none !important;
    }}
    .nav-links {{
      display: flex;
      align-items: center;
      gap: 20px;
      list-style: none;
    }}
    .nav-links a {{
      text-decoration: none;
      color: var(--text-body);
      font-size: 13.5px;
      font-weight: 500;
      transition: var(--transition-smooth);
    }}
    .nav-links a:hover, .nav-links a.active {{
      color: var(--hrl-crimson);
      font-weight: 600;
    }}
    .nav-cta {{
      background: var(--hrl-crimson);
      color: #FFFFFF !important;
      font-size: 12.5px;
      font-weight: 600;
      padding: 7px 18px;
      border-radius: var(--radius-pill);
      text-decoration: none;
    }}

    main {{
      flex: 1;
      max-width: 1240px;
      margin: 0 auto;
      padding: 44px 24px 80px;
      width: 100%;
    }}

    .hero-header {{
      text-align: center;
      max-width: 880px;
      margin: 0 auto 36px;
    }}
    /* Apple-Caliber Executive Company Motto Badge */
    .company-motto-badge {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: #FFFFFF;
      border: 1px solid rgba(0, 0, 0, 0.08);
      padding: 5px 18px 5px 6px;
      border-radius: var(--radius-pill);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
      transition: var(--transition-smooth);
      margin-bottom: 24px;
      vertical-align: middle;
    }}
    .company-motto-badge:hover {{
      border-color: rgba(0, 0, 0, 0.14);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
      transform: translateY(-1px);
    }}
    .motto-tag {{
      background: linear-gradient(135deg, #D1002D 0%, #B80026 100%);
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 11px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      box-shadow: 0 1px 3px rgba(209, 0, 45, 0.28);
      flex-shrink: 0;
    }}
    .motto-text {{
      color: #1D1D1F;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: -0.012em;
      line-height: 1;
      display: inline-flex;
      align-items: center;
    }}
    h1 {{
      font-size: clamp(32px, 5vw, 48px);
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      color: var(--text-dark);
      margin-bottom: 12px;
    }}
    p.lead-desc {{
      font-size: 16.5px;
      color: var(--text-body);
      line-height: 1.55;
    }}

    .search-filter-bar {{
      margin: 32px 0 28px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .search-input-wrapper {{
      position: relative;
      max-width: 640px;
      margin: 0 auto;
      width: 100%;
    }}
    .search-input {{
      width: 100%;
      padding: 14px 20px 14px 46px;
      font-size: 15px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
      background: #FFFFFF;
      outline: none;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
      font-family: inherit;
      transition: var(--transition-smooth);
    }}
    .search-input:focus {{
      border-color: var(--hrl-crimson);
      box-shadow: 0 6px 24px rgba(209, 0, 45, 0.12);
    }}
    .search-icon {{
      position: absolute;
      left: 18px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}

    .stats-bar {{
      display: flex;
      justify-content: center;
      gap: 18px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}
    .stat-chip {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-muted);
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      padding: 5px 14px;
      border-radius: var(--radius-pill);
    }}
    .stat-chip strong {{
      color: var(--hrl-crimson);
    }}

    .projects-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    @media (min-width: 680px) {{
      .projects-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (min-width: 1040px) {{
      .projects-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}

    .project-card {{
      background: var(--surface-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: var(--transition-smooth);
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .project-card:hover {{
      transform: translateY(-2px);
      border-color: var(--border-hover);
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }}
    .project-card-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .project-id-badge {{
      font-size: 11px;
      font-weight: 700;
      color: var(--hrl-crimson);
      background: var(--hrl-crimson-tint);
      border: 1px solid rgba(209, 0, 45, 0.2);
      padding: 2px 8px;
      border-radius: var(--radius-pill);
    }}
    .project-category {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }}
    .project-title {{
      font-size: 17px;
      font-weight: 700;
      color: var(--text-dark);
      letter-spacing: -0.015em;
      margin-bottom: 8px;
      line-height: 1.3;
    }}
    .project-desc {{
      font-size: 13.5px;
      color: var(--text-body);
      line-height: 1.5;
      margin-bottom: 16px;
      flex: 1;
    }}
    .tech-badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }}
    .tech-tag {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-body);
      background: var(--bg-page);
      border: 1px solid var(--border-subtle);
      padding: 2.5px 8px;
      border-radius: 6px;
    }}
    .project-links {{
      display: flex;
      gap: 10px;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
    }}
    .btn-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      padding: 6px 12px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
      color: var(--text-dark);
      transition: var(--transition-smooth);
    }}
    .btn-link:hover {{
      background: var(--bg-page);
      border-color: var(--border-hover);
    }}
    .btn-link-primary {{
      background: var(--hrl-crimson);
      color: #FFFFFF !important;
      border-color: transparent;
    }}
    .btn-link-primary:hover {{
      background: var(--hrl-crimson-dark);
    }}
    @media (max-width: 640px) {{
      .company-motto-badge {{
        padding: 6px 14px 6px 6px;
        gap: 8px;
        max-width: 100%;
        text-align: left;
      }}
    }}

    .apple-footer {{
      background: #FFFFFF;
      border-top: 1px solid var(--border-subtle);
      padding: 36px 24px;
      color: var(--text-muted);
      font-size: 12.5px;
      text-align: center;
    }}
    .apple-footer a {{
      color: var(--text-body);
      text-decoration: none;
    }}
    .apple-footer a:hover {{
      color: var(--hrl-crimson);
    }}
  </style>
</head>
<body>

  <div class="apple-ribbon">
    Master Software Architecture &amp; Project Catalog &bull; HRL International Private Limited
    <a href="https://hrlpavan.github.io/hrl-international-website-/">Corporate Portal &rarr;</a>
  </div>

  <nav class="apple-nav">
    <div class="nav-container">
      <a href="https://hrlpavan.github.io/hrl-international-website-/" class="nav-brand">
        <img src="https://hrlpavan.github.io/hrl-international-website-/assets/HRL%20INTERNATIONAL%20PRIVATE%20LIMITED%20CORE%20COUNTRY%20FLAG.png" alt="HRL Flag" />
        <span>HRL International</span>
      </a>
      <ul class="nav-links">
        <li><a href="https://hrlpavan.github.io/hrl-international-website-/">Overview</a></li>
        <li><a href="https://hrlpavan.github.io/hrl-international-website-/hrlpavan.html">Founder Entity</a></li>
        <li><a href="https://hrlpavan.github.io/hrl-international-website-/flag.html">Official Flag</a></li>
        <li><a href="index.html" class="active">Portfolio (53 Projects)</a></li>
        <li><a href="https://github.com/hrlpavan/all-projects-portfolio" target="_blank" rel="noopener noreferrer">GitHub Repo</a></li>
      </ul>
      <a href="https://hrlpavan.github.io/hrl-international-website-/flag.html" class="nav-cta">
        <span>Official Sovereign Flag</span>
      </a>
    </div>
  </nav>

  <main>
    <header class="hero-header">
      <div class="company-motto-badge">
        <span class="motto-tag">Company Motto</span>
        <span class="motto-text">We Can Do Everything Related To Software Sector Without Any Excuses!</span>
      </div>
      <h1>Master Project Portfolio</h1>
      <p class="lead-desc">
        Comprehensive catalog of all <strong>53 sovereign engineering projects</strong>, CUDA GPU runtimes, open-source repositories, and brand architectures authored by <strong>Pavan Kumar Sadashiv</strong> (<code>hrlpavan</code>) for <strong>HRL International Private Limited</strong>.
      </p>
    </header>

    <div class="search-filter-bar">
      <div class="search-input-wrapper">
        <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchInput" class="search-input" placeholder="Search projects by name, technology, or category (e.g., CUDA, Python, Flag, C++)..." oninput="filterProjects()" />
      </div>
      <div class="stats-bar">
        <div class="stat-chip">Total Systems: <strong>53</strong></div>
        <div class="stat-chip">Dual Synced: <strong>GitHub &bull; GitLab</strong></div>
        <div class="stat-chip">Showing: <strong id="showingCount">53</strong></div>
      </div>
    </div>

    <div class="projects-grid" id="projectsGrid"></div>
  </main>

  <footer class="apple-footer">
    <p>Copyright &copy; 2026 Pavan Kumar Sadashiv. HRL International&trade; is an asserted and registered trademark. All rights reserved.</p>
    <div style="margin-top: 10px;">
      <a href="https://hrlpavan.github.io/hrl-international-website-/">Corporate Portal</a> &bull; 
      <a href="https://hrlpavan.github.io/hrl-international-website-/hrlpavan.html">Founder Entity</a> &bull; 
      <a href="https://hrlpavan.github.io/hrl-international-website-/flag.html">Official Sovereign Flag</a> &bull; 
      <a href="https://github.com/hrlpavan/all-projects-portfolio">GitHub Master Repository</a>
    </div>
  </footer>

  <script>
    const allProjects = {projects_json_str};

    function renderProjects(projects) {{
      const grid = document.getElementById('projectsGrid');
      const countEl = document.getElementById('showingCount');
      countEl.innerText = projects.length;

      if (projects.length === 0) {{
        grid.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; padding: 48px; color: var(--text-muted);">No matching projects found. Try a different search term.</div>';
        return;
      }}

      grid.innerHTML = projects.map(p => {{
        const isFlag = p.id === 53;
        const liveLink = isFlag ? 'https://hrlpavan.github.io/hrl-international-website-/flag.html' : null;
        return `
          <div class="project-card" style="${{isFlag ? 'border-color: rgba(209, 0, 45, 0.35); box-shadow: 0 4px 20px rgba(209, 0, 45, 0.08);' : ''}}">
            <div>
              <div class="project-card-header">
                <span class="project-category">${{p.category || 'Engineering'}}</span>
                <span class="project-id-badge">#${{p.id}}</span>
              </div>
              <h3 class="project-title">${{p.title || p.name}}</h3>
              <p class="project-desc">${{p.desc || p.summary || ''}}</p>
              <div class="tech-badges">
                ${{(p.tech_stack || []).slice(0, 4).map(t => `<span class="tech-tag">${{t}}</span>`).join('')}}
              </div>
            </div>
            <div class="project-links">
              ${{liveLink ? `<a href="${{liveLink}}" class="btn-link btn-link-primary">View Flag</a>` : ''}}
              ${{p.html_url ? `<a href="${{p.html_url}}" target="_blank" rel="noopener noreferrer" class="btn-link ${{!liveLink ? 'btn-link-primary' : ''}}">GitHub</a>` : ''}}
              ${{p.gitlab_url ? `<a href="${{p.gitlab_url}}" target="_blank" rel="noopener noreferrer" class="btn-link">GitLab</a>` : ''}}
            </div>
          </div>
        `;
      }}).join('');
    }}

    function filterProjects() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      if (!query) {{
        renderProjects(allProjects);
        return;
      }}
      const filtered = allProjects.filter(p => {{
        const title = (p.title || '').toLowerCase();
        const name = (p.name || '').toLowerCase();
        const desc = (p.desc || '').toLowerCase();
        const category = (p.category || '').toLowerCase();
        const tech = (p.tech_stack || []).join(' ').toLowerCase();
        return title.includes(query) || name.includes(query) || desc.includes(query) || category.includes(query) || tech.includes(query);
      }});
      renderProjects(filtered);
    }}

    renderProjects(allProjects);
  </script>
</body>
</html>'''

with open('/Users/pavankumars/.gemini/antigravity/scratch/all-projects-portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated index.html for all-projects-portfolio')
