async function generateWorkout(){
  const goal = document.getElementById("workout-goal").value;
  const days = document.getElementById("workout-days").value;

  const res = await fetch(`/api/workout?goal=${goal}&days=${days}`);
  const data = await res.json();

  const box = document.getElementById("workout-cards");
  box.innerHTML = "";

  data.plan.forEach(day=>{
    box.innerHTML += `
      <div class="glass-card glow">
        <h3>${day.day}</h3>
        <ul>${day.exercises.map(e=>`<li>${e}</li>`).join("")}</ul>
      </div>
    `;
  });
}
