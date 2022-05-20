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
  data() {
    return {
      chartData: {},
    };
  },
  methods: {
    getData() {
      this.$axios.get("/test").then((response) => {
        this.chartData = response.data;
        console.log(this.chartData);
        this.drawNet();
      });
    },

    drawNet() {
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
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Network",
            type: "graph",
            layout: "force",
            data: this.chartData.node,
            links: this.chartData.edge,
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
            },
            force: {
              gravity: 0.2,
              repulsion: 40,
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
    this.getData();
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
