fetch('http://127.0.0.1:5500/output2.html')
    .then(res => console.log(res.getAllResponseHeader('Date'))
    )