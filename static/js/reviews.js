async function getReviews() {
    let response = await fetch('/api/v1/users/reviews', {
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
                <div style="border-radius: 15px; border: 2px solid gray; max-width: 400px; padding: 10px;">
                    <div class="toast-header">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                            <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                        </svg>
                        <strong style="padding-left: 10px;" class="me-auto">Пользователь ПрофТестиум</strong>
                    </div>
                    <div class="toast-body">
                        ${elem["text"]}
                    </div>
                </div><br>
                `
                content += html;
            }
            let block = document.getElementById('t-reviews');
            block.innerHTML = content;
        }
    } else {
        showToast("неизвестная ошибка")
    }
}


async function createReview() {
    let text = document.getElementById("review").value;
    let response = await fetch('/api/v1/users/reviews/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: text
        }),
    })
    let status = response.status
    let result = await response.json()

    if (status === 200) {
        showToast('Отзыв создан!')

        setTimeout(() => {
            location.reload()
        }, '1000')
    } else {
        showToast(result["detail"])
    }
}
