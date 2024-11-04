// main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import './style.css';

const app = createApp(App);

const pinia = createPinia();
app.use(pinia);
entry: path.resolve(__dirname, 'frontend/src/main.js'),
app.mount('#app');