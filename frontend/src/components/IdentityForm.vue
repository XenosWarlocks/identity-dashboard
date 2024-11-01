<template>
    <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-lg font-medium mb-6">Generate New Identity</h2>
        <form @submit.prevent="handleSubmit">
            <div class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700">Culture</label>
                    <select
                        v-model="formData.culture"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                    >
                        <option value="christian">Christian</option>
                        <option value="jewish">Jewish</option>
                        <option value="hindu">Hindu</option>
                        <option value="arabic">Arabic</option>
                        <option value="chinese">Chinese</option>
                        <option value="japanese">Japanese</option>
                    </select>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Password Length</label>
                    <input
                        type="number"
                        v-model="formData.passwordLength"
                        min="12"
                        max="32"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                    />
                </div>
                <div class="flex items-center mt-4">
                    <button
                        type="submit"
                        class="w-full inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                        :disabled="store.loading"
                    >
                        <template v-if="!store.loading">Generate Identity</template>
                        <template v-else>Generating...</template>
                    </button>
                </div>
            </div>
        </form>
        <div v-if="store.error" class="mt-4 p-4 bg-red-50 text-red-700 rounded-md">
            {{ store.error }}
        </div>
    </div>
</template>

<script>
import { ref } from 'vue'
import { useIdentityStore } from '../store/identity'

export default {
    name: 'IdentityForm',

    setup() {
        const store = useIdentityStore()
        const formData = ref({
            culture: 'christian',
            passwordLength: 16
        })

        const handleSubmit = async () => {
            try {
                await store.generateIdentity(formData.value.culture)
            } catch (error) {
                console.error('Failed to generate identity:', error)
            }
        }
        return {
            store,
            formData,
            handleSubmit
        }
    }
}
</script>