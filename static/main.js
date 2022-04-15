// const tellerId = JSON.parse(document.getElementById("teller").textContent);

// const tellerSocket = new WebSocket(
//   "ws://" + window.location.host + "/ws/teller-customers/" + tellerId + "/"
// );

// tellerSocket.onmessage = function (e) {
//   const data = JSON.parse(e.data);
//   document.querySelector("#customer-list").innerHTML += `
//   <div class="customer-div">
//   <span class="number" data-color="#345">${data.number}</span>
//   <h3>Name: ${data.name}</h3>
//   <h3>Code: ${data.code}</h3>
//   <h3>Arrived at: ${data.arrived_at}</h3>
//   <a class="customer-link" id="${data.code}" href="${data.checkout_url}">Check out</a>

// </div>
//     `;
// };
// tellerSocket.onclose = function () {
//   console.log("We lost connection");
// };
