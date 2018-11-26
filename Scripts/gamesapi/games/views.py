from games.models import GameCategory
from games.models import Game
from games.models import Player
from games.models import PlayerScore
from games.serializers import GameCategorySerializer
from games.serializers import GameSerializer
from games.serializers import PlayerSerializer
from games.serializers import PlayerScoreSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
#code added in lecture 25
from django.contrib.auth.models import User
from games.serializers import UserSerializer
from rest_framework import permissions
from games.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)
    #Added in lecture 32
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    #added in lecture 26
    permission_classes = (
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,
    )
    #Added in lecture 32
    filter_fields = (
    'name',
    'game_category',
    'release_date',
    'played',
    'owner',
    )
    search_fields = (
    '^name',
    )
    ordering_fields = (
    'name',
    'release_date'
    )
    #changed in lecture 25
    def perform_create(self, serializer):
        # Pass an additional owner field to create method
        # To set the owner to the user received in the request
        serializer.save(owner = self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    # added in lecture 26
    permission_classes = (
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,
    )


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'
    #Added in lecture 32
    filter_fields = (
    'name',
    'gender',
    )
    search_fields = (
    '^name',
    )
    ordering_fields = (
    'name',
    )


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'

#Added in lecture 32
class PlayerScoreFilter(filters.FilterSet):
    min_score = NumberFilter(
    name = 'score',lookup_expr='gte')
    max_score = NumberFilter(
    name = 'score',lookup_expr='lte')
    from_score_date = DateTimeFilter(
    name = 'score_date',lookup_expr='gte')
    to_score_date = DateTimeFilter(
    name = 'score_date',lookup_expr='lte')
    player_name = AllValuesFilter(
    name='player__name')
    game_name = AllValuesFilter(
    name='game__name')

    class Meta:
        model = PlayerScore
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            #player__name will be accessed as player_name
            'player_name',
            #game__name will be accessed as game_name
            'game_name',
        )

class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'
    #Added in lecture 32
    filter_class = PlayerScoreFilter
    ordering_fields = (
    'score',
    'score_date',
    )


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'

#added in lecture 17
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request)
            })

# lecture 16 end
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from games.models import Game
# from games.serializers import GameSerializer
#
#
# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         game_serializer = GameSerializer(games, many=True)
#         return Response(game_serializer.data)
#
#     elif request.method == 'POST':
#         game_serializer = GameSerializer(data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'POST'])
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         game_serializer = GameSerializer(game)
#         return Response(game_serializer.data)
#
#     elif request.method == 'PUT':
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#  this is lecture 2 code..now upended by newer code
# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many=True)
#         return JSONResponse(games_serializer.data)
#
#     elif request.method == 'POST':
#         game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(data=game_data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JSONResponse(game_serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         game_serializer = GameSerializer(game)
#         return JSONResponse(game_serializer.data)
#
#     elif request.method == 'PUT':
#         game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(game, data=game_data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JSONResponse(game_serializer.data)
#         return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         game.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
