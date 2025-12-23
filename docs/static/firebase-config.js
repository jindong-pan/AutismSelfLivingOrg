// Firebase配置
// Firebase JS SDK v12.7.0
const firebaseConfig = {
    apiKey: "AIzaSyDz3DtqF6RuJoKiRfcznepfO5zyXwcKMLc",
    authDomain: "peaceful-independence.firebaseapp.com",
    projectId: "peaceful-independence",
    storageBucket: "peaceful-independence.firebasestorage.app",
    messagingSenderId: "989115528458",
    appId: "1:989115528458:web:36615bf180d2110d1576f3",
    measurementId: "G-30HKN7XFT5"
};

// 初始化Firebase
const app = firebase.initializeApp(firebaseConfig);

// 初始化Firebase认证
const auth = firebase.auth();

// 导出认证实例
window.auth = auth;
