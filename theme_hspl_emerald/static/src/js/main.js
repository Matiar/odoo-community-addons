odoo.define("theme_hspl_emerald.theme_script", function (require) {
    "use strict";

    var sAnimations = require("website.content.snippets.animation");

    sAnimations.registry.themefunction = sAnimations.Class.extend({
        selector: "#wrapwrap",

        start: function () {
            // Dropdown menu slidedown on click
            if ($(window).innerWidth() < 1200) {
                $(".dropdown").on("show.bs.dropdown", function () {
                    $(this)
                        .find(".dropdown-menu")
                        .first()
                        .stop(true, true)
                        .slideDown(150);
                });
                $(".dropdown").on("hide.bs.dropdown", function () {
                    $(this)
                        .find(".dropdown-menu")
                        .first()
                        .stop(true, true)
                        .slideUp(150);
                });
            }
            // Dropdown menu slidedown on hover
            else {
                $("#wrapwrap  .dropdown").each(function () {
                    if (!$(this).closest(".o_extra_menu_items").length) {
                        $(this)
                            .closest("a")
                            .click(function () {
                                return false;
                            });
                        $(this).hover(
                            function () {
                                $(".dropdown-menu", this)
                                    .stop(true, true)
                                    .fadeIn("slow");
                                $(this).toggleClass("open");
                                $(".dropdown-menu", this)
                                    .stop(true, true)
                                    .addClass("slideInUp");
                            },
                            function () {
                                $(".dropdown-menu", this)
                                    .stop(true, true)
                                    .removeClass("slideInUp")
                                    .fadeOut(500);

                                $(this).toggleClass("open");
                            }
                        );
                    }
                });
            }
            $(".o_extra_menu_items .dropdown-menu").css("display", "none");
            $(".o_extra_menu_items .dropdown").click(function (event) {
                event.stopImmediatePropagation();
                $(this).find(".dropdown-menu").toggle();
            });

            var top_bar_height = $(".top-bar-main").outerHeight();
            if ($("body").find(".o_header_overlay").length > 0) {
                $("header:not(.o_header_affix)").addClass("transparent_header");
                $(".transparent_header").css("top", top_bar_height);
                $(".o_header_affix.affix").removeClass("transparent_header");
            }

            $("#wrapwrap").scroll(function () {
                if ($("#wrapwrap").scrollTop() > 70) {
                    $(".scroll-to-top").addClass("reveal");
                } else {
                    $(".scroll-to-top").removeClass("reveal");
                }
            });
            if ($("body").find("#leaf_map").length === 1) {
                // Creating map options
                var mapOptions = {
                    center: [17.385044, 78.486671],
                    zoom: 10,
                };

                // Creating a map object
                console.log(">>>>>>>>>>.", L);
                var map = new L.map("leaf_map", mapOptions);

                // Creating a Layer object
                var layer = new L.TileLayer(
                    "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                );

                // Adding layer to the map
                map.addLayer(layer);
            }
        },
    });
});
