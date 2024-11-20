<template>
  <div class="container">
    <MyMap :dataSource="dataSource" v-if="isShow"/>
  </div>
</template>


<script setup>
import MyMap from '@/components/MyMap/index.vue'
// import { dataSource } from './js/static-var'
import { summary } from '@/api/menu1'
import { ref, onMounted } from 'vue'
import { shapeData } from '@/components/MyMap/mapBuilder'
// Request data from the server
const dataSource = ref([])
const isShow=ref(false);

summary().then(res => {
  // parse the res data
  let dictionary = {}
  for (let prefix in res) {
    const info = res[prefix]
    const cc = info['cc']
    const outage_time = info['timestamps']
    if (!dictionary[cc]) {
      dictionary[cc] = 0
    }
    dictionary[cc] += outage_time.length
  }
  for (let cc in dictionary) {
    dataSource.value.push({
      cc: cc,
      times: dictionary[cc],
    })
  }
  for (const idx in shapeData['features']){
    const properties = shapeData['features'][idx]['properties']
    const other_cc = properties['cc']
    if (!dataSource.value.find(item => item.cc === other_cc)) {
      dataSource.value.push({
        cc: other_cc,
        times: 0
      })
    }
  } 
  console.log('dataSource', dataSource)
  isShow.value = true
}).catch(err => {
    console.log(err)
})
</script>

<style scoped lang="less">
.container{
  height: calc(100vh - 142px);
  .map{
    height: 100%;
  }
}
</style>
