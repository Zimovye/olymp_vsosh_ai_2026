const fs = require("fs");
const path = require("path");
const vscode = require("vscode");

function readHints(extensionPath) {
    const hintsPath = path.join(extensionPath, "hints.json");
    const text = fs.readFileSync(hintsPath, "utf8").replace(/^\uFEFF/, "");
    return JSON.parse(text);
}

function activate(context) {
    const provider = vscode.languages.registerHoverProvider(
        { language: "python", scheme: "file" },
        {
            provideHover(document, position) {
                const wordRange = document.getWordRangeAtPosition(position);
                if (!wordRange) {
                    return undefined;
                }

                const word = document.getText(wordRange);

                let hints;
                try {
                    // Перечитываем маленький словарь при наведении,
                    // чтобы новые подсказки появлялись без переустановки расширения.
                    hints = readHints(context.extensionPath);
                } catch (error) {
                    console.error("Не удалось прочитать hints.json:", error);
                    return undefined;
                }

                const hint = hints[word];
                if (!hint) {
                    return undefined;
                }

                const markdown = new vscode.MarkdownString();
                markdown.appendMarkdown(`### 🇷🇺 ${hint.title}\n\n`);
                markdown.appendMarkdown(`${hint.description}\n\n`);

                if (hint.example) {
                    markdown.appendMarkdown("**Пример:**\n\n");
                    markdown.appendCodeblock(hint.example, "python");
                }

                if (hint.note) {
                    markdown.appendMarkdown(`\n**Обрати внимание:** ${hint.note}`);
                }

                markdown.isTrusted = false;
                return new vscode.Hover(markdown, wordRange);
            }
        }
    );

    context.subscriptions.push(provider);
}

function deactivate() {}

module.exports = { activate, deactivate };
