import os,html
R=os.path.dirname(os.path.abspath(__file__))+'/apercu'
HUB='https://pascalb2211-crypto.github.io/voyages-thaimalin/'
AVIS='https://www.thaimalin.fr/guide-premium/avis-voyageurs-thai-malin'
SITE='https://www.thaimalin.fr'
G=[
 dict(slug='thailande',capr='Comment y aller depuis La Réunion',capa='Comment y aller depuis la France et l’Europe',name='Mini-guide Thaïlande',short='Thaïlande',emoji='🌴',price='4,99 €',n=24,
  tag="Bangkok, Chiang Mai, les îles — l’essentiel pour bien partir",
  buy='https://buy.stripe.com/eVq3cw3PD7rL8O9eeB97G03',
  caps=['Comment y aller : vols et itinéraires','Itinéraires conseillés','Les erreurs à éviter'],
  inside=['Avant de partir et formalités','Comment aller en Thaïlande','Parler thaï au quotidien','Où aller, itinéraires de 7 à 30 jours','Se déplacer, se loger, manger','Culture et traditions','Excursions et activités','Numéros utiles et SOS']),
 dict(slug='vietnam',capr='Comment aller au Vietnam depuis La Réunion',capa='Comment y aller depuis la France et l’Europe',name='Mini-guide Vietnam',short='Vietnam',emoji='🌿',price='4,99 €',n=26,
  tag="Hanoï, Hội An, Saïgon — nature, culture et évasion",
  buy='https://buy.stripe.com/5kQ6oI1Hv7rL6G16M997G08',
  caps=['Comment aller au Vietnam','Itinéraire type','Hội An, la ville aux lanternes'],
  inside=['Hanoï, Baie d’Ha Long, Ninh Binh, Sapa','Huế, Hội An, Nha Trang, Da Nang','Hô Chi Minh-Ville et delta du Mékong','Phú Quốc et Côn Đảo','Gastronomie vietnamienne','Shopping et souvenirs','Kit de départ et centre de réservation']),
 dict(slug='laos',capr='Comment aller au Laos depuis La Réunion',capa='Comment y aller depuis la France et l’Europe',name='Mini-guide Laos',short='Laos',emoji='🐘',price='6,99 €',n=27,
  tag="Luang Prabang, Vientiane, le royaume du Mékong",
  buy='https://buy.stripe.com/dRm5kE5XLbI12pLdax97G09',
  caps=['Comment aller au Laos','Luang Prabang','Quel itinéraire choisir ?'],
  inside=['Luang Prabang, Vang Vieng, Vientiane','Nord, Sud-Est, Sud, plateau des Bolovens','Les 4 000 îles','Manger, boire et sortir','Budget, internet et eSIM','Quand partir, quoi mettre dans son sac','Itinéraires de 5 à 12 jours']),
 dict(slug='cambodge',capr='De La Réunion au Cambodge',capa='Comment y aller depuis la France et l’Europe',name='Mini-guide Cambodge',short='Cambodge',emoji='🛕',price='6,99 €',n=26,
  tag="Angkor, Phnom Penh, plages et rencontres authentiques",
  buy='https://buy.stripe.com/cNidRa4THcM59Sd0nL97G0a',
  caps=['Comment aller au Cambodge','Siem Reap et les temples d’Angkor','Itinéraires conseillés'],
  inside=['Visa, e-visa et formalités','Phnom Penh, Siem Reap, Sihanoukville','Kep, Kampot, Battambang, Ratanakiri','Gastronomie et culture','Hébergements, internet et eSIM','Kit de survie en khmer','Centre de réservation']),
 dict(slug='plages',name='Mini-guide Plages de Thaïlande',short='Plages',emoji='🏖️',price='6,99 €',n=24,
  tag="Les plus belles plages, île par île",
  buy='https://buy.stripe.com/5kQ7sMbi58vPc0l1rP97G0b',
  caps=['Andaman ou golfe : quelle côte pour toi ?','Krabi, falaises et plages paradisiaques','Budget et conseils pratiques'],
  inside=['Phuket, Phi Phi, Krabi, Koh Lanta','Koh Samui, Phangan, Tao','Koh Lipe, Koh Yao Noi, autres îles','Snorkeling et plongée','Météo des plages mois par mois','Transports et où dormir par zone','Quiz des plages secrètes']),
]
CSS='''
:root{--bg:#0f1115;--card:#1a1d24;--card2:#222731;--line:#ffffff1a;--tx:#f2f2f2;--mut:#aab0bb;--or:#d35400;--or2:#f0955a}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--tx);font:16px/1.55 "Segoe UI",system-ui,Arial,sans-serif;-webkit-text-size-adjust:100%}
a{color:inherit}img,video{max-width:100%;display:block}
.w{max-width:960px;margin:0 auto;padding:0 18px}
header.top{position:sticky;top:0;z-index:20;background:#0f1115ee;backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.top .w{display:flex;align-items:center;justify-content:space-between;height:54px;gap:10px}
.logo{font-weight:800;letter-spacing:.3px;text-decoration:none}.logo b{color:var(--or2)}
.hubl{font-size:13px;font-weight:700;text-decoration:none;border:1px solid var(--or);color:var(--or2);padding:7px 12px;border-radius:99px;white-space:nowrap}
.btn{display:inline-block;text-decoration:none;font-weight:800;border:0;border-radius:12px;padding:14px 22px;cursor:pointer;font-size:16px;text-align:center}
.btn.pri{background:linear-gradient(135deg,#d35400,#f0955a);color:#fff}
.btn.alt{background:transparent;border:1.5px solid #ffffff40;color:#fff}
.btn.sm{padding:10px 14px;font-size:14px;border-radius:10px}
.hero{padding:44px 0 30px;text-align:center;background:radial-gradient(ellipse at 50% 0,#d3540033,transparent 65%)}
.hero h1{font-size:clamp(28px,6.5vw,44px);line-height:1.15;margin-bottom:14px}.hero h1 em{font-style:normal;color:var(--or2)}
.hero p{color:var(--mut);max-width:560px;margin:0 auto 22px;font-size:17px}
.hero .cta{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.badge{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:var(--or2);border:1px solid #f0955a55;border-radius:99px;padding:4px 12px;margin-bottom:14px}
section{padding:38px 0}
section h2{font-size:clamp(22px,5vw,30px);margin-bottom:6px}
.lead{color:var(--mut);margin-bottom:22px}
.steps{display:grid;gap:12px}
@media(min-width:700px){.steps{grid-template-columns:repeat(3,1fr)}}
.step{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}
.step .n{width:34px;height:34px;border-radius:50%;background:var(--or);display:grid;place-items:center;font-weight:800;margin-bottom:10px}
.step h3{font-size:17px;margin-bottom:4px}.step p{color:var(--mut);font-size:15px}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(270px,1fr))}
.gc{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}
.gc img.cv{width:100%;aspect-ratio:2/3;object-fit:cover;background:#222}
.gc .b{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.gc h3{font-size:18px}.gc .t{color:var(--mut);font-size:14px;flex:1}
.gc .pr{font-weight:800;color:var(--or2)}.gc .ed{font-size:11px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:var(--mut)}
.gc .row{display:flex;gap:8px;margin-top:6px}.gc .row .btn{flex:1}
.shots{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 18px 14px;margin:0 -18px;-webkit-overflow-scrolling:touch}
.shot{flex:0 0 min(62vw,230px);scroll-snap-align:center}
.shot img{border-radius:20px;border:1px solid var(--line);width:100%;aspect-ratio:390/844;object-fit:cover}
.shot p{font-size:14px;margin-top:8px;text-align:center}.shot p b{display:block;color:var(--or2)}
.feat{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:14px}
.feat div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;font-size:15px}.feat b{display:block;margin-bottom:2px}
.vid{max-width:300px;margin:0 auto;border-radius:22px;overflow:hidden;border:1px solid var(--line);background:#000}
.vid video{width:100%}
.two{display:grid;gap:12px}@media(min-width:700px){.two{grid-template-columns:1fr 1fr}}
.box{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}.box h3{margin-bottom:6px}.box ol{padding-left:20px;color:var(--mut);font-size:15px}.box li{margin:4px 0}
details{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:10px}
summary{font-weight:700;cursor:pointer;list-style:none}summary::-webkit-details-marker{display:none}
.faqmain>summary{font-size:22px;font-weight:800;padding:18px 0;border-bottom:1px solid var(--line)}.faqmain[open]>summary{margin-bottom:6px}summary::after{content:"+";float:right;color:var(--or2);font-size:20px;line-height:1}details[open] summary::after{content:"–"}
details p{color:var(--mut);margin-top:8px;font-size:15px}
.mail{background:linear-gradient(135deg,#d3540022,#1a1d24);border:1px solid #d3540055;border-radius:18px;padding:20px;text-align:center}
.mail form{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.mail input[type=email]{flex:1 1 200px;padding:13px;border-radius:10px;border:1px solid #ffffff30;background:#12151b;color:#fff;font-size:16px}
.mail label{font-size:12px;color:var(--mut);display:block;text-align:left;width:100%}
.mail .ok{color:#7be0a0;margin-top:10px;display:none}
footer .fl{margin-top:8px;line-height:1.9}footer{padding:30px 0 50px;color:var(--mut);font-size:14px;text-align:center;border-top:1px solid var(--line)}footer a{color:var(--or2)}
/* page guide */
.gh{display:flex;gap:16px;align-items:flex-start;padding:26px 0 14px}.gh img{width:104px;border-radius:10px;flex:none}
.gh h1{font-size:clamp(22px,5.5vw,32px);line-height:1.2;margin-bottom:6px}.gh p{color:var(--mut)}
.pv{max-width:560px;margin:0 auto 22px}.pv img{width:100%;border-radius:10px;border:1px solid var(--line);background:#222}
.pv .cap{display:flex;justify-content:space-between;font-size:14px;color:var(--mut);margin-bottom:8px}.pv .cap b{color:var(--tx)}
.lock{max-width:560px;margin:10px auto 0;background:var(--card);border:1px solid #d3540066;border-radius:18px;padding:22px;text-align:center}
.lock h2{font-size:22px}.lock ul{list-style:none;text-align:left;margin:14px auto;max-width:400px}.lock li{padding:5px 0 5px 24px;position:relative;color:var(--mut);font-size:15px}.lock li::before{content:"✓";position:absolute;left:0;color:var(--or2);font-weight:800}
.lock .btn{display:block;margin-top:10px}
.nav2{display:flex;justify-content:space-between;gap:8px;margin:26px 0;font-size:14px}.nav2 a{color:var(--or2);text-decoration:none;font-weight:700}
.sticky{position:sticky;bottom:0;background:#0f1115f2;border-top:1px solid var(--line);padding:10px 0;z-index:15}.sticky .w{display:flex;gap:8px;align-items:center}.sticky .btn{flex:1;padding:12px}.sticky .pp{font-weight:800;color:var(--or2);white-space:nowrap}
'''
def head(title,desc,img,depth):
    p='../'*depth
    return f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{p}{img}"><meta name="theme-color" content="#0f1115"><link rel="icon" href="{p}img/cover-thailande.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="{p}style.css"></head><body>
<header class="top"><div class="w"><a class="logo" href="{p}index.html">THAÏ <b>MALIN</b> · Aperçu</a><a class="hubl" href="{HUB}">J’ai déjà mon code</a></div></header>'''
foot=f'''<footer><div class="w"><p><b>© Thaï Malin</b> · Édition 2026</p><p class="fl"><a href="{SITE}">thaimalin.fr</a> · <a href="%sinfos.html">Infos pratiques</a> · <a href="{SITE}/contact">Contact</a> · <a href="{AVIS}">Avis voyageurs</a></p><p class="fl"><a href="{SITE}/mentions-legales">Mentions légales</a> · <a href="{SITE}/informations-legales/politique-de-confidentialite">Confidentialité</a> · <a href="{SITE}/cgu">CGU</a> · <a href="{SITE}/cgv">CGV</a></p></div></footer>
<script src="%sconfig.js"></script><script src="%sapp.js"></script></body></html>'''

LB=r'''
.pv img{cursor:zoom-in}
.lb{position:fixed;inset:0;background:#000e;z-index:100;display:none;flex-direction:column}
.lb.on{display:flex}
.lb .bar{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;color:#fff;font:700 14px Poppins,sans-serif;background:#000}
.lb .bar button{background:#ffffff22;color:#fff;border:0;border-radius:10px;font:700 15px Poppins,sans-serif;padding:8px 14px}
.lb .sc{flex:1;overflow:auto;-webkit-overflow-scrolling:touch;touch-action:pan-x pan-y pinch-zoom}
.lb img{display:block;width:100%;max-width:none;margin:0 auto}
.lb.z img{width:230%}
'''
EXTRA=r'''
.menusec{padding:7px 0}
.menu{padding:0;border-radius:18px;background:linear-gradient(145deg,var(--card2),var(--card));border:1px solid var(--line);box-shadow:0 6px 18px #0004;margin:0}
.menu>summary{display:flex;align-items:center;gap:14px;padding:15px 16px}
.menu>summary i{font-style:normal;flex:none;width:46px;height:46px;border-radius:14px;background:#d3540026;border:1px solid #d3540044;display:grid;place-items:center;font-size:23px}
.menu>summary span{display:block;font-size:17px;font-weight:800;line-height:1.25}
.menu>summary small{display:block;font-weight:500;color:var(--mut);font-size:13px;margin-top:2px}
.menu>summary::after,.menu[open]>summary::after{content:"";float:none;margin-left:auto;flex:none;width:9px;height:9px;border-right:2px solid var(--or2);border-bottom:2px solid var(--or2);transform:rotate(45deg);transition:transform .2s;font-size:0;margin-right:4px}
.menu[open]>summary::after{transform:rotate(-135deg);margin-top:6px}
.menu .mb{padding:14px 16px 18px;border-top:1px solid var(--line)}
.menu .mb details{background:#14171d}
.tabbar{position:fixed;left:0;right:0;bottom:0;z-index:30;display:flex;background:#0f1115f2;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-top:1px solid var(--line);padding:6px 4px calc(6px + env(safe-area-inset-bottom))}
.tabbar a{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;padding:5px 2px;border-radius:12px;color:var(--mut);text-decoration:none;font-size:11px;font-weight:600;line-height:1.1;text-align:center}
.tabbar a i{font-style:normal;font-size:20px;line-height:1.1;filter:grayscale(.6);opacity:.85}
.tabbar a.on{color:var(--or2);background:#d3540018}.tabbar a.on i{filter:none;opacity:1}
body.hastab{padding-bottom:84px}
html{scroll-behavior:smooth}

h1,h2,h3,.logo,.btn{font-family:Poppins,"Segoe UI",system-ui,sans-serif}
.hero{padding:30px 0 34px;text-align:center;background:radial-gradient(ellipse at 50% -10%,#d3540044,transparent 62%)}
.fan{position:relative;height:250px;max-width:340px;margin:6px auto 22px}
.fan img{position:absolute;bottom:0;width:150px;aspect-ratio:2/3;object-fit:cover;border-radius:12px;box-shadow:0 14px 30px #0009;border:2px solid #ffffff22}
.fan img:nth-child(1){left:2%;transform:rotate(-9deg);z-index:1}
.fan img:nth-child(2){left:50%;margin-left:-82px;width:164px;z-index:3;bottom:8px}
.fan img:nth-child(3){right:2%;transform:rotate(9deg);z-index:2}
.chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 20px}
.chips span{font-size:13px;font-weight:700;background:#ffffff12;border:1px solid var(--line);border-radius:99px;padding:6px 12px}
.chips span::before{content:"✓ ";color:var(--or2)}
.alt2{background:#14171d}
.gl{display:flex;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:12px;align-items:stretch}
.gl img{width:104px;flex:none;aspect-ratio:2/3;object-fit:cover;border-radius:10px;box-shadow:0 8px 18px #0008}
.gl .b{flex:1;display:flex;flex-direction:column;gap:4px;min-width:0}
.gl h3{font-size:17px;line-height:1.25}.gl .t{color:var(--mut);font-size:14px;line-height:1.4}
.gl .meta{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:12px;color:var(--mut);font-weight:700}
.gl .meta b{color:var(--or2);font-size:16px}
.gl .row{display:flex;gap:8px;margin-top:auto;padding-top:6px}.gl .row .btn{flex:1;padding:10px 8px;font-size:13.5px}
.list{display:grid;gap:12px}@media(min-width:760px){.list{grid-template-columns:1fr 1fr}}
.why{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.why>div{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px}
.why .i{font-size:26px;margin-bottom:6px}.why b{display:block;font-size:16px;margin-bottom:4px}.why p{color:var(--mut);font-size:14.5px}
.gh2{display:flex;gap:16px;align-items:center;padding:24px 0 8px}.gh2 img{width:128px;flex:none;border-radius:12px;box-shadow:0 12px 26px #000a}
.gh2 h1{font-size:clamp(22px,5.5vw,32px);line-height:1.2;margin-bottom:8px}
.pill{display:inline-block;font-size:12.5px;font-weight:700;background:#ffffff12;border:1px solid var(--line);border-radius:99px;padding:4px 10px;margin:0 6px 6px 0}
.pill.or{color:var(--or2);border-color:#f0955a66}
.pv .cap b{font-family:Poppins,sans-serif}
.pv img{box-shadow:0 12px 28px #0008}
.others{display:flex;gap:10px;overflow-x:auto;padding:4px 0 10px;scroll-snap-type:x mandatory}
.others a{flex:0 0 108px;scroll-snap-align:start;text-decoration:none;font-size:13px;font-weight:700;text-align:center}
.others img{width:100%;aspect-ratio:2/3;object-fit:cover;border-radius:10px;border:1px solid var(--line);margin-bottom:4px}
.lock li{color:#d6dae0}
.three{display:grid;gap:10px;margin:14px 0}.three div{display:flex;gap:10px;align-items:flex-start;text-align:left;font-size:14px;color:var(--mut)}.three b{flex:none;width:26px;height:26px;border-radius:50%;background:var(--or);color:#fff;display:grid;place-items:center;font-size:13px}
.seg{display:flex;gap:6px;margin-bottom:10px}.seg button{flex:1;font:700 13.5px Poppins,sans-serif;color:#fff;background:#ffffff12;border:1px solid var(--line);border-radius:10px;padding:10px 6px;cursor:pointer}.seg button.on{background:var(--or);border-color:var(--or)}
.quote{border-left:3px solid var(--or);padding:4px 0 4px 14px;color:var(--mut);font-size:15px;margin:10px 0}
'''

# ---------- index
fan=''.join(f'<img src="img/cover-{g}.webp" alt="" loading="eager">' for g in ['vietnam','plages','laos'])
cards=''
for g in G:
    cards+=f"""<article class="gl"><img loading="lazy" src="img/cover-{g['slug']}.webp" alt="Couverture {g['name']}"><div class="b"><div class="meta"><span>ÉDITION 2026</span><span>·</span><span>{g['n']} pages</span></div><h3>{g['emoji']} {g['name']}</h3><p class="t">{g['tag']}</p><div class="meta"><b>{g['price']}</b></div><div class="row"><a class="btn alt sm" href="guide/{g['slug']}.html">3 pages gratuites</a><a class="btn pri sm" href="{g['buy']}">Acheter</a></div></div></article>"""
shots=[('0-guides','Mes guides','Tous tes guides au même endroit'),('1-dates','Tes dates','Compte à rebours jusqu’au départ'),('2-vol','Ton vol','Rappels créés automatiquement'),('3-programme','Ton programme','Jour par jour, avec adresses et horaires'),('4-documents','Tes documents','Billets et réservations, même sans internet'),('5-checklist','Ta checklist','À cocher avant de partir'),('6-convertisseur','Convertisseur','Euros en monnaie locale, hors ligne')]
sh=''.join(f'<div class="shot"><img loading="lazy" src="img/shots/{f}.jpg" alt="{t}"><p><b>{t}</b>{d}</p></div>' for f,t,d in shots)
idx=head('Thaï Malin · Mini-guides de voyage en Asie, aperçu gratuit','Feuillette 3 pages gratuites de chaque mini-guide Thaï Malin (Thaïlande, Vietnam, Laos, Cambodge, Plages) et découvre le hub « Mon voyage ».','img/cover-thailande.webp',0)+f"""
<main>
<div class="hero"><div class="w"><div class="fan">{fan}</div>
<span class="badge">Édition 2026 · Guides de voyage en Asie</span>
<h1>Prépare ton voyage en Asie, <em>sans stress</em></h1>
<p>Des mini-guides clairs à lire sur ton téléphone, et une appli pour ranger tout ton voyage. Feuillette 3 pages gratuites de chaque guide avant d’acheter.</p>
<div class="chips"><span>5 guides</span><span>3 pages gratuites chacun</span><span>Marche hors ligne</span></div>
<div class="cta"><a class="btn pri" href="#guides">Voir les aperçus gratuits</a><a class="btn alt" href="{HUB}">J’ai déjà mon code</a></div></div></div>

<section id="guides"><div class="w"><h2>Choisis ton guide</h2><p class="lead">Touche « 3 pages gratuites » pour feuilleter avant d’acheter.</p><div class="list">{cards}</div></div></section>

<section class="alt2" id="video"><div class="w"><h2>Regarde l’appli en action</h2><p class="lead">Quelqu’un entre son code, ses dates, son vol, son programme… jusqu’au mode hors ligne.</p>
<div class="vid"><video controls playsinline preload="none" poster="video/poster.jpg" src="video/demo-hub.mp4"></video></div></div></section>

<section id="pourquoi" class="menusec"><div class="w"><details class="menu"><summary><i>✨</i><span>Pourquoi Thaï Malin ?<small>Des guides pensés pour partir l’esprit tranquille</small></span></summary><div class="mb">
<div class="why">
<div><div class="i">🗺️</div><b>Clair et visuel</b><p>Une page = un sujet : itinéraires, budget, culture, bons plans, avec des infographies faciles à lire.</p></div>
<div><div class="i">✈️</div><b>Comment y aller</b><p>Les vols, les escales, les formalités et le budget, pour un départ de La Réunion comme de France.</p></div>
<div><div class="i">📱</div><b>Dans ta poche</b><p>Tout s’ouvre sur ton téléphone, et reste disponible sans internet, même en plein voyage.</p></div>
<div><div class="i">🌺</div><b>Créé à La Réunion</b><p>Des conseils concrets, écrits par quelqu’un qui prépare ces voyages, pour tous ceux qui rêvent d’Asie.</p></div>
</div>
</div></details></div></section>

<section class="alt2" id="comment"><div class="w"><h2>Comment ça marche ?</h2><p class="lead">Trois étapes, tout se passe sur ton téléphone.</p>
<div class="steps">
<div class="step"><div class="n">1</div><h3>Choisis ton guide</h3><p>Feuillette 3 pages gratuites de chaque guide pour voir si le style et le contenu te conviennent.</p></div>
<div class="step"><div class="n">2</div><h3>Reçois ton code</h3><p>Après le paiement sécurisé Stripe, ton code d’accès arrive automatiquement par e-mail.</p></div>
<div class="step"><div class="n">3</div><h3>Ouvre « Mon voyage »</h3><p>Entre ton code, installe l’appli sur ton écran d’accueil : ton guide et ton voyage restent disponibles hors ligne.</p></div>
</div></div></section>

<section id="hub" class="menusec"><div class="w"><details class="menu"><summary><i>📱</i><span>« Mon voyage »<small>Ton compagnon de départ, inclus avec ton achat</small></span></summary><div class="mb"><p class="lead">Une appli web incluse avec ton achat, qui range tout ton voyage au même endroit. Fais défiler :</p>
<div class="shots">{sh}</div>
<div class="feat">
<div><b>📅 Dates et compte à rebours</b>Tu indiques ton départ et ton retour, l’appli compte les jours.</div>
<div><b>✈️ Vol et rappels</b>Numéro de vol, horaires : les rappels (enregistrement, formalités, départ, retour) se créent tout seuls et s’exportent vers ton agenda.</div>
<div><b>🗓️ Programme jour par jour</b>Ajoute activités, adresses et horaires, avec un lien Maps.</div>
<div><b>📄 Documents hors ligne</b>Billets, réservations, assurance : enregistrés sur ton téléphone, lisibles sans internet.</div>
<div><b>✅ Checklist de départ</b>13 points à cocher avant de partir.</div>
<div><b>💱 Convertisseur</b>Euros en monnaie locale, avec un taux modifiable.</div>
<div><b>📚 Tous tes guides</b>Tes mini-guides s’ouvrent depuis la même appli.</div>
<div><b>💾 Sauvegarde</b>Exporte et restaure ton voyage, ou commence-en un nouveau.</div>
</div></div></details></div></section>

<section class="alt2" id="install"><div class="w"><h2>Installer sur ton téléphone</h2><p class="lead">Facultatif, mais pratique : l’appli s’ouvre comme une vraie appli et marche hors ligne.</p>
<div class="two"><div class="box"><h3>🍎 iPhone (Safari)</h3><ol><li>Ouvre le lien du hub dans Safari.</li><li>Touche le bouton Partager.</li><li>Choisis « Sur l’écran d’accueil ».</li></ol></div>
<div class="box"><h3>🤖 Android (Chrome)</h3><ol><li>Ouvre le lien du hub dans Chrome.</li><li>Touche le menu ⋮.</li><li>Choisis « Installer l’application » ou « Ajouter à l’écran d’accueil ».</li></ol></div></div></div></section>

<section id="faq" class="menusec"><div class="w"><details class="menu"><summary><i>❓</i><span>Questions fréquentes<small>Code, paiement, accès, hors-ligne</small></span></summary><div class="mb">
<details><summary>Comment je reçois mon code ?</summary><p>Juste après le paiement, un e-mail automatique t’envoie ton code et le lien d’accès. Pense à regarder tes courriers indésirables.</p></details>
<details><summary>Combien de temps le code est-il valable ?</summary><p>Une fois entré sur ton téléphone, l’accès reste ouvert 12 mois sur cet appareil (Édition 2026).</p></details>
<details><summary>Ça marche sans internet ?</summary><p>Oui, une fois le guide ouvert et l’appli installée, tu peux consulter ton programme, tes documents et ta checklist hors ligne. La météo en direct et les liens demandent une connexion.</p></details>
<details><summary>Le paiement est-il sécurisé ?</summary><p>Le paiement passe par Stripe, qui gère la carte bancaire (Apple Pay et Google Pay selon ton téléphone). Thaï Malin ne voit jamais ton numéro de carte.</p></details>
<details><summary>Qu’est-ce que « Édition 2026 » ?</summary><p>Les guides sont mis à jour par édition. Ton achat te donne l’édition en cours ; une nouvelle édition sera annoncée sur thaimalin.fr.</p></details>
<details><summary>Mes données de voyage sont-elles envoyées quelque part ?</summary><p>Non. Tes dates, ton vol, ton programme et tes documents restent enregistrés uniquement sur ton téléphone.</p></details>
</div></details></div></section>

<section id="news" class="mailsec" hidden><div class="w"><div class="mail"><h2>Être prévenu des nouveaux guides</h2><p class="lead" style="margin-bottom:0">Facultatif : un e-mail seulement quand un nouveau guide sort. Tu peux continuer à lire les aperçus sans rien remplir.</p>
<form id="mailForm"><input type="email" id="mailIn" placeholder="ton@email.com" required autocomplete="email"><button class="btn pri" type="submit">Me prévenir</button>
<label><input type="checkbox" id="mailOk" required> J’accepte de recevoir un e-mail à chaque nouveau guide. Désinscription possible à tout moment.</label></form><p class="ok" id="mailDone">Merci ! Tu seras prévenu(e).</p></div></div></section>
<nav class="tabbar" aria-label="Navigation"><a href="#guides" data-t="guides"><i>📚</i>Guides</a><a href="#video" data-t="video"><i>▶️</i>Vidéo</a><a href="#pourquoi" data-t="pourquoi"><i>✨</i>Pourquoi</a><a href="#hub" data-t="hub"><i>📱</i>Mon voyage</a><a href="#faq" data-t="faq"><i>❓</i>FAQ</a></nav>
</main>"""+foot%('','','')
open(R+'/index.html','w',encoding='utf-8').write(idx)

# ---------- guide pages
for i,g in enumerate(G):
    prev=G[i-1];nxt=G[(i+1)%len(G)]
    def _pv(k):
        if k==0 and g.get('capr'):
            return f'<div class="pv" id="pv1"><div class="seg" role="tablist"><button type="button" data-from="r" class="on">🌺 Je pars de La Réunion</button><button type="button" data-from="a">🇪🇺 Je pars d’Europe</button></div><div class="cap"><b id="pv1cap" data-r="{html.escape(g["capr"])}" data-a="{html.escape(g["capa"])}">{html.escape(g["capr"])}</b><span>Aperçu 1/3</span></div><img id="pv1img" data-r="../img/p/{g["slug"]}-1r.webp" data-a="../img/p/{g["slug"]}-1a.webp" src="../img/p/{g["slug"]}-1r.webp" alt="{html.escape(g["capr"])}"></div>'
        return f'<div class="pv"><div class="cap"><b>{g["caps"][k]}</b><span>Aperçu {k+1}/3</span></div><img loading="{"eager" if k==0 else "lazy"}" src="../img/p/{g["slug"]}-{k+1}.webp" alt="{html.escape(g["caps"][k])}"></div>'
    pv=''.join(_pv(k) for k in range(3))
    li=''.join(f'<li>{x}</li>' for x in g['inside'])
    oth=''.join(f'<a href="{o["slug"]}.html"><img loading="lazy" src="../img/cover-{o["slug"]}.webp" alt="">{o["short"]}</a>' for o in G if o['slug']!=g['slug'])
    page=head(f'{g["name"]} · aperçu gratuit · Thaï Malin',f'3 pages gratuites du {g["name"]} (édition 2026) : {g["tag"]}.',f'img/cover-{g["slug"]}.webp',1)+f"""
<main class="w"><div class="gh2"><img src="../img/cover-{g['slug']}.webp" alt="Couverture {g['name']}"><div><h1>{g['emoji']} {g['name']}</h1><span class="pill or">Édition 2026</span><span class="pill">{g['n']} pages</span><span class="pill">{g['price']}</span><p style="color:var(--mut);font-size:15px;margin-top:4px">{g['tag']}</p></div></div>
<p class="quote">Voici 3 pages du guide, en entier et gratuites. Choisis d’où tu pars, et touche une page pour l’agrandir.</p>
{pv}
<div class="lock"><h2>Il reste {g['n']-3} pages à découvrir</h2><p style="color:var(--mut)">Dans le guide complet :</p><ul>{li}</ul>
<div class="three"><div><b>1</b>Tu paies en ligne, de façon sécurisée (Stripe).</div><div><b>2</b>Tu reçois ton code par e-mail, tout de suite.</div><div><b>3</b>Tu ouvres le guide sur ton téléphone, même hors ligne.</div></div>
<a class="btn pri" href="{g['buy']}">Acheter le guide · {g['price']}</a>
<a class="btn alt" href="{HUB}">J’ai déjà mon code</a></div>
<h2 style="font-size:18px;margin:26px 0 8px">Les autres guides</h2><div class="others">{oth}</div>
<div class="nav2"><a href="{prev['slug']}.html">← {prev['short']}</a><a href="../index.html#guides">Tous les guides</a><a href="{nxt['slug']}.html">{nxt['short']} →</a></div></main>
<div class="sticky"><div class="w"><span class="pp">{g['price']}</span><a class="btn pri" href="{g['buy']}">Acheter ce guide</a></div></div>"""+foot%('../','../','../')
    open(R+f'/guide/{g["slug"]}.html','w',encoding='utf-8').write(page)


# ---------- page infos
infos=head('Infos pratiques et contact · Thaï Malin','Comment recevoir ton code, durée d’accès, paiement sécurisé et contact Thaï Malin.','img/cover-thailande.webp',0)+f"""
<main class="w" style="padding:28px 0 10px"><h1 style="font-size:28px;margin-bottom:6px">Infos pratiques et contact</h1><p class="lead">Tout ce qu’il faut savoir avant et après l’achat.</p>
<div class="why" style="grid-template-columns:1fr">
<div><b>🔑 Recevoir mon code</b><p>Juste après le paiement, un e-mail automatique t’envoie ton code d’accès et le lien du guide. Regarde aussi tes courriers indésirables.</p></div>
<div><b>📱 Utiliser mon guide</b><p>Le guide s’ouvre dans ton navigateur et peut s’installer sur l’écran d’accueil. Une fois ouvert, il marche aussi sans connexion.</p></div>
<div><b>⏳ Durée de l’accès</b><p>Une fois ton code entré sur un téléphone, l’accès reste ouvert 12 mois sur cet appareil (Édition 2026). Le code est valable le mois de l’achat et le mois suivant.</p></div>
<div><b>💳 Paiement</b><p>Le paiement est géré par Stripe (carte bancaire, et Apple Pay ou Google Pay selon ton téléphone). Thaï Malin ne voit jamais ton numéro de carte.</p></div>
<div><b>✉️ Une question, un problème de code ?</b><p>Écris à <a href="mailto:contact@thaimalin.fr" style="color:var(--or2)">contact@thaimalin.fr</a> en indiquant le guide acheté et l’adresse e-mail utilisée pour le paiement.</p></div>
</div>
<p style="margin:22px 0"><a class="btn pri" href="index.html#guides">Voir les guides</a></p></main>"""+foot%('','','')
open(R+'/infos.html','w',encoding='utf-8').write(infos)

open(R+'/style.css','w').write(CSS+EXTRA+LB)
open(R+'/config.js','w').write('''// Inscription e-mail facultative (nouveaux guides). Laisser vide = le formulaire reste caché.
// Pour l'activer : renseigner l'adresse Supabase et la clé publique (anon), table "newsletter" (colonnes : email, created_at, source).
window.APERCU={SUPABASE_URL:"",SUPABASE_ANON_KEY:""};
''')
open(R+'/app.js','w').write('''(function(){
var tb=document.querySelector('.tabbar');
if(tb){document.body.classList.add('hastab');
 var tabs=[].slice.call(tb.querySelectorAll('a'));
 tabs.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
  var el=document.getElementById(a.getAttribute('data-t'));if(!el)return;
  var d=el.querySelector('details.menu');if(d)d.open=true;
  window.scrollTo({top:el.getBoundingClientRect().top+window.pageYOffset-60,behavior:'smooth'});})});
 function spy(){var cur=tabs[0];tabs.forEach(function(a){var el=document.getElementById(a.getAttribute('data-t'));if(el&&el.getBoundingClientRect().top<=window.innerHeight*0.5)cur=a});
  if(window.innerHeight+window.pageYOffset>=document.documentElement.scrollHeight-4)cur=tabs[tabs.length-1];
  tabs.forEach(function(a){a.classList.toggle('on',a===cur)})}
 window.addEventListener('scroll',spy,{passive:true});spy();}
var seg=document.querySelector('.seg');
if(seg){var img=document.getElementById('pv1img'),cap=document.getElementById('pv1cap'),bt=seg.querySelectorAll('button');
 function set(k){bt.forEach(function(b){b.classList.toggle('on',b.getAttribute('data-from')===k)});img.src=img.getAttribute('data-'+k);cap.textContent=cap.getAttribute('data-'+k);img.alt=cap.textContent;try{localStorage.setItem('tm-from',k)}catch(e){}}
 bt.forEach(function(b){b.addEventListener('click',function(){set(b.getAttribute('data-from'))})});
 var s='r';try{s=localStorage.getItem('tm-from')||'r'}catch(e){} if(s==='a')set('a');}
var pvs=document.querySelectorAll('.pv img');
if(pvs.length){var lb=document.createElement('div');lb.className='lb';lb.innerHTML='<div class="bar"><span>Touche l’image pour zoomer</span><button type="button">Fermer ✕</button></div><div class="sc"><img alt=""></div>';document.body.appendChild(lb);
 var li=lb.querySelector('img'),bx=lb.querySelector('button'),sc=lb.querySelector('.sc');
 function close(){lb.classList.remove('on','z');document.body.style.overflow=''}
 pvs.forEach(function(im){im.addEventListener('click',function(){li.src=im.src;li.alt=im.alt;lb.classList.remove('z');sc.scrollTop=0;sc.scrollLeft=0;lb.classList.add('on');document.body.style.overflow='hidden'})});
 li.addEventListener('click',function(){lb.classList.toggle('z');if(!lb.classList.contains('z')){sc.scrollLeft=0}});
 bx.addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});}
var c=window.APERCU||{},sec=document.getElementById('news');
if(!sec||!c.SUPABASE_URL||!c.SUPABASE_ANON_KEY)return;
sec.hidden=false;
var f=document.getElementById('mailForm');
f.addEventListener('submit',function(e){e.preventDefault();
 var em=document.getElementById('mailIn').value.trim();if(!em)return;
 fetch(c.SUPABASE_URL+'/rest/v1/newsletter',{method:'POST',headers:{'apikey':c.SUPABASE_ANON_KEY,'Authorization':'Bearer '+c.SUPABASE_ANON_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify({email:em,source:'apercu'})})
 .then(function(r){if(r.ok||r.status===409){f.style.display='none';document.getElementById('mailDone').style.display='block'}else{alert("Oups, l'inscription n'a pas fonctionné. Réessaie plus tard.")}})
 .catch(function(){alert("Oups, pas de connexion.")});});
})();
''')
open(R+'/.nojekyll','w').write('')
print('built')
