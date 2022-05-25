<template>
  <div class="chart-wrapper" id="barChart1"></div>
</template>

<script>
import * as echarts from "echarts";
var categories = [
  "Domain",
  "IP",
  "Cert",
  "Whois_Name",
  "Whois_Phone",
  "Whois_Email",
  "IP_C",
  "ASN",
];
export default {
  name: "NodeBar",
  data() {
    return {
      chartData: [0, 0, 0, 0, 0, 0, 0, 0],
    };
  },
  props: {
    node: Array,
  },
  methods: {
    getData() {
      // var nodeData = this.node
      for (var i = 0; i < 8; i++) {
        this.chartData[i] = 0;
      }
      for (var data of this.node) {
        for (i = 0; i < 8; i++) {
          if (data.category == categories[i]) {
            this.chartData[i] += 1;
          }
        }
      }
    },

    drawBar() {
      if (this.myChart != null) {
        this.myChart.dispose();
      }

      this.myChart = echarts.init(document.getElementById("barChart1"));
      var option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        xAxis: {
          type: "value",
          axisLabel: {
            textStyle: {
              fontFamilt: "Times New Roman",
              fontSize: "10",
              color: "#fff",
            },
          },
        },
        yAxis: {
          type: "category",
          data: [
            "Domain",
            "IP",
            "Cert",
            "W_Name",
            "W_Phone",
            "W_Email",
            "IP_C",
            "ASN",
          ],
          axisLabel: {
            textStyle: {
              fontFamilt: "Arial",
              fontSize: "8",
              color: "#fff",
            },
          },
        },
        series: [
          {
            data: this.chartData,
            type: "bar",
          },
        ],
      };
      this.myChart.setOption(option);
      window.onresize = () => {
        this.myChart.resize();
      };
    },
  },
  created() {
    this.getData();
  },
  mounted() {
    this.drawBar();
  },
  watch: {
    node: function () {
      this.getData();
      this.drawBar();
    },
  },
};
</script>

<style scoped>
#barChart1 {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}
</style>
