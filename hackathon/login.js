let auth0 = null;

async function initAuth0() {
  try {
    auth0 = await createAuth0Client({
      domain: "dev-3c24zvs84bcj8jcj.us.auth0.com",
      client_id: "0o4eMKwi7uaB8JjsuVqVAzl1zXxnFIh4",
    });
  } catch (error) {
    console.error("Error initializing Auth0:", error);
  }
}

async function login() {
  if (!auth0) {
    console.error("Auth0 client is not initialized");
    return;
  }

  try {
    await auth0.loginWithRedirect({
      redirect_uri: window.location.origin + "/callback.html",
    });
  } catch (error) {
    console.error("Login failed:", error);
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  await initAuth0();

  document.getElementById("login-form").addEventListener("submit", (event) => {
    event.preventDefault();
    login();
  });
});
