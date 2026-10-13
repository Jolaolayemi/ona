#!/usr/bin/env python3
"""Ona demo app screens, designed by Olayemi. Run: python3 tools/build.py
Writes site/index.html and site/s/<slug>/index.html (each screen a fixed 390x844 artboard).
Icons: Line Awesome (site/assets/icons, inlined). Font: Nunito (OFL, site/assets/fonts).
?figma=1 on any URL switches motion off for html.to.design."""
import os, re, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, '..', 'site'))
ICONS = os.path.join(SITE, 'assets', 'icons')
V = '5'  # cache-bust for css/js
USED = set()

def ic(name, cls=''):
    USED.add(name)
    s = open(os.path.join(ICONS, name + '.svg')).read()
    s = re.sub(r'<\?xml[^>]*>', '', s).strip()
    return s.replace('<svg', f'<svg class="i {cls}" aria-hidden="true" fill="currentColor"', 1)

# ---------- the guide character: a little sprout-topped block, flat vector ----------
def mascot(mood='happy', size=120, cls=''):
    Y, E, INK = '#FFC21A', '#E09E00', '#24233F'
    arms = {
        'happy': f'<path d="M20 70 Q10 78 12 90" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M100 70 Q110 78 108 90" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/>',
        'cheer': f'<path d="M22 62 Q8 50 10 32" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M98 62 Q112 50 110 32" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/>',
        'oops': f'<path d="M20 70 Q8 66 6 56" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M100 70 Q110 78 108 90" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/>',
        'worried': f'<path d="M22 74 Q30 84 42 84" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M98 74 Q90 84 78 84" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/>',
        'think': f'<path d="M20 70 Q10 78 12 90" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M100 72 Q104 62 94 56" stroke="{E}" stroke-width="9" fill="none" stroke-linecap="round"/>',
    }[mood]
    if mood == 'cheer':
        eyes = f'<path d="M38 60 Q46 50 54 60" stroke="{INK}" stroke-width="5.5" fill="none" stroke-linecap="round"/><path d="M66 60 Q74 50 82 60" stroke="{INK}" stroke-width="5.5" fill="none" stroke-linecap="round"/>'
        mouth = f'<path d="M47 74 H73 Q72 92 60 92 Q48 92 47 74Z" fill="{INK}"/><path d="M53 86 Q60 80 67 86 Q64 91 60 91 Q56 91 53 86Z" fill="#FF7A7A"/>'
    else:
        px, py = {'happy': (2, 3), 'oops': (0, 5), 'worried': (0, 2), 'think': (4, -3)}[mood]
        eyes = (f'<ellipse cx="46" cy="58" rx="10.5" ry="12.5" fill="#fff"/><ellipse cx="74" cy="58" rx="10.5" ry="12.5" fill="#fff"/>'
                f'<circle cx="{46+px}" cy="{58+py}" r="6" fill="{INK}"/><circle cx="{74+px}" cy="{58+py}" r="6" fill="{INK}"/>'
                f'<circle cx="{48+px}" cy="{55+py}" r="2" fill="#fff"/><circle cx="{76+px}" cy="{55+py}" r="2" fill="#fff"/>')
        if mood in ('oops', 'worried'):
            eyes += f'<path d="M36 42 L54 46" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/><path d="M84 42 L66 46" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'
        mouth = {
            'happy': f'<path d="M50 79 Q60 89 70 79" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>',
            'oops': f'<ellipse cx="60" cy="83" rx="5.5" ry="6.5" fill="{INK}"/>',
            'worried': f'<path d="M50 84 Q55 79 60 84 Q65 89 70 84" stroke="{INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>',
            'think': f'<path d="M52 82 H68" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>',
        }[mood]
    return (f'<svg class="guide {cls}" width="{size}" height="{size}" viewBox="0 0 120 120" aria-hidden="true">'
            f'<path d="M60 24 V12" stroke="#1E9F55" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M60 14 Q48 2 38 8 Q46 20 60 14Z" fill="#2BC26B"/><path d="M60 12 Q72 0 84 5 Q76 18 60 12Z" fill="#2BC26B"/>'
            f'{arms}<rect x="38" y="100" width="16" height="12" rx="6" fill="{E}"/><rect x="66" y="100" width="16" height="12" rx="6" fill="{E}"/>'
            f'<rect x="18" y="28" width="84" height="80" rx="30" fill="{E}"/><rect x="18" y="22" width="84" height="80" rx="30" fill="{Y}"/>'
            f'<ellipse cx="32" cy="76" rx="6" ry="4" fill="#FF8F6B" opacity=".55"/><ellipse cx="88" cy="76" rx="6" ry="4" fill="#FF8F6B" opacity=".55"/>'
            f'{eyes}{mouth}</svg>')

def flame(size=100, cls=''):
    return (f'<svg class="flame {cls}" width="{size}" height="{size*1.2:.0f}" viewBox="0 0 100 120" aria-hidden="true">'
            '<path d="M50 4 C58 26 88 44 88 76 C88 100 70 116 50 116 C30 116 12 100 12 76 C12 58 24 46 32 36 C34 50 40 56 46 58 C42 38 44 20 50 4Z" fill="#FF8A1F"/>'
            '<path d="M50 50 C57 65 71 74 71 91 C71 105 61 113 50 113 C39 113 29 105 29 91 C29 81 35 73 41 67 C43 75 46 79 50 81 C47 71 46 61 50 50Z" fill="#FFC21A"/>'
            '<path d="M50 84 C55 92 60 96 60 103 C60 109 55 112 50 112 C45 112 40 109 40 103 C40 97 45 92 50 84Z" fill="#FFF1C2"/></svg>')

def ring(pct, size=34, color='var(--gr)', inner='', stroke=5, cls=''):
    r = (size - stroke) / 2; L = 2 * math.pi * r
    return (f'<div class="ring {cls}" style="width:{size}px;height:{size}px;--c:{color};--len:{L:.1f};--off:{L*(1-pct):.1f}">'
            f'<svg viewBox="0 0 {size} {size}"><circle class="tr" cx="{size/2}" cy="{size/2}" r="{r:.1f}" style="stroke-width:{stroke}"/>'
            f'<circle class="pr" cx="{size/2}" cy="{size/2}" r="{r:.1f}" style="stroke-width:{stroke}"/></svg><div class="in">{inner}</div></div>')

def burst(top=220, n=26, seed=4, spread=1.0):
    rnd = random.Random(seed)
    cols = ['var(--vi)', 'var(--ye)', 'var(--gr)', 'var(--sk)', 'var(--or)', 'var(--pk)', 'var(--rd)']
    out = []
    for k in range(n):
        a = math.pi + (k / (n - 1)) * math.pi + rnd.uniform(-.12, .12)
        d = rnd.uniform(110, 175) * spread
        x, y = math.cos(a) * d * 1.05, min(math.sin(a) * d * .85, -8) + rnd.uniform(-10, 10)
        shape = rnd.choice(['sq', 'dot', 'tri', 'bar2', 'sq', 'bar2'])
        st = f'--c:{cols[k % len(cols)]};--x:{x:.0f}px;--y:{y:.0f}px;--r:{rnd.randint(-160,160)}deg;--d:{rnd.randint(0,140)}ms'
        if shape == 'dot': st += ';--br:50%;--s:9px'
        if shape == 'sq': st += f';--s:{rnd.choice([8,10,11])}px'
        out.append(f'<i class="{"tri" if shape=="tri" else "bar2" if shape=="bar2" else ""}" style="{st}"></i>')
    return f'<div class="burst" style="--top:{top}px" aria-hidden="true">' + ''.join(out) + '</div>'

def sb(t='9:41'):
    return f'<div class="sb"><span>{t}</span><span class="ic">{ic("signal-solid")}{ic("wifi-solid")}{ic("battery-full-solid")}</span></div>'
GB = '<div class="gb"></div>'

def lbar(p, right=''):
    return f'<div class="lbar"><a class="x" aria-label="Close">{ic("times-solid")}</a><div class="bar" style="--p:{p}%"><i></i></div>{right}</div>'

def hstats(streak='12', xp='340', goal=0.6):
    return (f'<div class="hstats"><div class="stat c-or">{ic("fire-solid")}<span>{streak}</span></div>'
            f'<div class="stat" style="color:var(--ye-e)">{ic("bolt-solid")}<span>{xp} XP</span></div>'
            f'<div class="stat" style="color:var(--sk)">{ic("gem-solid")}<span>1,240</span></div>'
            f'<div class="stat c-gr">{ring(goal, 34, "var(--gr)", ic("bullseye-solid"))}<span style="font-size:14px">30/50</span></div></div>')

def nav(on='learn'):
    items = [('learn', 'Learn', 'map-signs-solid'), ('practice', 'Practice', 'flask-solid'), ('scam', 'Scam check', 'shield-alt-solid'), ('rewards', 'Rewards', 'gift-solid'), ('me', 'Profile', 'user')]
    return '<nav class="nav">' + ''.join(f'<a class="{"on" if k==on else ""}">{ic(i)}<span>{l}</span></a>' for k, l, i in items) + '</nav>'

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="{vp}">
<title>{title_e}</title>
<script>if(/[?&]figma=1/.test(location.search))document.documentElement.classList.add('figma')</script>
<link rel="preload" href="/assets/fonts/nunito.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/ona.css?v={v}"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
</head>"""

def head(**k):
    k['title_e'] = k['title'].replace('·', '&middot;').replace('×', '&times;').replace('’', '&rsquo;')
    return HEAD.format(**k)

SCREENS = []
def screen(code, slug, name, note, inner, cls=''):
    SCREENS.append((code, slug, name, note))
    html = (head(vp='width=390, initial-scale=1', title=f'Ona · {code} {name}', v=V) +
            f'\n<body class="art"><main class="screen {cls}" data-screen="{code}">\n{inner}\n</main>\n<script src="/assets/ona.js?v={V}" defer></script></body></html>\n')
    d = os.path.join(SITE, 's', slug); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(html)

def node(kind, icon, x=0, extra=''):
    return f'<div class="node {kind}" style="--x:{x}px">{extra}{ic(icon)}</div>'

def sheet(kind, title, why, btn, icon, xp=''):
    xpc = f'<span class="chip ye popin" style="margin-left:auto;--d:480ms;background:#fff">{ic("bolt-solid")} {xp}</span>' if xp else ''
    return (f'<div class="sheet {kind}"><div class="hd"><span class="badge">{ic(icon)}</span>{title}{xpc}</div>'
            f'<p class="why">{why}</p><button class="btn {"gr" if kind=="ok" else "rd"}">{btn}</button>{GB}</div>')

def hexb(c, e, icon, lk=False):
    if lk: c, e = '#E6E5EE', '#CDCCD9'
    shape = (f'<svg class="shape" viewBox="0 0 78 84"><path d="M39 6 L72 24 V58 L39 78 L6 58 V24Z" fill="{e}" transform="translate(0 4)" stroke="{e}" stroke-width="8" stroke-linejoin="round"/>'
             f'<path d="M39 6 L72 24 V58 L39 76 L6 58 V24Z" fill="{c}" stroke="{c}" stroke-width="8" stroke-linejoin="round"/></svg>')
    col = '#ADACC0' if lk else '#fff'
    return f'<div class="hex" style="color:{col}">{shape}{ic("lock-solid" if lk else icon)}</div>'

# =========================== A. ONBOARDING ===========================
welcome_art = f"""<svg width="300" height="250" viewBox="0 0 300 250" aria-hidden="true">
<path d="M70 222 C 70 180, 230 190, 222 140 C 216 100, 90 112, 96 70 C 100 44, 170 40, 196 34" stroke="#E7E6EF" stroke-width="22" fill="none" stroke-linecap="round"/>
<path d="M70 222 C 70 180, 230 190, 222 140" stroke="#FFE7A3" stroke-width="22" fill="none" stroke-linecap="round"/>
<g><ellipse cx="222" cy="148" rx="30" ry="26" fill="#E09E00"/><ellipse cx="222" cy="140" rx="30" ry="26" fill="#FFC21A"/><path d="M210 140 l8 8 l16 -16" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><ellipse cx="96" cy="78" rx="30" ry="26" fill="#4F31D4"/><ellipse cx="96" cy="70" rx="30" ry="26" fill="#6C4CF5"/><path d="M96 56 l4.5 9 l10 1.4 l-7.2 7 l1.7 10 l-9 -4.7 l-9 4.7 l1.7 -10 l-7.2 -7 l10 -1.4z" fill="#fff"/></g>
<g><rect x="176" y="10" width="46" height="40" rx="12" fill="#CDCCD9" transform="translate(0 6)"/><rect x="176" y="10" width="46" height="40" rx="12" fill="#E6E5EE"/><path d="M193 26 v-4 a6 6 0 0 1 12 0 v4" stroke="#ADACC0" stroke-width="4" fill="none"/><rect x="189" y="26" width="20" height="15" rx="4" fill="#ADACC0"/></g>
</svg>"""
screen('A1', 'welcome', 'Welcome and promise', 'Start screen with the one-line promise',
f"""{sb()}
<div class="body center" style="align-items:center;justify-content:center;padding-bottom:10px">
  <div class="wm rise" style="--i:0">ona</div>
  <div style="position:relative;margin-top:26px;width:300px;height:250px;--i:1" class="rise">
    {welcome_art}
    <div style="position:absolute;left:10px;top:120px" class="bob">{mascot('happy',112)}</div>
  </div>
  <h1 class="h1 rise" style="--i:2;margin-top:22px">Learn crypto in<br>five minutes a day.</h1>
  <p class="p rise" style="--i:3;margin-top:10px;max-width:300px">And learn to spot a scam before it finds you.</p>
</div>
<div class="foot"><button class="btn">Get started</button><button class="btn ghost">I already have an account</button></div>{GB}""")

screen('A2', 'goal', 'Goal picker', 'Save in dollars · send money · understand crypto · spot scams',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Back">{ic("arrow-left-solid")}</a><div class="bar" style="--p:25%"><i></i></div></div>
<div class="body" style="padding-top:8px">
  <div class="say rise" style="--i:0">{mascot('happy',84)}<div class="bub" style="margin-bottom:22px">What brings you to Ona?</div></div>
  <div class="opts" style="margin-top:20px" data-pick>
    <button class="opt rise" style="--i:1"><span class="ico" style="background:var(--gr-t);color:var(--gr-d)">{ic("piggy-bank-solid")}</span><span>Save in dollars<span class="sub">Keep savings steady with stablecoins</span></span></button>
    <button class="opt rise" style="--i:2"><span class="ico" style="background:var(--sk-t);color:var(--sk-d)">{ic("paper-plane-solid")}</span><span>Send money<span class="sub">Pay people and businesses abroad</span></span></button>
    <button class="opt rise" style="--i:3"><span class="ico" style="background:var(--ye-t);color:var(--ye-d)">{ic("lightbulb")}</span><span>Understand crypto<span class="sub">Finally get what everyone means</span></span></button>
    <button class="opt sel rise" style="--i:4"><span class="ico" style="background:#fff;color:var(--vi)">{ic("shield-alt-solid")}</span><span>Spot scams<span class="sub" style="color:var(--vi-d);opacity:.8">Know the tricks before they reach you</span></span><span class="end">{ic("check-circle")}</span></button>
  </div>
</div>
<div class="foot"><button class="btn">Continue</button></div>{GB}""")

screen('A3', 'level-check', 'Three-question level check', 'Question 2 of 3, to pick a starting point',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Back">{ic("arrow-left-solid")}</a><div class="bar" style="--p:50%"><i></i></div></div>
<div class="body" style="padding-top:6px">
  <div class="row rise" style="--i:0;justify-content:space-between"><span class="chip vi">{ic("compass")} Level check</span><span class="sm" style="font-weight:900">2 of 3</span></div>
  <div class="row rise" style="--i:0;gap:8px;margin-top:14px"><div class="bar thin" style="--p:100%;--c:var(--gr)"><i></i></div><div class="bar thin" style="--p:100%;--c:var(--vi)"><i></i></div><div class="bar thin" style="--p:0%"><i></i></div></div>
  <h1 class="h2 rise" style="--i:1;margin-top:22px">You get sent 50 USDC. Roughly how much is that in US dollars?</h1>
  <div class="opts" style="margin-top:20px" data-pick>
    <button class="opt rise" style="--i:2"><span class="k">A</span>It depends, it changes a lot every day</button>
    <button class="opt sel rise" style="--i:3"><span class="k">B</span>About $50</button>
    <button class="opt rise" style="--i:4"><span class="k">C</span>Nothing until I sell it</button>
    <button class="opt rise" style="--i:5"><span class="k">D</span>I'm not sure yet</button>
  </div>
  <div class="grow"></div>
  <p class="sm center rise" style="--i:6;margin-bottom:6px">No pressure. This only picks where your path starts.</p>
</div>
<div class="foot"><button class="btn">Check</button><a class="link">I'm brand new, start from zero</a></div>{GB}""")

def goalopt(name, mins, xp, sel=False, i=0):
    return (f'<button class="opt {"sel" if sel else ""} rise" style="--i:{i};min-height:58px;padding:10px 16px"><span>{name}</span>'
            f'<span style="margin-left:auto;font-size:14px;color:{"var(--vi)" if sel else "var(--ink2)"};font-weight:800">{mins} min a day · {xp} XP</span></button>')
screen('A4', 'daily-goal', 'Daily goal, reminder and low-data mode', 'Set the habit before the first lesson',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Back">{ic("arrow-left-solid")}</a><div class="bar" style="--p:85%"><i></i></div></div>
<div class="body" style="padding-top:4px">
  <h1 class="h2 rise" style="--i:0">Pick a daily goal</h1>
  <p class="sm rise" style="--i:0;margin-top:4px">You can change it any time.</p>
  <div class="opts" style="margin-top:14px;gap:10px" data-pick>
    {goalopt('Easy','3','10',False,1)}{goalopt('Steady','5','20',True,2)}{goalopt('Keen','10','30',False,3)}{goalopt('Serious','15','50',False,4)}
  </div>
  <div class="card rise" style="--i:5;margin-top:16px;padding:6px 16px">
    <div class="li"><span class="ico" style="background:var(--or-t);color:var(--or)">{ic("bell")}</span><div><div class="t">Daily reminder</div><div class="s">One nudge a day, never more</div></div><span class="end" style="color:var(--vi)">7:30 PM {ic("angle-right-solid")}</span></div>
    <div class="li"><span class="ico" style="background:var(--sk-t);color:var(--sk)">{ic("signal-solid")}</span><div><div class="t">Low-data mode</div><div class="s">Text and pictures only. Lessons<br>download on Wi-Fi.</div></div><span class="end"><span class="tg on" role="switch" aria-checked="true"></span></span></div>
  </div>
</div>
<div class="foot"><button class="btn">Start my first lesson</button></div>{GB}""")

# =========================== B. HOME ===========================
halo = ring(0.4, 102, 'var(--vi)', '', 9)
cur_node = f"""<div class="node cur" style="--x:-62px"><div class="tip">START</div><div style="position:absolute;left:-12px;top:-15px">{halo}</div>{ic("star-solid")}</div>"""
screen('B1', 'path', 'Learning path map', 'Unit 1 unlocked, the rest of the path locked',
f"""{sb()}{hstats()}
<div class="body scroll">
  <div class="unit rise" style="--i:0"><div><div class="cap">Unit 1 · 5 lessons</div><div class="h3" style="font-size:20px;margin-top:2px">Stablecoins 101</div></div><span class="gbk">{ic("book-open-solid")}</span></div>
  <div class="path">
    {node('done','check-solid',34)}
    {node('done','check-solid',-26)}
    <div style="height:40px"></div>{cur_node}
    {node('lk','lock-solid',-30)}
    {node('lk','lock-solid',24)}
    {node('chest','trophy-solid',56)}
    <div style="position:absolute;left:0;top:300px" class="bob">{mascot('happy',92)}</div>
  </div>
  <div class="unit lk rise" style="--i:2;margin-top:8px"><div><div class="cap">Unit 2 · Locked</div><div class="h3" style="font-size:19px;margin-top:2px">Keep your wallet safe</div></div><span class="gbk">{ic("lock-solid")}</span></div>
  <div class="path" style="padding-top:20px">{node('lk','lock-solid',0)}</div>
</div>
{nav('learn')}{GB}""")

def day(l, state='', icon='fire-solid'):
    inner = ic(icon) if state else ''
    return f'<div class="day {state}"><b>{inner}</b>{l}</div>'
screen('B2', 'today', 'Header: streak, XP and daily goal', 'The header opened: streak week, XP today, goal ring',
f"""{sb()}{hstats()}
<div style="position:absolute;left:0;right:0;top:82px;bottom:86px;background:rgba(36,35,63,.35)"></div>
<div style="position:relative;background:#fff;border-radius:0 0 26px 26px;padding:6px 20px 22px;box-shadow:0 10px 0 rgba(36,35,63,.06);z-index:2" class="rise">
  <div class="row" style="justify-content:space-between;margin-top:8px">
    <div><div class="h1" style="font-size:40px;color:var(--or)"><span data-count="12">12</span></div><div class="h3" style="color:var(--or-d)">day streak</div></div>
    <div class="flick" style="line-height:0">{flame(72)}</div>
  </div>
  <div class="week" style="margin-top:14px">{day('M','on')}{day('T','on')}{day('W','frz','snowflake-solid')}{day('T','on')}{day('F','on')}{day('S','on')}{day('S','today')}</div>
  <p class="sm" style="margin-top:12px">{ic("snowflake-solid","c-sk")} A streak freeze covered Wednesday. 1 freeze left.</p>
  <div class="card" style="margin-top:16px;display:flex;align-items:center;gap:16px">
    {ring(0.6, 86, 'var(--gr)', '<span style="font-size:18px;font-weight:900;color:var(--ink)">60%</span>', 10)}
    <div style="flex:1"><div class="h3">Daily goal</div><div class="sm" style="margin-top:2px">30 of 50 XP today. One more lesson and you're there.</div>
    <div class="row" style="gap:8px;margin-top:10px"><span class="chip ye">{ic("bolt-solid")} 340 XP total</span></div></div>
  </div>
</div>
<div class="grow"></div>
{nav('learn')}{GB}""")

# =========================== C. LESSON LOOP ===========================
scale_art = """<svg width="310" height="170" viewBox="0 0 310 170" aria-hidden="true">
<rect x="0" y="0" width="310" height="170" rx="20" fill="#E3F2FF"/>
<rect x="147" y="44" width="16" height="96" rx="6" fill="#6C4CF5"/><rect x="113" y="138" width="84" height="14" rx="7" fill="#4F31D4"/>
<rect x="56" y="40" width="198" height="10" rx="5" fill="#4F31D4"/><circle cx="155" cy="45" r="11" fill="#6C4CF5"/><circle cx="155" cy="45" r="4" fill="#fff"/>
<path d="M70 50 L48 98 M70 50 L92 98" stroke="#4F31D4" stroke-width="3"/><path d="M240 50 L218 98 M240 50 L262 98" stroke="#4F31D4" stroke-width="3"/>
<path d="M40 98 H100 Q98 112 70 112 Q42 112 40 98Z" fill="#4F31D4"/><path d="M210 98 H270 Q268 112 240 112 Q212 112 210 98Z" fill="#4F31D4"/>
<circle cx="70" cy="80" r="22" fill="#1E9F55"/><circle cx="70" cy="76" r="22" fill="#2BC26B"/><text x="70" y="84" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="22" fill="#fff">$1</text>
<circle cx="240" cy="80" r="22" fill="#1688D8"/><circle cx="240" cy="76" r="22" fill="#2BA8FF"/><text x="240" y="81" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="11.5" fill="#fff">1 USDC</text>
<rect x="128" y="10" width="54" height="22" rx="11" fill="#fff"/><text x="155" y="25.5" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="12" fill="#2BA8FF">= same</text>
</svg>"""
screen('C1', 'lesson-story', 'Story lesson card', '60-second illustrated story, Lesson 1',
f"""{sb()}{lbar(20, '<span class="chip">' + ic("clock") + ' 60s</span>')}
<div class="body" style="padding-top:2px">
  <div class="cap rise" style="--i:0;color:var(--vi)">Stablecoins 101 · Lesson 1</div>
  <h1 class="h2 rise" style="--i:0;margin-top:4px">Meet the stablecoin</h1>
  <div class="rise" style="--i:1;margin-top:14px">{scale_art}</div>
  <p class="p rise" style="--i:2;margin-top:14px;color:var(--ink)">Sam does design work for a client in another country. A bank transfer takes days and loses $25 in fees.</p>
  <p class="p rise" style="--i:3;margin-top:8px;color:var(--ink)">The client offers to pay in <b class="c-vi">USDC</b> instead. It arrives in minutes.</p>
  <div class="card rise" style="--i:4;margin-top:14px;background:var(--ye-t);border-color:#FFE08A;display:flex;gap:12px;align-items:flex-start;padding:12px 14px">
    <span style="font-size:26px;color:var(--ye-e)">{ic("lightbulb")}</span>
    <div style="font-size:15px;line-height:1.4;font-weight:800">A stablecoin is a token built to stay at one price, usually $1. That's what makes it useful for saving and paying.</div>
  </div>
</div>
<div class="foot"><button class="btn">Continue</button></div>{GB}""")

MCQ = [('A', 'Bitcoin'), ('B', 'USDC'), ('C', 'A brand-new meme coin'), ('D', 'An NFT')]
def mcq(state=None):
    out = []
    for i, (k, t) in enumerate(MCQ):
        cls = ''
        if state == 'sel' and k == 'B': cls = 'sel'
        if state == 'ok' and k == 'B': cls = 'ok'
        end = f'<span class="end">{ic("check-circle")}</span>' if cls == 'ok' else ''
        out.append(f'<button class="opt {cls} rise" style="--i:{i+1}"><span class="k">{k}</span>{t}{end}</button>')
    return ''.join(out)
mc_head = f"""<div class="row rise" style="--i:0;gap:8px"><span class="chip vi">{ic("comment-dots")} New question</span></div>
  <h1 class="h2 rise" style="--i:0;margin-top:14px">Which one is built to stay at $1?</h1>"""
screen('C2a', 'q-multiple-choice', 'Question: multiple choice', 'Answer picked, ready to check',
f"""{sb()}{lbar(40)}
<div class="body" style="padding-top:6px">{mc_head}
  <div class="opts" style="margin-top:22px" data-pick>{mcq('sel')}</div>
  <div class="grow"></div>
  <div class="say" style="margin-bottom:6px">{mascot('think',70)}<div class="bub" style="font-size:14.5px;margin-bottom:14px">Hint: think back to Sam's story.</div></div>
</div>
<div class="foot"><button class="btn">Check</button></div>{GB}""")

scam_card = lambda extra='', extra2='', h='': f"""<div class="deck rise" style="--i:1;{h}">
    <div class="sw b2"></div><div class="sw b1"></div>
    <div class="sw top" {extra}>
      <span class="stamp scam">SCAM</span><span class="stamp legit">LEGIT</span>
      <div class="cap" style="margin-bottom:12px">Direct message</div>
      <div class="from"><span class="av" style="background:var(--sk)">{ic("user-shield-solid")}</span><div><div class="h3" style="font-size:16px">Wallet Support Team</div><div class="sm">@wallet_help_desk2 · just now</div></div></div>
      <div class="msg">Hi! We noticed unusual activity on your wallet and it has been <b>locked</b>. To unlock it, reply with your 12-word recovery phrase within 24 hours, or your funds will be lost.</div>
      {extra2}
    </div>
  </div>"""
screen('C2b', 'q-scam-or-legit', 'Question: scam or legit? swipe', 'Daily scam check, swipe left or right',
f"""{sb()}{lbar(60)}
<div class="body" style="padding-top:6px">
  <div class="row rise" style="--i:0;justify-content:space-between"><span class="chip rd">{ic("shield-alt-solid")} Scam or legit?</span><span class="sm" style="font-weight:900">Daily check · 3 of 5</span></div>
  <h1 class="h2 rise" style="--i:0;margin-top:12px">Is this message a scam?</h1>
  {scam_card()}
  <div class="grow"></div>
  <p class="sm center" style="margin-bottom:12px">{ic("arrow-left-solid")} Swipe left for scam · right for legit {ic("arrow-right-solid")}</p>
  <div class="swbtns"><button class="btn rd">{ic("times-solid")} Scam</button><button class="btn gr">{ic("check-solid")} Legit</button></div>
</div>
<div style="height:14px"></div>{GB}""")

screen('C2c', 'q-order-steps', 'Question: put the steps in order', 'Drag to order. One step mid-drag',
f"""{sb()}{lbar(70)}
<div class="body" style="padding-top:6px">
  <div class="row rise" style="--i:0"><span class="chip sk">{ic("sort-solid") if False else ic("grip-lines-solid")} Put in order</span></div>
  <h1 class="h2 rise" style="--i:0;margin-top:12px">You're paying someone 200 USDC. What's the safe order?</h1>
  <div class="ord" style="margin-top:18px">
    <div class="oi rise" style="--i:1"><span class="n">1</span>Copy their address straight from them<span class="gh">{ic("grip-lines-solid")}</span></div>
    <div class="oi rise" style="--i:2"><span class="n">2</span>Check the first and last 4 characters match<span class="gh">{ic("grip-lines-solid")}</span></div>
    <div class="oi slot rise" style="--i:3">.</div>
    <div class="oi lift rise" style="--i:3;margin-top:-50px"><span class="n" style="background:var(--vi);color:#fff">3</span>Send a small test amount first<span class="gh" style="color:var(--vi)">{ic("grip-lines-solid")}</span></div>
    <div class="oi rise" style="--i:4"><span class="n">4</span>Once they confirm it arrived, send the rest<span class="gh">{ic("grip-lines-solid")}</span></div>
  </div>
  <div class="grow"></div>
  <p class="sm center" style="margin-bottom:6px">Hold and drag a step to move it.</p>
</div>
<div class="foot"><button class="btn">Check</button></div>{GB}""")

screen('C3a', 'feedback-correct', 'Feedback: correct', 'Green sheet with a one-line why',
f"""{sb()}{lbar(50)}
<div class="body" style="padding-top:6px">{mc_head}
  <div class="opts" style="margin-top:22px">{mcq('ok')}</div>
</div>
{sheet('ok', 'Nice, that’s right!', 'USDC is backed by dollars and similar assets held in reserve, so 1 USDC aims to stay worth $1.', 'Continue', 'check-solid', '+10 XP')}""")

screen('C3b', 'feedback-incorrect', 'Feedback: incorrect', 'Red sheet with a one-line why, card shakes',
f"""{sb()}{lbar(60)}
<div class="body" style="padding-top:6px">
  <div class="row" style="justify-content:space-between"><span class="chip rd">{ic("shield-alt-solid")} Scam or legit?</span><span class="sm" style="font-weight:900">You said: Legit</span></div>
  <h1 class="h2" style="margin-top:12px">Is this message a scam?</h1>
  <div class="shake">{scam_card('style="border-color:var(--rd)"', '<div class="cap" style="margin-top:14px;color:var(--rd)">Red flags</div><div class="row" style="gap:8px;margin-top:8px;flex-wrap:wrap"><span class="chip rd">' + ic("clock") + ' Rushes you</span><span class="chip rd">' + ic("key-solid") + ' Asks for your phrase</span><span class="chip rd">' + ic("user-shield-solid") + ' Unofficial account</span></div>', 'height:380px').replace('class="stamp scam"','class="stamp scam" style="opacity:1"')}</div>
</div>
{sheet('bad', 'Not quite. It’s a scam.', 'Real support will never ask for your recovery phrase. Anyone who has it can empty your wallet.', 'Got it', 'times-solid')}""")

screen('C4a', 'lesson-complete', 'Lesson complete', 'XP earned, accuracy and time, with a burst',
f"""{sb()}
<div class="body center" style="align-items:center;justify-content:center;padding-bottom:20px">
  {burst(300, 28, 7)}
  <div class="popin" style="--d:80ms">{mascot('cheer',170)}</div>
  <h1 class="h1 rise" style="--i:3;margin-top:22px;color:var(--vi);font-size:32px">Lesson complete!</h1>
  <p class="p rise" style="--i:4;margin-top:8px">You got 4 of 5 right on the first try.</p>
  <div class="tiles rise" style="--i:5;width:100%;margin-top:30px">
    <div class="tile" style="--c:var(--ye-e)"><div class="t">XP earned</div><div class="v">{ic("bolt-solid")}<span data-count="15" data-delay="500">15</span></div></div>
    <div class="tile" style="--c:var(--gr)"><div class="t">Accuracy</div><div class="v">{ic("bullseye-solid")}<span data-count="80" data-suf="%" data-delay="600">80%</span></div></div>
    <div class="tile" style="--c:var(--sk)"><div class="t">Time</div><div class="v">{ic("stopwatch-solid")}4:12</div></div>
  </div>
  <div class="card rise" style="--i:6;width:100%;margin-top:16px;padding:12px 14px;display:flex;align-items:center;gap:12px;text-align:left">
    <span style="font-size:24px;color:var(--vi)">{ic("redo-alt-solid")}</span><span class="sm" style="color:var(--ink);font-size:14px">The one you missed comes back in your next review, so it sticks.</span>
  </div>
</div>
<div class="foot"><button class="btn">Continue</button></div>{GB}""")

screen('C4b', 'streak-extended', 'Streak extended', 'Flame celebration and the week so far',
f"""{sb()}
<div class="body center" style="align-items:center;justify-content:center;padding-bottom:10px">
  {burst(330, 22, 11, .95)}
  <div class="popin" style="--d:60ms;position:relative">
    <div class="flick">{flame(140)}</div>
  </div>
  <div class="rise" style="--i:3;font-size:84px;font-weight:1000;line-height:1;color:var(--or);margin-top:6px"><span data-count="13" data-delay="450">13</span></div>
  <div class="h2 rise" style="--i:4;color:var(--or-d)">day streak!</div>
  <div class="card rise" style="--i:5;width:100%;margin-top:28px">
    <div class="week">{day('M','on')}{day('T','on')}{day('W','on')}{day('T','on')}{day('F','on')}{day('S','on')}{day('S','today')}</div>
    <p class="sm" style="margin-top:14px;color:var(--ink)">Come back tomorrow to keep it going. Miss a day? A streak freeze has your back.</p>
  </div>
</div>
<div class="foot"><button class="btn or">Continue</button></div>{GB}""")

def lbarrow(name, pct, col):
    return (f'<div style="margin-top:12px"><div class="row" style="justify-content:space-between;font-size:14.5px;font-weight:800"><span>{name}</span><span style="color:{col}">{pct}%</span></div>'
            f'<div class="bar thin" style="--p:{pct}%;--c:{col};margin-top:6px"><i></i></div></div>')
screen('C5', 'unit-quiz', 'Unit quiz: mastery score', 'Unit 1 results, payout waits for a re-check',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Close">{ic("times-solid")}</a><span class="h3" style="flex:1;text-align:center;margin-right:26px">Unit 1 quiz</span></div>
<div class="body" style="padding-top:4px">
  <div class="center rise" style="--i:0;display:flex;flex-direction:column;align-items:center">
    <div style="position:relative">{ring(0.86, 150, 'var(--vi)', '<div><div style="font-size:40px;font-weight:1000;color:var(--ink);line-height:1"><span data-count="86" data-suf="%">86%</span></div><div class="cap" style="margin-top:4px">Mastery</div></div>', 14)}</div>
    <h1 class="h2" style="margin-top:14px">Stablecoins 101: mastered</h1>
    <p class="sm" style="margin-top:4px">12 of 14 right · 80% or more counts as mastered</p>
  </div>
  <div class="card rise" style="--i:1;margin-top:16px;padding:6px 16px 16px">
    {lbarrow('What a stablecoin is',100,'var(--gr)')}{lbarrow('How it holds $1',100,'var(--gr)')}{lbarrow('Sending safely',75,'var(--ye-e)')}{lbarrow('Fees and networks',67,'var(--or)')}{lbarrow('Spotting stablecoin scams',100,'var(--gr)')}
  </div>
  <div class="practice rise" style="--i:2;margin-top:14px;background:var(--vi-t);border-color:#d9d0ff;color:var(--vi-d)">{ic("calendar")}<span>Quick re-check in 3 days (Fri, Oct 16). Pass it to unlock this unit's reward.</span></div>
</div>
<div class="foot"><button class="btn">Continue</button><a class="link" style="padding:0">Review the 2 I missed</a></div>{GB}""")

# =========================== D. PRACTICE SANDBOX ===========================
screen('D1', 'sandbox-send', 'Practice wallet: send test USDT', 'Double-check the address, see the fee',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Back">{ic("arrow-left-solid")}</a><span class="h3" style="flex:1">Send test USDT</span><span class="chip ye">{ic("flask-solid")} Practice</span></div>
<div class="body" style="padding-top:4px;gap:12px">
  <div class="practice rise" style="--i:0">{ic("info-circle-solid")}<span>Practice wallet. Test money only, nothing real moves.</span></div>
  <div class="field rise" style="--i:1"><div class="lb">To address</div><div class="addr"><mark>TQ7x</mark> 4mWb 8RkL zq2N f6uY cVt3 JhPa <mark>9fKp</mark></div></div>
  <div class="card rise" style="--i:2;padding:12px 14px;border-color:#B8EBCB;background:var(--gr-t)">
    <div class="row" style="gap:10px"><span class="chk">{ic("check-solid")}</span><span style="font-size:15px;font-weight:900;color:var(--gr-d)">Double-checked</span></div>
    <div class="row" style="gap:10px;margin-top:10px">
      <div style="flex:1;background:#fff;border-radius:12px;padding:8px 10px"><div class="cap">Starts with</div><div style="font-size:22px;font-weight:1000;letter-spacing:.06em">TQ7x</div></div>
      <div style="flex:1;background:#fff;border-radius:12px;padding:8px 10px"><div class="cap">Ends with</div><div style="font-size:22px;font-weight:1000;letter-spacing:.06em">9fKp</div></div>
    </div>
    <div class="sm" style="margin-top:8px;color:#1d6b40">Matches the address your contact sent you.</div>
  </div>
  <div class="field rise" style="--i:3;display:flex;align-items:center"><div><div class="lb">Amount</div><div style="font-size:30px;font-weight:1000">25.00 <span style="font-size:18px;color:var(--ink2)">test USDT</span></div></div><span class="chip" style="margin-left:auto">Max 100</span></div>
  <div class="rise" style="--i:4;padding:0 4px">
    <div class="kv"><span>Network fee</span><b>1.00 test USDT</b></div>
    <div class="kv" style="border-top:2px solid var(--line)"><span>They receive</span><b>25.00 test USDT</b></div>
    <div class="kv"><span style="font-weight:900;color:var(--ink)">Total from you</span><b style="font-size:17px">26.00 test USDT</b></div>
  </div>
</div>
<div class="foot"><button class="btn">Review and send</button></div>{GB}""")

def signed(icon, col, t, s):
    return f'<div class="li"><span class="ico" style="background:{col[0]};color:{col[1]}">{ic(icon)}</span><div><div class="t">{t}</div><div class="s">{s}</div></div></div>'
screen('D2', 'sandbox-debrief', 'Debrief: here’s what you just signed', 'Plain-words recap of the practice send',
f"""{sb()}
<div class="body" style="padding-top:22px">
  <div class="rise" style="--i:0;display:flex;align-items:center;justify-content:space-between"><span class="chip ye">{ic("flask-solid")} Practice send done</span>{mascot('happy',64)}</div>
  <h1 class="h1 rise" style="--i:0;margin-top:4px">Here’s what you<br>just signed</h1>
  <div class="card rise" style="--i:1;margin-top:18px;padding:4px 16px">
    {signed('paper-plane-solid',('var(--vi-t)','var(--vi)'),'You sent 25 test USDT','To TQ7x…9fKp, the address you checked')}
    {signed('coins-solid',('var(--ye-t)','var(--ye-e)'),'You paid a 1 test USDT fee','It goes to the network, not to Ona')}
    {signed('ban-solid',('var(--rd-t)','var(--rd)'),'It can’t be undone','No bank or app can reverse a send')}
    {signed('key-solid',('var(--gr-t)','var(--gr-d)'),'Nobody got your keys','Signing a send never needs your recovery phrase')}
  </div>
  <div class="row rise" style="--i:2;margin-top:18px;justify-content:space-between"><span class="cap">How you did</span><span class="chip ye popin" style="--d:600ms">{ic("bolt-solid")} +10 XP</span></div>
  <div class="row rise" style="--i:2;margin-top:8px;gap:8px;flex-wrap:wrap">
    <span class="chip gr">{ic("check-solid")} Checked the address</span><span class="chip gr">{ic("check-solid")} Read the fee</span><span class="chip or">{ic("lightbulb")} Next time: test amount first</span>
  </div>
</div>
<div class="foot"><button class="btn">Continue</button><a class="link" style="padding:0">Try it again</a></div>{GB}""")

# =========================== E. REWARDS & PROGRESSION ===========================
lvl_badge = f"""<svg width="190" height="206" viewBox="0 0 190 206" aria-hidden="true">
<path d="M95 14 L170 56 V140 L95 184 L20 140 V56Z" fill="#4F31D4" transform="translate(0 12)" stroke="#4F31D4" stroke-width="18" stroke-linejoin="round"/>
<path d="M95 14 L170 56 V140 L95 184 L20 140 V56Z" fill="#6C4CF5" stroke="#6C4CF5" stroke-width="18" stroke-linejoin="round"/>
<path d="M95 38 L150 69 V128 L95 160 L40 128 V69Z" fill="#7E62FF"/>
<text x="95" y="128" text-anchor="middle" font-family="Nunito" font-weight="1000" font-size="78" fill="#fff">4</text>
<rect x="45" y="168" width="100" height="30" rx="15" fill="#FFC21A"/><text x="95" y="189" text-anchor="middle" font-family="Nunito" font-weight="1000" font-size="15" fill="#24233F" letter-spacing="1.5">LEVEL UP</text>
</svg>"""
screen('E1', 'level-up', 'Level-up moment', 'Level 4 reached, what it unlocks',
f"""{sb()}
<div class="body center" style="align-items:center;justify-content:center;padding-bottom:10px">
  {burst(330, 26, 21)}
  <div class="popin" style="--d:60ms">{lvl_badge}</div>
  <h1 class="h1 rise" style="--i:3;margin-top:18px">You're Level 4!</h1>
  <p class="p rise" style="--i:4;margin-top:6px">Level 4 · Careful Sender</p>
  <div class="card rise" style="--i:5;width:100%;margin-top:22px;text-align:left;padding:4px 16px">
    <div class="li"><span class="ico" style="background:var(--vi-t);color:var(--vi)">{ic("lock-open-solid")}</span><div><div class="t">Unit 2 unlocked</div><div class="s">Keep your wallet safe</div></div></div>
    <div class="li"><span class="ico" style="background:var(--sk-t);color:var(--sk)">{ic("snowflake-solid")}</span><div><div class="t">+1 streak freeze</div><div class="s">Now you can hold 2</div></div></div>
  </div>
  <div style="width:100%;margin-top:16px;--i:6" class="rise"><div class="row" style="justify-content:space-between" ><span class="sm">Level 5</span><span class="sm">120 / 600 XP</span></div><div class="bar thin" style="--p:20%;--c:var(--ye);margin-top:6px"><i></i></div></div>
</div>
<div class="foot"><button class="btn">Continue</button></div>{GB}""")

B = [('First step','Finish a lesson','var(--gr)','var(--gr-e)','shoe-prints-solid' if False else 'seedling-solid',False),
     ('Week strong','7-day streak','var(--or)','var(--or-e)','fire-solid',False),
     ('Scam spotter','Catch 10 scams','var(--rd)','var(--rd-e)','shield-alt-solid',False),
     ('Address pro','Check 5 addresses','var(--sk)','var(--sk-e)','search-solid',False),
     ('Stable hands','Master Unit 1','var(--vi)','var(--vi-e)','dollar-sign-solid',False),
     ('Sandbox start','First practice send','var(--ye)','var(--ye-e)','flask-solid',False),
     ('Month strong','30-day streak','','','fire-solid',True),
     ('Perfect quiz','100% on a unit quiz','','','bullseye-solid',True),
     ('Key keeper','Finish Unit 2','','','key-solid',True)]
cards = ''.join(f'<div class="bdg {"lk" if lk else ""} rise" style="--i:{i//3+1}">{hexb(c,e,icn,lk)}<span>{n}<br><span class="s">{s}</span></span></div>' for i,(n,s,c,e,icn,lk) in enumerate(B))
screen('E2', 'badges', 'Badge collection', 'Six earned, the rest locked',
f"""{sb()}
<div class="lbar"><a class="x" aria-label="Back">{ic("arrow-left-solid")}</a><span class="h3" style="flex:1">Badges</span><span class="chip vi">6 of 12</span></div>
<div class="body" style="padding-top:6px">
  <div class="card rise" style="--i:0;display:flex;align-items:center;gap:14px;padding:12px 14px">
    {hexb('var(--rd)','var(--rd-e)','shield-alt-solid')}
    <div style="flex:1"><div class="cap" style="color:var(--rd)">Next up</div><div class="h3">Scam spotter II</div><div class="sm">Catch 25 scams · 14 / 25</div><div class="bar thin" style="--p:56%;--c:var(--rd);margin-top:8px"><i></i></div></div>
  </div>
  <div class="badges" style="margin-top:20px">{cards}</div>
</div>
{nav('me')}{GB}""")

screen('E3', 'rewards', 'Rewards wallet', 'Points, and the rule for a small stablecoin payout',
f"""{sb()}
<div class="lbar"><span class="h3" style="flex:1;font-size:20px">Rewards</span><span class="chip">{ic("question-circle")} How it works</span></div>
<div class="body" style="padding-top:2px">
  <div class="rise" style="--i:0;border-radius:22px;background:var(--sk);box-shadow:0 6px 0 var(--sk-e);color:#fff;padding:18px">
    <div class="row" style="justify-content:space-between"><span class="cap" style="color:rgba(255,255,255,.85)">Your points</span><span style="font-size:28px">{ic("gem-solid")}</span></div>
    <div style="font-size:44px;font-weight:1000;line-height:1.05;margin-top:4px"><span data-count="1240">1,240</span></div>
    <div style="font-size:14px;font-weight:800;opacity:.9;margin-top:4px">Points come from mastering lessons, not from speed.</div>
  </div>
  <div class="card rise" style="--i:1;margin-top:16px;padding:14px 16px">
    <div class="row" style="justify-content:space-between"><span class="h3">Payout rule</span><span class="tag-ex">Example</span></div>
    <div class="row" style="gap:10px;margin-top:10px;font-size:17px;font-weight:900"><span class="chip sk" style="height:36px;font-size:15px">{ic("gem-solid")} 1,000 pts</span>{ic("arrow-right-solid","c-vi")}<span class="chip gr" style="height:36px;font-size:15px">{ic("dollar-sign-solid")} 1 USDC</span></div>
    <div class="sm" style="margin-top:10px;color:var(--ink)">Unlocked when you pass a unit's re-check 3 days later. Up to 5 USDC a month.</div>
  </div>
  <div class="card rise" style="--i:2;margin-top:12px;padding:12px 14px;display:flex;align-items:center;gap:12px">
    {ring(0.66,48,'var(--vi)',ic("lock-solid"),6)}
    <div style="flex:1"><div class="t" style="font-size:15px;font-weight:900">Unit 1 payout</div><div class="sm">Day 2 of 3 · re-check opens Fri, Oct 16</div></div>
  </div>
  <p class="sm rise" style="--i:3;margin-top:14px">{ic("info-circle-solid","c-vi")} Rewards are paid from Ona's learning budget, never from other learners. Ona has no buy or invest button.</p>
</div>
<div class="foot"><button class="btn off">Convert after re-check</button></div>
{nav('rewards')}{GB}""")

# =========================== F. RE-ENGAGEMENT ===========================
screen('F1', 'streak-at-risk', 'Streak at risk: notification and widget', 'Lock screen with a gentle evening nudge',
f"""<div class="sb"><span>20:41</span><span class="ic">{ic("signal-solid")}{ic("wifi-solid")}{ic("battery-full-solid")}</span></div>
<div class="body" style="padding-top:0">
  <div class="clock">20:41</div>
  <div class="date">Tuesday, October 13</div>
  <div class="notif rise" style="--i:2;margin-top:34px">
    <div class="ap"><span class="appic">o</span>Ona · now</div>
    <div class="row" style="align-items:flex-start;margin-top:8px;gap:12px">
      <div style="flex:1"><div style="font-size:16px;font-weight:900">Your 12-day streak ends at midnight</div><div class="sm" style="margin-top:3px;font-size:14px">One 3-minute lesson keeps it going. You're on lesson 3 of Stablecoins 101.</div></div>
      {mascot('worried',56)}
    </div>
    <div class="row" style="gap:10px;margin-top:12px"><span class="chip vi" style="height:34px">Start lesson</span><span class="chip" style="height:34px">Remind me at 22:00</span></div>
  </div>
  <div class="row rise" style="--i:3;gap:14px;margin-top:16px;align-items:stretch">
    <div class="widget">
      <div class="row" style="justify-content:space-between"><span class="appic">o</span><span class="cap" style="color:var(--or)">At risk</span></div>
      <div class="row" style="gap:4px;margin-top:10px"><span class="flick" style="display:flex">{flame(38)}</span><span style="font-size:40px;font-weight:1000">12</span></div>
      <div class="sm" style="margin-top:2px">Today's lesson isn't done yet</div>
    </div>
    <div class="widget" style="flex:1;display:flex;flex-direction:column;justify-content:space-between">
      <div class="cap">Daily goal</div>
      {ring(0.1,74,'var(--gr)','<span style="font-size:15px;font-weight:900;color:var(--ink)">5/50</span>',9)}
      <div class="sm">XP today</div>
    </div>
  </div>
  <div class="grow"></div>
  <div class="row" style="justify-content:space-between;padding:0 30px 10px;font-size:26px;opacity:.9">{ic("mobile-alt-solid")}<span style="font-size:13px;font-weight:800;opacity:.8">Swipe up to unlock</span>{ic("lock-solid")}</div>
</div>{GB}""", cls='lock dark')

screen('F2', 'streak-freeze', 'Streak freeze and repair', 'A missed day, covered. Repair by learning, not paying',
f"""{sb()}
<div class="body center" style="align-items:center;padding-top:34px">
  <div class="popin" style="--d:60ms;position:relative;width:150px;height:150px;border-radius:40px;background:var(--sk-t);display:flex;align-items:center;justify-content:center">
    <span style="font-size:96px;color:var(--sk);display:flex">{ic("snowflake-solid")}</span>
    <span style="position:absolute;right:-12px;bottom:-10px;width:62px;height:62px;border-radius:50%;background:var(--or);color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center;border:5px solid #fff">{ic("fire-solid")}</span>
  </div>
  <h1 class="h1 rise" style="--i:2;margin-top:26px">Your streak is safe</h1>
  <p class="p rise" style="--i:3;margin-top:8px;max-width:310px">You missed yesterday, so a streak freeze kept your 12-day streak going.</p>
  <div class="card rise" style="--i:4;width:100%;margin-top:22px">
    <div class="week">{day('W','on')}{day('T','on')}{day('F','on')}{day('S','on')}{day('S','on')}{day('M','frz','snowflake-solid')}{day('T','today')}</div>
    <div class="row" style="justify-content:space-between;margin-top:14px;padding-top:12px;border-top:2px solid var(--line)"><span class="sm" style="color:var(--ink)">Freezes left</span><span style="display:flex;gap:4px;font-size:22px;color:var(--sk)">{ic("snowflake-solid")}<span style="color:var(--line2)">{ic("snowflake-solid")}</span></span></div>
  </div>
  <div class="card rise" style="--i:5;width:100%;margin-top:12px;text-align:left;display:flex;gap:12px;align-items:flex-start;padding:12px 14px;background:var(--soft)">
    <span style="font-size:24px;color:var(--vi)">{ic("wrench-solid")}</span>
    <div><div class="t" style="font-size:15px;font-weight:900">No freeze next time?</div><div class="sm">Repair a broken streak within 2 days by finishing 2 extra lessons. No payment, ever.</div></div>
  </div>
</div>
<div class="foot"><button class="btn">Keep my streak going</button></div>{GB}""")

# =========================== INDEX ===========================
FLOWS = [('A', 'Onboarding'), ('B', 'Home'), ('C', 'Lesson loop'), ('D', 'Practice sandbox'), ('E', 'Rewards and progression'), ('F', 'Re-engagement')]
sections = []
for L, title in FLOWS:
    items = [s for s in SCREENS if s[0].startswith(L)]
    cards = ''.join(f'<a class="th" href="/s/{slug}/"><div class="fr"><iframe src="/s/{slug}/" title="{code} {name}" loading="lazy" tabindex="-1"></iframe></div>'
                    f'<div class="nm">{code} · {name}<small>{note}</small></div></a>' for code, slug, name, note in items)
    sections.append(f'<h2><span>{L}</span>{title} <small class="sm" style="font-size:14px">{len(items)} screens</small></h2><div class="ixg">{cards}</div>')
index = (head(vp='width=device-width, initial-scale=1', title='Ona · Learn crypto five minutes a day · Demo build by Olayemi', v=V) + f"""
<body><div class="ix">
<header><div><div class="wm">ona</div><h1 class="h1" style="margin-top:14px;max-width:640px">Learn crypto five minutes a day, and learn to spot a scam before it finds you.</h1>
<p class="lbl" style="margin-top:12px">Demo build · Self-initiated · Designed by Olayemi</p></div></header>
<p class="note">An Android-first learning app for crypto beginners, with one full unit, Stablecoins 101, designed end to end.</p>
{''.join(sections)}
<footer>Demo build · Self-initiated project · Designed by Olayemi. Not financial advice.</footer>
</div><script src="/assets/ona.js?v={V}" defer></script></body></html>
""")
open(os.path.join(SITE, 'index.html'), 'w').write(index)
open(os.path.join(SITE, 'assets', 'favicon.svg'), 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#6C4CF5"/><text x="32" y="44" text-anchor="middle" font-family="Nunito,Arial,sans-serif" font-weight="900" font-size="36" fill="#fff">o</text></svg>')
open(os.path.join(HERE, '..', 'screens.txt'), 'w').write('\n'.join(f'{c}\t{s}\t{n}' for c, s, n, _ in SCREENS) + '\n')
print(len(SCREENS), 'screens;', len(USED), 'icons used')
open(os.path.join(HERE, 'icons_used.txt'), 'w').write('\n'.join(sorted(USED)))
