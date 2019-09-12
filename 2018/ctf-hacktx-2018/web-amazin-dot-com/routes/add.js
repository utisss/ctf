var express = require('express');
var router = express.Router();
const products = require("../products.json");
const Cart = require("../cart");

/* POST add a new product. */
router.post('/add', function(req, res, next) {
    let currentCart = Cart.deserialize(req.query.cart);
    let newProductId = req.body.id;

    let newCart = Cart.addTo(currentCart, newProductId);
    res.redirect('/?cart=' + encodeURIComponent(Cart.serialize(newCart)));
});

module.exports = router;
