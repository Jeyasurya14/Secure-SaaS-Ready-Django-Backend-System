from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None:
            return super().render(data, accepted_media_type, renderer_context)
            
        response = renderer_context.get('response')
        status_code = response.status_code if response else 200
        
        # If data is None, make it empty dict
        if data is None:
            data = {}

        response_data = {
            'success': True,
            'message': 'Success',
            'data': data
        }

        if status_code >= 400:
            response_data['success'] = False
            response_data['message'] = 'Error'
            # If the data itself contains 'detail' or is a list of errors, we map it to 'errors'
            response_data['errors'] = data
            if isinstance(data, dict) and 'detail' in data:
                response_data['message'] = data['detail']
            # Clear 'data' on error or keep it equal to errors? usually separate.
            response_data['data'] = None

        return super().render(response_data, accepted_media_type, renderer_context)
