(this["webpackJsonpreact-reddit-app"]=this["webpackJsonpreact-reddit-app"]||[]).push([[0],[,,,,,,,,,,,,function(e,t,a){},function(e,t,a){},,function(e,t,a){},function(e,t,a){},function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),l=a(6),r=a.n(l),i=(a(12),a(13),a(2)),o=a(7),m=(a(15),function(e){var t=e.closeModal;return c.a.createElement("div",{className:"overlay"},c.a.createElement("div",{className:"content"},c.a.createElement("div",{name:"times",onClick:t,style:{color:"white",padding:"10px",cursor:"pointer",backgroundColor:"transparent",border:0,position:"absolute",top:"-2.5rem",right:"0.3rem"}},"X"),e.children))});var u=function(e){e.fallback;var t=Object(n.useState)(""),a=Object(i.a)(t,2),l=a[0],r=a[1],u=Object(n.useState)(""),s=Object(i.a)(u,2),d=s[0],E=s[1],v=Object(n.useState)(""),p=Object(i.a)(v,2),f=(p[0],p[1]),b=Object(n.useState)([]),h=Object(i.a)(b,2),g=h[0],j=h[1],S=Object(n.useState)(!1),N=Object(i.a)(S,2),O=N[0],k=N[1];Object(n.useEffect)((function(){fetch("/home").then((function(e){return e.json()})).then((function(e){return j(e)}))}),[]);var _=Object(o.a)(),w=_.register,y=_.handleSubmit,C=function(e){var t="/home";""!=e.gender&&(t="/search/"+e.gender+"/"+e.type);fetch(t).then((function(e){return e.json().then((function(e){return j(e)}))}))};function F(){return c.a.createElement("div",null,c.a.createElement("h1",null,"Show Me"),c.a.createElement("form",{onSubmit:y(C)},c.a.createElement("select",{name:"gender",ref:w},c.a.createElement("option",{value:""},"Select.."),c.a.createElement("option",{value:"F"},"F"),c.a.createElement("option",{value:"M"},"M")),c.a.createElement("select",{name:"type",ref:w},c.a.createElement("option",{value:""},"Select.."),c.a.createElement("option",{value:"1"},"Loss"),c.a.createElement("option",{value:"2"},"Gain")),c.a.createElement("input",{type:"submit",value:"Search"})))}function M(e){var t=e.items,a=e.fallback;return t&&0!==t.length?t.map((function(e){return c.a.createElement("article",null,c.a.createElement("a",{className:"thumbnail",name:e.post_thumbnail,onClick:function(){return function(e,t,a,n){r(e),E(t),f(a),k(n)}(e.post_title,e.post_url,e.post_permalink,!0)},"data-position":"left center"},c.a.createElement("img",{src:e.post_thumbnail,alt:e.post_title})),c.a.createElement("h2",null,e.post_title))})):a}function L(e){e.items,e.fallback;return c.a.createElement("div",{id:"viewer"},c.a.createElement("div",{className:"inner"},c.a.createElement("div",{className:"nav-next"}),c.a.createElement("div",{className:"nav-previous"}),c.a.createElement("div",{className:"toggle"})),c.a.createElement("div",{className:"slide active"},c.a.createElement("div",{className:"caption"},l),c.a.createElement("div",{className:"image"},c.a.createElement("img",{className:"view",src:d}))))}return c.a.createElement("div",null,c.a.createElement("div",{id:"main"},c.a.createElement("h1",null,"Progress Pic Search"),c.a.createElement(F,null),c.a.createElement("div",{className:"modal-modal"},O&&c.a.createElement(m,{closeModal:function(){return k(!1)}},c.a.createElement(L,{items:g}))),c.a.createElement("section",{id:"thumbnails"},c.a.createElement(M,{items:g,fallback:"Loading..."}))),c.a.createElement(L,{items:g}))};a(16);var s=function(){return c.a.createElement(u,null)},d=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,18)).then((function(t){var a=t.getCLS,n=t.getFID,c=t.getFCP,l=t.getLCP,r=t.getTTFB;a(e),n(e),c(e),l(e),r(e)}))};r.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(s,null)),document.getElementById("root")),d()}],[[17,1,2]]]);
//# sourceMappingURL=main.3b4da97c.chunk.js.map