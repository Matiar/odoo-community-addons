odoo.define('load_pyecharts', function (require) {
    "use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');
    var AbstractAction = require('web.AbstractAction');


    var PyEcharts = AbstractAction.extend({
        template: 'pyecharts_template',

        init: function(parent, data){
            return this._super.apply(this, arguments);
        },

        start: function(){
            $(document).ready(function() {
                // demo begin

                // var chart1 = echarts.init(document.getElementById('bar1'), 'white', {renderer: 'canvas'});
                // var chart2 = echarts.init(document.getElementById('bar2'), 'white', {renderer: 'canvas'});
                //
                // $(function () {
                //     fetchData1();
                // });
                //
                // function fetchData1() {
                //     $.ajax({
                //         type: "GET",
                //         url: "/demo",
                //         dataType: 'json',
                //         success: function (result) {
                //             chart1.setOption(result.bar1);
                //             chart2.setOption(result.bar2);
                //         },
                //         error: function(request) {
                //             console.log("error")
                //         },
                //     });
                // }

                // demo end


                $(function () {
                    fetchData();
                });
                function fetchData() {
                    $.ajax({
                        type: "GET",
                        url: "/pyecharts",
                        dataType: 'json',
                        success: function (result) {
                            console.log('success');
                            console.log(result);
                            var count = result.count;
                            var column = result.column;
                            var theme = result.theme;
                            var height = result.height;
                            var col = "col-md-" + String(12 / column);
                            var details = result.details;
                            var ech = document.getElementById("ech");
                            for (var detail in details) {
                                console.log(details[detail]);
                                var detailDiv = document.createElement("div");
                                detailDiv.setAttribute("class", col);
                                var d = document.createElement("div");
                                d.setAttribute("id", details[detail]['sequence']);
                                d.style.width = "100%";
                                d.style.height = height + 'px';
                                // d.style.border = "1px solid #B0E2FF";
                                d.style.marginBottom = "10px";
                                d.style.boxShadow = "0 0 1px rgb(0 0 0 / 13%), 0 1px 3px rgb(0 0 0 / 20%)";
                                detailDiv.appendChild(d);

                                ech.appendChild(detailDiv);

                                var chart = echarts.init(document.getElementById(details[detail]['sequence']), theme, {renderer: 'canvas'});
                                chart.setOption(details[detail]['edata']);
                            }
                        },
                        error: function(request) {
                            console.log("error")
                        },
                    });
                }
            });
            return true;
        },


    });
    core.action_registry.add('load_pyecharts', PyEcharts);
});
