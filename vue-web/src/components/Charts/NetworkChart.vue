<template>
  <div class="chart-wrapper" id="netChart"></div>
</template>

<script>
import * as echarts from "echarts";
var categories = [
  { name: "Domain" },
  { name: "IP" },
  { name: "Cert" },
  { name: "Whois_Name" },
  { name: "Whois_Phone" },
  { name: "Whois_Email" },
  { name: "IP_C" },
  { name: "ASN" },
];
export default {
  name: "NetChart",
  props: {
    node: Array,
    edge: Array,
  },
  // data() {
  //   return {
  //     chartData: {},
  //   };
  // },
  methods: {
    // getData() {
    //   this.chartData.node = this.node;
    //   this.chartData.edge = this.edge;
    // },

    drawNet() {
      if (this.myChart != null) {
        this.myChart.dispose();
      }
      this.myChart = echarts.init(document.getElementById("netChart"));
      var option = {
        legend: [
          {
            // selectedMode: 'single',
            data: categories,
            textStyle: {
              color: "white",
            },
          },
        ],
        // animationDuration: 1500,
        // animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Network",
            type: "graph",
            layout: "force",
            tooltip: {
              show: true,
            },
            // data: this.chartData.node,
            // links: this.chartData.edge,
            data: this.node,
            links: this.edge,
            categories: categories,
            roam: true,
            label: {
              position: "right",
              formatter: "{b}",
            },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
            emphasis: {
              focus: "adjacency",
              lineStyle: {
                width: 10,
              },
              linkLabel: {
                show: true,
                formatter: '{@source}',
              },
            },
            force: {
              gravity: 0.4,
              repulsion: 20,
            },
          },
        ],
      };
      this.myChart.setOption(option);
      window.onresize = () => {
        this.myChart.resize();
      };
    },
  },

  mounted() {
    this.drawNet();
  },

  watch: {
    node: function () {
      this.drawNet();
    },
  },
};
</script>

<style scoped>
#netChart {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}
</style>
