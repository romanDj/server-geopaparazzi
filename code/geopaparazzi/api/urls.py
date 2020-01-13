from tastypie.api import Api

from . import api as resources
from . import resourcebase_api as resourcebase_resources

api = Api(api_name='api')

api.register(resources.GroupCategoryResource())
api.register(resources.GroupResource())
api.register(resources.OwnersResource())
api.register(resources.ProfileResource())
api.register(resources.RegionResource())
api.register(resources.StyleResource())
api.register(resources.TagResource())
api.register(resources.ThesaurusKeywordResource())
api.register(resources.TopicCategoryResource())
api.register(resourcebase_resources.DocumentResource())
api.register(resourcebase_resources.FeaturedResourceBaseResource())
api.register(resourcebase_resources.LayerResource())
api.register(resourcebase_resources.MapResource())
api.register(resourcebase_resources.ResourceBaseResource())
