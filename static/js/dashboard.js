async function logSleep(){
    const hrs = sleepHours.value;
    const res = await fetch("/api/sleep",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({hours:hrs})
    });
    const data = await res.json();
    sleepMsg.innerText = data.message + " | Avg: " + data.average;
}

async function logWater(){
    const l = waterLiters.value;
    const res = await fetch("/api/water",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({liters:l})
    });
    const data = await res.json();
    waterMsg.innerText = data.message + " | Total: " + data.total;
}
