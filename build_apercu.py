import os,html
R=os.path.dirname(os.path.abspath(__file__))+'/apercu'
HUB='https://pascalb2211-crypto.github.io/voyages-thaimalin/'
AVIS='https://www.thaimalin.fr/guide-premium/avis-voyageurs-thai-malin'
SITE='https://www.thaimalin.fr'
G=[
 dict(slug='thailande',name='Mini-guide Thaïlande',short='Thaïlande',emoji='🌴',price='4,99 €',n=23,
  tag="Bangkok, Chiang Mai, les îles — pensé pour les Réunionnais",
  buy='https://buy.stripe.com/eVq3cw3PD7rL8O9eeB97G03',
  caps=['Comment y aller depuis La Réunion','Itinéraires conseillés','Les erreurs à éviter'],
  inside=['Avant de partir et formalités','Comment aller en Thaïlande','Parler thaï au quotidien','Où aller, itinéraires de 7 à 30 jours','Se déplacer, se loger, manger','Culture et traditions','Excursions et activités','Numéros utiles et SOS']),
 dict(slug='vietnam',name='Mini-guide Vietnam',short='Vietnam',emoji='🌿',price='4,99 €',n=25,
  tag="Hanoï, Hội An, Saïgon — nature, culture et évasion",
  buy='https://buy.stripe.com/5kQ6oI1Hv7rL6G16M997G08',
  caps=['Comment aller au Vietnam depuis La Réunion','Itinéraire type','Hội An, la ville aux lanternes'],
  inside=['Hanoï, Baie d’Ha Long, Ninh Binh, Sapa','Huế, Hội An, Nha Trang, Da Nang','Hô Chi Minh-Ville et delta du Mékong','Phú Quốc et Côn Đảo','Gastronomie vietnamienne','Shopping et souvenirs','Kit de départ et centre de réservation']),
 dict(slug='laos',name='Mini-guide Laos',short='Laos',emoji='🐘',price='6,99 €',n=26,
  tag="Luang Prabang, Vientiane, le royaume du Mékong",
  buy='https://buy.stripe.com/dRm5kE5XLbI12pLdax97G09',
  caps=['Comment aller au Laos depuis La Réunion','Luang Prabang','Quel itinéraire choisir ?'],
  inside=['Luang Prabang, Vang Vieng, Vientiane','Nord, Sud-Est, Sud, plateau des Bolovens','Les 4 000 îles','Manger, boire et sortir','Budget, internet et eSIM','Quand partir, quoi mettre dans son sac','Itinéraires de 5 à 12 jours']),
 dict(slug='cambodge',name='Mini-guide Cambodge',short='Cambodge',emoji='🛕',price='6,99 €',n=25,
  tag="Angkor, Phnom Penh, plages et rencontres authentiques",
  buy='https://buy.stripe.com/cNidRa4THcM59Sd0nL97G0a',
  caps=['De La Réunion au Cambodge','Siem Reap et les temples d’Angkor','Itinéraires conseillés'],
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
summary::after{content:"+";float:right;color:var(--or2);font-size:20px;line-height:1}details[open] summary::after{content:"–"}
details p{color:var(--mut);margin-top:8px;font-size:15px}
.mail{background:linear-gradient(135deg,#d3540022,#1a1d24);border:1px solid #d3540055;border-radius:18px;padding:20px;text-align:center}
.mail form{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.mail input[type=email]{flex:1 1 200px;padding:13px;border-radius:10px;border:1px solid #ffffff30;background:#12151b;color:#fff;font-size:16px}
.mail label{font-size:12px;color:var(--mut);display:block;text-align:left;width:100%}
.mail .ok{color:#7be0a0;margin-top:10px;display:none}
footer{padding:30px 0 50px;color:var(--mut);font-size:14px;text-align:center;border-top:1px solid var(--line)}footer a{color:var(--or2)}
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
<link rel="stylesheet" href="{p}style.css"></head><body>
<header class="top"><div class="w"><a class="logo" href="{p}index.html">THAÏ <b>MALIN</b> · Aperçu</a><a class="hubl" href="{HUB}">J’ai déjà mon code</a></div></header>'''
foot=f'''<footer><div class="w"><p>© Thaï Malin · <a href="{SITE}">thaimalin.fr</a> · Édition 2026</p><p style="margin-top:6px"><a href="{AVIS}">Avis voyageurs</a></p></div></footer>
<script src="%sconfig.js"></script><script src="%sapp.js"></script></body></html>'''

# ---------- index
cards=''
for g in G:
    cards+=f'''<article class="gc"><img class="cv" loading="lazy" src="img/cover-{g['slug']}.webp" alt="Couverture {g['name']}"><div class="b"><span class="ed">Édition 2026 · {g['n']} pages</span><h3>{g['emoji']} {g['name']}</h3><p class="t">{g['tag']}</p><div class="pr">{g['price']}</div><div class="row"><a class="btn alt sm" href="guide/{g['slug']}.html">Voir 3 pages gratuites</a><a class="btn pri sm" href="{g['buy']}">Acheter</a></div></div></article>'''
shots=[('0-guides','Mes guides','Tous tes guides au même endroit'),('1-dates','Tes dates','Compte à rebours jusqu’au départ'),('2-vol','Ton vol','Rappels créés automatiquement'),('3-programme','Ton programme','Jour par jour, avec adresses et horaires'),('4-documents','Tes documents','Billets et réservations, même sans internet'),('5-checklist','Ta checklist','À cocher avant de partir'),('6-convertisseur','Convertisseur','Euros en monnaie locale, hors ligne')]
sh=''.join(f'<div class="shot"><img loading="lazy" src="img/shots/{f}.jpg" alt="{t}"><p><b>{t}</b>{d}</p></div>' for f,t,d in shots)
idx=head('Thaï Malin · Mini-guides de voyage en Asie, aperçu gratuit','Feuillette 3 pages gratuites de chaque mini-guide Thaï Malin (Thaïlande, Vietnam, Laos, Cambodge, Plages) et découvre le hub « Mon voyage ».','img/cover-thailande.webp',0)+f'''
<main>
<div class="hero"><div class="w"><span class="badge">Édition 2026 · Fait par un Réunionnais</span>
<h1>Prépare ton voyage en Asie, <em>depuis La Réunion</em></h1>
<p>Des mini-guides clairs, des codes par e-mail, et un hub « Mon voyage » pour ranger tes dates, ton vol, ton programme et tes billets. Feuillette 3 pages gratuites de chaque guide avant d’acheter.</p>
<div class="cta"><a class="btn pri" href="#guides">Voir les aperçus gratuits</a><a class="btn alt" href="{HUB}">J’ai déjà mon code</a></div></div></div>

<section id="video"><div class="w"><h2>Regarde l’appli en action</h2><p class="lead">Quelqu’un entre son code, ses dates, son vol, son programme… jusqu’au mode hors ligne.</p>
<div class="vid"><video controls playsinline preload="none" poster="video/poster.jpg" src="video/demo-hub.mp4"></video></div></div></section>

<section id="comment"><div class="w"><h2>Comment ça marche ?</h2><p class="lead">Trois étapes, tout se passe sur ton téléphone.</p>
<div class="steps">
<div class="step"><div class="n">1</div><h3>Choisis ton guide</h3><p>Feuillette 3 pages gratuites de chaque guide pour voir si le style et le contenu te conviennent.</p></div>
<div class="step"><div class="n">2</div><h3>Reçois ton code</h3><p>Après le paiement sécurisé Stripe, ton code d’accès arrive automatiquement par e-mail.</p></div>
<div class="step"><div class="n">3</div><h3>Ouvre « Mon voyage »</h3><p>Entre ton code, installe l’appli sur ton écran d’accueil : ton guide et ton voyage restent disponibles hors ligne.</p></div>
</div></div></section>

<section id="guides"><div class="w"><h2>Les 5 mini-guides</h2><p class="lead">Chaque guide est une édition 2026. Touche « Voir 3 pages gratuites » pour l’aperçu.</p><div class="grid">{cards}</div></div></section>

<section id="hub"><div class="w"><h2>« Mon voyage » : ton compagnon de départ</h2><p class="lead">Une appli web incluse avec ton achat, qui range tout ton voyage au même endroit. Fais défiler :</p></div>
<div class="w"><div class="shots">{sh}</div>
<div class="feat">
<div><b>📅 Dates et compte à rebours</b>Tu indiques ton départ et ton retour, l’appli compte les jours.</div>
<div><b>✈️ Vol et rappels</b>Numéro de vol, horaires : les rappels (enregistrement, formalités, départ, retour) se créent tout seuls et s’exportent vers ton agenda.</div>
<div><b>🗓️ Programme jour par jour</b>Ajoute activités, adresses et horaires, avec un lien Maps.</div>
<div><b>📄 Documents hors ligne</b>Billets, réservations, assurance : enregistrés sur ton téléphone, lisibles sans internet.</div>
<div><b>✅ Checklist de départ</b>13 points à cocher avant de partir.</div>
<div><b>💱 Convertisseur</b>Euros en monnaie locale, avec un taux modifiable.</div>
<div><b>📚 Tous tes guides</b>Tes mini-guides s’ouvrent depuis la même appli.</div>
<div><b>💾 Sauvegarde</b>Exporte et restaure ton voyage, ou commence-en un nouveau.</div>
</div></div></section>



<section id="install"><div class="w"><h2>Installer sur ton téléphone</h2><p class="lead">Facultatif, mais pratique : l’appli s’ouvre comme une vraie appli et marche hors ligne.</p>
<div class="two"><div class="box"><h3>🍎 iPhone (Safari)</h3><ol><li>Ouvre le lien du hub dans Safari.</li><li>Touche le bouton Partager.</li><li>Choisis « Sur l’écran d’accueil ».</li></ol></div>
<div class="box"><h3>🤖 Android (Chrome)</h3><ol><li>Ouvre le lien du hub dans Chrome.</li><li>Touche le menu ⋮.</li><li>Choisis « Installer l’application » ou « Ajouter à l’écran d’accueil ».</li></ol></div></div></div></section>

<section id="faq"><div class="w"><h2>Questions fréquentes</h2><p class="lead"> </p>
<details><summary>Comment je reçois mon code ?</summary><p>Juste après le paiement, un e-mail automatique t’envoie ton code et le lien d’accès. Pense à regarder tes courriers indésirables.</p></details>
<details><summary>Combien de temps le code est-il valable ?</summary><p>Une fois entré sur ton téléphone, l’accès reste ouvert 120 jours sur cet appareil.</p></details>
<details><summary>Ça marche sans internet ?</summary><p>Oui, une fois le guide ouvert et l’appli installée, tu peux consulter ton programme, tes documents et ta checklist hors ligne. La météo en direct et les liens demandent une connexion.</p></details>
<details><summary>Le paiement est-il sécurisé ?</summary><p>Le paiement passe par Stripe, qui gère la carte bancaire (Apple Pay et Google Pay selon ton téléphone). Thaï Malin ne voit jamais ton numéro de carte.</p></details>
<details><summary>Qu’est-ce que « Édition 2026 » ?</summary><p>Les guides sont mis à jour par édition. Ton achat te donne l’édition en cours ; une nouvelle édition sera annoncée sur thaimalin.fr.</p></details>
<details><summary>Mes données de voyage sont-elles envoyées quelque part ?</summary><p>Non. Tes dates, ton vol, ton programme et tes documents restent enregistrés uniquement sur ton téléphone.</p></details>
</div></section>

<section id="news" class="mailsec" hidden><div class="w"><div class="mail"><h2>Être prévenu des nouveaux guides</h2><p class="lead" style="margin-bottom:0">Facultatif : un e-mail seulement quand un nouveau guide sort. Tu peux continuer à lire les aperçus sans rien remplir.</p>
<form id="mailForm"><input type="email" id="mailIn" placeholder="ton@email.com" required autocomplete="email"><button class="btn pri" type="submit">Me prévenir</button>
<label><input type="checkbox" id="mailOk" required> J’accepte de recevoir un e-mail à chaque nouveau guide. Désinscription possible à tout moment.</label></form><p class="ok" id="mailDone">Merci ! Tu seras prévenu(e).</p></div></div></section>
</main>'''+foot%('','')
open(R+'/index.html','w',encoding='utf-8').write(idx)

# ---------- guide pages
for i,g in enumerate(G):
    prev=G[i-1];nxt=G[(i+1)%len(G)]
    pv=''.join(f'<div class="pv"><div class="cap"><b>{g["caps"][k]}</b><span>Aperçu {k+1}/3</span></div><img loading="{"eager" if k==0 else "lazy"}" src="../img/p/{g["slug"]}-{k+1}.webp" alt="{html.escape(g["caps"][k])}"></div>' for k in range(3))
    li=''.join(f'<li>{x}</li>' for x in g['inside'])
    page=head(f'{g["name"]} · aperçu gratuit · Thaï Malin',f'3 pages gratuites du {g["name"]} (édition 2026) : {g["tag"]}.',f'img/cover-{g["slug"]}.webp',1)+f'''
<main class="w"><div class="gh"><img src="../img/cover-{g['slug']}.webp" alt="Couverture"><div><span class="badge">Aperçu gratuit · Édition 2026</span><h1>{g['emoji']} {g['name']}</h1><p>{g['tag']}</p></div></div>
{pv}
<div class="lock"><h2>Il reste {g['n']-3} pages à découvrir</h2><p style="color:var(--mut)">Dans le guide complet :</p><ul>{li}</ul>
<a class="btn pri" href="{g['buy']}">Acheter le guide · {g['price']}</a>
<a class="btn alt" href="{HUB}">J’ai déjà mon code</a>
<p style="color:var(--mut);font-size:13px;margin-top:12px">Paiement sécurisé Stripe. Ton code arrive par e-mail juste après l’achat.</p></div>
<div class="nav2"><a href="{prev['slug']}.html">← {prev['short']}</a><a href="../index.html#guides">Tous les guides</a><a href="{nxt['slug']}.html">{nxt['short']} →</a></div></main>
<div class="sticky"><div class="w"><span class="pp">{g['price']}</span><a class="btn pri" href="{g['buy']}">Acheter ce guide</a></div></div>'''+foot%('../','../')
    open(R+f'/guide/{g["slug"]}.html','w',encoding='utf-8').write(page)

open(R+'/style.css','w').write(CSS)
open(R+'/config.js','w').write('''// Inscription e-mail facultative (nouveaux guides). Laisser vide = le formulaire reste caché.
// Pour l'activer : renseigner l'adresse Supabase et la clé publique (anon), table "newsletter" (colonnes : email, created_at, source).
window.APERCU={SUPABASE_URL:"",SUPABASE_ANON_KEY:""};
''')
open(R+'/app.js','w').write('''(function(){
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
