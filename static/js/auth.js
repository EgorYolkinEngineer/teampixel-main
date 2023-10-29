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
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
	})
	let status = response.status
	let result = await response.json()

	if (status === 200) {
		document.getElementById("editFirstName").value = result["user"]["first_name"];
		document.getElementById("editLastName").value = result["user"]["last_name"];
		document.getElementById("fullName").innerHTML = `
		${result["user"]["first_name"]} 
		${result["user"]["last_name"]} 
		`
		
		if (result["user"]["patronymic"]) {
			document.getElementById("fullName").innerHTML += result["user"]["patronymic"];
			document.getElementById("editPatronymic").value = result["user"]["patronymic"]; 
		} else {
			document.getElementById("fill-profile-info-alert").classList.remove("d-none")
		}

		if (result["user"]["department"]) {
			document.getElementById("department").textContent = result["user"]["department"]["name"];
		}
		if (result["user"]["portal"]) {
			document.getElementById("portal").textContent = result["user"]["portal"]["name"];
		}

		console.log(result["user"]["avatar"]);

		if (result["user"]["avatar"]) {
			document.getElementById("avatar").src = "/" + result["user"]["avatar"];
		}
	} else if (status === 422) {
		showToast(result['detail'][0]['msg'])
	} else if (status === 400) {
		showToast(result['detail'])
	} else {
		showToast('неизвестная ошибка!')
	}
}


async function updateAvatar() {
	var form = new FormData();
	form.append(
		'avatar', 
		document.getElementById('editAvatar').files[0]
	);

	console.log(document.getElementById('editAvatar').files[0]);

	// var xhr = new XMLHttpRequest();
	// xhr.open('PATCH', '/api/v1/users/update');
	// xhr.send(form);

	// console.log(xhr.response.json());

	let response = await fetch('/api/v1/users/update', {
		method: 'PATCH',
		body: form
	})

	let status = response.status
	let result = await response.json()

	if (status === 200) {
		location.reload();
	} else if (status === 422) {
		showToast(result['detail'][0]['msg'])
	} else if (status === 400) {
		showToast(result['detail'])
	} else {
		showToast('неизвестная ошибка!')
	}
}


async function updateUser() {
	
	let firstName = document.getElementById("editFirstName").value;
	let lastName = document.getElementById("editLastName").value;
	let patronymic = document.getElementById("editPatronymic").value; 

	let response = await fetch('/api/v1/users/update', {
		method: 'PATCH',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			first_name: firstName, 
			last_name: lastName,
			patronymic: patronymic
		})
	})

	let status = response.status
	let result = await response.json()

	if (status === 200) {
		location.reload();
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

			localStorage.setItem("user_role", result["user"]["role"]);

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
			
			localStorage.setItem("user_role", result["user"]["role"]);

			if (result["user"]["role"] === "SUPERUSER") {
				setTimeout(() => {
					location.href = '/dashboard/admin/'
				}, '2000')
			} else {
				setTimeout(() => {
					location.href = '/profile/'
				}, '2000')
			}
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

			localStorage.setItem("user_role", result["user"]["role"]);

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