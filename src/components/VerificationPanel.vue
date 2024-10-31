<!-- src/components/VerificationPanel.vue -->
<template>
    <div class="verification-panel">
        <h2>Verification Dashboard</h2>
        <div class="verification-steps">
            <div
                v-for="(step, index) in verificationSteps" 
                :key="index" 
                class="verification-step"
                :class="{
                    'completed': step.status === 'completed', 
                    'in-progress': step.status === 'in-progress',
                    'pending': step.status === 'pending'
                }"
            >
                <span class="step-name">{{ step.name }}</span>
                <span class="step-status">{{ step.status }}</span>
                <button
                    @click="updateStepStatus(index)" 
                    :disabled="step.status === 'completed'"
                >
                    {{ step.status === 'completed' ? 'Verified' : 'Verify' }}
                </button>
            </div>
        </div>
        <div class="verification-actions">
            <button
                @click="startVerification" 
                :disabled="!canStartVerification"
            >
                Start Verification Process
            </button>
            <button
                @click="resetVerification" 
                :disabled="!canResetVerification"
            >
                Reset Verification
            </button>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      verificationSteps: [
        { name: 'URL Validation', status: 'pending' },
        { name: 'Content Check', status: 'pending' },
        { name: 'Source Verification', status: 'pending' },
        { name: 'Final Approval', status: 'pending' }
      ]
    }
  },
  computed: {
    canStartVerification() {
      return this.verificationSteps.every(step => step.status === 'pending');
    },
    canResetVerification() {
      return this.verificationSteps.some(step => step.status !== 'pending');
    }
  },
  methods: {
    updateStepStatus(index) {
      const currentStep = this.verificationSteps[index];
      
      // Simple verification logic
      if (currentStep.status === 'pending') {
        currentStep.status = 'in-progress';
      } else if (currentStep.status === 'in-progress') {
        currentStep.status = 'completed';
      }
      
      // Emit an event for parent component to handle
      this.$emit('step-verified', {
        stepName: currentStep.name,
        status: currentStep.status
      });
    },
    startVerification() {
      this.verificationSteps.forEach(step => {
        if (step.status === 'pending') {
          step.status = 'in-progress';
        }
      });
    },
    resetVerification() {
      this.verificationSteps.forEach(step => {
        step.status = 'pending';
      });
    }
  }
}
</script>

<style scoped>
.verification-panel {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
}

.verification-steps {
    margin-bottom: 20px;
}

.verification-step {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.verification-step.pending {
    background-color: #fff3cd;
}

.verification-step.in-progress {
    background-color: #cce5ff;
}

.verification-step.completed {
    background-color: #d4edda;
}
</style>
