// Mobile menu toggle
(function(){var b=document.querySelector('.menu-toggle'),n=document.getElementById('mainnav');
if(!b||!n)return;b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'Close':'Menu';});})();
