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