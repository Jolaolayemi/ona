/* Ona demo screens: small interactions. Everything is visible without this file. */
(function(){
  var root=document.documentElement;
  var still=root.classList.contains('figma')||(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  // count-up numbers (final value is already in the HTML)
  if(!still){
    document.querySelectorAll('[data-count]').forEach(function(el){
      var end=parseFloat(el.getAttribute('data-count')),pre=el.getAttribute('data-pre')||'',suf=el.getAttribute('data-suf')||'';
      var dur=900,t0=null,delay=+(el.getAttribute('data-delay')||250);
      function fmt(v){return pre+Math.round(v).toLocaleString('en-US')+suf}
      el.textContent=fmt(0);
      setTimeout(function(){requestAnimationFrame(function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur);k=1-Math.pow(1-k,3);el.textContent=fmt(end*k);if(k<1)requestAnimationFrame(step);});},delay);
    });
  }
  // tap to select an option (single choice inside a group)
  document.querySelectorAll('[data-pick]').forEach(function(g){
    g.addEventListener('click',function(e){var o=e.target.closest('.opt');if(!o||!g.contains(o))return;
      g.querySelectorAll('.opt').forEach(function(x){x.classList.remove('sel')});o.classList.add('sel');});
  });
  // toggles
  document.querySelectorAll('.tg').forEach(function(t){t.addEventListener('click',function(){t.classList.toggle('on')})});
  // swipe card: drag left for scam, right for legit, springs back
  var card=document.querySelector('.sw.top');
  if(card){
    var sx=0,dx=0,down=false,sc=card.querySelector('.stamp.scam'),lg=card.querySelector('.stamp.legit');
    card.addEventListener('pointerdown',function(e){down=true;sx=e.clientX;card.setPointerCapture(e.pointerId);card.style.transition='none'});
    card.addEventListener('pointermove',function(e){if(!down)return;dx=e.clientX-sx;card.style.transform='translateX('+dx+'px) rotate('+(dx/18)+'deg)';
      if(sc)sc.style.opacity=Math.min(1,Math.max(0,-dx/90));if(lg)lg.style.opacity=Math.min(1,Math.max(0,dx/90));});
    function up(){if(!down)return;down=false;card.style.transition='';card.style.transform='';if(sc)sc.style.opacity='';if(lg)lg.style.opacity='';}
    card.addEventListener('pointerup',up);card.addEventListener('pointercancel',up);
  }
  // index: fit thumbnails on small screens
  function fit(){document.querySelectorAll('.th .fr').forEach(function(f){f.style.setProperty('--k',(f.clientWidth/390).toFixed(4))})}
  if(document.querySelector('.ixg')){fit();addEventListener('resize',fit)}
})();
