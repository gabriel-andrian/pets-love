from http import HTTPStatus


def build_api_response(http_status) -> tuple:
    return build_response_message(http_status), http_status


def build_response_message(http_status):
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad Request',
        HTTPStatus.CREATED: 'Created',
        HTTPStatus.NOT_FOUND: 'Not Found',
        HTTPStatus.OK: 'Successful Requisition',
        HTTPStatus.UNAUTHORIZED: 'Unauthorized',
        HTTPStatus.FORBIDDEN: 'Forbidden'
    }

    return {'msg': messages[http_status]}
