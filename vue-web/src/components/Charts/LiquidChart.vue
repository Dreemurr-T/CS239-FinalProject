<template>
  <div class="chart-wrapper" id="liquidChart"></div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-liquidfill";

export default {
  name: "LiquidChart",
  props: {
    node: Array,
  },
  computed: {
    node_len: function () {
      return this.node.length;
    },
  },
  methods: {
    drawLiquid() {
      if (this.myChart != null) {
        this.myChart.dispose();
      }
      this.myChart = echarts.init(document.getElementById("liquidChart"));
      var option = {
        title: {
          text: "当前团伙相对数据库中最大团伙的规模比例",
          left: "center",
          top: "bottom",
          textStyle:{
            color: "#FFFFFF",
            fontSize: "15px",
          },
        },
        series: [
          {
            type: "liquidFill",
            data: [(this.node_len/3113).toFixed(4)],
            radius: '70%',
          },
        ],
        tooltip: {
          show: true,
        },
        backgroundStyle: {
          color: "#FFFFFF",
        },
      };
      this.myChart.setOption(option);
      window.onresize = () => {
        this.myChart.resize();
      };
    },
  },
  mounted() {
    this.drawLiquid();
  },
  watch: {
    node: function() {
      this.drawLiquid();
    }
  }
};
</script>

<style scoped>
#liquidChart {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  margin-top: -10px;
}
</style>
