<template>
  <div class="home">
    <nav-bar></nav-bar>
    <div class="main-container">
      <div class="left-charts">
        <div class="chart-item">
          <box-container :boxTitle="'全部节点信息'">
            <node-list></node-list>
          </box-container>
          <box-container :boxTitle="'全部边信息'">
            <edge-list></edge-list>
          </box-container>
        </div>
      </div>
      <div class="mid-charts">
        <div class="chart-item">
          <box-container :boxTitle="'网络资产图谱'">
          <net-chart></net-chart>
          /></box-container>
        </div>
      </div>
      <div class="right-charts">
        <div class="chart-item">
          <box-container :boxTitle="'节点统计信息'">
            <node-bar></node-bar>
          </box-container>
          <box-container :boxTitle="'边统计信息'">
            <edge-bar></edge-bar>
          </box-container>
          <box-container :boxTitle="'涉及资产分布'">
            <industry-pie></industry-pie>
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
import NodeList from "@/components/List/NodeList.vue";
import EdgeList from "@/components/List/EdgeList.vue"
import NetChart from "@/components/Charts/NetworkChart.vue"
import NodeBar from "@/components/Charts/NodeBar.vue"
import EdgeBar from "@/components/Charts/EdgeBar.vue"
import IndustryPie from "@/components/Charts/IndustryPie.vue"

export default {
  name: "HomeView",
  components: {
    NavBar,
    BoxContainer,
    NodeList,
    EdgeList,
    NetChart,
    NodeBar,
    EdgeBar,
    IndustryPie,
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
  font-size: 0px;

  .left-charts {
    vertical-align: middle;
    display: inline-block;
    line-height: 10px;
    margin-top: 10px;
    width: 24%;
    height: 100%;
    .chart-item {
      height: 49.5%;
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
    .chart-item {
      height: 99%;
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
      height: 33%;
      width: 100%;
    }
  }
}
</style>
