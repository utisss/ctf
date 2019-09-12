const bigInt = require("big-integer");
const config = require("./config");
const counts = [bigInt.zero, bigInt.zero, bigInt.zero, bigInt.zero];
const maxVote = bigInt("2147483647");

// id: number
// vote: string
const cast = (id, vote) => {
    if (id < 0 || id >= counts.length) {
        return 0;
    }

    try {
        let value = bigInt(vote, 10);
        if (!value.isPositive()) {
            return 0;
        }

        if (value.greater(maxVote)) {
            value = maxVote;
        }

        counts[id] = counts[id].plus(value);

        if (value.greater(config.maxVote)) {
            return 1;
        }

    } catch (e) {
    }

    return 0;
}

module.exports = {
    counts,
    cast
};
