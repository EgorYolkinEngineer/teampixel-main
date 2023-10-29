async function getUserModules() {
    let response = await fetch('/api/v1/vr/modules/all/', {
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
                <div class="card" style="width: 15rem;">
                    <img src="/static/images/vr2.png" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h1>${elem["name"]}</h1>
                        <a href="${elem["urlFile"]}" download>
                            <button type="button" class="btn btn-dark">Загрузить</button>
                        </a>
                    </div>
                </div>
                `
                content += html;
            }
            let block = document.getElementById('modules');
            block.innerHTML = content;
        }
    } else {
        showToast(result["detail"])
    }
}