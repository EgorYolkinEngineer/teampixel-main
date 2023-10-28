async function getDepartaments() {
    let response = await fetch('/api/v1/school/all', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
	})
	let status = response.status
	let result = await response.json()

	if (status === 200) {
        let select = document.getElementById('selectDepartment');

        result.forEach(function(item) {
            let option = document.createElement('option');
            option.value = item.id;
            option.text = item.name;
            select.appendChild(option);
        });
    }
}


async function getUserTests() {
    let response = await fetch('/api/v1/tests/user', {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
	})
	let status = response.status
	let result = await response.json()

	if (status === 200) {
        console.log(result);
        
        let select = document.getElementById('selectDepartment');

        result.forEach(function(item) {
            let option = document.createElement('option');
            option.value = item.id;
            option.text = item.name;
            select.appendChild(option);
        });
    }
}