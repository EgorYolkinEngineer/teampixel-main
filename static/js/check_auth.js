if (getCookie("access_token")) {
    document.getElementById("auth-header-button").classList.toggle('d-none');
    document.getElementById("my-profile-header-button").classList.toggle('d-none');

    let userRole = localStorage.getItem("user_role");

    if (userRole === "SUPERUSER") {
        document.getElementById("profileOpenHref").href = "/dashboard/admin/";
    }
}
