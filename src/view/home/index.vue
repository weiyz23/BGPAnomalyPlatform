<template>
  <div class="container">
    <!-- <ejs-maps :titleSettings='titleSettings' :legendSettings='legendSettings'>
      <e-layers>
          <e-layer :shapeData='shapeData' :shapePropertyPath='shapePropertyPath' :shapeDataPath='shapeDataPath' :dataSource='dataSource' :shapeSettings='shapeSettings' :dataLabelSettings='dataLabelSettings' :tooltipSettings='tooltipSettings'></e-layer>
      </e-layers>
    </ejs-maps> -->
    <!-- <div id="map" class="map"></div> -->
  </div>
</template>


<script setup>
// import { MapsComponent as EjsMaps, LayersDirective as ELayers, LayerDirective as ELayer, MapAjax , Legend , DataLabel , MapsTooltip } from '@syncfusion/ej2-vue-maps';
// import { Maps } from '@syncfusion/ej2-maps';
// import { dataLabelSettings, legendSettings, tooltipSettings, shapeSettings } from './js/static-var.js'

// Maps.Inject(Legend, DataLabel, MapsTooltip);
// import { getCurrentInstance } from 'vue'
// const { proxy } = getCurrentInstance()

// const dataSource =  [{  "Country": "China", "Membership": "Permanent"},
//   {"Country": "France","Membership": "Permanent" },
//   { "Country": "Russia","Membership": "Permanent"},
//   {"Country": "Kazakhstan","Membership": "Non-Permanent"},
//   { "Country": "Poland","Membership": "Non-Permanent"},
//   {"Country": "Sweden","Membership": "Non-Permanent"}];

// defineProps({
//   titleSettings: {
//     type: Object,
//     default: () => 'BGP中断事件发生情况'
//   },
//   shapeData: {
//     type: Object,
//     default: () => new MapAjax('https://cdn.syncfusion.com/maps/map-data/world-map.json')
//   },
//   dataSource: {
//     type: Array,
//     default: () => {}
//   },
//   shapePropertyPath: {
//     type: String,
//     default: () => 'name'
//   },
//   shapeDataPath: {
//     type: String,
//     default: () => 'Country'
//   },
//   shapeSettings: {
//     type: Object,
//     default: () => {}
//   },
//   dataLabelSettings: {
//     type: Object,
//     default: () => dataLabelSettings
//   },
//   legendSettings: {
//     type: Object,
//     default: () => legendSettings
//   },
//   tooltipSettings: {
//     type: Object,
//     default: () => tooltipSettings
//   }
// })
</script>

<style scoped lang="less">
.container{
  height: calc(100vh - 142px);
  .map{
    height: 100%;
  }
}
</style>
