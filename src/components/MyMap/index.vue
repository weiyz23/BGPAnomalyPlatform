<template>
  <ejs-maps :titleSettings='titleSettings' :legendSettings='legendSettings'>
      <e-layers>
          <e-layer :shapeData='shapeData' :shapePropertyPath='shapePropertyPath' :shapeDataPath='shapeDataPath' :dataSource='dataSource' :shapeSettings='shapeSettings' :dataLabelSettings='dataLabelSettings' :tooltipSettings='tooltipSettings'></e-layer>
      </e-layers>
  </ejs-maps>
</template>



<script>
import { MapsComponent, LayersDirective, LayerDirective, MapAjax, Legend, DataLabel, MapsTooltip } from '@syncfusion/ej2-vue-maps';
import { dataLabelSettings, tooltipSettings, shapeData, shapeSettings, shapePropertyPath, shapeDataPath, titleSettings, legendSettings } from './mapBuilder';
import { watch } from 'vue';


export default {
  name: "App",
  // Declaring component and its directives
  components: {
      'ejs-maps' : MapsComponent,
      'e-layers' : LayersDirective,
      'e-layer' : LayerDirective
  },
  props: {
    dataSource: {
      type: Array,
      default: () => [
        { "cc": "CN", "times": 10 },
        { "cc": "IN", "times": 8 },
        { "cc": "ID", "times": 7 },
        { "cc": "BR", "times": 6 },
        { "cc": "US", "times": 5 },
      ]
    }
  },
  data() {
    return {
      // Specifying Maps properties
      titleSettings: titleSettings,
      legendSettings: legendSettings,
      shapeData: shapeData,
      shapePropertyPath: shapePropertyPath,
      shapeDataPath: shapeDataPath,
      shapeSettings: shapeSettings,
      dataLabelSettings: dataLabelSettings,
      tooltipSettings: tooltipSettings
    };
  },
  provide: {
    maps:[Legend, DataLabel, MapsTooltip]
  },
  setup(props) {
    console.log('props', props)
    console.log('shapeData', shapeData)
  },
};
</script>