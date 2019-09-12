var express = require('express');
var router = express.Router();
const Products = require("../products.json");
const Cart = require("../cart");

/* GET checkout page. */
router.get('/checkout', function(req, res, next) {
  const userCart = Cart.deserialize(req.query.cart);
  const cartQuantity = Cart.computeQuantity(userCart);

  if (cartQuantity === 0) {
    res.redirect('/');
  }

  const userProducts = Products.map((product) => {
    return {
      ...product,
      qty: userCart[product.id] || 0,
    }
  }).filter((product) => product.qty != 0);
  const cartTotal = Cart.computeTotal(userCart);

  res.render('checkout', { 
    title: 'Checkout Now',
    products: userProducts,
    cartString: encodeURIComponent(Cart.serialize(userCart)),
    cartQuantity: Cart.computeQuantity(userCart),
    cartTotal,
    payEnabled: cartTotal === 0,
  });
});

module.exports = router;
