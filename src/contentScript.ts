// contentScript.ts 

export function toggleSiderBar() {
    const existingSideBar = document.getElementById('side-bar');
    if (existingSideBar) {
        existingSideBar.remove();
    }
    else {
        const sideBar = document.createElement('div');
        sideBar.id = 'side-bar';
        sideBar.style.position = 'fixed';
        sideBar.style.top = '0';
        sideBar.style.right = '0';
        sideBar.style.width = '200px';
        sideBar.style.height = '100%';
        sideBar.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        sideBar.style.zIndex = '9999999999';
        document.body.appendChild(sideBar);
    }
}