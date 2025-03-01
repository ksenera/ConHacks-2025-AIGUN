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
    sideBar.style.backgroundColor = 'rgb(255, 255, 255)';
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

    const bubbleContainer = document.createElement('div');
    bubbleContainer.style.display = 'flex';
    bubbleContainer.style.flexDirection = 'column';
    bubbleContainer.style.gap = '1.5rem';   
    bubbleContainer.style.marginTop = '1rem';

    const environmentalRow = document.createElement('div');
    environmentalRow.style.cssText = `display: flex; align-items: center;`;
    environmentalRow.innerHTML = `
      <div style="width: 120px;">Environmental</div>
      <svg width="50" height="50">
        <circle cx="25" cy="25" r="25" fill="lightgreen" />
      </svg>
    `;
    bubbleContainer.appendChild(environmentalRow);

    const socialRow = document.createElement('div');
    socialRow.style.cssText = `display: flex; align-items: center;`;
    socialRow.innerHTML = `
      <div style="width: 120px;">Social</div>
      <svg width="70" height="70">
        <circle cx="35" cy="35" r="35" fill="lightblue" />
      </svg>
    `;
    bubbleContainer.appendChild(socialRow);

    const governanceRow = document.createElement('div');
    governanceRow.style.cssText = `display: flex; align-items: center;`;
    governanceRow.innerHTML = `
      <div style="width: 150px;">Governance</div>
      <svg width="40" height="40">
        <circle cx="20" cy="20" r="20" fill="pink" />
      </svg>
    `;
    bubbleContainer.appendChild(governanceRow);

    const esgSummaryCard = document.createElement('div');
    esgSummaryCard.style.cssText = `
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 20px;
      margin-bottom: 1rem;
    `;
    esgSummaryCard.innerHTML = `
      <h3 style="margin-top: 0;">Score Summary</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor...</p>
    `;

    sideBar.appendChild(tabHeader);

    const newsContent = document.createElement('div');
    newsContent.id = 'news-content';
    newsContent.style.padding = '10px';
    newsContent.textContent = 'News content';
    // news tab hidden by default    
    newsContent.style.display = 'none';

    const newsCard = document.createElement('div');
    newsCard.style.cssText = `
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 10px;
      margin-bottom: 1rem;
    `;
    newsCard.innerHTML = `
      <h3 style="margin-top: 0;">Title</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor...</p>
      <p><strong>Read More:</strong> <a href="#">link</a></p>
    `;
    newsContent.appendChild(newsCard);

    sideBar.appendChild(esgContent);
    sideBar.appendChild(newsContent);
    esgContent.appendChild(bubbleContainer);
    esgContent.appendChild(esgSummaryCard);

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