"""
Renders a 1024x1024 editorial "World News Brief" infographic to entry.png
using Playwright + system Chrome (headless), driven by a self-contained
HTML/CSS/SVG document.
"""
import os
from playwright.sync_api import sync_playwright

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
CHROME_PATH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @font-face { font-family: 'SysSans'; src: local('Arial'); }
  :root{
    --ink:#0f172a;
    --paper:#f8f6f0;
    --rule:#0f172a;
    --accent:#b4231f;
    --gold:#c9a24b;
    --sub:#44403c;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html,body{
    width:1024px; height:1024px; overflow:hidden;
    font-family:'Georgia','Times New Roman',serif;
    background:var(--paper);
    -webkit-font-smoothing:antialiased;
  }
  .stage{ width:1024px; height:1024px; position:relative; background:var(--paper); }

  /* ===== HEADER ===== */
  .header{
    width:1024px; height:132px; background:var(--ink);
    position:relative; color:#f8f6f0;
    display:flex; flex-direction:column; justify-content:center;
    padding:16px 34px 14px 34px;
    border-bottom:6px solid var(--gold);
    overflow:hidden;
  }
  .kicker{
    font-family:'Arial Narrow','Arial',sans-serif; font-size:13px; letter-spacing:3px;
    color:var(--gold); font-weight:700; text-transform:uppercase;
    display:flex; justify-content:space-between; align-items:center;
    white-space:nowrap;
  }
  .masthead{
    font-family:'Georgia',serif; font-weight:900; font-size:40px; line-height:1.05;
    letter-spacing:0.2px; margin-top:4px; color:#f8f6f0;
    text-transform:uppercase; white-space:nowrap;
  }
  .masthead .accent{ color:var(--gold); }
  .subline{
    font-family:'Arial Narrow','Arial',sans-serif; font-size:15px; letter-spacing:2px;
    color:#cbd5e1; margin-top:4px; text-transform:uppercase; font-weight:600;
  }

  /* ===== GRID ===== */
  .grid{
    width:1024px; height:800px;
    display:grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 258px 258px 258px;
    gap:12px;
    padding:12px;
  }
  .grid .wide{ grid-column: 1 / span 2; }

  .card{
    background:#fffdf8;
    border:1px solid #d9d2c3;
    box-shadow: 0 2px 0 rgba(15,23,42,0.06);
    position:relative;
    display:flex;
    padding:14px 16px 12px 16px;
    overflow:hidden;
  }
  .card::before{
    content:"";
    position:absolute; left:0; top:0; bottom:0; width:6px;
    background:var(--accent);
  }
  .card.gold::before{ background:var(--gold); }

  .art{
    width:118px; min-width:118px; height:100%;
    display:flex; align-items:center; justify-content:center;
    margin-right:12px;
  }
  .art svg{ width:112px; height:112px; }

  .body{
    display:flex; flex-direction:column; justify-content:center;
    flex:1; min-width:0; overflow:hidden;
  }
  .tag{
    font-family:'Arial Narrow','Arial',sans-serif; font-size:11.5px; font-weight:800;
    letter-spacing:1.3px; color:var(--accent); text-transform:uppercase; margin-bottom:6px;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  }
  .card.gold .tag{ color:#9a7620; }
  .headline{
    font-family:'Georgia',serif; font-weight:800; font-size:19px; line-height:1.2;
    color:var(--ink); margin-bottom:7px; letter-spacing:-0.1px;
    display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;
    overflow:hidden;
  }
  .dek{
    font-family:'Arial','Helvetica',sans-serif; font-size:12.5px; line-height:1.36;
    color:var(--sub); font-weight:400;
    display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical;
    overflow:hidden;
  }
  .wide .headline{ font-size:22px; -webkit-line-clamp:2; }
  .wide .art{ width:150px; min-width:150px; }
  .wide .art svg{ width:142px; height:142px; }
  .wide .dek{ font-size:13.5px; max-width:660px; -webkit-line-clamp:2; }

  /* ===== FOOTER ===== */
  .footer{
    width:1024px; height:92px; background:var(--ink);
    display:flex; align-items:center; justify-content:space-between;
    padding:0 34px; border-top:4px solid var(--gold);
  }
  .footer .brand{
    font-family:'Arial Narrow','Arial',sans-serif; color:#f8f6f0; font-size:16px;
    font-weight:800; letter-spacing:3px; text-transform:uppercase;
  }
  .footer .brand span{ color:var(--gold); }
  .footer .strip{
    display:flex; gap:10px;
  }
  .dot{ width:10px; height:10px; border-radius:50%; background:var(--gold); }
  .footer .ed{
    font-family:'Arial Narrow','Arial',sans-serif; color:#cbd5e1; font-size:12.5px;
    letter-spacing:1.5px; text-transform:uppercase; font-weight:600;
  }
</style>
</head>
<body>
<div class="stage">

  <div class="header">
    <div class="kicker"><span>GLOBAL EDITION &middot; NO. 046</span><span>FIVE STORIES &middot; 24H DESK</span></div>
    <div class="masthead">SATURDAY 21 NOVEMBER 2026</div>
    <div class="subline">WORLD NEWS BRIEF <span class="accent">&middot;</span> DIPLOMACY &nbsp;/&nbsp; CONFLICT &nbsp;/&nbsp; LAW</div>
  </div>

  <div class="grid">

    <!-- 1: ICJ Myanmar -->
    <div class="card">
      <div class="art">
        <svg viewBox="0 0 140 140">
          <circle cx="70" cy="70" r="62" fill="#fdf1ee"/>
          <rect x="34" y="94" width="72" height="8" fill="#0f172a"/>
          <rect x="40" y="58" width="6" height="36" fill="#0f172a"/>
          <rect x="98" y="58" width="6" height="36" fill="#0f172a"/>
          <rect x="66" y="40" width="8" height="54" fill="#0f172a"/>
          <polygon points="70,20 100,52 40,52" fill="#0f172a"/>
          <rect x="24" y="60" width="26" height="4" fill="#0f172a"/>
          <polygon points="27,64 37,64 32,80" fill="none" stroke="#0f172a" stroke-width="4" stroke-linejoin="round"/>
          <rect x="90" y="60" width="26" height="4" fill="#0f172a"/>
          <polygon points="93,64 103,64 98,80" fill="none" stroke="#0f172a" stroke-width="4" stroke-linejoin="round"/>
          <circle cx="70" cy="46" r="4" fill="#b4231f"/>
        </svg>
      </div>
      <div class="body">
        <div class="tag">The Hague &middot; Justice</div>
        <div class="headline">ICJ RULES MYANMAR COMMITTED GENOCIDE</div>
        <div class="dek">ICJ finds Myanmar responsible for genocide against the Rohingya in a historic 9&ndash;6 ruling; UK responds by expelling Myanmar's defense attach&eacute;.</div>
      </div>
    </div>

    <!-- 2: Shenzhen summit -->
    <div class="card gold">
      <div class="art">
        <svg viewBox="0 0 140 140">
          <circle cx="70" cy="70" r="62" fill="#fbf4e3"/>
          <rect x="30" y="92" width="80" height="10" fill="#0f172a"/>
          <circle cx="48" cy="70" r="16" fill="none" stroke="#0f172a" stroke-width="5"/>
          <circle cx="92" cy="70" r="16" fill="none" stroke="#0f172a" stroke-width="5"/>
          <circle cx="70" cy="46" r="16" fill="none" stroke="#b4231f" stroke-width="5"/>
          <line x1="58" y1="60" x2="62" y2="56" stroke="#0f172a" stroke-width="4"/>
          <line x1="82" y1="60" x2="78" y2="56" stroke="#0f172a" stroke-width="4"/>
          <rect x="60" y="86" width="20" height="6" fill="#0f172a"/>
        </svg>
      </div>
      <div class="body">
        <div class="tag">Shenzhen &middot; Diplomacy</div>
        <div class="headline">TRUMP, XI, PUTIN HOLD 3-WAY TALKS</div>
        <div class="dek">Closed-door trilateral summit ends with a 4-point peace declaration &mdash; scrutinized for omitting any mention of Ukraine.</div>
      </div>
    </div>

    <!-- 3: Hormuz / Yemen -->
    <div class="card">
      <div class="art">
        <svg viewBox="0 0 140 140">
          <circle cx="70" cy="70" r="62" fill="#fdf1ee"/>
          <rect x="18" y="86" width="104" height="10" fill="#2b4a63"/>
          <path d="M40 86 L48 66 L90 66 L98 86 Z" fill="#0f172a"/>
          <rect x="60" y="50" width="8" height="18" fill="#0f172a"/>
          <path d="M60 78 Q70 68 80 78" stroke="#b4231f" stroke-width="4" fill="none"/>
          <path d="M76 56 Q84 44 94 52 Q90 40 100 36 Q94 48 102 52 Q88 54 76 56Z" fill="#b4231f"/>
          <path d="M34 76 Q38 68 46 76 Q42 66 50 62" stroke="#b4231f" stroke-width="3" fill="none"/>
        </svg>
      </div>
      <div class="body">
        <div class="tag">Strait of Hormuz &middot; Security</div>
        <div class="headline">TANKER FIRE OFF OMAN, STRIKES HIT YEMEN</div>
        <div class="dek">An oil tanker catches fire near Khasab amid Hormuz tensions, while a Saudi-led coalition strikes Houthi supply routes in Yemen.</div>
      </div>
    </div>

    <!-- 5: Arch ruling -->
    <div class="card">
      <div class="art">
        <svg viewBox="0 0 140 140">
          <circle cx="70" cy="70" r="62" fill="#fdf1ee"/>
          <path d="M34 104 L34 70 A36 36 0 0 1 106 70 L106 104" fill="none" stroke="#0f172a" stroke-width="9"/>
          <rect x="22" y="100" width="24" height="8" fill="#0f172a"/>
          <rect x="94" y="100" width="24" height="8" fill="#0f172a"/>
          <g transform="translate(70,100)">
            <circle r="15" fill="#fff" stroke="#b4231f" stroke-width="4"/>
            <line x1="-8" y1="0" x2="8" y2="0" stroke="#b4231f" stroke-width="4"/>
            <line x1="0" y1="-8" x2="0" y2="8" stroke="#b4231f" stroke-width="4" transform="rotate(45)"/>
          </g>
        </svg>
      </div>
      <div class="body">
        <div class="tag">Alexandria, VA &middot; Courts</div>
        <div class="headline">JUDGE MOVES TO BLOCK TRIUMPHAL ARCH</div>
        <div class="dek">Federal judge Leonie Brinkema signals she will halt the planned triumphal arch indefinitely following an Arlington lawsuit.</div>
      </div>
    </div>

    <!-- 4: UK-EU reset / Poland (wide banner, full width) -->
    <div class="card wide gold">
      <div class="art">
        <svg viewBox="0 0 160 160">
          <circle cx="80" cy="80" r="70" fill="#fbf4e3"/>
          <circle cx="56" cy="80" r="28" fill="none" stroke="#0f172a" stroke-width="5"/>
          <circle cx="104" cy="80" r="28" fill="none" stroke="#c9a24b" stroke-width="5"/>
          <path d="M56 56 A28 28 0 0 1 56 104" fill="none" stroke="#b4231f" stroke-width="4"/>
          <g transform="translate(96,40) rotate(25)">
            <polygon points="0,0 36,6 0,12" fill="#b4231f"/>
            <rect x="-4" y="4" width="8" height="4" fill="#0f172a"/>
          </g>
          <polygon points="120,30 126,42 138,30 126,30" fill="#0f172a"/>
        </svg>
      </div>
      <div class="body">
        <div class="tag">London / Brussels &amp; Lublin &middot; Policy &amp; Alert</div>
        <div class="headline">UK-EU DRAFT YOUTH RESET AS RUSSIAN MISSILE HITS POLAND</div>
        <div class="dek">Burnham and EU leaders sketch a 100,000-place youth mobility reset, as a Russian Kh-101 cruise missile strikes a field near Lublin, triggering air-defense alerts across Poland.</div>
      </div>
    </div>

  </div>

  <div class="footer">
    <div class="brand">WORLD NEWS <span>BRIEF</span></div>
    <div class="strip"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
    <div class="ed">Five Verified Stories &middot; 20&ndash;21 Nov 2026</div>
  </div>

</div>
</body>
</html>
"""

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        page = browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
        page.set_content(HTML, wait_until="networkidle")
        page.wait_for_timeout(150)
        page.screenshot(path=OUT_PATH, type="png", clip={"x": 0, "y": 0, "width": 1024, "height": 1024})
        browser.close()

    size = os.path.getsize(OUT_PATH)
    print(f"Saved {OUT_PATH} ({size} bytes)")

if __name__ == "__main__":
    main()
