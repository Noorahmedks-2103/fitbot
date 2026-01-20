function loadDiet() {
  fetch(`/api/diet?goal=${goal.value}&days=${days.value}&mode=${mode.value}`)
    .then(r => r.json())
    .then(d => {
      dietCards.innerHTML = d.days.map(day => `
        <div class="card">
          <h3>${day.day}</h3>
          <p>🍳 ${day.breakfast}</p>
          <p>🍛 ${day.lunch}</p>
          <p>🍎 ${day.snack}</p>
          <p>🌙 ${day.dinner}</p>
        </div>
      `).join("");
    });
}
