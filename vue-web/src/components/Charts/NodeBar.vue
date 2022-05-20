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
  methods: {
    getData() {
      this.$axios.get("/test").then((response) => {
        var nodeData = response.data.node;
        for (var data of nodeData) {
          for (var i = 0; i < 8; i++) {
            if (data.category == categories[i]) {
              this.chartData[i] += 1;
            }
          }
        }
        this.drawBar();
      });
    },

    drawBar() {
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
              color: "#fff"
            }
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
              color: "#fff"
            }
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
  mounted() {
    this.getData();
  },
};
</script>

<style scoped>
#barChart1 {
  box-sizing: border-box;
  width: 100%;
  height: 130%;
  margin-top: -50px;
}
</style>
