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
  methods: {
    getData() {
      this.$axios.get("/test").then((response) => {
        var edgeData = response.data.edge;
        for (var data of edgeData) {
          for (var i = 0; i < 11; i++) {
            if (data.relation == categories[i]) {
              this.chartData[i] += 1;
            }
          }
        }
        this.drawBar();
      });
    },

    drawBar() {
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
            textStyle: {
              fontFamilt: "Times New Roman",
              fontSize: "10",
              color: "#fff",
            },
          },
        },
        xAxis: {
          type: "category",
          data: categories,
          axisLabel: {
            show: false,
          },
        },
        series: [
          {
            data: this.chartData,
            type: "bar",
            itemStyle: {
                color: "pink"
            }
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
#barChart2 {
  box-sizing: border-box;
  width: 100%;
  height: 130%;
  margin-top:-50px;
}
</style>
