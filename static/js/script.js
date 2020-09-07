function addInput(category) {
  if (category == "steps") {
    var method = document.querySelector("#steps");
    var input = document.createElement("input");
    input.className = "input";
    input.type = "text";
    input.name = `step`;
    method.appendChild(input);
  } else {
    var ingredients = document.querySelector("#ingredients");
    var input = document.createElement("input");
    input.className = "input";
    input.type = "text";
    input.name = `ingredient`;
    ingredients.appendChild(input);
  }
}
function removeInput(category) {
  if (category == "steps") {
    var method = document.querySelector("#steps");
    method.removeChild(steps.lastElementChild);
  } else {
    var ingredients = document.querySelector("#ingredients");
    ingredients.removeChild(ingredients.lastElementChild);
  }
}

function eventListeners() {
  if (
    window.location.href.includes("add_recipe") ||
    window.location.href.includes("edit_recipe")
  ) {
    document.querySelector("#add-ingredient").onclick = () =>
      addInput("ingredient");
    document.querySelector("#remove-ingredient").onclick = () =>
      removeInput("ingredient");
    document.querySelector("#add-step").onclick = () => addInput("steps");
    document.querySelector("#remove-step").onclick = () => removeInput("steps");
  }
}
eventListeners();
