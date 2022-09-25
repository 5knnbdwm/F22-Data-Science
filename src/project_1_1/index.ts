import * as aq from "arquero";
import fs from "fs";

export async function action() {
  console.log(fs.readdirSync("@/"));
  // console.log(await fs.readFileSync("./national/yob2021.txt"));
  // const dt = await aq.loadCSV("./national/yob2021.txt", { autoType: true });
  // console.log(dt.size);
  console.log("here");
}
