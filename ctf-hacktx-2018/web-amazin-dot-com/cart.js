/*

interface ICart {
    string : number
}

*/

const base64 = require("base-64");
const products = require("./products");

const catalog = new Map();
for (const product of products) {
    catalog.set(product.id, product.price);
}

function deserialize(b64) {
    if (!b64) {
        return {};
    }

    var cart = {};
    try {
        cart = JSON.parse(base64.decode(b64));
    } catch (e) {
        console.error(e);
        return {};
    }

    const items = Array.from(Object.keys(cart));
    for (let item of items) {
        if (!catalog.has(item) || !Number.isInteger(cart[item])) {
            return {};
        }
    }

    return cart;
}

function serialize(cart) {
    return base64.encode(JSON.stringify(cart));
}

function addTo(cart, item) {
    if (!item || !catalog.has(item)) {
        return cart;
    }

    if (!cart[item]) {
        cart[item] = 1;
    } else {
        cart[item] += 1;
    }

    return cart;
}

function computeQuantity(cart) {
    var qty = 0;
    const items = Array.from(Object.keys(cart));
    for (const item of items) {
        qty += cart[item];
    }

    return qty;
}

function computeTotal(cart) {
    var total = 0;
    const items = Array.from(Object.keys(cart));
    for (const item of items) {
        total += cart[item] * catalog.get(item);
    }

    return Number(total.toFixed(2));
} 

module.exports = {
    deserialize,
    serialize,
    addTo,
    computeTotal,
    computeQuantity
}