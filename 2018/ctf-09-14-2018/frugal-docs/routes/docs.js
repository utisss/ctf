var express = require('express');
var router = express.Router();

const nye = `
Bill Nye the Science Guy
Bill Nye the Science Guy
Bill, Bill, Bill, Bill, Bill, Bill
Bill Nye the Science Guy
(Science rules)
Bill Nye the Science Guy
(Inertia is a property of matter)
Bill, Bill, Bill, Bill, Bill, Bill
Bill Nye the Science Guy
Bill, Bill, Bill,
(T-minus seven seconds)
Bill, Bill, Bill, Bill, Bill, Bill, Bill,
Bill Nye, the Science Guy
`;

/* GET users listing. */
router.get('/', function(req, res, next) {
    res.status(400);
    res.send('No document ID provided.');
});

router.get('/bil', function(req, res, next) {
    res.send(nye); 
});

router.get('/wil', function(req, res, next) {
    res.send(nye); 
});

router.get('/aaa', function(req, res, next) {
    res.send(`The American Automobile Association (AAA pronounced "Triple A") is a federation of motor clubs throughout North America. AAA is a privately held national member association, and service business with over 58 million members [1] in the United States and Canada.[2] AAA provides services to its members, including roadside assistance and others. Its national headquarters are in Heathrow, Florida.[3]`); 
});

router.get('/aab', function(req, res, next) {
    res.send("there's over 10,000 of me. and only one of you."); 
});

router.get('/aba', function(req, res, next) {
    res.send(`ABBA's record sales are estimated at 400 million copies worldwide,[2][3] making them one of the best-selling music artists of all time.[4] They are also the best-selling band from continental Europe and from outside the English-speaking world.[4] ABBA is the first group from a non-English-speaking country to achieve consistent success in the charts of English-speaking countries, including the United Kingdom, Ireland, Canada, Australia, New Zealand, South Africa, and the United States.[5] They have a joint record eight consecutive number-one albums in the UK.[6] The group also enjoyed significant success in Latin America, and recorded a collection of their hit songs in Spanish.`);
});

router.get('/ana', function(req, res, next) {
    res.send(`ANAKIN: I should have known the Jedi were plotting to take over . . .

OBI-WAN: From the Sith!!! Anakin, Chancellor Palpatine is evil.

ANAKIN: From the Jedi point of view! From my point of view, the Jedi are evil.

OBI-WAN: Well, then you are lost!

ANAKIN: This is the end for you, My Master. I wish it were otherwise.

ANAKIN jumps and flips onto OBI- WAN's platform. The fighting continues again until OBI-WAN jumps toward the safety of the black sandy edge of the lava river. He yells at Anakin.

OBI-WAN: It's over, Anakin. I have the high ground.

ANAKIN: You underestimate my power!

OBI-WAN: Don't try it.

ANAKIN follows, and OBI-WAN cuts his young apprentice at the knees, then cuts off his left arm in the blink of an eye. ANAKIN tumbles down the embankment and rolls to a stop near the edge of the lava.

ANAKIN struggles to pull himself up the embankment with his mechanical hand. His thin leather glove has been burned off. He keeps sliding down in the black sand.

OBI-WAN: (continuing) . . . You were the Chosen One! It was said that you would, destroy the Sith, not join them. It was you who would bring balance to the Force, not leave it in Darkness.

OBI-WAN picks up Anakin's light saber and begins to walk away. He stops and looks back.

ANAKIN: I hate you!

OBI-WAN: You were my brother, Anakin. I loved you.`);
});

router.get('/jcl', function(req, res, next) {
    res.send('jester city limits > austin city limits. change my mind'); 
});

router.get('/afw', function(req, res, next) {
    res.send('utflag{sp4c3_f0rc3_6rut3_f0rc3}'); 
});

router.get('/ian', function(req, res, next) {
    res.send('isss dues: 0. egads dues: 10. do the math.'); 
});

router.get('/min', function(req, res, next) {
    res.send('isss dues: 0. egads dues: 10. do the math.'); 
});

router.get('/nel', function(req, res, next) {
    res.send(':facebook:'); 
});

router.get('/ant', function(req, res, next) {
    res.send(':quora:'); 
});

router.get('/acm', function(req, res, next) {
    res.send('chicken stock. vegetable stock. laughing stock.'); 
});

router.get('/cui', function(req, res, next) {
    res.send('https://en.wikipedia.org/wiki/Illuminati');
});

router.get('/abs', function(req, res, next) {
    res.send(`
The rectus abdominis muscle, also known as the "abdominal muscles" or "abs", is a paired muscle running vertically on each side of the anterior wall of the human abdomen, as well as that of some other mammals. There are two parallel muscles, separated by a midline band of connective tissue called the linea alba. It extends from the pubic symphysis, pubic crest and pubic tubercle inferiorly, to the xiphoid process and costal cartilages of ribs V to VII superiorly.[1] The proximal attachments are the pubic crest and the pubic symphysis. It attaches distally at the costal cartilages of ribs 5-7 and the xiphoid process of the sternum.[2]

The rectus abdominis muscle is contained in the rectus sheath, which consists of the aponeuroses of the lateral abdominal muscles. Bands of connective tissue called the tendinous intersections traverse the rectus abdominus, which separates this parallel muscle into distinct muscle bellies. The outer, most lateral line, defining the "abs" is the linea semilunaris. In the abdomens of people with big muscles and low body fat, these muscle bellies can be viewed externally and are commonly referred to as "four", "six", "eight", or even "ten packs", depending on how many are visible; however, six is the most common.`);
});

router.get('/uta', function(req, res, next) {
    res.send(`
What starts here changes the world.

The University of Texas at Austin provides public access to a first-class education and the tools of discovery. This has resulted in a culture of ambition and leadership, where physical scale is matched by bold goals and achievements.`);
});

router.get('/anm', function(req, res, next) {
    res.send(`
Garbage, trash, rubbish, or refuse is waste material that is discarded by humans, usually due to a perceived lack of utility. The term generally does not encompass bodily waste products, purely liquid or gaseous wastes, nor toxic waste products. Garbage is commonly sorted and classified into kinds of material suitable for specific kinds of disposal.`);
});

router.get('/wow', function(req, res, next) {
    res.send('https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg');
});

router.get(/^\/[a-z][a-z][a-z]$/, function(req, res, next) {
    res.status(404);
    res.send('No document with found with this id.');
});

module.exports = router;
