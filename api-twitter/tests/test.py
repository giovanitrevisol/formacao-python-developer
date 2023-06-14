from unittest import mock
from src.services import _get_trends  # chamando método privado para teste


def test_get_success_trends():
    # Arrange (Arranjo)
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [
        {
            "trends": [
                {"name": "#elenaovemmais", "url": "http://twitter.com/search?q=%23EleNaoVemMais"},
                {"name": "anrtprado", "url": "http://twitter.com/search?q=anrtprado"},
            ]
        }
    ]

    # Act (Ação)
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert (Verificação)
    assert trends == [
        {"name": "#elenaovemmais", "url": "http://twitter.com/search?q=%23EleNaoVemMais"},
        {"name": "anrtprado", "url": "http://twitter.com/search?q=anrtprado"},
    ]


def test_get_no_success_trends():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [{"trends": []}]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == []