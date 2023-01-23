const URL = "https://api.github.com/users/"

function getUser(event) {
    event.preventDefault()
    console.log("click")
    const gitResultDiv = document.querySelector("#gitResults")
    gitResultDiv.innerHTML = "Just taking a quick peek..."
    const gitName = document.querySelector("#gitName").value
    fetch(URL + gitName)
        .then(response => response.json())
        .then(gitData => {
            console.log(gitData)
            gitResultDiv.innerHTML = `
            <h3>Name: ${gitData.name}</h3>
            <img class="image" src= ${gitData.avatar_url}>
            `
        })
        .catch(err => console.log(err))
}
