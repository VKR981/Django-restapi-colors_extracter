window.onload = function () {
    document.getElementById('inputGroupFileAddon04').onclick = function (e) {
        e.preventDefault()
        let image = document.getElementById("inputGroupFile04").files[0];
        console.log(image);
        let formData = new FormData();

        formData.append("image", image);
        fetch('http://127.0.0.1:8000/api/', {
            method: "POST",
            body: formData
        }).then(res => (res.json().then(data => {
            console.log(data.colors);
            document.getElementById('pri').setAttribute('style', `background-color: rgb(${data.colors[0]});`)
            document.getElementById('sec').setAttribute('style', `background-color: rgb(${data.colors[1]});`)
        })));

    }
}