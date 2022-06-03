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
var edgeImpact = {
  r_cert: 2.5,
  r_subdomain: 2.5,
  r_request_jump: 2.5,
  r_dns_a: 2.5,
  r_whois_name: 2,
  r_whois_phone: 2,
  r_whois_email: 2,
  r_cert_chain: 1.5,
  r_cname: 1.5,
  r_asn: 1,
  r_cidr: 1,
};
export default {
  name: "NetChart",
  props: {
    node: Array,
    edge: Array,
  },
  data() {
    return {
      // nodeData: [],
      edgeData: [],
    };
  },
  methods: {
    getData() {
      // this.nodeData = [];
      this.edgeData = this.edge;
      for (var edge of this.edgeData) {
        var relation = edge["relation"];
        edge["lineStyle"] = {
          width: edgeImpact[relation],
        };
      }
    },

    drawNet() {
      this.myChart = echarts.init(document.getElementById("netChart"));
      // console.log(this.edgeData);
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
        tooltip: {
          trigger: "item",
          backgroundColor: "None",
          borderWidth: 0,
          formatter: function (params) {
            if (params.data.source) {
              return params.data.relation;
            } else {
              return params.data.name;
            }
          },
          textStyle: {
            color: "#fff",
            fontSize: 12,
          },
        },
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Network",
            type: "graph",
            layout: "force",
            edgeSymbol: ["none", "arrow"],
            edgeSymbolSize: "5",
            zoom: 0.4,
            roam: true,
            // label: {
            //   position: "right",
            //   formatter: "{b}",
            // },
            lineStyle: {
              color: "source",
              curveness: 0.2,
            },
            emphasis: {
              label: {
                show: false,
              },
              focus: "adjacency",
              lineStyle: {
                width: 6,
              },
            },
            force: {
              gravity: 0.1,
              repulsion: 40,
            },
            data: this.node,
            links: this.edgeData,
            categories: categories,
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
    this.drawNet();
  },

  watch: {
    node: function () {
      this.myChart.dispose();
      this.getData();
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
