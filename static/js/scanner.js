const input=document.getElementById("foodImage");
const preview=document.getElementById("preview");
const result=document.getElementById("scanResult");

input.addEventListener("change",()=>{
  const file=input.files[0];
  if(!file)return;

  const reader=new FileReader();
  reader.onload=e=>{
    preview.src=e.target.result;
    result.style.display="block";
    result.innerHTML=`
      <h3>Food Detected</h3>
      <p>Estimated Calories: ~250 kcal</p>
      <p>Category: Healthy Meal</p>
    `;
  };
  reader.readAsDataURL(file);
});
