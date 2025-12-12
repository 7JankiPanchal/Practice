const express = require('express');
const app = express();
const port = process.env.PORT || 3000;


app.get('/', (req, res) => {
res.send('<h1>Jenkins + Docker + Kubernetes — Sample App</h1><p>Deployed via CI/CD</p>');
});


app.listen(port, () => console.log(`App listening on port ${port}`));