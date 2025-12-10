// Independent Spectrum - 网站交互脚本

document.addEventListener('DOMContentLoaded', function() {
    // 移动导航菜单
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // 导航链接点击处理
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();

            // 关闭移动菜单
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
            }

            // 获取目标部分
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    // 平滑滚动到目标部分
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });

                    // 更新活动链接
                    navItems.forEach(navItem => navItem.classList.remove('active'));
                    this.classList.add('active');
                }
            }
        });
    });

    // 滚动时更新导航状态
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === `#${sectionId}`) {
                        item.classList.add('active');
                    }
                });
            }
        });

        // 导航栏滚动效果
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });

    // 按钮点击动画
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // 如果是外部链接，允许正常跳转
            if (this.href && !this.href.includes('#')) {
                return;
            }

            // 添加点击效果
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 100);
        });
    });

    // 卡片悬停效果
    const cards = document.querySelectorAll('.mission-card, .stat-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // 页面加载动画
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // 观察需要动画的元素
    const animateElements = document.querySelectorAll('.mission-card, .stat-card, .cta');
    animateElements.forEach(element => {
        observer.observe(element);
    });

    // 表单处理 (如果有表单)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // 显示提交成功消息
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = '发送中...';
            submitBtn.disabled = true;

            // 模拟表单提交
            setTimeout(() => {
                submitBtn.textContent = '发送成功！';
                submitBtn.style.background = '#10B981';

                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = '';
                }, 2000);
            }, 1000);
        });
    });

    // 键盘导航支持
    document.addEventListener('keydown', function(e) {
        // ESC 键关闭移动菜单
        if (e.key === 'Escape' && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });

    // 语言链接现在使用简单的HTML链接，不需要JavaScript

// 页面加载完成后的初始化
    window.addEventListener('load', function() {
        // 添加加载完成类
        document.body.classList.add('loaded');

        // 初始化页面标题
        document.title = 'Independent Spectrum | Relieving Burdens, Enabling Independence';
    });

    // 性能监控 (可选)
    if ('performance' in window) {
        window.addEventListener('load', function() {
            const perfData = performance.getEntriesByType('navigation')[0];
            const pageLoadTime = perfData.loadEventEnd - perfData.loadEventStart;

            // 可以发送到分析服务
            console.log(`页面加载时间: ${pageLoadTime}ms`);
        });
    }

    // 错误处理
    window.addEventListener('error', function(e) {
        console.error('JavaScript错误:', e.error);
        // 可以发送错误报告到监控服务
    });

    // 服务工作线程注册 (用于PWA功能 - 未来扩展)
    if ('serviceWorker' in navigator) {
        // 未来可以添加离线功能
        // navigator.serviceWorker.register('/sw.js');
    }
});

// 工具函数
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 平滑滚动到元素
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// 获取当前滚动位置
function getScrollPosition() {
    return window.pageYOffset || document.documentElement.scrollTop;
}

// 检查元素是否在视口中
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// 导出函数供其他脚本使用
window.IndependentSpectrum = {
    scrollToElement,
    getScrollPosition,
    isElementInViewport
};
