<template>
    <div class="identity-generator">
        <!-- Settings Panel -->
        <div class="settings-panel">
            <h2 Generator Settings></h2>
            <div class="form-group">
                <label>Culture:</label>
                <select v-model="settings.culture">
                    <option v-for="culture in availableCultures"
                            :key="culture.value"
                            :value="culture.value"
                    >
                        {{ culture.label }}
                    </option>
                </select>
            </div>
            <div class="form-group">
                <label>Password Length:</label>
                <input
                    type="number" 
                    v-model.number="settings.passwordLength" 
                    min="12" 
                    max="32"
                >
            </div>
            <div class="form-group">
                <label>
                    <input type="checkbox" v-model="settings.headless">
                    Headless Mode
                </label>
            </div>
            <div class="form-group">
                <label>Recovery Email (optional):</label>
                <input type="email" v-model="settings.recoveryEmail">
            </div>
            <div class="form-group">
                <label>Recovery Phone (optional):</label>
                <input type="tel" v-model="settings.recoveryPhone">
            </div>
            <div class="actions">
                <button
                    @click="generateIdentity" 
                    :disabled="generationStatus === 'generating'"
                    class="primary"
                >
                    Generate Identity
                </button>
                <button
                    @click="createGmailAccount" 
                    :disabled="!canCreateGmail"
                    class="secondary"
                >
                    Create Gmail Account
                </button>
            </div>
        </div>

        <!-- Identity Display -->
        <div v-if="identity" class="identity-display">
            <h2>Generated Identity</h2>
            <div class="identity-details">
                <div class="detail-item">
                    <span class="label">Full Name:</span>
                    <span class="value">{{ identity.name }}</span>
                </div>
                <div class="detail-item">
                    <span class="label">Email:</span>
                    <span class="value">{{ identity.email }}</span>
                </div>
                <div class="detail-item">
                    <span class="label">Password:</span>
                    <span class="value">
                        <span class="password">{{ identity.password }}</span>
                        <button @click="copyToClipboard(identity.password)" class="copy-btn">
                            Copy
                        </button>
                    </span>
                </div>
                <div class="detail-item">
                    <span class="label">Culture:</span>
                    <span class="value">{{ identity.culture }}</span>
                </div>
            </div>
        </div>

        <!-- Process Logs -->
         <div class="process-logs">
            <div class="logs-header">
                <h2>Process Logs</h2>
                <button @click="clearLogs" class="clear-btn">Clear</button>
            </div>
            <div class="logs-container">
                <div
                    v-for="(log, index) in logs" 
                    :key="index" 
                    class="log-entry"
                >
                    <span class="timestamp">{{ formatTimestamp(log.timestamp) }}</span>
                    <span class="message">{{ log.message }}</span>
                </div>
            </div>
         </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
    name: 'IdentityGenerator',
    computed: {
        ...mapState('identity',[
            'identity',
            'generationStatus',
            'logs',
            'availableCultures'
        ]),
        settings: {
            get() {
                return this.$store.state.identity.settings;
            },
            set(value) {
                this.updateSettings(value);
            },
        },
        canCreateGmail() {
            return this.identity && this.generationStatus !== 'generating';
        }
    },
    methods: {
        ...mapActions('identity', [
            'generateIdentity',
            'createGmailAccount',
            'updateSettings',
            'clearLogs'
        ]),
        async copyToClipboard(text) {
            try {
                await navigator.clipboard.writeText(text);
                this.$store.commit('identity/ADD_LOG', 'Password copied to clipboard');
            } catch (error) {
                this.$store.commit('identity/ADD_LOG', 'Failed to copy password');
            }
        },
        formatTimestamp(timestamp) {
            return new Date(timestamp).toLocaleTimeString();
        }
    }
}
</script>

<style scoped>
.identity-generator {
  display: grid;
    grid-template-columns: 300px 1fr;
    grid-gap: 20px;
    padding: 20px;
    height: 100vh;
}

.settings-panel {
    background: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
}

.identity-display {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.detail-item {
    display: flex;
    margin-bottom: 10px;
}

.label {
    font-weight: bold;
    width: 120px;
}

.password {
    font-family: monospace;
}

.process-logs {
    grid-column: 1 / -1;
    background: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
}

.logs-container {
    height: 200px;
    overflow-y: auto;
    background: white;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.log-entry {
    padding: 5px;
    border-bottom: 1px solid #eee;
}

.timestamp {
    color: #666;
    margin-right: 10px;
}

button {
    padding: 8px 16px;
    border-radius: 4px;
    border: none;
    cursor: pointer;
}

button.primary {
    background: #007bff;
    color: white;
}

button.secondary {
    background: #6c757d;
    color: white;
}

button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}