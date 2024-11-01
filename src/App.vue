<!-- src/App.vue -->
<template>
  <div id="app" class="dashboard">
    <header class="dashboard-header">
      <h1>Verification Dashboard</h1>
    </header>
    <div class="dashboard-content">
      <div  class="browser-section">
        <mini-browser ref="miniBrowser" />
      </div>
      <div class="verification-section">
        <verification-panel @step-verified="handleStepVerification"/>
      </div>
    </div>
  </div>
</template>

<script>

import MiniBrowser from './components/MiniBrowser.vue';
import VerificationPanel from './components/VerificationPanel.vue';

export default {
  name: 'App',
  components: {
    MiniBrowser,
    VerificationPanel
  },
  methods: {
    handleStepVerification(stepInfo) {
      console.log('Step Verified:', stepInfo);
    }
  }
}
</script>

<style>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.dashboard-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 20px;
}
</style>