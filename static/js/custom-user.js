(function($) {
    $(document).ready(function() {
        var $availability = $('#id_availability');
        var $count = $('#id_count');

        function toggleCountFieldVisibility() {
            if ($availability.is(':checked')) {
                $count.parent().show();
            } else {
                $count.parent().hide();
            }
        }

        toggleCountFieldVisibility();
        $availability.on('change', toggleCountFieldVisibility);
    });
})(jQuery);
