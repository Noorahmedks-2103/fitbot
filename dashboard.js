function loadDashboard() {
    fetch("/api/dashboard/data")
    .then(res => res.json())
    .then(data => {
        document.getElementById("sleep-hours").innerText =
            data.sleep.length + " entries";

        document.getElementById("water-intake").innerText =
            data.water.reduce((a, b) => a + b, 0).toFixed(1) + " L";

        document.getElementById("workouts-done").innerText =
            data.workouts + " sessions";

        document.getElementById("diet-streak").innerText =
            data.diet_streak + " days streak";
    });
}

loadDashboard();
