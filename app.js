(function(){
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
