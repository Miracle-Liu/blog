function http() {
}

http.get = (...args) => {
    return new Promise((resolve, reject) => {
        axios.get(...args).then(({ data }) => {
            var { code, msg, res } = data;
            if (code == 0) {
                resolve(res);
            } else {
                alert(msg);
            }
        })
    })
}
http.post = (...args) => {
    return new Promise((resolve, reject) => {
        axios.post(...args, { headers: { "X-CSRFToken": Cookies.get('csrftoken') } }).then(({ data }) => {
            var { code, msg, res } = data;
            if (code == 0) {
                resolve(res);
            } else {
                alert(msg);
            }
        })
    })
}