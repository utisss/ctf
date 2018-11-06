const speakeasy = require("speakeasy");

const timingWindow = 1000 * 60;
const now = Date.now();
const firstIndex = (now - (now % timingWindow)) / timingWindow;
let buckets = {};
buckets[firstIndex] = speakeasy.generateSecret();

const users = new Map();
users.set("willh", firstIndex);

function createSecret(username, timestamp) {
    timestamp = timestamp - (timestamp % timingWindow);
    var bucket = timestamp / timingWindow;
    //console.log(`username: ${username}, bucket: ${bucket}`);
    users.set(username, bucket);

    if (buckets[bucket]) {
        return buckets[bucket];
    }

    buckets[bucket] = speakeasy.generateSecret();
    return buckets[bucket];
}

function getSecret(username) {
    if (!users.get(username)) {
        return null;
    }

    return buckets[users.get(username)];
}

function getIndex(username) {
    return users.get(username);
}

function verifySecret(username, otp) {
    let secret = null;
    if (!(secret = getSecret(username))) {
        return false;
    }

    return speakeasy.totp.verify({
        secret: secret.base32,
        encoding: 'base32',
        token: otp,
    });
}

module.exports = {
    initialTimestamp: now,
    createSecret,
    getSecret,
    getIndex,
    verifySecret,
    firstIndex,
}
