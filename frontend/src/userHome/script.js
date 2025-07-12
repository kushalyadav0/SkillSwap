//----------------------------------------------------------
//  Utilities
//----------------------------------------------------------
const $ = (sel, par = document) => par.querySelector(sel);
const $all = (sel, par = document) => [...par.querySelectorAll(sel)];

const api = {
  async getProfiles(q = "", availability = "") {
    const url = `/api/public_profiles/?q=${encodeURIComponent(q)}&availability=${availability}`;
    return fetch(url).then(r => r.json());
  },
  async createSwap(payload) {
    return fetch("/api/create_swap/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }).then(r => r.json());
  },
  async chat(msg) {
    return fetch("/api/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    }).then(r => r.json());
  },
};

//----------------------------------------------------------
//  Render profile cards
//----------------------------------------------------------
const grid = $("#userGrid");
function renderCards(list = []) {
  grid.innerHTML = list
    .map(
      (u) => `
    <div class="card" data-id="${u.id}">
      <img src="${u.photo_url}" alt="${u.name}" class="profile-photo" />
      <div class="info">
        <h3>${u.name}</h3>
        <p><strong>Offers:</strong> ${u.skills_offered.join(", ")}</p>
        <p><strong>Wants:</strong> ${u.skills_wanted.join(", ")}</p>
        <p class="rating">⭐ ${u.rating.toFixed(1)}/5</p>
      </div>
      <button class="request">Request</button>
    </div>`
    )
    .join("");
}

//----------------------------------------------------------
//  Event wiring
//----------------------------------------------------------
async function loadProfiles() {
  const q = $("#searchInput").value.trim();
  const availability = $("#availabilitySelect")?.value || "";
  const profiles = await api.getProfiles(q, availability);
  renderCards(profiles);
}

$("#searchBtn").addEventListener("click", loadProfiles);
$("#searchInput").addEventListener("keydown", (e) => e.key === "Enter" && loadProfiles());
$("#availabilitySelect").addEventListener("change", loadProfiles);

// delegate click on any “Request” button
grid.addEventListener("click", async (e) => {
  if (!e.target.matches(".request")) return;
  const card = e.target.closest(".card");
  const requesteeId = card.dataset.id;
  const offered = prompt("Which of YOUR skills do you offer?");
  const wanted  = prompt("Which skill of theirs do you want?");
  if (!offered || !wanted) return;

  const res = await api.createSwap({
    requester_id: 1,          // TODO: inject real logged‑in user id
    requestee_id: Number(requesteeId),
    offered_skill: offered,
    wanted_skill: wanted,
  });
  if (res.ok) alert("Swap request sent!");
});

//----------------------------------------------------------
//  Chat window
//----------------------------------------------------------
const fab = $("#fabChat");
const chatWin = $("#chatWindow");
const chatBody = $("#chatBody");
const chatInput = $("#chatMsg");
const sendBtn = $("#sendBtn");

fab.onclick = () => chatWin.classList.toggle("hidden");
sendBtn.onclick = sendMsg;
chatInput.onkeydown = (e) => e.key === "Enter" && sendMsg();

function appendMsg(text, sender) {
  const div = document.createElement("div");
  div.className = `chat-msg ${sender}`;
  div.textContent = text;
  chatBody.appendChild(div);
  chatBody.scrollTop = chatBody.scrollHeight;
}

async function sendMsg() {
  const text = chatInput.value.trim();
  if (!text) return;
  appendMsg(text, "user");
  chatInput.value = "";
  const { response } = await api.chat(text);
  appendMsg(response || "...", "bot");
}

//----------------------------------------------------------
//  Init
//----------------------------------------------------------
loadProfiles();
