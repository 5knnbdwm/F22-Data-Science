import * as aq from "arquero";

export async function action() {
  const dt = await aq.loadCSV("./national/yob2021.csv", { autoType: true });
  console.log(dt.size);
  console.log("here");
}
