<template>
  <div class="home">
    <nav-bar v-model:index="index"></nav-bar>
    <div class="main-container">
      <!--
      <div class="left-charts">
        <div class="chart-item">

          <box-container :boxTitle="'全部节点信息'">
            <node-list v-if="flag" :node="node"></node-list>
          </box-container>
          <box-container :boxTitle="'全部边信息'">
            <edge-list v-if="flag" :edge="edge"></edge-list>
          </box-container>
        
        </div>
      </div>
-->
      <div class="left-charts">
        <div class="chart-item">
          <box-container :boxTitle="'概览'">
            <sim-info
              v-if="flag"
              :index="index"
              :node="node"
              :edge="edge"
            ></sim-info>
          </box-container>
        </div>
        <div class="chart-item">
          <box-container :boxTitle="'团伙规模'">
            <liquid-chart v-if="flag" :node="node"></liquid-chart>
          </box-container>
        </div>
        <div class="chart-item">
          <box-container :boxTitle="'涉及资产分布'">
            <industry-pie v-if="flag" :node="node"></industry-pie>
          </box-container>
        </div>
      </div>
      <div class="mid-charts">
        <div class="chart-item1">
          <box-container :boxTitle="'网络资产图谱'">
            <net-chart v-if="flag" :node="node" :edge="edge"></net-chart>
            /></box-container
          >
        </div>
        <div class="chart-item2">
          <box-container :boxTitle="'核心资产图谱'"> </box-container>
        </div>
      </div>
      <div class="right-charts">
        <div class="chart-item">
          <box-container :boxTitle="'节点统计信息'">
            <node-bar v-if="flag" :node="node"></node-bar>
          </box-container>
          <box-container :boxTitle="'边统计信息'">
            <edge-bar v-if="flag" :edge="edge"></edge-bar>
          </box-container>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import BoxContainer from "@/components/Box/BoxContainer.vue";
import NetChart from "@/components/Charts/NetworkChart.vue";
import NodeBar from "@/components/Charts/NodeBar.vue";
import EdgeBar from "@/components/Charts/EdgeBar.vue";
import IndustryPie from "@/components/Charts/IndustryPie.vue";
import LiquidChart from "@/components/Charts/LiquidChart.vue";
import SimInfo from "@/components/List/SimpleInfo.vue";

export default {
  name: "HomeView",
  data() {
    return {
      flag: false,
      node: [],
      edge: [],
      index: 1,
    };
  },
  components: {
    NavBar,
    BoxContainer,
    NetChart,
    NodeBar,
    EdgeBar,
    IndustryPie,
    LiquidChart,
    SimInfo,
  },

  methods: {
    getData(index) {
      var url = "/" + index.toString();
      this.$axios
        .get(url)
        .then((res) => {
          this.node = res.data.node;
          this.edge = res.data.edge;
          this.flag = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getData(this.index);
  },

  watch: {
    index: function () {
      this.getData(this.index);
    },
  },
};
</script>

<style lang="scss" scoped>
.home {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url("../assets/bg.png") no-repeat center center;
  background-size: cover;
}
.main-container {
  position: relative;
  height: calc(100% - 80px);
  box-sizing: border-box;
  padding-bottom: 10px;
  width: 100%;

  .left-charts {
    vertical-align: middle;
    display: inline-block;
    width: 24%;
    height: 100%;
    margin-top: 10px;
    .chart-item {
      height: 33%;
      width: 100%;
    }
  }

  .mid-charts {
    vertical-align: middle;
    display: inline-block;
    width: 50%;
    height: 100%;
    margin-top: 10px;
    margin-left: 5px;
    margin-right: 5px;
    .chart-item1 {
      height: 60%;
      width: 100%;
    }
    .chart-item2 {
      height: 39%;
      width: 100%;
    }
  }

  .right-charts {
    vertical-align: middle;
    display: inline-block;
    margin-top: 10px;
    width: 24%;
    height: 100%;
    .chart-item {
      height: 49.5%;
      width: 100%;
    }
  }
}
</style>
