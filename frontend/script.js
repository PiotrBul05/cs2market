const API_URL = "http://127.0.0.1:8000/items";

async function loadItems() {
    const container = document.getElementById("items");

    try {
        const response = await fetch(API_URL);
        
        if (!response.ok) {
            throw new Error("Nie udało się pobrać danych");
        }

        const data = await response.json();
        container.innerHTML = "";

        data.forEach(item => {
            const card = document.createElement("div");
            card.className = "item-card";
            card.innerHTML = `
                <h3>${item.name}</h3>
                <p class="rarity">${item.rarity}</p>
                <p class="price">$${item.price}</p>
            `;
            container.appendChild(card);
        });

    } catch (error) {
        container.innerHTML = `<p style="color: red;">Błąd: ${error.message}</p>`;
        console.error(error);
    }
}

loadItems();