window.onload = () => {
    fetch("/api/profile/get")
        .then(res => res.json())
        .then(p => {
            document.getElementById("age").value = p.age;
            document.getElementById("height").value = p.height;
            document.getElementById("weight").value = p.weight;
            document.getElementById("gender").value = p.gender;
        });
};

document.getElementById("saveProfile").onclick = () => {
    const data = {
        age: document.getElementById("age").value,
        height: document.getElementById("height").value,
        weight: document.getElementById("weight").value,
        gender: document.getElementById("gender").value
    };

    fetch("/api/profile/save", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById("saveMsg").innerText = "Saved!";
    });
};
