<template>
    <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-lg font-medium mb-6">Generated Identities</h2>

        <div v-if="store.loading && !store.identities.length" class="text-center py-4">
            Loading identities...
        </div>

        <div v-else-if="!store.identities.length" class="text-center py-4 text-gray-500">
            No identities generated yet
        </div>

        <div v-else class="space-y-4">
            <div v-for="identity in store.identities" :key="identity.id" class="border rounded-lg p-4">
                <div class="flex justify-between items-start">
                    <div>
                        <h3 class="font-medium">{{ identity.name }}</h3>
                        <p class="text-sm text-gray-500">Culture: {{ identity.culture }}</p>
                    </div>
                    <button
                        v-if="!identity.gmail_creation_attempted"
                        @click="createGmail(identity)"
                        class="inline-flex items-center px-3 py-1 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                        :disabled="store.loading"
                    >
                        Create Gmail
                    </button>
                    <span
                        v-else-if="identity.gmail_created" 
                        class="inline-flex items-center px-3 py-1 text-sm font-medium text-green-700 bg-green-100 rounded-md"
                    >
                        Gmail Created
                    </span>
                    <span
                        v-else
                        class="inline-flex items-center px-3 py-1 text-sm font-medium text-red-700 bg-red-100 rounded-md"
                    >
                        Gmail Failed
                    </span>
                </div>

                <div class="mt-4 grid grid-cols-2 gap-4 text-sm">
                    <div>
                        <p><strong>Email:</strong> {{ identity.email }}</p>
                        <p><strong>Password:</strong> {{ identity.password }}</p>
                    </div>
                    <div>
                        <p><strong>First Name:</strong> {{ identity.first_name }}</p>
                        <p><strong>Last Name:</strong> {{ identity.last_name }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { onMounted } from 'vue'
import { useIdentityStore } from '../store/identity'

export default {
    name: 'IdentityList',

    setup() {
        const store = useIdentityStore()

        onMounted(async () => {
            await store.fetchIdentities()
        })

        const createGmail = async (identity) => {
            try {
                await store.createGmailAccount(identity.id, {
                    headless: false,
                    recovery_email: null,
                    recovery_phone: null
                })
            } catch (error) {
                console.error('Failed to create Gmail account:', error)
            }
        }
        return {
            store,
            createGmail
        }
    }
}
</script>