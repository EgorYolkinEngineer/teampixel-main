async function getUserTests() {
    let response = await fetch('/api/v1/tests/user', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		}
	})

    let status = response.status
	let result = await response.json()

    if (status === 200) {
        if (result.length > 0) {
            let content = '';
            for (let item in result) {
                let elem = result[item];

                let html = `
                <div class="test-card card w-100">
                    <div class="card-body">
                    <h5 class="card-title">${elem["name"]}</h5>
                    <span class="badge rounded-pill text-bg-dark">${elem["department_name"]}</span>
                    <br><br>
                    <a href="/test/${elem["id"]}" class="btn btn-primary">Начать прохождение</a>
                    </div>
                </div><br>
                `
                content += html;
            }
            let block = document.getElementById('tests');
            block.innerHTML = content;
        }
    } else {
        showToast("неизвестная ошибка")
    }
}


async function getTest(test_id) {
    let response = await fetch('/api/v1/tests/' + test_id, {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		}
	})

    let status = response.status
	let result = await response.json()

    if (status === 200) {
        console.log(result);

        document.getElementById("testName").innerHTML = result["name"];
        document.getElementById("testDepartment").innerHTML = result["department_name"];

        let block = document.getElementById('testForms');
        
        for (let item in result["content"]) {
            let elem = result["content"][item];
            let form = document.createElement("form");
            let formHTML = `<form><p>${elem["question"]}</p>`;

            for (let answer in elem["answers"]) {
                formHTML += `
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                    <label class="form-check-label" for="flexRadioDefault1">
                    ${elem["answers"][answer]}
                    </label>
                </div>
                `;
            }
            form.innerHTML = formHTML + "</form><br>";

            console.log(elem["answers"]);

            block.innerHTML += '<form>' + form.innerHTML + '</form>';
        }
    } else {
        showToast("неизвестная ошибка")
    }
}


function generateRandomNumber() {
    return Math.floor(Math.random() * 100) + 1;
}


function submitTest() {
    let number = generateRandomNumber();

    document.querySelector(".testResult").innerHTML = number;

    if (number < 50) {
        document.getElementById("test-result-danger").classList.remove("d-none");
        document.getElementById("test-result-success").classList.set("d-none");
    } else {
        document.getElementById("test-result-success").classList.remove("d-none");
        document.getElementById("test-result-danger").classList.set("d-none");
    }
}