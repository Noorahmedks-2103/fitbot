function send(){
  let box=document.getElementById("chatBox");
  let input=document.getElementById("chatInput");
  let msg=input.value;

  box.innerHTML+=`<p class="chat-user">You: ${msg}</p>`;

  fetch("/api/chat",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({message:msg})
  })
  .then(r=>r.json())
  .then(d=>{
    if(d.type==="text")
      box.innerHTML+=`<p class="chat-ai">Bot: ${d.data}</p>`;
    if(d.type==="list")
      d.data.forEach(i=>box.innerHTML+=`<p class="chat-ai">Bot: ${i}</p>`);
  });

  input.value="";
}
