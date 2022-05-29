<template>
  <div class="chart-wrapper" id="barChart2"></div>
</template>

<script>
import * as echarts from "echarts";
var categories = [
  "r_cert",
  "r_subdomain",
  "r_request_jump",
  "r_dns_a",
  "r_whois_name",
  "r_whois_email",
  "r_whois_phone",
  "r_cert_chain",
  "r_cname",
  "r_asn",
  "r_cidr",
];

export default {
  name: "EdgeBar",
  data() {
    return {
      chartData: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    };
  },
  props: {
    edge: Array,
  },
  methods: {
    getData() {
      for (var i = 0; i < 11; i++) {
        this.chartData[i] = 0;
      }
      for (var data of this.edge) {
        for (i = 0; i < 11; i++) {
          if (data.relation == categories[i]) {
            this.chartData[i] += 1;
          }
        }
      }
    },

    drawBar() {
      if (this.myChart != null) {
        this.myChart.dispose();
      }
      this.myChart = echarts.init(document.getElementById("barChart2"));
      var option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        yAxis: {
          type: "value",
          axisLabel: {
            fontFamily: "Times New Roman",
            fontSize: "10",
            color: "#fff",
          },
        },
        xAxis: {
          type: "category",
          data: categories,
          axisLabel: {
            margin: 5,
            rotate: -90,
            color: "#FFFFFF",
            fontSize: 9,
            fontFamily: "Arial",
          },
        },
        series: [
          {
            data: this.chartData,
            type: "bar",
            itemStyle: {
              color: "pink",
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
  created() {
    this.getData();
  },
  mounted() {
    this.drawBar();
  },
  watch: {
    edge: function () {
      this.getData();
      this.drawBar();
    },
  },
};
</script>

<style scoped>
#barChart2 {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}
</style>
