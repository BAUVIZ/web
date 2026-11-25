#!/usr/bin/env python3
"""Four structurally-identical, visually-distinct BAUVIZ page designs.
Same real content, four different compositions."""
import build as B

LOGO = B.LOGO
def logo(h="64px"):
    return f'<img class="logo" src="{LOGO}" alt="BAUVIZ logo" style="height:{h}">'

NAV = B.nav_items()
TOPICS = B.topics_html()
DATES = B.dates_html()
ORG = B.org_html()
STEER = B.steering_html()
STYPES = B.submit_types_html()
AUD = B.audience_html()
PROG = B.program_html()

# =========================================================================
# A — "Blueprint": conservative, light, closest to the ETVIS reference.
# =========================================================================
A_CSS = r"""
:root{--teal:#1f6d7e;--teal2:#2d889d;--ink:#33383c;--mut:#6b7377;--line:#dfe4e6;--bg:#ffffff;--soft:#f6f8f9}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:"Helvetica Neue",Arial,sans-serif;color:var(--ink);line-height:1.6;background:var(--bg)}
a{color:var(--teal);text-decoration:none} a:hover{text-decoration:underline}
nav.top{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line);
  display:flex;align-items:center;gap:24px;padding:0 32px;height:60px}
nav.top .brand{display:flex;align-items:center;gap:12px;font-weight:700;letter-spacing:.5px;color:var(--ink)}
nav.top .brand img{height:34px}
nav.top ul{display:flex;gap:22px;list-style:none;margin:0 auto;padding:0}
nav.top li a{color:var(--ink);font-size:14px} nav.top li a:hover{color:var(--teal);text-decoration:none}
.hero{text-align:center;padding:80px 24px 64px;border-bottom:1px solid var(--line)}
.hero .logo{height:120px}
.hero h1{font-size:52px;margin:18px 0 6px;letter-spacing:2px;color:var(--ink);font-weight:800}
.hero h1 span{color:var(--teal)}
.hero .sub{font-size:19px;color:var(--mut);letter-spacing:.5px;margin:0 0 14px}
.hero .meta{font-size:15px;color:var(--teal);font-weight:600}
main{max-width:980px;margin:0 auto;padding:0 24px}
section{padding:56px 0;border-bottom:1px solid var(--line)}
section:last-of-type{border-bottom:none}
h2{font-size:26px;margin:0 0 8px;color:var(--ink);text-transform:uppercase;letter-spacing:1px}
h2 .n{color:var(--teal);font-weight:400;margin-right:10px}
.lead{font-size:16.5px;color:#3d4448;max-width:820px}
h3{font-size:15px;text-transform:uppercase;letter-spacing:1.5px;color:var(--mut);margin:34px 0 14px}
.pg{display:flex;flex-direction:column}
.pg-row{display:grid;grid-template-columns:170px 1fr;gap:20px;padding:12px 0;border-bottom:1px dashed var(--line)}
.pg-row:last-child{border-bottom:none}
.pg-t{font-variant-numeric:tabular-nums;color:var(--teal);font-weight:600}
.note{font-size:13px;color:var(--mut);font-style:italic;margin-top:14px}
.tba{font-weight:700;font-size:22px;letter-spacing:6px;color:var(--teal);margin:6px 0 0}
.topics{display:grid;grid-template-columns:1fr 1fr;gap:26px 40px}
.topic .topic-h{font-weight:700;color:var(--teal);margin-bottom:6px;font-size:15px}
.topic ul{margin:0;padding-left:18px} .topic li{margin:3px 0;font-size:14.5px;color:#464d51}
.types{display:grid;grid-template-columns:1fr 1fr;gap:14px 32px}
.stype{padding:14px 16px;background:var(--soft);border-left:3px solid var(--teal2)}
.s-name{font-weight:700;margin-bottom:4px} .s-desc{font-size:14px;color:var(--mut)}
.dates .dt-row{display:grid;grid-template-columns:1fr 1fr;gap:10px 24px;padding:12px 0;border-bottom:1px solid var(--line)}
.dt-k{font-weight:600} .dt-v{color:var(--teal);font-weight:600;text-align:right}
.dates-tz{font-size:13px;color:var(--mut);margin-top:10px;font-style:italic}
.people{display:flex;flex-direction:column;gap:14px}
.person{display:flex;flex-direction:column}
.p-name{font-weight:700;font-size:16px} .p-aff{font-size:15px;color:var(--mut)}
.steering .people{display:grid;grid-template-columns:1fr 1fr;gap:14px 32px}
.aud{columns:2;column-gap:40px;padding-left:18px;margin:0} .aud li{margin:4px 0;font-size:14.5px;break-inside:avoid}
.contact p{font-size:16px;margin:0} .contact a{font-weight:600}
.support{background:var(--soft);border:none;padding:48px 24px}
.support .wrap{max-width:980px;margin:0 auto}
footer{background:#223033;color:#cfd8da;text-align:center;padding:26px 16px;font-size:13px}
footer a{color:#fff}
@media(max-width:720px){.hero h1{font-size:38px}nav.top ul{display:none}.topics,.types,.aud,.steering .people{grid-template-columns:1fr;columns:1}.pg-row{grid-template-columns:1fr;gap:4px}}
"""

A_BODY = f"""
<nav class="top"><div class="brand">{logo('34px')} BAUVIZ</div><ul>{NAV}</ul></nav>
<header class="hero">{logo('120px')}
  <h1>BAU<span>VIZ</span> 2027</h1>
  <p class="sub">{B.SUBTITLE}</p>
  <p class="meta">{B.META}</p></header>
<main>
 <section id="about"><h2>About</h2><p class="lead">{B.ABOUT}</p></section>
 <section id="program"><h2>Program</h2><div class="pg">{PROG}</div><p class="note">{B.PROGRAM_NOTE}</p></section>
 <section id="format"><h2>Format &amp; Audience</h2><p class="lead">{B.FORMAT}</p>
   <h3>Target audience</h3><ul class="aud">{AUD}</ul></section>
 <section id="topics"><h2>Topics</h2><div class="topics">{TOPICS}</div></section>
 <section id="submit"><h2>Submission</h2><div class="types">{STYPES}</div>
   <h3>Process &amp; policies</h3><p class="lead">{B.SUBMIT_PROC}</p></section>
 <section id="dates" class="dates"><h2>Important Dates</h2>{DATES}
   <p class="dates-tz">{B.DATES_TZ}</p></section>
 <section id="org"><h2>Organizers</h2><div class="people">{ORG}</div>
   <h3>Steering committee</h3><div class="steering"><div class="people">{STEER}</div></div>
   <h3>Program committee</h3><p class="lead">{B.PC_NOTE}</p></section>
 <section id="contact" class="contact"><h2>Contact</h2><p>{B.CONTACT}</p></section>
</main>
<footer>{B.FOOT}</footer>
"""

# =========================================================================
# B — "Dark Twin": dark, tech, wireframe/neon, left-aligned, timeline.
# =========================================================================
B_CSS = r"""
:root{--bg:#0a1416;--bg2:#0e1c1f;--panel:#122428;--teal:#2d889d;--teal2:#46b6c9;--line:#1d3a40;--ink:#e8f1f2;--mut:#8fa6ab}
*{box-sizing:border-box} html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.65;
  font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
  background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:46px 46px;opacity:.16}
a{color:var(--teal2);text-decoration:none} a:hover{text-decoration:underline}
.mono{font-family:"DejaVu Sans Mono","SFMono-Regular",Consolas,monospace}
nav.top{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:20px;
  padding:0 34px;height:64px;background:rgba(10,20,22,.92);backdrop-filter:blur(6px);
  border-bottom:1px solid var(--line)}
nav.top .brand{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:2px}
nav.top .brand img{height:30px;filter:brightness(1.5)}
nav.top .brand b{color:var(--teal2)}
nav.top ul{display:flex;gap:20px;list-style:none;margin:0 auto;padding:0}
nav.top li a{color:var(--mut);font-size:13px;letter-spacing:1px;text-transform:uppercase}
nav.top li a:hover{color:var(--teal2);text-decoration:none}
.wrap{position:relative;z-index:1}
.hero{padding:96px 34px 72px;max-width:1180px;margin:0 auto;display:grid;
  grid-template-columns:auto 1fr;gap:48px;align-items:center}
.hero .logo{height:150px;filter:brightness(1.35) drop-shadow(0 0 24px rgba(70,182,201,.25))}
.hero .tag{color:var(--teal2);font-size:13px;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px}
.hero h1{font-size:60px;line-height:1.02;margin:0 0 10px;font-weight:800;letter-spacing:-1px}
.hero h1 b{color:var(--teal2)}
.hero .sub{font-size:18px;color:var(--ink);margin:0 0 16px;max-width:560px}
.hero .meta{color:var(--mut);font-size:15px}
.hero .meta span{color:var(--teal2)}
.hero::after{content:"";grid-column:1/3;border-bottom:1px solid var(--line);margin-top:18px}
main{max-width:1180px;margin:0 auto;padding:0 34px}
section{padding:54px 0;border-top:1px solid var(--line)}
h2{margin:0 0 22px;font-size:22px;letter-spacing:2px;text-transform:uppercase;display:flex;align-items:baseline;gap:14px}
h2 .idx{color:var(--teal2);font-size:14px;letter-spacing:1px}
.lead{font-size:16px;color:#c7d6d8;max-width:780px}
h3{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--teal);margin:30px 0 14px}
.tl{border-left:2px solid var(--line);margin-left:8px;padding-left:26px;display:flex;flex-direction:column;gap:16px}
.pg-row{position:relative}
.pg-row::before{content:"";position:absolute;left:-33px;top:6px;width:12px;height:12px;border-radius:50%;
  background:var(--bg);border:2px solid var(--teal2)}
.pg-t{color:var(--teal2);font-weight:700;font-size:14px;letter-spacing:.5px}
.pg-d{color:#cddcde;font-size:15px}
.note{color:var(--mut);font-size:13px;font-style:italic;margin-top:16px}
.tba{font-weight:800;font-size:22px;letter-spacing:6px;color:var(--teal2);margin:6px 0 0}
.aud{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:10px 28px}
.aud li{padding:10px 14px;background:var(--panel);border:1px solid var(--line);border-radius:4px;font-size:14.5px}
.aud li::before{content:"\25B8 ";color:var(--teal2)}
.topics{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.topic{background:var(--panel);border:1px solid var(--line);border-top:2px solid var(--teal);border-radius:4px;padding:16px}
.topic-h{font-weight:700;color:var(--teal2);font-size:14px;margin-bottom:10px;letter-spacing:.3px}
.topic ul{margin:0;padding-left:16px} .topic li{font-size:13.5px;color:#b6c8ca;margin:5px 0}
.types{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.stype{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:14px 16px}
.s-name{color:var(--teal2);font-weight:700;margin-bottom:5px} .s-desc{color:#aebfc2;font-size:13.5px}
.dates{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.dt-row{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:16px;text-align:left}
.dt-k{display:block;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px}
.dt-v{color:var(--teal2);font-weight:700;font-size:15px}
.dates-tz{grid-column:1/5;color:var(--mut);font-size:13px;font-style:italic}
.people{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.person{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:16px}
.p-name{color:var(--ink);font-weight:700;font-size:15px} .p-aff{color:var(--mut);font-size:13px;margin-top:4px}
.steering .people{grid-template-columns:1fr 1fr}
.contact{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.contact .mail{font-family:"DejaVu Sans Mono",monospace;color:var(--teal2);font-size:18px;
  border:1px solid var(--line);padding:12px 18px;border-radius:4px;background:var(--panel)}
.support{background:var(--bg2)} .support .wrap{max-width:1180px;margin:0 auto;padding:54px 34px}
footer{border-top:1px solid var(--line);color:var(--mut);text-align:center;padding:28px 16px;font-size:13px;position:relative;z-index:1}
@media(max-width:820px){.hero{grid-template-columns:1fr;gap:24px}.hero h1{font-size:42px}
 nav.top ul{display:none}.topics{grid-template-columns:1fr}.dates{grid-template-columns:1fr 1fr}
 .dates-tz{grid-column:1/3}.people,.steering .people,.types,.aud{grid-template-columns:1fr}}
"""

B_BODY = f"""
<nav class="top"><div class="brand">{logo('30px')} BAU<b>VIZ</b></div><ul>{NAV}</ul></nav>
<div class="wrap">
<header class="hero">
  <div>{logo('150px')}</div>
  <div>
    <div class="tag mono">EuroVis 2027 &middot; Half-day workshop</div>
    <h1>BAU<b>VIZ</b> 2027</h1>
    <p class="sub">{B.SUBTITLE}</p>
    <p class="meta"><span>Stuttgart, Germany</span> &middot; TBA &middot; in conjunction with EuroVis 2027</p>
  </div>
</header>
<main>
 <section id="about"><h2><span class="idx mono">01</span>About</h2><p class="lead">{B.ABOUT}</p></section>
 <section id="program"><h2><span class="idx mono">02</span>Program</h2><div class="tl">{PROG}</div><p class="note">{B.PROGRAM_NOTE}</p></section>
 <section id="format"><h2><span class="idx mono">03</span>Format &amp; Audience</h2><p class="lead">{B.FORMAT}</p>
   <h3>Target audience</h3><ul class="aud">{AUD}</ul></section>
 <section id="topics"><h2><span class="idx mono">04</span>Topics</h2><div class="topics">{TOPICS}</div></section>
 <section id="submit"><h2><span class="idx mono">05</span>Submission</h2><div class="types">{STYPES}</div>
   <h3>Process &amp; policies</h3><p class="lead">{B.SUBMIT_PROC}</p></section>
 <section id="dates"><h2><span class="idx mono">06</span>Important Dates</h2><div class="dates">{DATES}<div class="dates-tz">{B.DATES_TZ}</div></div></section>
 <section id="org"><h2><span class="idx mono">07</span>Organization</h2>
   <h3 style="margin-top:0">Organizers</h3><div class="people">{ORG}</div>
   <h3>Steering committee</h3><div class="steering"><div class="people">{STEER}</div></div>
   <h3>Program committee</h3><p class="lead">{B.PC_NOTE}</p></section>
 <section id="contact"><h2><span class="idx mono">08</span>Contact</h2>
   <div class="contact"><span class="mail">{B.CONTACT}</span><span style="color:var(--mut)">for any further enquiry</span></div></section>
</main>
</div>
<footer>{B.FOOT}</footer>
"""

# =========================================================================
# C — "Editorial": asymmetric split, magazine, big index numbers, whitespace.
# =========================================================================
C_CSS = r"""
:root{--ink:#1c1f21;--mut:#66707a;--teal:#1f6d7e;--teal2:#2d889d;--line:#d7dde0;--bg:#fbfcfc;--body:#2c3135;--body2:#3c4246}
body.dark{--ink:#eceff0;--mut:#97a2a8;--teal:#4fb0c3;--teal2:#6cc7d8;--line:#2b3338;--bg:#0f1416;--body:#c6cfce;--body2:#a9b5ba}
*{box-sizing:border-box} html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,"Times New Roman",serif;color:var(--ink);line-height:1.6;background:var(--bg);transition:background .3s,color .3s}
.sans{font-family:"Helvetica Neue",Arial,sans-serif}
a{color:var(--teal);text-decoration:none;border-bottom:1px solid rgba(31,109,126,.3)} a:hover{border-bottom-color:var(--teal)}
nav.top{display:flex;align-items:center;justify-content:space-between;padding:18px 44px;
  border-bottom:2px solid var(--ink)}
nav.top .brand{display:flex;align-items:center;gap:14px;font-family:"Helvetica Neue",Arial,sans-serif;
  font-weight:700;letter-spacing:2px;font-size:18px}
nav.top .brand img{height:34px}
nav.top ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-family:"Helvetica Neue",Arial,sans-serif;font-size:13px;letter-spacing:.5px}
nav.top li a{color:var(--ink);border-bottom:none} nav.top li a:hover{color:var(--teal)}
.nav-right{display:flex;align-items:center;gap:18px}
.theme-btn{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:1px;
  border:1.5px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;
  padding:7px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:8px;transition:all .25s}
.theme-btn:hover{border-color:var(--teal);color:var(--teal)}
.theme-btn .ico{font-size:14px;line-height:1}
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:end;
  padding:72px 44px 56px;max-width:1180px;margin:0 auto}
.hero .logo{height:210px;margin-bottom:22px}
.hero .sub{font-size:20px;font-style:italic;color:var(--mut);margin:0 0 0}
.hero .facts{border-left:2px solid var(--teal);padding-left:22px;font-family:"Helvetica Neue",Arial,sans-serif}
.hero .facts div{margin:12px 0;font-size:14px}
.hero .facts .k{color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:1.5px}
.hero .facts .val{font-size:16px;color:var(--ink);font-weight:600}
main{max-width:1180px;margin:0 auto;padding:0 44px}
section{padding:46px 0;border-top:1px solid var(--line)}
.sec-head{display:flex;align-items:baseline;gap:22px;margin-bottom:26px}
.sec-head .num{font-family:"Helvetica Neue",Arial,sans-serif;font-size:54px;font-weight:800;color:var(--teal2);opacity:.5;line-height:1}
.sec-head h2{font-family:"Helvetica Neue",Arial,sans-serif;font-size:30px;margin:0;letter-spacing:-.5px}
.lead{font-size:18px;color:var(--body);max-width:760px}
h3{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:2px;text-transform:uppercase;
  color:var(--mut);margin:34px 0 16px}
.pg{display:flex;flex-direction:column}
.pg-row{display:grid;grid-template-columns:190px 1fr;gap:24px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.pg-row:last-child{border-bottom:none}
.pg-t{font-family:"Helvetica Neue",Arial,sans-serif;font-variant-numeric:tabular-nums;font-weight:700;color:var(--teal);font-size:15px}
.pg-d{font-size:16px}
.note{font-style:italic;color:var(--mut);font-size:14px;margin-top:16px}
.tba{font-family:"Helvetica Neue",Arial,sans-serif;font-size:24px;font-weight:700;letter-spacing:8px;color:var(--teal);margin:10px 0 0}
.aud{columns:2;column-gap:48px;padding-left:0;list-style:none;margin:0;font-size:15px}
.aud li{margin:6px 0;padding-left:18px;position:relative;break-inside:avoid}
.aud li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;background:var(--teal2)}
.topics{display:grid;grid-template-columns:1fr 1fr;gap:30px 48px}
.topic{border-top:2px solid var(--ink);padding-top:12px}
.topic-h{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;color:var(--teal);margin-bottom:8px;font-size:15px}
.topic ul{margin:0;padding-left:0;list-style:none;font-size:15px;color:var(--body)}
.topic li{margin:6px 0;padding-left:18px;position:relative;break-inside:avoid}
.topic li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;background:var(--teal2)}
.types{display:grid;grid-template-columns:1fr 1fr;gap:22px 40px}
.stype{padding-top:10px;border-top:1px solid var(--line)}
.s-name{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;margin-bottom:5px;font-size:15px}
.s-desc{font-size:15px;color:var(--mut)}
.dates{display:flex;flex-direction:column}
.dt-row{display:grid;grid-template-columns:1fr auto;gap:20px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.dt-row:last-of-type{border-bottom:none}
.dt-k{font-size:16px} .dt-v{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;color:var(--teal);font-size:16px}
.dates-tz{font-style:italic;color:var(--mut);font-size:13px;margin-top:12px}
.people{display:grid;grid-template-columns:1fr 1fr;gap:18px 48px}
.p-name{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:16px}
.p-aff{font-size:14px;color:var(--mut)}
.steering .people{grid-template-columns:1fr 1fr}
.contact .mail{font-family:"Helvetica Neue",Arial,sans-serif;font-size:22px;font-weight:600}
.support{max-width:1180px;margin:0 auto;padding:40px 44px 60px;border-top:2px solid var(--ink)}
.support .sec-head{margin-bottom:14px}
footer{border-top:1px solid var(--line);padding:24px 44px;font-size:13px;color:var(--mut);
  font-family:"Helvetica Neue",Arial,sans-serif;text-align:center}
@media(max-width:820px){.hero{grid-template-columns:1fr;gap:24px}.hero h1{font-size:52px}
 nav.top{flex-direction:column;align-items:flex-start;gap:12px}.topics,.types,.people,.steering .people{grid-template-columns:1fr;columns:1}
 .aud{columns:1}.sec-head{gap:14px}.sec-head .num{font-size:38px}}
"""

C_BODY = f"""
<nav class="top"><div class="brand">{logo('34px')} BAUVIZ 2027</div>
  <div class="nav-right"><ul>{NAV}</ul>
    <button id="theme-toggle" class="theme-btn" aria-label="Toggle dark mode"><span class="ico">&#9680;</span><span class="lbl">Dark</span></button>
  </div></nav>
<script>(function(){{
  var b=document.body,btn=document.getElementById('theme-toggle');
  function apply(d){{b.classList.toggle('dark',d);btn.querySelector('.ico').textContent=d?'☾':'☼';btn.querySelector('.lbl').textContent=d?'Light':'Dark';
    document.querySelectorAll('.logo').forEach(function(im){{im.src=d?'BAUVIZ-logo-dark.svg':'BAUVIZ-logo.svg'}});
    try{{localStorage.setItem('bauviz-theme',d?'dark':'light')}}catch(e){{}}}}
  var s;try{{s=localStorage.getItem('bauviz-theme')}}catch(e){{}}
  if(s==='dark'){{apply(true)}}else if(!s&&window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches){{apply(true)}}
  btn.addEventListener('click',function(){{apply(!b.classList.contains('dark'))}});
}})();</script>
<header class="hero">
  <div>{logo('210px')}
    <p class="sub">Workshop in conjunction with EuroVis 2027</p></div>
  <div class="facts">
    <div><div class="k">Location</div><div class="val">Stuttgart, Germany</div></div>
    <div><div class="k">Dates</div><div class="val">TBA</div></div>
    <div><div class="k">Format</div><div class="val">Half-day workshop</div></div>
    <div><div class="k">Contact</div><div class="val"><a href="mailto:{B.CONTACT}">{B.CONTACT}</a></div></div>
  </div>
</header>
<main>
 <section id="about"><div class="sec-head"><span class="num">01</span><h2>About</h2></div><p class="lead">{B.ABOUT}</p></section>
 <section id="program"><div class="sec-head"><span class="num">02</span><h2>Program</h2></div><div class="pg">{PROG}</div><p class="note">{B.PROGRAM_NOTE}</p></section>
 <section id="format"><div class="sec-head"><span class="num">03</span><h2>Format &amp; Audience</h2></div><p class="lead">{B.FORMAT}</p>
   <h3>Target audience</h3><ul class="aud">{AUD}</ul></section>
 <section id="topics"><div class="sec-head"><span class="num">04</span><h2>Topics</h2></div><div class="topics">{TOPICS}</div></section>
 <section id="submit"><div class="sec-head"><span class="num">05</span><h2>Submission</h2></div><div class="types">{STYPES}</div>
   <h3>Process &amp; policies</h3><p class="lead">{B.SUBMIT_PROC}</p></section>
 <section id="dates"><div class="sec-head"><span class="num">06</span><h2>Important Dates</h2></div><div class="dates">{DATES}<p class="dates-tz">{B.DATES_TZ}</p></div></section>
 <section id="org"><div class="sec-head"><span class="num">07</span><h2>Organization</h2></div>
   <h3 style="margin-top:0">Organizers</h3><div class="people">{ORG}</div>
   <h3>Steering committee</h3><div class="steering"><div class="people">{STEER}</div></div>
   <h3>Program committee</h3><p class="lead">{B.PC_NOTE}</p></section>
 <section id="contact"><div class="sec-head"><span class="num">08</span><h2>Contact</h2></div>
   <p class="contact"><a class="mail" href="mailto:{B.CONTACT}">{B.CONTACT}</a></p></section>
</main>
<footer>{B.FOOT}</footer>
"""

# =========================================================================
# D — "Drafting Sheet": left rail nav, blueprint grid, technical corner ticks.
# =========================================================================
D_CSS = r"""
:root{--ink:#233135;--mut:#5f6d72;--teal:#1f6d7e;--teal2:#2d889d;--line:#c9d4d8;--bg:#ffffff;--paper:#f3f7f8;--panel:#ffffff}
*{box-sizing:border-box} html{scroll-behavior:smooth}
body{margin:0;font-family:"Helvetica Neue",Arial,sans-serif;color:var(--ink);line-height:1.55}
a{color:var(--teal);text-decoration:none} a:hover{text-decoration:underline}
body{background-color:var(--paper);
  background-image:linear-gradient(rgba(31,109,126,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(31,109,126,.05) 1px,transparent 1px);
  background-size:28px 28px}
.shell{display:grid;grid-template-columns:248px 1fr;min-height:100vh}
aside.rail{position:sticky;top:0;align-self:start;height:100vh;background:var(--bg);
  border-right:1px solid var(--line);padding:28px 22px;display:flex;flex-direction:column}
.rail .brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:1px;margin-bottom:6px}
.rail .brand img{height:30px}
.rail .yr{color:var(--teal);font-size:12px;letter-spacing:2px;margin-bottom:26px;padding-bottom:20px;border-bottom:1px solid var(--line)}
.rail nav{display:flex;flex-direction:column;gap:2px}
.rail nav a{padding:9px 12px;border-radius:4px;font-size:13.5px;color:var(--ink);letter-spacing:.3px;border-left:2px solid transparent}
.rail nav a:hover{background:var(--paper);border-left-color:var(--teal2);text-decoration:none}
.rail nav a .no{color:var(--teal2);font-size:11px;margin-right:8px;font-variant-numeric:tabular-nums}
.rail .foot{margin-top:auto;font-size:11.5px;color:var(--mut);padding-top:18px;border-top:1px solid var(--line)}
.rail .foot .mail{color:var(--teal);font-weight:600}
.content{padding:0}
.hero{position:relative;background:var(--bg);border-bottom:1px solid var(--line);padding:64px 56px}
.hero .tick{position:absolute;width:16px;height:16px;border:2px solid var(--teal2)}
.hero .t-tl{top:14px;left:14px;border-right:none;border-bottom:none}
.hero .t-tr{top:14px;right:14px;border-left:none;border-bottom:none}
.hero .t-bl{bottom:14px;left:14px;border-right:none;border-top:none}
.hero .t-br{bottom:14px;right:14px;border-left:none;border-top:none}
.hero .row{display:flex;align-items:center;gap:40px;flex-wrap:wrap}
.hero .logo{height:140px}
.hero .tx h1{font-size:54px;margin:0;font-weight:800;letter-spacing:1px}
.hero .tx h1 .v{color:var(--teal)}
.hero .tx .sub{font-size:18px;color:var(--mut);margin:6px 0 0}
.hero .chips{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}
.chip{border:1px solid var(--line);background:var(--paper);padding:7px 14px;font-size:13px;border-radius:3px}
.chip b{color:var(--teal)}
main{padding:0 56px 40px}
section{position:relative;padding:44px 0;border-bottom:1px solid var(--line)}
section:last-child{border-bottom:none}
.sec-tag{display:inline-flex;align-items:center;gap:12px;margin-bottom:18px}
.sec-tag .lbl{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--mut);font-weight:600}
.sec-tag .bar{width:44px;height:2px;background:var(--teal)}
h2{font-size:24px;margin:0 0 20px}
.lead{font-size:15.5px;color:#37434a;max-width:760px}
h3{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--mut);margin:30px 0 14px}
.pg-row{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:11px 0;border-bottom:1px solid var(--line)}
.pg-row:last-child{border-bottom:none}
.pg-t{font-variant-numeric:tabular-nums;color:var(--teal);font-weight:700;font-size:14px}
.note{font-size:13px;color:var(--mut);font-style:italic;margin-top:14px}
.tba{font-weight:700;font-size:20px;letter-spacing:6px;color:var(--teal);margin:6px 0 0}
.aud{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:9px 28px}
.aud li{font-size:14px;padding-left:16px;position:relative}
.aud li::before{content:"\2713";position:absolute;left:0;color:var(--teal2);font-weight:700}
.topics{display:grid;grid-template-columns:1fr 1fr;gap:20px 36px}
.topic{background:var(--panel);border:1px solid var(--line);padding:16px 18px}
.topic::before{content:"";position:absolute}
.topic .topic-h{font-weight:700;color:var(--teal);margin-bottom:8px;font-size:14px;display:flex;justify-content:space-between;align-items:center}
.topic .topic-h .ci{font-size:11px;color:var(--teal2);font-variant-numeric:tabular-nums}
.topic ul{margin:0;padding-left:16px;font-size:13.5px;color:#43494d} .topic li{margin:4px 0}
.types{display:grid;grid-template-columns:1fr 1fr;gap:14px 30px}
.stype{border:1px solid var(--line);background:var(--panel);padding:14px 16px;border-radius:3px}
.s-name{font-weight:700;margin-bottom:5px;font-size:14.5px} .s-desc{font-size:13px;color:var(--mut)}
.dates{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.dt-row{border:1px solid var(--line);background:var(--panel);padding:16px;display:flex;justify-content:space-between;gap:16px;border-radius:3px}
.dt-k{font-weight:600;font-size:14px} .dt-v{color:var(--teal);font-weight:700;text-align:right}
.dates-tz{grid-column:1/3;font-size:13px;color:var(--mut);font-style:italic}
.people{display:grid;grid-template-columns:1fr 1fr;gap:14px 30px}
.person{border-left:3px solid var(--teal2);padding-left:14px}
.p-name{font-weight:700;font-size:15.5px} .p-aff{font-size:13.5px;color:var(--mut)}
.steering .people{grid-template-columns:1fr 1fr}
.contact .mail{font-size:20px;font-weight:700}
.support{background:var(--bg);margin:0 -56px;padding:44px 56px;border-bottom:1px solid var(--line)}
footer{background:#223033;color:#cdd8da;padding:22px 56px;font-size:12.5px;position:relative}
@media(max-width:900px){.shell{grid-template-columns:1fr}aside.rail{position:static;height:auto}
 .hero{padding:40px 24px}.hero .row{gap:24px}.hero .tx h1{font-size:40px}
 main{padding:0 24px}.support{margin:0 -24px;padding:40px 24px}footer{padding:22px 24px}
 .topics,.types,.dates,.people,.steering .people,.aud{grid-template-columns:1fr}.dates-tz{grid-column:1/2}}
"""

D_NAV = "\n".join(f'<a href="{h}"><span class="no">{i:02d}</span>{t}</a>'
                  for i,(t,h) in enumerate(B.NAV,1))
D_BODY = f"""
<div class="shell">
<aside class="rail">
  <div class="brand">{logo('30px')} BAUVIZ</div>
  <div class="yr">2027 &middot; STUTTGART</div>
  <nav>{D_NAV}</nav>
  <div class="foot">Contact<br><span class="mail">{B.CONTACT}</span></div>
</aside>
<div class="content">
<header class="hero">
  <span class="tick t-tl"></span><span class="tick t-tr"></span><span class="tick t-bl"></span><span class="tick t-br"></span>
  <div class="row">
    {logo('140px')}
    <div class="tx">
      <h1>BAU<span class="v">VIZ</span> 2027</h1>
      <p class="sub">{B.SUBTITLE}</p>
      <div class="chips">
        <span class="chip">Stuttgart, Germany</span>
        <span class="chip"><b>TBA</b></span>
        <span class="chip">in conjunction with EuroVis 2027</span>
        <span class="chip">Half-day workshop</span>
      </div>
    </div>
  </div>
</header>
<main>
 <section id="about"><div class="sec-tag"><span class="bar"></span><span class="lbl">01 &middot; About</span></div><h2>The workshop</h2><p class="lead">{B.ABOUT}</p></section>
 <section id="program"><div class="sec-tag"><span class="bar"></span><span class="lbl">02 &middot; Program</span></div><h2>Schedule</h2><div class="pg">{PROG}</div><p class="note">{B.PROGRAM_NOTE}</p></section>
 <section id="format"><div class="sec-tag"><span class="bar"></span><span class="lbl">03 &middot; Format &amp; Audience</span></div><h2>How it works</h2><p class="lead">{B.FORMAT}</p>
   <h3>Target audience</h3><ul class="aud">{AUD}</ul></section>
 <section id="topics"><div class="sec-tag"><span class="bar"></span><span class="lbl">04 &middot; Topics</span></div><h2>Scope &amp; topics</h2><div class="topics">{TOPICS}</div></section>
 <section id="submit"><div class="sec-tag"><span class="bar"></span><span class="lbl">05 &middot; Submission</span></div><h2>Call for papers</h2><div class="types">{STYPES}</div>
   <h3>Process &amp; policies</h3><p class="lead">{B.SUBMIT_PROC}</p></section>
 <section id="dates"><div class="sec-tag"><span class="bar"></span><span class="lbl">06 &middot; Dates</span></div><h2>Important dates</h2><div class="dates">{DATES}<div class="dates-tz">{B.DATES_TZ}</div></div></section>
 <section id="org"><div class="sec-tag"><span class="bar"></span><span class="lbl">07 &middot; Organization</span></div><h2>People</h2>
   <h3 style="margin-top:0">Organizers</h3><div class="people">{ORG}</div>
   <h3>Steering committee</h3><div class="steering"><div class="people">{STEER}</div></div>
   <h3>Program committee</h3><p class="lead">{B.PC_NOTE}</p></section>
 <section id="contact"><div class="sec-tag"><span class="bar"></span><span class="lbl">08 &middot; Contact</span></div><h2>Get in touch</h2>
   <p class="contact"><a class="mail" href="mailto:{B.CONTACT}">{B.CONTACT}</a></p></section>
</main>
<footer>{B.FOOT}</footer>
</div>
</div>
"""

DESIGNS = [
    ("A-blueprint",  "Blueprint (conservative, light)",     A_CSS, A_BODY),
    ("B-dark-twin",  "Dark Twin (dark, tech, timeline)",   B_CSS, B_BODY),
    ("C-editorial",  "Editorial (asymmetric split, serif)", C_CSS, C_BODY),
    ("D-drafting",   "Drafting Sheet (left rail, blueprint grid)", D_CSS, D_BODY),
]

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, label, css, body in DESIGNS:
        path = os.path.join(here, f"{name}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(B.page_wrap(css, body))
        print(f"wrote {path}  ({label})")
