const { createApp } = Vue

const TestApp = {
    data(){
        return {
            records: []
        }
    },
    async created(){
        await this.getRecords()
    },
    methods: {
        async getRecords(){
            const response = await fetch(window.location, {
                method: 'get',
                headers: {
                    'X-Requested_With': 'XMLHttpRequest'
                }
            })
            this.records = await response.json()
        }
    },
    delimiters: ['{', '}']
}

createApp(TestApp).mount('#app')