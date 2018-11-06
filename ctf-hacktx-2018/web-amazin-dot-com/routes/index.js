var express = require('express');
var router = express.Router();
const Products = require("../products.json");
const Cart = require("../cart");

/* GET home page. */
router.get('/', function(req, res, next) {
  const userCart = Cart.deserialize(req.query.cart);
  const cartQuantity = Cart.computeQuantity(userCart);

  res.render('index', { 
    title: 'Home',
    products: Products,
    cartString: encodeURIComponent(Cart.serialize(userCart)),
    cartQuantity,
    checkoutEnabled: cartQuantity !== 0
  });
});

module.exports = router;
