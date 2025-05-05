// 导航栏鼠标悬停效果
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.color = '#ff9900';
    });
    link.addEventListener('mouseout', () => {
        link.style.color = 'white';
    });
});

// 可添加更多交互功能