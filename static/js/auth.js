function toggleAuth() {
	document.getElementById('registration').classList.toggle('d-none')
	document.getElementById('login').classList.toggle('d-none')
}

function toggleSchoolRegister() {
	document.getElementById('school-registration').classList.toggle('d-none')
	document.getElementById('admin-registration').classList.toggle('d-none')
}


async function getUser() {
	let response = await fetch('/api/v1/users/me', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			email: email.value,
			first_name: firstName.value,
			last_name: lastName.value,
			password: password.value,
		}),
	})
	let status = response.status
	let result = await response.json()

	if (status === 201) {
		console.log(result);
	} else if (status === 422) {
		showToast(result['detail'][0]['msg'])
	} else if (status === 400) {
		showToast(result['detail'])
	} else {
		showToast('неизвестная ошибка!')
	}
}


async function register() {
	let email = document.getElementById('registration-email')
	let firstName = document.getElementById('registration-first-name')
	let lastName = document.getElementById('registration-last-name')
	let password = document.getElementById('registration-password')
	let flexCheck = document.getElementById('registration-flex-check')

	if (!flexCheck.checked) {
		flexCheck.classList.add('is-invalid')
	} else {
		flexCheck.classList.remove('is-invalid')
	}

	if (firstName.value.length === 0) {
		firstName.classList.add('is-invalid')
	} else {
		firstName.classList.remove('is-invalid')
	}
	if (lastName.value.length === 0) {
		lastName.classList.add('is-invalid')
	} else {
		lastName.classList.remove('is-invalid')
	}

	if (password.value.length === 0) {
		password.classList.add('is-invalid')
	} else {
		password.classList.remove('is-invalid')
	}

	if (email.value.length === 0) {
		email.classList.add('is-invalid')
	} else {
		email.classList.remove('is-invalid')
	}

	if (
		email.value.length > 0 &&
		password.value.length > 0 &&
		email.value.length > 0 &&
		flexCheck.checked
	) {
		let response = await fetch('/api/v1/auth/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				email: email.value,
				first_name: firstName.value,
				last_name: lastName.value,
				password: password.value,
			}),
		})
		let status = response.status
		let result = await response.json()

		if (status === 201) {
			showToast('Вы успешно зарегистрировались!')

			var expirationDate = new Date();
			expirationDate.setDate(expirationDate.getDate() + 30);
			document.cookie = "access_token=" + result['access_token'] + "; " + 
							  "expires=" + expirationDate.toUTCString() + 
							  "; path=/;";
			document.cookie = "refresh_token=" + result['refresh_token'] + "; " + 
							  "expires=" + expirationDate.toUTCString() + 
							  "; path=/;";

			setTimeout(() => {
				location.href = '/profile/'
			}, '2000')
		} else if (status === 422) {
			showToast(result['detail'][0]['msg'])
		} else if (status === 400) {
			showToast(result['detail'])
		} else {
			showToast('неизвестная ошибка!')
		}
	}
}

async function login() {
	let email = document.getElementById('login-email')
	let password = document.getElementById('login-password')
	let flexCheck = document.getElementById('login-flex-check')

	if (!flexCheck.checked) {
		flexCheck.classList.add('is-invalid')
	} else {
		flexCheck.classList.remove('is-invalid')
	}

	if (email.value.length === 0) {
		email.classList.add('is-invalid')
	} else {
		email.classList.remove('is-invalid')
	}

	if (password.value.length === 0) {
		password.classList.add('is-invalid')
	} else {
		password.classList.remove('is-invalid')
	}

	if (
		email.value.length > 0 &&
		password.value.length > 0 &&
		flexCheck.checked
	) {
		let response = await fetch('/api/v1/auth/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				password: password.value,
				email: email.value,
			}),
		})
		let status = response.status
		let result = await response.json()

		if (status === 200) {
			showToast('Вы успешно вошли в систему!')
			
			var expirationDate = new Date();
			expirationDate.setDate(expirationDate.getDate() + 30);
			document.cookie = "access_token=" + result['access_token'] + "; " + 
							  "expires=" + expirationDate.toUTCString() + 
							  "; path=/;";
			document.cookie = "refresh_token=" + result['refresh_token'] + "; ";

			setTimeout(() => {
				location.href = '/profile/'
			}, '2000')
		} else if (status === 422) {
			showToast(result['detail'][0]['msg'])
		} else if (status === 400) {
			showToast(result['detail'])
		} else {
			showToast('неизвестная ошибка!')
		}
	}
}


async function schoolRegister() {
	let portalEmail = document.getElementById('portal-email')
	let portalName = document.getElementById('portal-name')
	let portalInn = document.getElementById('portal-inn')
	let portalAddress = document.getElementById('portal-address')
	let portalPhone = document.getElementById('portal-phone')
	
	let email = document.getElementById('registration-email')
	let firstName = document.getElementById('registration-first-name')
	let lastName = document.getElementById('registration-last-name')
	let password = document.getElementById('registration-password')
	let flexCheck = document.getElementById('registration-flex-check')

	if (!flexCheck.checked) {
		flexCheck.classList.add('is-invalid')
	} else {
		flexCheck.classList.remove('is-invalid')
	}

	if (firstName.value.length === 0) {
		firstName.classList.add('is-invalid')
	} else {
		firstName.classList.remove('is-invalid')
	}
	if (lastName.value.length === 0) {
		lastName.classList.add('is-invalid')
	} else {
		lastName.classList.remove('is-invalid')
	}

	if (password.value.length === 0) {
		password.classList.add('is-invalid')
	} else {
		password.classList.remove('is-invalid')
	}

	if (email.value.length === 0) {
		email.classList.add('is-invalid')
	} else {
		email.classList.remove('is-invalid')
	}

	if (
		email.value.length > 0 &&
		password.value.length > 0 &&
		email.value.length > 0 &&
		flexCheck.checked
	) {
		let response = await fetch('/api/v1/school/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				"user": {
					email: email.value,
					first_name: firstName.value,
					last_name: lastName.value,
					password: password.value,
				}, 
				"portal": {
					email: portalEmail.value,
					address: portalAddress.value,
					name: portalName.value,
					inn: portalInn.value, 
					phone: portalPhone.value
				}
			}),
		})
		let status = response.status
		let result = await response.json()

		if (status === 200) {
			showToast('Вы успешно зарегистрировали школу!')

			var expirationDate = new Date();
			expirationDate.setDate(expirationDate.getDate() + 30);
			document.cookie = "access_token=" + result['access_token'] + "; " + 
							  "expires=" + expirationDate.toUTCString() + 
							  "; path=/;";
			document.cookie = "refresh_token=" + result['refresh_token'] + "; " + 
							  "expires=" + expirationDate.toUTCString() + 
							  "; path=/;";

			setTimeout(() => {
				location.href = '/profile/'
			}, '2000')
		} else if (status === 422) {
			showToast(result['detail'][0]['msg'])
		} else if (status === 400) {
			showToast(result['detail'])
		} else {
			showToast('неизвестная ошибка!')
		}
	}
}