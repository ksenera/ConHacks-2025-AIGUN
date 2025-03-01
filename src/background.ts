// background.ts

import { toggleSiderBar } from "./contentScript";

chrome.action.onClicked.addListener((tab) => {
    if (!tab.id) {
        return;
    }
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: toggleSiderBar
    });
});