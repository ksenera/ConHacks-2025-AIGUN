// contentScript.ts 

export function toggleSiderBar() {
    const existingSideBar = document.getElementById('side-bar');
    if (existingSideBar) {
        existingSideBar.remove();
        return;
    }
    
    // new sidebar 
    const sideBar = document.createElement('div');
    sideBar.id = 'side-bar';
    sideBar.style.position = 'fixed';
    sideBar.style.top = '0';
    sideBar.style.right = '0';
    sideBar.style.width = '300px';
    sideBar.style.height = '100%';
    sideBar.style.borderLeft = '1px solid black';
    sideBar.style.backgroundColor = 'rgba(145, 232, 110, 0.5)';
    sideBar.style.boxShadow = '-2px 0 5px rgba(0, 0, 0, 0.5)';
    sideBar.style.zIndex = '9999999999';
    sideBar.style.overflowY = 'auto';

    // tab container 
    const tabHeader = document.createElement('div');
    tabHeader.style.display = 'flex';
    tabHeader.style.borderBottom = '1px solid black';

    const esgTab = document.createElement('div');
    esgTab.textContent = 'ESG Scores';
    esgTab.style.padding = '10px';
    esgTab.style.flex = '1';
    esgTab.style.textAlign = 'center';
    esgTab.style.cursor = 'pointer';
    esgTab.style.borderRight = '1px solid black';
    esgTab.style.backgroundColor = 'rgba(242, 234, 161, 0.1)';

    const newsTab = document.createElement('div');
    newsTab.textContent = 'News';
    newsTab.style.padding = '10px';
    newsTab.style.flex = '1';
    newsTab.style.textAlign = 'center';
    newsTab.style.cursor = 'pointer';   

    tabHeader.appendChild(esgTab);
    tabHeader.appendChild(newsTab);

    // content container esg is the first tab
    const esgContent = document.createElement('div');
    esgContent.id = 'esg-content';
    esgContent.style.padding = '10px';
    esgContent.textContent = 'ESG Scores content';

    const newsContent = document.createElement('div');
    newsContent.id = 'news-content';
    newsContent.style.padding = '10px';
    newsContent.textContent = 'News content';
    // news tab hidden by default    
    newsContent.style.display = 'none';

    sideBar.appendChild(tabHeader);
    sideBar.appendChild(esgContent);
    sideBar.appendChild(newsContent);

    document.body.appendChild(sideBar);

    // switch between the esg tab and the news tab 
    esgTab.addEventListener('click', () => {
        esgTab.style.backgroundColor = 'rgba(253, 239, 152, 0.1)';
        newsTab.style.backgroundColor = 'transparent';
        esgContent.style.display = 'block';
        newsContent.style.display = 'none';
    });

    newsTab.addEventListener('click', () => {
        newsTab.style.backgroundColor = 'rgba(144, 219, 233, 0.1)';
        esgTab.style.backgroundColor = 'transparent';
        newsContent.style.display = 'block';
        esgContent.style.display = 'none';
    });
    
}