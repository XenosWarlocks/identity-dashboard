<!-- src/components/MiniBrowser.vue -->
<template>
    <div class="mini-browser">
        <div class="browser-controls">
            <button @click="goBack" :disabled="!canGoBack">←</button>
            <button @click="goForward" :disabled="!canGoForward">→</button>
            <input
                v-model="currentUrl" 
                @keyup.enter="navigateTo"
                placeholder="Enter URL"
                class="url-input"
            />
            <button @click="navigateTo">Go</button>
            <button @click="refreshPage">Refresh</button>
        </div>
        <iframe
            ref="browserFrame"
            :src="currentUrl" 
            @load="onPageLoad"
            class="browser-frame"
        ></iframe>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                currentUrl: 'http://localhost:8080/',
                browserHistory: [],
                currentHistoryIndex: -1,
                canGoBack: false,
                canGoForward: false
            }
        },

        methods: {
            navigateTo() {
                if (this.currentUrl) {
                    // Ensure URL has protocol
                    const formattedUrl = this.currentUrl.startsWith('http') ? this.currentUrl : `https://${this.currentUrl}`;
                    // Update history
                    this.browserHistory = this.browserHistory.slice(0, this.currentHistoryIndex + 1);
                    this.browserHistory.push(formattedUrl);
                    this.currentHistoryIndex++;

                    this.$refs.browserFrame.src = formattedUrl;
                    this.updateNavigationState();
                }
            },
            goBack() {
                if (this.canGoBack) {
                    this.currentHistoryIndex--;
                    this.$refs.browserFrame.src = this.browserHistory[this.currentHistoryIndex];
                    this.currentUrl = this.browserHistory[this.currentHistoryIndex];
                    this.updateNavigationState();
                }
            },
            goForward() {
                if (this.canGoForward) {
                    this.currentHistoryIndex++;
                    this.$refs.browserFrame.src = this.browserHistory[this.currentHistoryIndex];
                    this.currentUrl = this.browserHistory[this.currentHistoryIndex];
                    this.updateNavigationState();
                }
            },
            refreshPage() {this.$refs.browserFrame.contentWindow.location.reload();},
            onPageLoad() {this.updateNavigationState();},
            updateNavigationState() {
                this.canGoBack = this.currentHistoryIndex > 0;
                this.canGoForward = this.currentHistoryIndex < this.browserHistory.length - 1;
            }
        }
    }
</script>

<style scoped>
.mini-browser {
    width: 100%;
    height: 600px;
    border: 1px solid #ddd;
    display: flex;
    flex-direction: column;
}

.browser-controls {
    display: flex;
    padding: 10px;
    background-color: #f0f0f0;
}

.url-input {
    flex-grow: 1;
    margin: 0 10px;
    padding: 5px;
}

.browser-frame {
    width: 100%;
    height: 100%;
    border: none;
}
</style>