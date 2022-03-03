const { createApp } = Vue

const TestApp = {
    data(){
        return {
            record: {
                'date': '',
                'title': '',
                'amount': '',
                'distance': '',
            },
            pages_count: '',
            errors: [],
            records: [],
            parameters: {
                'page': 1,
                'order_by':'id',
                'sort': 'asc',
                'filter': {
                    'field': null,
                    'condition': null,
                    'value': null
                }
            }
        }
    },
    async created(){
        await this.getRecords()
    },
    methods: {
        async getRecords(){
            const response = await fetch(window.location, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested_With': 'XMLHttpRequest'
                },
                body: JSON.stringify(this.parameters)
            })
            res = await response.json()
            this.records = res.records
            this.errors = res.errors
            this.pages_count = res.pages_count
        },
        async createRecord(){
            await this.getRecords()

            const response = await fetch(window.location + 'create', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested_With': 'XMLHttpRequest',
                },
                body: JSON.stringify(this.record)
            })
            if (response.status != 204){
                this.errors = await response.json()
            }
            await this.getRecords()
        },
        async setSort(order_by){
            if (this.parameters.order_by === order_by){
                this.parameters.sort = this.parameters.sort === 'asc'?'desc':'asc';
            } else {
                this.parameters.order_by = order_by;
                this.parameters.sort = 'asc';
            }
            await this.getRecords()
        },
        async setPage(page){
            this.parameters.page = page;
            await this.getRecords()
        },
        async setFilter(submitEvent){
            this.parameters.filter.field = submitEvent.target.elements.field.value
            this.parameters.filter.condition = submitEvent.target.elements.condition.value
            this.parameters.filter.value = submitEvent.target.elements.value.value
            await this.getRecords()
        }
    },
    delimiters: ['{', '}']
}

createApp(TestApp).mount('#app')