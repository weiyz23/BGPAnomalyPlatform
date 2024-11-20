// 地图组件常量
export const dataLabelSettings = {
  visible: true,
  labelPath: 'name',
  smartLabelMode: 'Trim'
};
export const legendSettings = {
  visible: true
};
export const tooltipSettings = {
  visible: true,
  valuePath: 'Country'
};
// from light green to red
export const shapeSettings = {
  colorValuePath: 'density',
  fill: '#E5E5E5',
  colorMapping: [
    {
      from: 0, to: 1, color: 'rgb(0, 200, 0)'
    },
    {
      from: 1, to: 3, color: 'rgb(25, 100, 0)'
    },
    {
      from: 3, to: 10, color: 'rgb(125, 50, 0)'
    },
    {
      from: 10, to: 100000, color: 'rgb(200, 0, 0)'
    },
  ]
};