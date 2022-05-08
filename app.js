const screenshot = require("screenshot-desktop");
const fs = require("fs");
const moment = require("moment");
const path = require("path");

const PATH = path.resolve(process.env["USERPROFILE"], "Pictures/DailyRecap");

screenshot.listDisplays().then((displays) => {
    const date = moment();

    const imageDir = path.join(
        PATH,
        date.format("yyyy"),
        date.format("MMMM"),
        date.format("DD"),
        date.format("HH") + "-00"
    );

    if (!fs.existsSync(imageDir)) {
        fs.mkdirSync(imageDir, { recursive: true });
    }

    displays.forEach((display, idx) => {
        const imagePath = path.join(imageDir, date.format("HH-MM-ss") + "_DISPLAY" + idx + ".png");

        screenshot({
            screen: display.id,
        })
            .then((imgBuffer) => {
                fs.writeFileSync(imagePath, imgBuffer);
                console.log(`${imagePath} screenshot saved`);
            })
            .catch((err) => {
                console.log(err);
            });
    });
});
