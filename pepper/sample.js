<script>
<!--
jQuery( function() {
    jQuery( '#jquery-sample-button' ) . toggle(
        function() {
            jQuery . ajax( {
                url: 'jquery-sample-ajax-json.php',
                dataType: 'json',
                data: {
                    year: '2011',
                    month: '11',
                    day: '25'
                },
                success: function( data ) {
                    jQuery . each( data, function( key, value ) {
                        jQuery( '#jquery-sample-ajax' ) . append( '<p>' + key + ': ' + value + '</p>' );
                    } );
                    jQuery( '#jquery-sample-textStatus' ) . text( '読み込み成功' );
                },
                error: function( data ) {
                    jQuery( '#jquery-sample-textStatus' ) . text( '読み込み失敗' );
                }
            } );
        },
        function() {
            jQuery( '#jquery-sample-ajax' ) . html( '' );
            jQuery( '#jquery-sample-textStatus' ) . text( '' );
        }
    );
} );
// -->
</script>