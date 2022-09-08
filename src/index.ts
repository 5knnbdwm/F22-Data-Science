import { readdirSync } from "fs";
import prompts from "prompts";

const callProject = async (projectFolder: string) => {
  const { action } = await import(`./${projectFolder}`);
  action();
};

const askUserWrapper = async (
  preSelectedFolder: string | undefined,
  folder: string[]
) => {
  let selectedFolder = preSelectedFolder ? preSelectedFolder : "";

  if (selectedFolder === "") selectedFolder = await askUserInput(folder);
  if (selectedFolder !== "cancel") {
    await callProject(selectedFolder);
    askUserWrapper(preSelectedFolder, folder);
  }

  return;
};

const askUserInput = async (folders: string[]) => {
  const onAction = () => {
    return true;
  };
  const response = await prompts(
    {
      type: "select",
      name: "folder",
      message: "What project would you like to run?",
      choices: [
        { title: "Cancel", value: "cancel" },
        ...folders.map((item) => {
          return { title: item, value: item };
        }),
      ],
    },
    { onSubmit: onAction, onCancel: onAction }
  );

  return response.folder;
};

const main = async () => {
  const allFolders = await readdirSync("./dist").filter(
    (item: string) => !(item.includes(".js") || item.includes(".ts"))
  );

  let selectedFolder = undefined as string | undefined;

  if (process.env.FOLDER !== undefined) {
    if (allFolders.includes(process.env.FOLDER))
      selectedFolder = process.env.FOLDER;
  }

  askUserWrapper(selectedFolder, allFolders);
};

main();
