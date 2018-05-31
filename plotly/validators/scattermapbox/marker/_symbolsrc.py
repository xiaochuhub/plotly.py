import _plotly_utils.basevalidators


class SymbolsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='symbolsrc',
        parent_name='scattermapbox.marker',
        **kwargs
    ):
        super(SymbolsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )