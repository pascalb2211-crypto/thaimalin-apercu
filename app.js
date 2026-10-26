(function(){
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
