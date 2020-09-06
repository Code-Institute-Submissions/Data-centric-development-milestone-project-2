           function addInput(category) {
                 if (category == 'steps') {
                    console.log(category)
                    const method = document.querySelector('#steps');
                    console.log("method"+method)
                    const input = document.createElement('input');
                    input.className = 'input';
                    input.type = 'text';
                    input.name = `step`
                    method.appendChild(input);
                    console.log(method)
                    console.log(length)
                    console.log(input)
                }else{
                    console.log(category)
                    const ingredients = document.querySelector('#ingredients');
                    const input = document.createElement('input');
                    input.className = 'input';
                    input.type = 'text';
                    input.name = `ingredient`
                    ingredients.appendChild(input);
                    console.log(ingredients)
                    console.log(length)
                    console.log(input)
                }
            }
            function removeInput(category) {
                if (category == 'steps') {
                    const method = document.querySelector('#steps');
                    method.removeChild(steps.lastElementChild);
                }
                else{
                console.log(category)
                const ingredients = document.querySelector('#ingredients');
                 ingredients.removeChild(ingredients.lastElementChild);
                } 
            }

            function eventListeners() {
                    if ((window.location.href.includes('add_recipe')) || (window.location.href.includes('edit_recipe'))) {
                    document.querySelector('#add-ingredient').onclick = () => addInput('ingredient');
                    document.querySelector('#remove-ingredient').onclick = () => removeInput('ingredient');
                    document.querySelector('#add-step').onclick = () => addInput('steps');
                    document.querySelector('#remove-step').onclick = () => removeInput('steps');
                }
            }   
            eventListeners();