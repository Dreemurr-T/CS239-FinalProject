<template>
  <div class="chart-wrapper" id="pieChart"></div>
</template>

<script>
import * as echarts from "echarts";
var categories = ["A", "B", "C", "D", "E", "F", "G", "I"];

export default {
  name: "IndustryPie",
  data() {
    return {
      chartData: [
        {
          name: "涉黄",
          value: 0,
        },
        {
          name: "涉赌",
          value: 0,
        },
        {
          name: "涉骗",
          value: 0,
        },
        {
          name: "涉毒",
          value: 0,
        },
        {
          name: "涉枪",
          value: 0,
        },
        {
          name: "黑客",
          value: 0,
        },
        {
          name: "非法交易平台",
          value: 0,
        },
        {
          name: "非法支付平台",
          value: 0,
        },
        {
          name: "其他",
          value: 0,
        },
      ],
    };
  },
  methods: {
    getData() {
      this.$axios.get("/test").then((response) => {
        var nodeData = response.data.node;
        for (var data of nodeData) {
          var industryData = data.industry;
          for (var i = 0; i < industryData.length; i++) {
            for (var j = 0; j < 8; j++) {
              if (industryData[i] == categories[j]) {
                this.chartData[j].value += 1;
              }
            }
          }
        }
        this.drawPie();
      });
    },

    drawPie() {
      this.myChart = echarts.init(document.getElementById("pieChart"));
      var plotData = this.chartData.filter((item) => item.value != 0);
      var maxNum = 0;
      for (var i = 0; i < 8; i++) {
        if (this.chartData[i].value > maxNum) {
          maxNum = this.chartData[i].value;
        }
      }
      var option = {
        tooltip: {
          trigger: "item",
        },
        visualMap: {
          show: false,
          min: 0,
          max: maxNum + 3,
          inRange: {
            colorLightness: [0, 1],
          },
        },
        series: [
          {
            name: "Industry",
            type: "pie",
            radius: "70%",
            center: ["50%", "50%"],
            data: plotData.sort(function (a, b) {
              return a.value - b.value;
            }),
            roseType: "radius",
            label: {
              color: "rgba(255, 255, 255, 0.6)",
            },
            labelLine: {
              lineStyle: {
                color: "rgba(255, 255, 255, 0.3)",
              },
              smooth: 0.2,
              length: 10,
              length2: 20,
            },
            itemStyle: {
              color: "#c23531",
              shadowBlur: 200,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
            animationType: "scale",
            animationEasing: "elasticOut",
            animationDelay: function (idx) {
              return Math.random() * 200;
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
#pieChart {
  box-sizing: border-box;
  width: 100%;
  height: 130%;
  margin-top: -50px;
}
</style>
